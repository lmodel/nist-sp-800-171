# nist-sp-800-171

This project is a LinkML model of Special Publication (SP) 800-171 Revision 3,
in which the National Institute of Standards and Technology (NIST) sets the
security requirements for protecting controlled unclassified information (CUI)
in nonfederal systems and organizations, and of the assessment procedures that
SP 800-171A Revision 3 gives each requirement. It covers the families, the
security requirements with their statements, discussions, references and
source controls, the organization-defined parameters, and the assessment
objectives and methods.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): how the elements are named and what the model leaves out
- [`nist_sp_800_171.yaml`](schema/nist_sp_800_171.yaml): the schema

## Validating data

`linkml-validate -s src/nist_sp_800_171/schema/nist_sp_800_171.yaml -C Sp800171Requirement requirement.yaml`
checks a file against the JSON Schema generated from the schema, and
`tests/test_data.py` holds every example to it.

Validate a file before loading it into either model in
`src/nist_sp_800_171/datamodel/`. LinkML 1.12.1 generates models that check
less:

- The dataclasses check required fields and enum values, but no pattern.
- The Pydantic models also check the patterns a field carries itself, such as
  the form of `sp800171_revision` or a blank discussion. They do not check the
  patterns of the seven identifier types, so a family number, a requirement,
  item, parameter or objective identifier, a source control or a cited
  publication's name goes unchecked.

No check covers these rules:

- that a requirement's identifier starts with its family's number, a statement
  item's with its requirement's, a numbered item's with its lettered item's,
  and a parameter's and an objective's with their requirement's;
- that no family, requirement, statement item, parameter or objective
  identifier repeats;
- that a requirement has a statement or statement items, never both;
- that a requirement in force carries a title, a discussion, at least one
  source control and at least one assessment objective;
- that a withdrawn requirement carries nothing but its identifier, its status
  and the requirements that incorporate it or those that address it, never
  both, that only a withdrawn requirement carries those, and that each of them
  is in force;
- that an objective's identifier is A and the item it assesses, or its
  requirement when it names no item, with at most a bracketed number, so the
  catalog's dotted form `A.03.01.01.b.01` passes the pattern as the objective
  of a numbered item;
- that an objective's assessed item is an item of the same requirement;
- that every insert placeholder in a statement, an item, a choice or an
  objective has the catalog's form and names a parameter of the same
  requirement;
- that a selection parameter has both its choices and its count, and any
  other parameter its usage and guideline.

`tests/test_upstream.py` checks all of them over NIST's catalog of Revision 3.
