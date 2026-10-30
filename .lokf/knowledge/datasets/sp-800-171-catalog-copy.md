---
type: Dataset
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/datasets/sp-800-171-catalog-copy
genre: reference
title: NIST's SP 800-171 catalog copy
description: NIST's catalog of SP 800-171 Revision 3 in the Open Security Controls Assessment Language (OSCAL), which carries the assessment procedures of SP 800-171A Revision 3 too, copied with NIST's licence from usnistgov/oscal-content v1.6.0 into `src/nist_sp_800_171/schema/oscal-content/` and matched to that release by git object hash. The tests derive the whole publication from it.
resource: src/nist_sp_800_171/schema/oscal-content
license: CC0-1.0
derivedFrom:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/references/sp-800-171
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/references/sp-800-171a
sources:
  - id: nist_sp800-171_rev3_catalog.json
    resource: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json
    title: the metadata, the groups, the controls and the back matter
  - id: notice
    resource: NOTICE
    title: the NIST sections
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the pins
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the derivation, the counts and the known departures
  - id: about.md
    resource: docs/about.md
    title: where NIST's catalog departs from the publication
  - resource: src/nist_sp_800_171/schema/oscal-content/LICENSE.md
    title: NIST's licence
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:32:20Z"
status: draft
---

# NIST's SP 800-171 catalog copy

`src/nist_sp_800_171/schema/oscal-content/` holds two files: `NIST_SP800-171_rev3_catalog.json`, the catalog of SP 800-171 Revision 3 that NIST publishes in the Open Security Controls Assessment Language (OSCAL), and NIST's `LICENSE.md`. NOTICE says that both were retrieved from usnistgov/oscal-content at commit `f0de6d8d8c059d374f15e0ae07508d82e370fc1d`, the v1.6.0 release, and are identical to their counterparts there.[^notice] It also says that NIST's work is in the public domain within the United States, and that NIST dedicates it to the worldwide public domain under CC0 1.0.

## What the catalog holds

The catalog's metadata names its framework version `SP_800_171_3_0_0` and its publication status `Final`, and numbers the catalog itself `1.1.0`. It says that NIST's Cybersecurity And Privacy Open Reference Datasets In OSCAL (CAPORDINO) generated it. It is written in OSCAL `v1.2.3`.[^nist_sp800-171_rev3_catalog.json] Its 17 groups, of class `family`, are the families. The groups' controls of class `requirement`, 130 in all, are the security requirements. 97 carry a `label` property and are in force. 33 carry the property `status: withdrawn` and links with the relations `incorporated_into` or `addressed_by` to the requirements that took their place.

A requirement in force has these parts, the last two from SP 800-171A:

- a `statement` part, with `item` parts where the statement is lettered;
- a `guidance` part that is the discussion;
- `assessment-objective` parts, with an `assessment-for` link to the item each assesses;
- `assessment-method` parts, with their `assessment-objects`.

Its `params` are the organization-defined parameters, and its `reference` links point at the back matter's 224 resources: 65 publications with citations, and 155 resources titled with SP 800-53 control identifiers, such as `AC-02`, that link to NIST's reference tool.

`tests/test_upstream.py` derives an `Sp800171Publication` from the copy with the standard library's JSON parser, validates it, and holds it to the catalog's counts:

- 17 families;
- 130 requirements, of which 97 in force and 33 withdrawn;
- 24 incorporated-into and 17 addressed-by links;
- 252 statement items;
- 88 parameters, of which 3 selections;
- 422 assessment objectives and 281 assessment methods;
- 199 references to 65 publications, and 157 source-control references to 155 controls.[^test_upstream.py]

The test writes an objective's identifier as SP 800-171A does, with the number of a split objective in square brackets, where the catalog writes it with a dot.

The catalog departs from the publication in three places, which `docs/about.md` lists with the publications' page numbers and the test holds as `KNOWN_DEPARTURES`. SP 800-171A gives requirements 03.01.22 and 03.14.03 the examine, interview and test methods, which the catalog leaves out, so the publication has 287 methods. SP 800-171 and SP 800-171A say that 03.13.08 addresses the withdrawn 03.08.06, where the catalog says it incorporates it, so the publication has 23 incorporated-into and 18 addressed-by links.[^about.md]

## The pins

`scripts/check_upstream_release.py` pins the tag `v1.6.0`, the commit, and each file's git object hash: `814a0937a20cc1cad1bd7542847093c66d73af59` for the catalog and `109af23dd24c2c465143aeab12ffebfffe2a4cd5` for the licence.[^check_upstream_release.py] The test checks the hashes offline, and the upstream watch checks them against the pinned commit every week. [Update the upstream pins](../playbooks/update-upstream-pins.md) says how to replace the copy.

[^notice]: NOTICE, the section NIST's SP 800-171 catalog in OSCAL
[^nist_sp800-171_rev3_catalog.json]: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json, the metadata, the groups and the back matter
[^test_upstream.py]: tests/test_upstream.py, the COUNTS table and the derive function
[^check_upstream_release.py]: scripts/check_upstream_release.py, PINNED_TAG, PINNED_COMMIT and PINNED_BLOBS
[^about.md]: docs/about.md, the section Where NIST's catalog departs from the publication
