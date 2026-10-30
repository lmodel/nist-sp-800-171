---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/glossary/withdrawn-requirement
genre: reference
title: Withdrawn requirement
description: "In SP 800-171 Revision 3, a requirement of an earlier revision that the revision withdrew: it keeps its number, is marked withdrawn, and names the requirements that incorporate or address what it required where the catalog states them. The schema renders one as an `Sp800171Requirement` with `requirement_status: withdrawn`."
definition: A requirement that Revision 3 of SP 800-171 withdrew, which keeps its number and names the requirements that incorporate or address what it required, where the catalog states them, and nothing else.
resource: src/nist_sp_800_171/schema/nist_sp_800_171.yaml
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/references/sp-800-171
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/datasets/nist-sp-800-171-linkml-schema
sources:
  - id: nist_sp_800_171.yaml
    resource: src/nist_sp_800_171/schema/nist_sp_800_171.yaml
    title: the class Sp800171Requirement
  - id: nist_sp800-171_rev3_catalog.json
    resource: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json
    title: the catalog's elements
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:13:03Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T09:04:23Z"
---

# Withdrawn requirement

Revision 3 withdrew 33 of the 130 numbered requirements. The schema renders each as an `Sp800171Requirement` with `requirement_status: withdrawn`, the one value of `Sp800171RequirementStatus`, and its successors in `incorporated_into_requirements` or `addressed_by_requirements`, as the catalog states them. A requirement in force carries no status.[^nist_sp_800_171.yaml] In NIST's catalog a withdrawn requirement carries the property `status: withdrawn` and a title that is its number. It has links with the relations `incorporated_into` (24 in all) or `addressed_by` (17 in all) to the requirements that took its place. Six withdrawn requirements name none.[^nist_sp800-171_rev3_catalog.json] `tests/test_upstream.py` holds that a withdrawn requirement carries nothing else, and that each successor is in force.

[^nist_sp_800_171.yaml]: src/nist_sp_800_171/schema/nist_sp_800_171.yaml, the class Sp800171Requirement and the enum Sp800171RequirementStatus
[^nist_sp800-171_rev3_catalog.json]: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json, the controls with the status property
