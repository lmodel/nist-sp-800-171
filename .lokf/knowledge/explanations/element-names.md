---
type: Explanation
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/explanations/element-names
genre: explanation
title: Element names and the shared namespace
description: "How the schema names its elements so that its adapt copy can sit beside LOKF's schema and the slsa, github-actions, oscal, spdx and nist-sp-800-218 copies: classes with the `Sp800171` prefix, every slot qualified with the publication's own noun, NIST's identifiers kept in the publication's forms, `title` and `description` carrying LOKF's IRIs, and no other key shared, which `tests/test_schema_rules.py` checks."
resource: docs/about.md
about:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/datasets/nist-sp-800-171-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
    title: the naming paragraphs
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: SHARED_WITH_NEIGHBOURS and the name tests
  - id: linkmllint.yaml
    resource: .linkmllint.yaml
    title: the comment
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:32:20Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T09:10:34Z"
---

# Element names and the shared namespace

Element names are the schema's own. Classes carry the `Sp800171` prefix, such as `Sp800171Requirement`, so that they can be imported beside other vocabularies. Slots are snake_case, and each is qualified with the publication's own noun, such as `requirement_discussion` or `odp_guideline`, so that none shares a name with a neighbouring schema. The identifiers keep the forms NIST gives them: `03.01` for a family, `03.01.01` for a requirement, `03.01.01.a` for a statement item, `A.03.01.01.ODP[01]` for a parameter and `A.03.01.01.b[01]` for an assessment objective.[^about.md] Every element is in the `nist_sp_800_171:` namespace, `https://w3id.org/lmodel/nist-sp-800-171/`.

`.linkmllint.yaml` applies linkml-lint's recommended rules as they are and relaxes none: the enums' values, such as `withdrawn` and `one_or_more`, are snake_case, and the publication's identifiers are values the patterned types describe, not element names.[^linkmllint.yaml]

## Beside other schemas

A host imports the adapt copy beside LOKF's `lokf.yaml` and other adapt copies, and LinkML merges them into one namespace, where the last definition of a name wins silently. The README says that no class, enum or type therefore shares a name with LOKF's or with the copies of slsa, github-actions, oscal, spdx and nist-sp-800-218. A slot shares a name only where it carries LOKF's meaning and IRI, as `title` and `description` do, so `lokf adapt` folds the two into LOKF's and renames nothing.[^readme.md]

`tests/test_schema_rules.py` checks the copy against `lokf.yaml` and the schema assets of slsa v0.7.0, github-actions v0.2.1, oscal v0.1.0, spdx v0.1.0 and nist-sp-800-218 v0.1.0. Its list of keys shared with each neighbour is empty, so a new shared key fails the test, and it checks that every `oscal:` mapping names a class of the oscal copy, by the IRI a renamed class keeps.[^test_schema_rules.py]

[^about.md]: docs/about.md, the paragraph on element names
[^linkmllint.yaml]: .linkmllint.yaml, the comment
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS and SHARED_WITH_NEIGHBOURS
