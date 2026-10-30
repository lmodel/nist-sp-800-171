---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/glossary/family
genre: reference
title: Family
description: In SP 800-171, one of the seventeen groups the security requirements are sorted into, numbered 03.01 Access Control to 03.17 Supply Chain Risk Management. The schema renders a family as `Sp800171Family`, with its number in `family_number`.
definition: One of the seventeen groups that SP 800-171 Revision 3 sorts its security requirements into, each with a number such as 03.01 and a name such as Access Control.
resource: src/nist_sp_800_171/schema/nist_sp_800_171.yaml
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/references/sp-800-171
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/datasets/nist-sp-800-171-linkml-schema
sources:
  - id: nist_sp_800_171.yaml
    resource: src/nist_sp_800_171/schema/nist_sp_800_171.yaml
    title: the class Sp800171Family
  - id: nist_sp800-171_rev3_catalog.json
    resource: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json
    title: the catalog's elements
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:13:03Z"
status: draft
---

# Family

The schema describes a family as one of the seventeen groups that SP 800-171 Revision 3 sorts its security requirements into, such as Access Control (03.01) or Supply Chain Risk Management (03.17). It renders a family as `Sp800171Family`, which requires `family_number` and a `title` and may hold the family's requirements in `family_requirements`.[^nist_sp_800_171.yaml] NIST's catalog renders each family as a group of class `family` with no text of its own, so a family's `description` is in the words of whoever records it.[^nist_sp800-171_rev3_catalog.json] In a knowledge bundle a requirement names its family with `isPartOf` instead. The bundle describes each family under [families](../families/index.md).

[^nist_sp_800_171.yaml]: src/nist_sp_800_171/schema/nist_sp_800_171.yaml, the class Sp800171Family
[^nist_sp800-171_rev3_catalog.json]: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json, the groups
