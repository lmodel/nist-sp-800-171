---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/glossary/assessment-objective
genre: reference
title: Assessment objective
description: In SP 800-171A, one determination statement that an assessor checks for a requirement, such as A.03.01.01.b[01], tied to the requirement or to one item of its statement. The schema renders one as `Sp800171AssessmentObjective`, with its identifier in `requirement_objective_id`.
definition: One determination statement of SP 800-171A that an assessor checks, tied to a requirement or to one item of its statement.
resource: src/nist_sp_800_171/schema/nist_sp_800_171.yaml
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/references/sp-800-171a
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/datasets/nist-sp-800-171-linkml-schema
sources:
  - id: nist_sp_800_171.yaml
    resource: src/nist_sp_800_171/schema/nist_sp_800_171.yaml
    title: the class Sp800171AssessmentObjective
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

# Assessment objective

The schema describes an assessment objective as one determination statement of SP 800-171A that an assessor checks, tied to the requirement or to one item of its statement. It renders one as `Sp800171AssessmentObjective`, which requires `requirement_objective_id`, such as `A.03.01.01.b[01]`, and `requirement_determination`. An objective may name the item it assesses in `assessed_requirement_item`.[^nist_sp_800_171.yaml] NIST's catalog renders an objective as an `assessment-objective` part of its requirement, with an `assessment-for` link to the statement item it assesses. The catalog writes the number of a split objective with a dot, where SP 800-171A writes it in square brackets.[^nist_sp800-171_rev3_catalog.json] Revision 3 has 422 objectives.

[^nist_sp_800_171.yaml]: src/nist_sp_800_171/schema/nist_sp_800_171.yaml, the class Sp800171AssessmentObjective and the type sp800171_objective_identifier
[^nist_sp800-171_rev3_catalog.json]: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json, the assessment-objective parts
