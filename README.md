<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# nist-sp-800-171

NIST SP 800-171 Protecting Controlled Unclassified Information (CUI) in Nonfederal Systems and Organizations, Revision 3, with the SP 800-171A assessment procedures (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/nist-sp-800-171](https://lmodel.github.io/nist-sp-800-171)

## What it models

The schema models the security requirements for protecting controlled unclassified information (CUI) in nonfederal systems and organizations, which the National Institute of Standards and Technology (NIST) sets in [Special Publication (SP) 800-171 Revision 3](https://doi.org/10.6028/NIST.SP.800-171r3) of May 2024. [SP 800-171A Revision 3](https://doi.org/10.6028/NIST.SP.800-171Ar3) gives the procedures for assessing them. The schema holds the seventeen families (`Sp800171Family`), the 130 requirements (`Sp800171Requirement`) with their statement items and organization-defined parameters (`Sp800171Parameter`), the assessment objectives and methods of SP 800-171A, and the publications the requirements reference.

[src/nist_sp_800_171/schema/oscal-content/](src/nist_sp_800_171/schema/oscal-content) holds NIST's catalog of both publications in the Open Security Controls Assessment Language (OSCAL), from usnistgov/oscal-content v1.6.0, and `tests/test_upstream.py` derives the whole publication from it. [docs/about.md](docs/about.md#where-nists-catalog-departs-from-the-publication) lists where the catalog departs from the publication. A weekly workflow opens an issue when NIST registers the next final revision, changes the catalog, or the copy drifts.

## Mappings

* **OSCAL**: each class names its counterpart in [lmodel/oscal](https://github.com/lmodel/oscal) in `broad_mappings`: a family is a group, a requirement a control, and a statement item, an objective and a method are parts.
* **SP 800-53 Revision 5**: a requirement's `source_controls` lists the controls it is drawn from, such as `AC-02`, as data, not as a mapping.
* **Referenced publications**: `Sp800171Reference` names each by its short name, such as `FIPS 140-3`, with its citation and DOI.

## Not modelled here

* The publication's chapters and appendices outside the requirements, such as the introduction, the glossary and the tailoring criteria.
* SP 800-171A beyond the objectives and methods the catalog carries for each requirement.
* The enhanced security requirements of SP 800-172, and the requirements of Revision 2 that Revision 3 withdrew, except as a withdrawn requirement's number, status and successors.
* The catalog's own metadata, roles and parties, and the four back-matter resources that no requirement references.
* The rules no pattern can check, which [docs/index.md](docs/index.md) lists.

## Repository Structure

* [docs/](docs/): the website's pages, with the generated schema pages in [elements/](docs/elements/)
* [examples/](examples/): usage examples
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the upstream watch
* [src/nist_sp_800_171/schema/](src/nist_sp_800_171/schema): the LinkML schema, `nist_sp_800_171.yaml` (edit this), and NIST's catalog copy
* [src/nist_sp_800_171/datamodel/](src/nist_sp_800_171/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/schema/nist-sp-800-171.yaml`, is the copy `just lokf-adapt` writes from `src/nist_sp_800_171/schema/nist_sp_800_171.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-nist-sp-800-171.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots these classes on `Concept`, so a concept may name any of them as its `type`. In Obsidian, add them to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
Sp800171Family, Sp800171Requirement, Sp800171Parameter
```

A concept writes the publication's identifier in `family_number`, `requirement_id` or `odp_id`. A requirement's concept names its family's concept in `isPartOf`, and a parameter's concept names its requirement's.

No class, enum or type of the copy shares a name with LOKF's schema or with another lmodel copy, and `tests/test_schema_rules.py` fails on a new shared name.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in `.lokf/knowledge/` is under CC BY 4.0.

SP 800-171 and SP 800-171A are works of the United States Government and are not subject to copyright in the United States. The schema's descriptions are this project's own words, and NIST's catalog keeps NIST's licence beside it: see [NOTICE](NOTICE). This is not an official NIST project, and its use implies no endorsement by NIST.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
