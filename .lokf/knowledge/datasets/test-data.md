---
type: Dataset
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/datasets/test-data
genre: reference
title: Test data and tests
description: "The schema's tests: nine valid examples and 43 counter-examples under `tests/data/`, `tests/test_data.py`, which holds each to the validator, `tests/test_upstream.py`, which derives the publication from NIST's catalog, `tests/test_watch.py`, which runs the upstream watch against a stubbed upstream, and `tests/test_schema_rules.py`, which holds the adapt copy apart from LOKF and the slsa, github-actions, oscal, spdx and nist-sp-800-218 copies in `tests/neighbours/`."
resource: tests
sources:
  - id: data
    resource: tests/data
    title: the valid and invalid examples
  - id: test_data.py
    resource: tests/test_data.py
    title: the data tests
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: the derivation, the counts and the known departures
  - id: test_watch.py
    resource: tests/test_watch.py
    title: the watch against a stubbed upstream
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: the neighbours and their checksums
  - resource: tests/neighbours
    title: the five released adapt copies
  - resource: tests/data/README.md
    title: the naming rule
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:39:12Z"
status: draft
---

# Test data and tests

`tests/data/valid/` holds nine examples, one for each class and two for `Sp800171Requirement`, one of them withdrawn, and `tests/data/invalid/` holds 43 counter-examples, each invalid for one reason.[^data] A file's class is the part of its name before the first hyphen, such as `Sp800171Requirement-withdrawn.yaml`, and a counter-example's first line, `# Fails at:`, names the place in the data where it breaks the schema. The counter-examples break each constraint the schema states:

- a missing required field, or an empty list where at least one entry is required;
- an identifier of the wrong form, such as the catalog's dotted form of a parameter identifier, a family number without its zeros, an objective's identifier without its A or a source control without its zero;
- an unknown status, method or selection count;
- a withdrawn requirement incorporated into a family or addressed by a statement item;
- a blank statement, item, discussion, parameter label, determination or assessment object;
- a reference whose address is not a digital object identifier at doi.org;
- a key the class does not declare.

`tests/test_data.py` loads each valid example into the dataclasses, holds each to the validator, which must pass a valid example and fail a counter-example at the place its first line names, and checks that every class has an example.[^test_data.py] `tests/test_upstream.py` derives the whole of Revision 3 from NIST's catalog copy and holds it to the validator and to the catalog's counts, as [NIST's SP 800-171 catalog copy](sp-800-171-catalog-copy.md) says. It also holds the rules no pattern can check, which `docs/index.md` lists: that identifiers nest and never repeat, that a requirement has a statement or items and never both, what a requirement in force and a withdrawn one carry, the form of an objective's identifier, that an insert placeholder names a parameter of its own requirement, and what a parameter carries. It holds the places where the catalog departs from the publication in `KNOWN_DEPARTURES`, so a corrected catalog fails it, and it holds each valid example to the facts the catalog gives for the identifiers the example names.[^test_upstream.py] `tests/test_watch.py` runs `scripts/check_upstream_release.py` against answers it builds itself, with no network: a release that drops the catalog's folder, a network failure, a file NIST adds, a moved tag and a changed licence.[^test_watch.py]

`tests/test_schema_rules.py` checks the adapt copy against LOKF's `lokf.yaml` and five neighbours: the schema assets of lmodel/slsa v0.7.0, lmodel/github-actions v0.2.1, lmodel/oscal v0.1.0, lmodel/spdx v0.1.0 and lmodel/nist-sp-800-218 v0.1.0, each pinned by its SHA-256 checksum.[^test_schema_rules.py] No class, enum, type or subset may share a name, and the copy shares no key with a neighbour. The test also checks that the copy roots exactly the three concept classes, that every mapping uses a prefix the copy binds, and that every `oscal:` mapping names a class of lmodel/oscal's copy. `just test` runs the tests, generates the project into `tmp/`, and runs the examples through `linkml-run-examples`.

[^data]: tests/data, valid/ and invalid/
[^test_data.py]: tests/test_data.py, the four tests
[^test_upstream.py]: tests/test_upstream.py, the tests, COUNTS and KNOWN_DEPARTURES
[^test_watch.py]: tests/test_watch.py, the stubbed upstream and its six tests
[^test_schema_rules.py]: tests/test_schema_rules.py, NEIGHBOURS and the tests
