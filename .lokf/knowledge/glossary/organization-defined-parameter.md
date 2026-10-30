---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/glossary/organization-defined-parameter
genre: reference
title: Organization-defined parameter (ODP)
description: In SP 800-171, a value, such as a time period or a frequency, that a requirement statement leaves to the organization, identified as SP 800-171A writes it, such as A.03.01.01.ODP[01], with the guideline SP 800-171A gives for defining it; a few are selections among choices. The schema renders one as `Sp800171Parameter`, with its identifier in `odp_id`.
definition: A value, such as a time period or a frequency, that a requirement statement of SP 800-171 leaves to the organization, with the guideline SP 800-171A gives for defining it; a few parameters are a selection among choices instead of a value.
resource: src/nist_sp_800_171/schema/nist_sp_800_171.yaml
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/references/sp-800-171a
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/datasets/nist-sp-800-171-linkml-schema
sources:
  - id: nist_sp_800_171.yaml
    resource: src/nist_sp_800_171/schema/nist_sp_800_171.yaml
    title: the class Sp800171Parameter
  - id: nist_sp800-171_rev3_catalog.json
    resource: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json
    title: the catalog's elements
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:13:03Z"
status: draft
---

# Organization-defined parameter (ODP)

The schema describes an organization-defined parameter as a value, such as a time period or a frequency, that a requirement statement leaves to the organization, with the guideline SP 800-171A gives for defining it. It renders one as `Sp800171Parameter`, which requires `odp_id`, such as `A.03.01.01.ODP[01]`, and `odp_label`, the kind of value, and may hold `odp_usage`, how the statement names it, `odp_guideline`, the determination that the value is defined, and for a selection `odp_choices` with `odp_selection_count`.[^nist_sp_800_171.yaml] NIST's catalog renders a parameter as an OSCAL parameter of its requirement, with the publication's identifier in its `label` property and a `select` block for a selection; a statement marks the parameter's place with an insert placeholder that names it.[^nist_sp800-171_rev3_catalog.json] Revision 3 has 88 parameters, 3 of them selections, and a knowledge bundle may type a concept with `Sp800171Parameter` and name its requirement's concept in `isPartOf`.

[^nist_sp_800_171.yaml]: src/nist_sp_800_171/schema/nist_sp_800_171.yaml, the class Sp800171Parameter
[^nist_sp800-171_rev3_catalog.json]: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json, the params of each control
