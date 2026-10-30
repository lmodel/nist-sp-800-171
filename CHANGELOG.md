# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

### Added

- **A LinkML schema of NIST Special Publication (SP) 800-171 Revision 3**, the security requirements for protecting controlled unclassified information (CUI) in nonfederal systems and organizations, with the assessment procedures of SP 800-171A Revision 3. It holds the seventeen families, the 97 security requirements in force and the 33 withdrawn ones with the requirements that took their place where the catalog names them, each requirement's statement items, discussion, references and SP 800-53 source controls, the 88 organization-defined parameters, and the assessment objectives and methods.
- **A copy of NIST's SP 800-171 catalog from usnistgov/oscal-content v1.6.0, and a weekly upstream watch.** A test derives the whole publication from the copy and holds it to the validator and to the publication's counts, and the watch also asks doi.org whether NIST has published Revision 4.
- **`.lokf/nist-sp-800-171.yaml`, the schema's `lokf adapt` copy, rooted on the family, the security requirement and the organization-defined parameter.** The knowledge release attaches it as `schema-<tag>-nist-sp-800-171.yaml`, and tests hold its names apart from those of the Linked Open Knowledge Format (LOKF) and of the slsa, github-actions, oscal, spdx and nist-sp-800-218 copies, with which it shares no key.
- **An example of each class and a counter-example for each constraint**, held to the validator by `just test`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.59.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.

### Changed

- **The schema models the publication's own elements, not a copy of a catalog in the Open Security Controls Assessment Language (OSCAL).** The OSCAL-shaped classes shared names with LOKF's and lmodel/oscal's, and their `class_uri: linkml:Any` let a catalog with any keys validate.
- **The schema's name is `nist_sp_800_171`, as its file and package are; the project's name is `nist-sp-800-171`, as the repository is; and the Python project's name is `nist-sp-800-171-linkml`.** PyPI publishing stays off.

### Removed

- **The PyPI publishing workflow and the mkdocs site and its preview.** The knowledge website replaces the site.
- **The unpinned copy of NIST's catalog under `tests/data/nist/`.** The pinned copy under `src/nist_sp_800_171/schema/oscal-content/` replaces it.
