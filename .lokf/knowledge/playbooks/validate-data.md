---
type: Playbook
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/playbooks/validate-data
genre: how-to
title: Validate data against the schema
description: "How to validate SP 800-171 data with `linkml-validate` before loading it into the generated Python models, which check less: the dataclasses check no pattern, and the Pydantic models miss the identifier types' patterns. No check covers the nesting of identifiers, a repeated one, or the shape of a withdrawn requirement."
resource: docs/index.md
about:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/datasets/nist-sp-800-171-linkml-schema
sources:
  - id: docs-index.md
    resource: docs/index.md
    title: the Validating data section
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:32:20Z"
status: draft
---

# Validate data against the schema

Run `linkml-validate -s src/nist_sp_800_171/schema/nist_sp_800_171.yaml -C Sp800171Requirement requirement.yaml`, naming the class the file holds. It checks the file against the JSON Schema the validator generates from the schema, and `tests/test_data.py` holds every example to the same check.[^docs-index.md]

Validate a file before loading it into either model in `src/nist_sp_800_171/datamodel/`. The page says that the models LinkML 1.12.1 generates check less:

- the dataclasses check required fields and enum values, but no pattern;
- the Pydantic models also check the patterns a field carries itself, such as the form of `sp800171_revision` or a blank discussion, but not the patterns of the seven identifier types.

No check covers nine rules: that identifiers nest inside the identifier of what holds them; that no family, requirement, item, parameter or objective identifier repeats; that a requirement has a statement or items and never both; that a requirement in force carries a title, a discussion, a source control and an objective; that a withdrawn requirement carries nothing but its identifier, status and successors, never both kinds, that only a withdrawn one carries those and that each is in force; that an objective's identifier is A and the item it assesses, or its requirement, with at most a bracketed number, so the catalog's dotted form passes the pattern; that an objective's assessed item belongs to the same requirement; that an insert placeholder has the catalog's form and names a parameter of the same requirement; and that a selection parameter has both its choices and its count, and any other parameter its usage and guideline. `tests/test_upstream.py` checks all of them over NIST's catalog of Revision 3.

[^docs-index.md]: docs/index.md, Validating data
