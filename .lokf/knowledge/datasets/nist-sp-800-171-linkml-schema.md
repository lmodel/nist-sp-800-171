---
type: Dataset
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/datasets/nist-sp-800-171-linkml-schema
genre: reference
title: nist-sp-800-171 LinkML schema
description: "The LinkML schema of NIST SP 800-171 Revision 3, `src/nist_sp_800_171/schema/nist_sp_800_171.yaml` (schema id `https://w3id.org/lmodel/nist-sp-800-171`, version 3.0.0): eight classes, three enums and seven identifier types. Its `lokf adapt` copy `.lokf/nist-sp-800-171.yaml`, rooted on the family, the security requirement and the organization-defined parameter, is the bundle's domain schema."
resource: src/nist_sp_800_171/schema/nist_sp_800_171.yaml
version: 3.0.0
license: Apache-2.0
derivedFrom:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/references/sp-800-171
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/references/sp-800-171a
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/datasets/sp-800-171-catalog-copy
sources:
  - id: nist_sp_800_171.yaml
    resource: src/nist_sp_800_171/schema/nist_sp_800_171.yaml
    title: the header, the classes, the enums and the types
  - id: readme.md
    resource: README.md
    title: the What it models and Knowledge Trust Ladder (KTL) sections
  - id: project.justfile
    resource: project.justfile
    title: the lokf-adapt recipes and their roots
  - id: nist-sp-800-171.yaml
    resource: .lokf/nist-sp-800-171.yaml
    title: the notes lokf adapt wrote
  - resource: .lokf/justfile
    title: the schema line
  - resource: .lokf/pyproject.toml
    title: the tool.lokf table
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:32:20Z"
status: draft
---

# nist-sp-800-171 LinkML schema

`src/nist_sp_800_171/schema/nist_sp_800_171.yaml` is the schema, titled "Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations (SP 800-171 Revision 3)". Its header gives `version: 3.0.0`, the publication's revision as NIST's Cybersecurity and Privacy Reference Tool numbers it. Its `source: https://doi.org/10.6028/NIST.SP.800-171r3` is the digital object identifier of NIST Special Publication (SP) 800-171 Revision 3.[^nist_sp_800_171.yaml] Its annotations name the reference tool's identifier `SP_800_171_3_0_0`, the publication date `2024-05`, and the usnistgov/oscal-content tag `v1.6.0` and commit `f0de6d8d8c059d374f15e0ae07508d82e370fc1d` of the catalog copy. A comment says that `scripts/check_upstream_release.py` reads the same pins, that the catalog's own metadata version numbers the catalog and not the publication, and that the release tags are the schema's own versions. The schema declares the prefix `nist_sp_800_171:` as `https://w3id.org/lmodel/nist-sp-800-171/` and the license Apache-2.0, and it imports only `linkml:types`.

## Classes

- **`Sp800171Publication`** is the tree root: one revision as a whole. It requires `sp800171_revision`, one number such as `3`, and at least one family in `requirement_families`.
- **`Sp800171Family`** is one of the seventeen families. It requires `family_number`, such as `03.01`, and a `title`, and it may hold its requirements in `family_requirements`.
- **`Sp800171Requirement`** is a security requirement. It requires `requirement_id`, such as `03.01.01`. It may hold a `title`, a `requirement_statement` or `requirement_items`, a `requirement_discussion`, `requirement_parameters`, `requirement_objectives`, `requirement_methods`, `requirement_references` and `source_controls`. A withdrawn requirement sets `requirement_status: withdrawn` and may name its successors in `incorporated_into_requirements` or `addressed_by_requirements`.
- **`Sp800171RequirementItem`** is one lettered or numbered item of a statement. It requires `requirement_item_id`, such as `03.01.01.a`, and `requirement_item_text`, and it may hold `requirement_subitems`.
- **`Sp800171Parameter`** is an organization-defined parameter. It requires `odp_id`, such as `A.03.01.01.ODP[01]`, and `odp_label`, and it may hold `odp_usage`, `odp_guideline`, `odp_choices` and `odp_selection_count`.
- **`Sp800171AssessmentObjective`** is one determination statement of SP 800-171A. It requires `requirement_objective_id`, such as `A.03.01.01.b[01]`, and `requirement_determination`, and it may name the item it assesses in `assessed_requirement_item`.
- **`Sp800171AssessmentMethod`** is one of the three methods. It requires `requirement_method_kind` and at least one object in `requirement_method_objects`.
- **`Sp800171Reference`** is a publication a requirement references. It requires `cited_publication`, such as `SP 800-63-3`, `cited_publication_citation`, and `cited_publication_url`, which must be a digital object identifier at doi.org.

The three enums are `Sp800171RequirementStatus` (`withdrawn`), `Sp800171AssessmentMethodKind` (`examine`, `interview`, `test`) and `Sp800171SelectionCount` (`one`, `one_or_more`). Seven types hold the forms of the identifiers, each with a pattern: `sp800171_family_identifier`, `sp800171_requirement_identifier`, `sp800171_item_identifier`, `sp800171_odp_identifier`, `sp800171_objective_identifier`, `sp800171_source_control_identifier` and `sp800171_cited_publication_name`. The schema's slots `title` and `description` carry the IRIs `schema:name` and `schema:description`.

A blank statement, item text, discussion, parameter label, determination or assessment object fails the pattern `^\s*\S`, which the validator and the Pydantic models read alike.

## Mappings

Each class names a class of lmodel/oscal in `broad_mappings`: `oscal:Catalog` for the publication, `oscal:Group` for the family, `oscal:Control` for the requirement, `oscal:Part` for the statement item, the objective and the method, `oscal:Parameter` for the parameter and `oscal:Resource` for the reference. A comment in the header says that NIST's catalog renders the elements that way. [Scope, influences and mappings](../explanations/scope-and-influences.md) says more.

## As the bundle's domain schema

A LOKF domain schema is a LinkML schema that imports LOKF's `lokf.yaml` and adds a host's classes and keys, so that `lokf validate` checks the concepts typed with them. The README says that this bundle's domain schema is `.lokf/nist-sp-800-171.yaml`, which `lokf adapt` writes from the schema. Edit the source, never the copy.[^readme.md] The `schema :=` line of `.lokf/justfile` and the `[tool.lokf]` table of `.lokf/pyproject.toml` both name the copy.

`project.justfile` passes three roots to `lokf adapt`: `Sp800171Family`, `Sp800171Requirement` and `Sp800171Parameter`. Its comment says that these are the three elements that SP 800-171 gives an identifier and that other documents cite, such as a system security plan or an assessment. It also says that a statement item, an objective, a method and a reference stay inlined in their requirement.[^project.justfile] The copy's notes say that `lokf adapt` re-rooted the three classes on `Concept` and folded `title` and `description` into LOKF's slots.[^nist-sp-800-171.yaml] The copy renames nothing, and `Sp800171Publication` is no longer a tree root in it. The concepts under `families/` in this bundle are typed `Sp800171Family`.

The generated models, `project/` and the adapt copy come from this file: see [Generated artefacts](generated-artefacts.md). [Element names and the shared namespace](../explanations/element-names.md) says why no class, enum or type shares a name with LOKF's or a neighbour's.

[^nist_sp_800_171.yaml]: src/nist_sp_800_171/schema/nist_sp_800_171.yaml, the header and the classes
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^project.justfile]: project.justfile, the knowledge bundle recipes
[^nist-sp-800-171.yaml]: .lokf/nist-sp-800-171.yaml, the notes
