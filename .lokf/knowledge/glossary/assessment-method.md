---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/glossary/assessment-method
genre: reference
title: Assessment method
description: In SP 800-171A, one of the three methods applied to a requirement, examine, interview or test, with the assessment objects (documents, people, processes or mechanisms) it is applied to. The schema renders one as `Sp800171AssessmentMethod`, with the method in `requirement_method_kind` and the objects in `requirement_method_objects`.
definition: One of the three methods SP 800-171A applies to a requirement, examine, interview or test, with the assessment objects it is applied to.
resource: src/nist_sp_800_171/schema/nist_sp_800_171.yaml
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/references/sp-800-171a
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/datasets/nist-sp-800-171-linkml-schema
sources:
  - id: nist_sp_800_171.yaml
    resource: src/nist_sp_800_171/schema/nist_sp_800_171.yaml
    title: the class Sp800171AssessmentMethod
  - id: nist_sp800-171_rev3_catalog.json
    resource: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json
    title: the catalog's elements
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:13:03Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T08:32:20Z"
---

# Assessment method

The schema describes an assessment method as one of the three methods SP 800-171A applies to a requirement, examine, interview or test, with the assessment objects it is applied to. It renders one as `Sp800171AssessmentMethod`, which requires `requirement_method_kind`, a value of `Sp800171AssessmentMethodKind`, and `requirement_method_objects`, one entry per object.[^nist_sp_800_171.yaml] NIST's catalog renders a method as an `assessment-method` part whose `method` property is `EXAMINE`, `INTERVIEW` or `TEST`, with its objects in one `assessment-objects` part separated by blank lines.[^nist_sp800-171_rev3_catalog.json] Revision 3 has 281 methods: 95 examine, 95 interview and 91 test. Two requirements in force, 03.01.22 and 03.14.03, have no method in the catalog, and four more have no test method; `tests/test_upstream.py` holds those gaps as the catalog gives them.

[^nist_sp_800_171.yaml]: src/nist_sp_800_171/schema/nist_sp_800_171.yaml, the class Sp800171AssessmentMethod and the enum Sp800171AssessmentMethodKind
[^nist_sp800-171_rev3_catalog.json]: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json, the assessment-method parts
