---
type: Playbook
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Update the upstream pins
description: "What to do when the weekly upstream watch reports that NIST registered the next final revision of SP 800-171, released a changed catalog in usnistgov/oscal-content, or that the copy drifted: replace the copy whole from one release, move the pins in `scripts/check_upstream_release.py` and the schema header, and run the tests."
resource: scripts/check_upstream_release.py
about:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/datasets/sp-800-171-catalog-copy
sources:
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the docstring, the pins and the report lines
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: the item on the catalog copy
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the pin and revision tests
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:13:03Z"
status: draft
---

# Update the upstream pins

`scripts/check_upstream_release.py` runs every Monday in [Upstream watch](../workflows/upstream-watch.md) with the standard library alone. It reports three kinds of finding.[^check_upstream_release.py]

- **NIST registered `10.6028/NIST.SP.800-171r4`**, the identifier of the next final revision. Read the publication, decide whether the schema moves to it, and replace the copy once usnistgov/oscal-content publishes its catalog. A draft's identifier (`.ipd`, `.2pd` or `.fpd`) is reported for information only.
- **A newer release of usnistgov/oscal-content changes the catalog**, or holds a new revision folder under `nist.gov/SP800-171/`. A release that leaves the catalog's blob as it was is reported and needs nothing.
- **A copied file differs from its pinned blob**, or the folder holds a file the script does not pin.

To replace the copy, take both files from one release: the catalog from `nist.gov/SP800-171/rev3/json/` and `LICENSE.md` from the root. Never edit them.[^contributing.md] Then move `PINNED_TAG`, `PINNED_COMMIT` and `PINNED_BLOBS` in the script, and the `oscal_content_tag` and `oscal_content_commit` annotations and the `see_also` tree in the schema header, and update NOTICE. Run `just test`: `tests/test_upstream.py` checks that the header and the script name the same pins, that each file has its pinned hash, and that the derived publication still validates with the publication's counts.[^test_upstream.py] A new revision also moves the header's `version`, the `cprt_framework_version` annotation and `PINNED_PATH`, `EDITIONS_PATH` and the identifiers in the script.

[^check_upstream_release.py]: scripts/check_upstream_release.py, the docstring and check_editions and check_catalog
[^contributing.md]: CONTRIBUTING.md, the item on the catalog copy
[^test_upstream.py]: tests/test_upstream.py, the pin, hash and revision tests
