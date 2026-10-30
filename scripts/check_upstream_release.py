#!/usr/bin/env python3
"""Check NIST's SP 800-171 catalog copy against NIST's releases and publications.

Three things can go wrong with ``src/nist_sp_800_171/schema/oscal-content/``
without any change in this repository:

- NIST publishes a newer revision of SP 800-171, so the schema falls behind;
- NIST releases a changed catalog of the pinned edition in
  usnistgov/oscal-content, moves the pinned tag, or moves the catalog's
  folder;
- the copied files drift from the files they were taken from.

The copy has no version in its path, so the release, the commit its tag
names and each file's git object hash are pinned below. This script asks the
GitHub API for usnistgov/oscal-content's latest release, for the commit the
pinned tag names and for a few folder listings. It compares every copied
file with its blob by git object hash, so nothing is downloaded but listings.
It asks doi.org whether NIST has registered the identifier of the next final
edition, because NIST registers one for every publication. It prints a
Markdown report and exits 1 when a newer edition is out, the catalog or its
folder changed, the tag moved, a file differs, or a check could not finish.
A file NIST adds beside the catalog is reported for information only.

Set ``GITHUB_TOKEN`` to raise the API rate limit. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
COPY = ROOT / "src" / "nist_sp_800_171" / "schema" / "oscal-content"
API = "https://api.github.com/repos/usnistgov/oscal-content"
DOI_API = "https://doi.org/api/handles/"
USER_AGENT = "lmodel-nist-sp-800-171-upstream-check"

# The release and the commit its tag names. Move them together when the copy
# is replaced from a newer release, with PINNED_BLOBS and the schema header's
# annotations.
PINNED_TAG = "v1.6.0"
PINNED_COMMIT = "f0de6d8d8c059d374f15e0ae07508d82e370fc1d"

# The folder that holds the pinned edition's catalogs, and the folder that
# holds every edition NIST has published in OSCAL.
PINNED_PATH = "nist.gov/SP800-171/rev3/json"
EDITIONS_PATH = "nist.gov/SP800-171"
PINNED_EDITIONS = {"rev3"}

# Each copied file, the path it was taken from at PINNED_COMMIT, and its git
# object hash there. tests/test_upstream.py checks the hashes offline.
PINNED_BLOBS = {
    "NIST_SP800-171_rev3_catalog.json": (
        f"{PINNED_PATH}/NIST_SP800-171_rev3_catalog.json",
        "814a0937a20cc1cad1bd7542847093c66d73af59",
    ),
    "LICENSE.md": ("LICENSE.md", "109af23dd24c2c465143aeab12ffebfffe2a4cd5"),
}

# The files in PINNED_PATH that the copy leaves out on purpose: the minified
# form of the same catalog. Any other file there is reported as new.
UNCOPIED = {"NIST_SP800-171_rev3_catalog-min.json"}

# The revision the schema renders, as its digital object identifier (DOI), and
# the identifier NIST would give the next final revision. Drafts of that
# revision are reported, not acted on: the schema follows final revisions.
PINNED_DOI = "10.6028/NIST.SP.800-171r3"
NEXT_FINAL_DOI = "10.6028/NIST.SP.800-171r4"
NEXT_DRAFT_DOIS = (
    "10.6028/NIST.SP.800-171r4.ipd",
    "10.6028/NIST.SP.800-171r4.2pd",
    "10.6028/NIST.SP.800-171r4.fpd",
)


def _get(url: str) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/vnd.github+json", "User-Agent": USER_AGENT},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith(API):
        # urllib copies ordinary headers onto a redirect, wherever it leads,
        # so the token goes in a header that stays with this request alone.
        req.add_unredirected_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read()


def _version_key(tag: str) -> tuple[int, ...]:
    """Numeric parts of a tag, padded so that v1.6 and v1.6.0 order alike."""
    parts = [int(x) for x in re.findall(r"\d+", tag)]
    return tuple(parts + [0] * (4 - len(parts)))


def _blob_sha(path: Path) -> str:
    """The git object hash of a file, as the contents API reports it."""
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def _listing(path: str, ref: str) -> dict[str, dict]:
    """The entries of one folder at a ref, by name, or the one entry when the
    path is a file. Empty when the ref holds nothing at the path."""
    try:
        entries = json.loads(_get(f"{API}/contents/{path}?ref={ref}"))
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return {}
        raise
    if isinstance(entries, dict):
        entries = [entries]
    return {e["name"]: e for e in entries}


def _tag_commit(tag: str) -> str | None:
    """The commit a tag names, read through the tag object when the tag is
    annotated, or None when the tag is gone."""
    try:
        target = json.loads(_get(f"{API}/git/ref/tags/{tag}"))["object"]
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        raise
    if target["type"] == "tag":
        target = json.loads(_get(f"{API}/git/tags/{target['sha']}"))["object"]
    return target["sha"]


def _blobs_at(ref: str) -> tuple[dict[str, str | None], dict[str, dict]]:
    """Each pinned file's git object hash at a ref, None where the ref lacks
    the file, and the listing of PINNED_PATH there."""
    listings = {PINNED_PATH: _listing(PINNED_PATH, ref)}
    shas = {}
    for name, (source, _sha) in PINNED_BLOBS.items():
        folder, _, base = source.rpartition("/")
        where = folder or base
        if where not in listings:
            listings[where] = _listing(where, ref)
        shas[name] = listings[where].get(base, {}).get("sha")
    return shas, listings[PINNED_PATH]


def _unlisted(folder: dict[str, dict], ref: str) -> list[str]:
    """A line for information naming the files in PINNED_PATH at a ref that
    the copy neither pins nor leaves out on purpose."""
    pinned = {source.rpartition("/")[2] for source, _sha in PINNED_BLOBS.values()}
    new = sorted(
        name
        for name, entry in folder.items()
        if entry.get("type", "file") == "file" and name not in pinned | UNCOPIED
    )
    if not new:
        return []
    return [
        f"- For information: `{PINNED_PATH}/` at {ref} also holds "
        + ", ".join(f"`{name}`" for name in new)
        + ", which the copy does not pin."
    ]


def _doi_registered(doi: str) -> bool:
    """Whether doi.org knows the identifier. Code 1 is found, 100 is not."""
    try:
        answer = json.loads(_get(DOI_API + doi))
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return False
        raise
    return answer.get("responseCode") == 1


def check_editions() -> tuple[list[str], bool]:
    """Report whether NIST has published another revision of SP 800-171."""
    report, attention = [], False
    if not _doi_registered(PINNED_DOI):
        attention = True
        report.append(
            f"- **doi.org no longer knows `{PINNED_DOI}`**, the pinned revision."
        )
    if _doi_registered(NEXT_FINAL_DOI):
        attention = True
        report.append(
            f"- **NIST has registered `{NEXT_FINAL_DOI}`, the next final revision of SP 800-171.** "
            f"Read https://doi.org/{NEXT_FINAL_DOI}, decide whether the schema moves to it, and "
            "replace the copy once usnistgov/oscal-content publishes its catalog."
        )
    else:
        report.append(
            f"- No final revision after the pinned one: `{NEXT_FINAL_DOI}` is not registered."
        )
    drafts = [doi for doi in NEXT_DRAFT_DOIS if _doi_registered(doi)]
    if drafts:
        report.append(
            "- Drafts of the next revision, for information: "
            + ", ".join(f"https://doi.org/{doi}" for doi in drafts)
            + "."
        )
    return report, attention


def check_catalog() -> tuple[list[str], bool]:
    """Report whether the catalog copy is current and intact."""
    report = [
        f"- Pinned release: usnistgov/oscal-content {PINNED_TAG}, commit "
        f"`{PINNED_COMMIT[:12]}`, `{PINNED_PATH}/` copied to "
        "`src/nist_sp_800_171/schema/oscal-content/`."
    ]
    attention = False

    tagged = _tag_commit(PINNED_TAG)
    if tagged is None:
        attention = True
        report.append(
            f"- **usnistgov/oscal-content no longer has the tag `{PINNED_TAG}`.**"
        )
    elif tagged != PINNED_COMMIT:
        attention = True
        report.append(
            f"- **The tag `{PINNED_TAG}` now names commit `{tagged[:12]}`, not the "
            f"pinned `{PINNED_COMMIT[:12]}`.** Compare the two before moving any pin."
        )

    pinned_shas, pinned_folder = _blobs_at(PINNED_COMMIT)
    report += _unlisted(pinned_folder, PINNED_TAG)

    latest = json.loads(_get(f"{API}/releases/latest"))["tag_name"]
    if _version_key(latest) > _version_key(PINNED_TAG):
        latest_shas, latest_folder = _blobs_at(latest)
        changed = False
        if not latest_folder:
            changed = attention = True
            report.append(
                f"- **usnistgov/oscal-content {latest} no longer holds `{PINNED_PATH}/`.**"
            )
        for name, (source, pinned_sha) in sorted(PINNED_BLOBS.items()):
            if not latest_folder and source.startswith(f"{PINNED_PATH}/"):
                continue
            theirs = latest_shas[name]
            if theirs is None:
                changed = attention = True
                report.append(
                    f"- **usnistgov/oscal-content {latest} no longer holds `{source}`.**"
                )
            elif theirs != pinned_sha:
                changed = attention = True
                report.append(
                    f"- **usnistgov/oscal-content {latest} changes `{source}`.** Replace "
                    f"`src/nist_sp_800_171/schema/oscal-content/{name}` with the file at that "
                    f"tag (https://github.com/usnistgov/oscal-content/tree/{latest}), move the "
                    "pins here and in the schema header, and run `just test`."
                )
        if not changed:
            report.append(
                f"- Latest release: {latest}, which holds the pinned files unchanged."
            )
        report += _unlisted(latest_folder, latest)
        editions = _listing(EDITIONS_PATH, latest)
        if not editions:
            attention = True
            report.append(
                f"- **usnistgov/oscal-content {latest} no longer holds `{EDITIONS_PATH}/`.**"
            )
        others = {
            n for n, e in editions.items() if e["type"] == "dir"
        } - PINNED_EDITIONS
        if others:
            attention = True
            report.append(
                f"- **usnistgov/oscal-content {latest} holds another revision of SP 800-171:** "
                + ", ".join(f"`{EDITIONS_PATH}/{e}/`" for e in sorted(others))
                + "."
            )
    else:
        report.append(f"- Latest release: {latest}, the pinned one.")

    matching, differing = 0, []
    for name, (source, pinned_sha) in sorted(PINNED_BLOBS.items()):
        path = COPY / name
        if not path.is_file():
            differing.append(f"`{name}` is missing from the copy")
        elif pinned_shas[name] != pinned_sha:
            differing.append(f"`{source}` at {PINNED_TAG} is not the pinned blob")
        elif _blob_sha(path) != pinned_sha:
            differing.append(f"`{name}` differs from `{source}` at {PINNED_TAG}")
        else:
            matching += 1
    extra = sorted(p.name for p in COPY.iterdir() if p.name not in PINNED_BLOBS)
    differing += [f"`{name}` is in the copy but not pinned" for name in extra]
    report.append(
        f"- {matching} of {len(PINNED_BLOBS)} copied files match the pinned commit byte for byte."
    )
    if differing:
        attention = True
        report.append(f"- **{len(differing)} problem(s) with the copy:**")
        report += [f"  - {d}" for d in differing]
    return report, attention


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines, attention = [], False
    # A check that cannot reach doi.org or GitHub becomes a line of the
    # report rather than a traceback, so the other check still runs and the
    # issue says what failed.
    for name, part in (("editions", check_editions), ("catalog", check_catalog)):
        try:
            found, needs = part()
        except (urllib.error.URLError, TimeoutError, OSError) as err:
            found, needs = [f"- **The {name} check could not finish: {err}.**"], True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())
