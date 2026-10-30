# Change Log

## 2026-10-30

* **Changed**: nist-sp-800-171 LinkML schema now says `family_number` is a slot of its own, so the dataclasses key the families by their number.
* **Changed**: Generated artefacts no longer says `just test` leaves a generation date; LinkML 1.12.1 writes none.
* **Changed**: Update the upstream pins now regenerates the project, the docs and the adapt copy before `just test`.
* **Prose**: reworded 23 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Changed**: Test data and tests now counts 43 counter-examples, with a reference missing its citation or its address among them.
* **Changed**: the generators' settings moved from `config.yaml` to `.linkml/generators.yaml`.
* **Changed**: nist-sp-800-171 LinkML schema now says the parameter maps to `oscal:Parameter`, the class lmodel/oscal's copy renames OscalParameter, and that a reference requires its citation and a doi.org address.
* **Changed**: NIST's SP 800-171 catalog copy now gives the counts as the catalog's and names the three places where it departs from the publication.
* **Changed**: Test data and tests now counts 41 counter-examples, each naming where it fails, and covers the stubbed watch tests, the catalog's known departures, the check of valid examples against the catalog and the oscal mapping check.
* **Changed**: Media Protection now says that the publication, unlike NIST's catalog, has 03.13.08 address 03.08.06.
* **Changed**: Validate data against the schema now names LinkML 1.12.1 and the nine rules `docs/index.md` lists as checked over the catalog alone.
* **Changed**: Update the upstream pins now covers the watch's new findings: a dropped folder or file, a moved tag, a file NIST adds, and a check that could not finish.
* **Changed**: Upstream watch now says the job stops after ten minutes and reports a check that could not finish.
* **Changed**: Security policy now counts four Dependabot entries, the website's npm packages among them.
* **Changed**: Documentation site now says the old class pages redirect to their successors' pages.
* **Changed**: Element names and the shared namespace now says the schema rules test checks the oscal mappings.
* **Changed**: Security policy now says that a ruleset on `main` blocks deletion and force-pushes, as `SECURITY.md` does since the repository's settings were read; two settings remain not in force.
* **Added**: Documentation site, from `website/site.config.mjs` and `website/README.md`.
* **Added**: nist-sp-800-171 LinkML schema, from `src/nist_sp_800_171/schema/nist_sp_800_171.yaml`, its adapt copy and the lokf-adapt recipes.
* **Added**: NIST's SP 800-171 catalog copy, from `src/nist_sp_800_171/schema/oscal-content/`, NOTICE and the watch's pins.
* **Added**: Generated artefacts, from the justfile's recipes, `config.yaml` and `project/`.
* **Added**: Test data and tests, from `tests/`.
* **Added**: Scope, influences and mappings, from the README, the changelog and `docs/about.md`.
* **Added**: Element names and the shared namespace, from `docs/about.md`, the README, `.linkmllint.yaml` and the schema rules test.
* **Added**: Family, from the class `Sp800171Family` and NIST's catalog copy.
* **Added**: Security requirement, from the classes `Sp800171Requirement` and `Sp800171RequirementItem` and NIST's catalog copy.
* **Added**: Withdrawn requirement, from the enum `Sp800171RequirementStatus` and NIST's catalog copy.
* **Added**: Organization-defined parameter (ODP), from the class `Sp800171Parameter` and NIST's catalog copy.
* **Added**: Assessment objective, from the class `Sp800171AssessmentObjective` and NIST's catalog copy.
* **Added**: Assessment method, from the class `Sp800171AssessmentMethod` and NIST's catalog copy.
* **Added**: Regenerate and test after a schema change, from CONTRIBUTING.md and the recipes.
* **Added**: Validate data against the schema, from `docs/index.md`.
* **Added**: Update the upstream pins, from `scripts/check_upstream_release.py` and its tests.
* **Added**: Cut a release, from `.releaserc.json`, the changelog and CONTRIBUTING.md.
* **Added**: AI covenant, from `AI_COVENANT.md`.
* **Added**: License and attribution, from NOTICE, LICENSE and the README.
* **Added**: Security policy, from `SECURITY.md` and the Dependabot settings.
* **Added**: Build and test (main.yaml), from `.github/workflows/main.yaml`.
* **Added**: Lint & docs (lint-and-docs.yaml), from `.github/workflows/lint-and-docs.yaml`.
* **Added**: Upstream watch (upstream-watch.yaml), from `.github/workflows/upstream-watch.yaml`.
* **Added**: Semantic release (semantic-release.yml), from `.github/workflows/semantic-release.yml`.
* **Added**: Knowledge Registrar (knowledge-registrar.yaml), from `.github/workflows/knowledge-registrar.yaml`.
* **Added**: Knowledge Librarian (knowledge-librarian.yaml), from `.github/workflows/knowledge-librarian.yaml`.
* **Added**: Knowledge Release (knowledge-release.yaml), from `.github/workflows/knowledge-release.yaml`.
* **Added**: Knowledge sync (knowledge-sync.yaml), from `.github/workflows/knowledge-sync.yaml`.
* **Added**: Knowledge website (knowledge-website.yaml), from `.github/workflows/knowledge-website.yaml`.
* **Added**: Access Control, the family 03.01, from NIST's catalog copy.
* **Added**: Awareness and Training, the family 03.02, from NIST's catalog copy.
* **Added**: Audit and Accountability, the family 03.03, from NIST's catalog copy.
* **Added**: Configuration Management, the family 03.04, from NIST's catalog copy.
* **Added**: Identification and Authentication, the family 03.05, from NIST's catalog copy.
* **Added**: Incident Response, the family 03.06, from NIST's catalog copy.
* **Added**: Maintenance, the family 03.07, from NIST's catalog copy.
* **Added**: Media Protection, the family 03.08, from NIST's catalog copy.
* **Added**: Personnel Security, the family 03.09, from NIST's catalog copy.
* **Added**: Physical Protection, the family 03.10, from NIST's catalog copy.
* **Added**: Risk Assessment, the family 03.11, from NIST's catalog copy.
* **Added**: Security Assessment and Monitoring, the family 03.12, from NIST's catalog copy.
* **Added**: System and Communications Protection, the family 03.13, from NIST's catalog copy.
* **Added**: System and Information Integrity, the family 03.14, from NIST's catalog copy.
* **Added**: Planning, the family 03.15, from NIST's catalog copy.
* **Added**: System and Services Acquisition, the family 03.16, from NIST's catalog copy.
* **Added**: Supply Chain Risk Management, the family 03.17, from NIST's catalog copy.
* **Added**: NIST SP 800-171 Revision 3, from NIST's publication and project pages.
* **Added**: NIST SP 800-171A Revision 3, from NIST's publication page and the schema.
* **Added**: Knowledge sources map, the bootstrap's map of what each source yields and how to re-check it, with the paths left out on purpose.
* **Removal**: the sidecar's two example services, which the bootstrap's concepts replace.

## 2026-10-29

* **Initialization**: Scaffolded the LOKF bundle for nist-sp-800-171 with placeholder
  services. Real concepts to follow.
