"""Checks scripts/check_upstream_release.py against a stubbed upstream.

The script asks the GitHub API and doi.org what NIST has published. These
tests replace its one network function, _get, with answers built here, so
they read no network: a newer release that dropped the catalog's folder, a
network failure, a file NIST adds beside the catalog, and a moved tag.
"""

import importlib.util
import io
import json
import re
import urllib.error
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent


@pytest.fixture
def watch():
    """A fresh copy of the script's module, so a stub never outlives a test."""
    spec = importlib.util.spec_from_file_location(
        "watch_under_test", ROOT / "scripts" / "check_upstream_release.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _not_found(url):
    return urllib.error.HTTPError(url, 404, "Not Found", {}, io.BytesIO(b"{}"))


class Upstream:
    """What the GitHub API and doi.org answer: by default, the pinned release
    as the latest one, the tag on the pinned commit, and the pinned files."""

    def __init__(self, watch):
        self.watch = watch
        self.latest = watch.PINNED_TAG
        self.tag_commit = watch.PINNED_COMMIT
        self.registered = {watch.PINNED_DOI}
        self.doi_error = None
        self.listings = {}
        self.release(watch.PINNED_COMMIT)

    def release(self, ref, folder=True, extra=(), editions=("rev3",)):
        """The listings a ref holds: the pinned folder with the pinned and
        the uncopied files and any extra ones, LICENSE.md and the editions."""
        w = self.watch
        files = [
            {"name": source.rpartition("/")[2], "sha": sha, "type": "file"}
            for source, sha in w.PINNED_BLOBS.values()
            if source.startswith(f"{w.PINNED_PATH}/")
        ]
        files += [{"name": n, "sha": "0" * 40, "type": "file"} for n in w.UNCOPIED]
        files += [{"name": n, "sha": "1" * 40, "type": "file"} for n in extra]
        if folder:
            self.listings[(w.PINNED_PATH, ref)] = files
        _source, license_sha = w.PINNED_BLOBS["LICENSE.md"]
        self.listings[("LICENSE.md", ref)] = {
            "name": "LICENSE.md",
            "sha": license_sha,
            "type": "file",
        }
        self.listings[(w.EDITIONS_PATH, ref)] = [
            {"name": e, "type": "dir"} for e in editions
        ]

    def __call__(self, url):
        w = self.watch
        if url.startswith(w.DOI_API):
            if self.doi_error:
                raise self.doi_error
            if url[len(w.DOI_API) :] in self.registered:
                return b'{"responseCode": 1}'
            raise _not_found(url)
        path = url[len(w.API) :]
        if path == "/releases/latest":
            return json.dumps({"tag_name": self.latest}).encode()
        if path == f"/git/ref/tags/{w.PINNED_TAG}":
            return json.dumps({"object": {"type": "tag", "sha": "a" * 40}}).encode()
        if path == f"/git/tags/{'a' * 40}":
            return json.dumps(
                {"object": {"type": "commit", "sha": self.tag_commit}}
            ).encode()
        match = re.fullmatch(r"/contents/(.+)\?ref=(.+)", path)
        if match and (match[1], match[2]) in self.listings:
            return json.dumps(self.listings[(match[1], match[2])]).encode()
        raise _not_found(url)


def _run(watch, upstream, tmp_path):
    watch._get = upstream
    report = tmp_path / "report.md"
    code = watch.main(["--report", str(report)])
    return code, report.read_text()


def test_the_pinned_release_needs_nothing(watch, tmp_path):
    """With nothing moved, the report says so and the exit is 0."""
    code, text = _run(watch, Upstream(watch), tmp_path)
    assert code == 0, text
    assert "2 of 2 copied files match" in text
    assert "**" not in text


def test_a_newer_release_without_the_folder_is_reported(watch, tmp_path):
    """A newer release whose contents API answers 404 for the catalog's folder
    is a finding, not a traceback."""
    upstream = Upstream(watch)
    upstream.latest = "v1.7.0"
    upstream.release("v1.7.0", folder=False)
    code, text = _run(watch, upstream, tmp_path)
    assert code == 1
    assert f"v1.7.0 no longer holds `{watch.PINNED_PATH}/`" in text
    assert "changes `" not in text


def test_a_network_failure_still_writes_the_report(watch, tmp_path):
    """When doi.org cannot be reached, the editions check says so, the catalog
    check still runs, and the exit is 1."""
    upstream = Upstream(watch)
    upstream.doi_error = urllib.error.URLError("timed out")
    code, text = _run(watch, upstream, tmp_path)
    assert code == 1
    assert "**The editions check could not finish: <urlopen error timed out>.**" in text
    assert "2 of 2 copied files match" in text


def test_a_file_nist_adds_is_reported_for_information(watch, tmp_path):
    """A new file beside the catalog at a newer release is named, but sets no
    attention when the pinned files are unchanged."""
    upstream = Upstream(watch)
    upstream.latest = "v1.7.0"
    upstream.release("v1.7.0", extra=["NIST_SP800-171_rev3_profile.json"])
    code, text = _run(watch, upstream, tmp_path)
    assert code == 0, text
    assert "For information" in text
    assert "`NIST_SP800-171_rev3_profile.json`" in text
    assert "holds the pinned files unchanged" in text


def test_a_moved_tag_is_reported(watch, tmp_path):
    """A pinned tag that now names another commit is a finding."""
    upstream = Upstream(watch)
    upstream.tag_commit = "b" * 40
    code, text = _run(watch, upstream, tmp_path)
    assert code == 1
    assert f"The tag `{watch.PINNED_TAG}` now names commit `{'b' * 12}`" in text


def test_a_changed_licence_at_a_newer_release_is_reported(watch, tmp_path):
    """Every pinned file is compared at a newer release, LICENSE.md included."""
    upstream = Upstream(watch)
    upstream.latest = "v1.7.0"
    upstream.release("v1.7.0")
    upstream.listings[("LICENSE.md", "v1.7.0")]["sha"] = "c" * 40
    code, text = _run(watch, upstream, tmp_path)
    assert code == 1
    assert "v1.7.0 changes `LICENSE.md`" in text
