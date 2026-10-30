---
type: GlossaryTerm
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/glossary/security-requirement
genre: reference
title: Security requirement
description: In SP 800-171, a numbered, named requirement for protecting CUI, such as 03.01.01 Account Management, with its statement, discussion, references and SP 800-53 source controls, the organization-defined parameters its statement leaves open, and the assessment objectives and methods SP 800-171A gives it. The schema renders one as `Sp800171Requirement`, with its identifier in `requirement_id`.
definition: A numbered, named requirement of SP 800-171 for protecting controlled unclassified information, with its statement, discussion, references and source controls, the parameters its statement leaves to the organization, and the assessment procedures of SP 800-171A.
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
    at: "2026-10-30T08:32:20Z"
---

# Security requirement

The schema describes a security requirement as a numbered, named requirement for protecting CUI, with its statement, discussion, references and source controls, the organization-defined parameters its statement leaves open, and the assessment objectives and methods SP 800-171A gives it. It renders one as `Sp800171Requirement`, which requires `requirement_id`, such as `03.01.01`. A statement is either one piece of text in `requirement_statement` or lettered items in `requirement_items`, each an `Sp800171RequirementItem` with an identifier such as `03.01.01.a` and its numbered items.[^nist_sp_800_171.yaml] NIST's catalog renders a requirement as a control of class `requirement`, whose `statement` and `guidance` parts hold the statement and the discussion, and whose `reference` links point at the publications it cites and at the SP 800-53 controls it is drawn from.[^nist_sp800-171_rev3_catalog.json] A [withdrawn requirement](withdrawn-requirement.md) keeps its number and names its successors.

[^nist_sp_800_171.yaml]: src/nist_sp_800_171/schema/nist_sp_800_171.yaml, the classes Sp800171Requirement and Sp800171RequirementItem
[^nist_sp800-171_rev3_catalog.json]: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json, the controls of class requirement
