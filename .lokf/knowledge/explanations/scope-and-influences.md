---
type: Explanation
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/explanations/scope-and-influences
genre: explanation
title: Scope, influences and mappings
description: "What the schema renders and what it leaves out: SP 800-171 Revision 3 with the procedures of SP 800-171A Revision 3 and nothing beyond them, with lmodel/slsa as its one influence on layout. It maps its classes to lmodel/oscal's, as NIST's catalog renders them, carries each requirement's SP 800-53 source controls as data, and names the publications the requirements reference; it models neither the publication's other chapters, SP 800-172 nor the withdrawn requirements' former text."
resource: README.md
about:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/datasets/nist-sp-800-171-linkml-schema
sources:
  - id: readme.md
    resource: README.md
    title: the What it models, Influences, Mappings and Not modelled here sections
  - id: changelog.md
    resource: CHANGELOG.md
    title: the Changed entries
  - id: about.md
    resource: docs/about.md
    title: the section on what is left out
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:13:03Z"
status: draft
verified:
  - by: process:ktl-librarian
    at: "2026-10-30T08:54:19Z"
---

# Scope, influences and mappings

The schema renders one publication, SP 800-171, at one final revision, Revision 3, with the assessment procedures that SP 800-171A Revision 3 gives each requirement. The README's Influences section says that nothing beyond the two publications shaped it, and that its release asset and governance files follow lmodel/slsa.[^readme.md]

## Why the publication's own elements

The schema models the family, the security requirement, the statement item, the organization-defined parameter, the assessment objective, the assessment method and the reference, which [the glossary](../glossary/index.md) defines. The changelog says that it replaced classes copied from the shape of an OSCAL catalog. Those classes shared names with LOKF's and lmodel/oscal's, and their `class_uri: linkml:Any` let a catalog with any keys validate.[^changelog.md] NIST's catalog in OSCAL stays in the repository as the upstream copy that the tests read.

## Mappings

The README says that the schema crosses to three kinds of vocabulary and borrows from none. NIST's catalog renders a family as an OSCAL group, a requirement as a control, a statement item, an objective and a method as parts, a parameter as a parameter and a reference as a back-matter resource. So each class names its lmodel/oscal counterpart in `broad_mappings`. The OSCAL class is the more general one. A requirement's `source_controls` carries the identifiers of the SP 800-53 Revision 5 controls it is drawn from, such as `AC-02`. That is data in a document, not a mapping in the schema, which binds no prefix for a model of SP 800-53. `Sp800171Reference` names each publication a requirement references by its short name, with the citation and the digital object identifier the catalog gives it.

## Not modelled here

- the publication's chapters and appendices outside the requirements, such as the introduction, the glossary and the tailoring criteria;
- SP 800-171A beyond the objectives and methods the catalog carries for each requirement;
- the enhanced security requirements of SP 800-172, and what a withdrawn requirement once required, beyond its number, status and successors;
- the catalog's own metadata, roles and parties, and the four back-matter resources no requirement references.[^about.md]

[^readme.md]: README.md, the Influences, Mappings and Not modelled here sections
[^changelog.md]: CHANGELOG.md, the Changed entries under Unreleased
[^about.md]: docs/about.md, What is left out
