---
type: Playbook
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test after a schema change
description: "How to change the schema and check it: `uv sync --group dev`, edit `src/nist_sp_800_171/schema/nist_sp_800_171.yaml`, then `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and the pre-commit hooks before a pull request."
resource: CONTRIBUTING.md
about:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/datasets/nist-sp-800-171-linkml-schema
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: the Development setup and Before opening a pull request sections
  - id: justfile
    resource: justfile
    title: the lint, gen-project, gen-doc and test recipes
  - id: project.justfile
    resource: project.justfile
    title: the lokf-adapt recipes
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:13:03Z"
status: draft
---

# Regenerate and test after a schema change

You need Python 3.10 or later, uv and just. Clone the repository, run `uv sync --group dev`, and run `just --list` to see the recipes.[^contributing.md]

1. Edit `src/nist_sp_800_171/schema/nist_sp_800_171.yaml`, and name the section or table of SP 800-171 or SP 800-171A it renders in the pull request.
2. Run `just lint`, which runs `linkml-lint --ignore-warnings` over the schema folder, so that only errors fail it.[^justfile]
3. Run `just gen-project` and `just gen-doc`, and commit what they write in `project/`, `src/nist_sp_800_171/datamodel/` and `docs/schema/`.
4. Run `just lokf-adapt`, which rewrites `.lokf/nist-sp-800-171.yaml`, and commit it. `just lokf-adapt-check` fails when the copy is stale.[^project.justfile]
5. Run `just test`. Add an example of a new class to `tests/data/valid/` and a counter-example of a new constraint to `tests/data/invalid/`.
6. Run the pre-commit hooks on what you staged, with `uvx pre-commit run`.

CI installs with `uv sync --locked`, so a dependency change commits `uv.lock` too. A change in behaviour adds an entry under `## [Unreleased]` in `CHANGELOG.md`.

[^contributing.md]: CONTRIBUTING.md, Development setup and Before opening a pull request
[^justfile]: justfile, the lint recipe
[^project.justfile]: project.justfile, lokf-adapt and lokf-adapt-check
