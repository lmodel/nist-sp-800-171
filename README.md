<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# nist-sp-800-171

NIST SP 800-171 Protecting Controlled Unclassified Information (CUI) in Nonfederal Systems and Organizations, Revision 3, with the SP 800-171A assessment procedures (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/nist-sp-800-171](https://lmodel.github.io/nist-sp-800-171)

## What it models

The security requirements for protecting controlled unclassified information (CUI) in nonfederal systems and organizations, which the National Institute of Standards and Technology (NIST) sets in [Special Publication (SP) 800-171 Revision 3](https://doi.org/10.6028/NIST.SP.800-171r3) of May 2024, and the procedures for assessing them in [SP 800-171A Revision 3](https://doi.org/10.6028/NIST.SP.800-171Ar3):

* **Families** (`Sp800171Family`): the seventeen families that sort the requirements, from Access Control (`03.01`) to Supply Chain Risk Management (`03.17`).
* **Security requirements** (`Sp800171Requirement`): the 130 numbered requirements, such as `03.01.01` Account Management. 97 are in force, with a statement, a discussion, references and the SP 800-53 controls they are drawn from. 33 are withdrawn and keep their number, their status and the requirements that incorporate or address what they required.
* **Statement items** (`Sp800171RequirementItem`): the 252 lettered and numbered items of the 68 requirement statements that have them, such as `03.01.01.a` and `03.01.01.c.01`. The other 29 statements are one piece of text.
* **Organization-defined parameters** (`Sp800171Parameter`): the 88 values, such as `A.03.01.01.ODP[01]`, that the requirements leave to the organization, each with the guideline SP 800-171A gives for defining it. Three are selections among choices.
* **Assessment objectives** (`Sp800171AssessmentObjective`): the 422 determination statements of SP 800-171A, such as `A.03.01.01.b[01]`, each tied to the requirement or to one item of its statement.
* **Assessment methods** (`Sp800171AssessmentMethod`): the 281 examine, interview and test entries of SP 800-171A, each with its assessment objects.
* **References** (`Sp800171Reference`): the 199 references from the requirements to 65 NIST publications, with their citations and addresses.
* **The publication** (`Sp800171Publication`): one revision as a single document that holds all of these.

The schema header's `version` is the publication's revision, 3.0.0, as NIST's Cybersecurity and Privacy Reference Tool numbers it (`SP_800_171_3_0_0`). Its `source` is the publication's digital object identifier (DOI). NIST also publishes the requirements and the assessment procedures together as a catalog in the Open Security Controls Assessment Language (OSCAL). [src/nist_sp_800_171/schema/oscal-content/](src/nist_sp_800_171/schema/oscal-content) holds that catalog as usnistgov/oscal-content released it in v1.6.0, matched to the release by git object hash. `tests/test_upstream.py` derives the whole publication from the copy, validates it, and holds it to the counts above. A weekly workflow opens an issue when NIST registers the next final revision, changes the catalog, or the copy drifts.

Revision 3 is the current edition, and NIST has published no draft of a Revision 4. Release tags number the schema's versions.

## Influences

None beyond SP 800-171 and SP 800-171A themselves: the schema renders one publication, and its release asset and governance files follow [lmodel/slsa](https://github.com/lmodel/slsa).

## Mappings

The schema crosses to three kinds of vocabulary and borrows from none.

* **OSCAL**: NIST's catalog renders a family as an OSCAL group, a requirement as a control, a statement item, an objective and a method as parts, a parameter as a parameter, and a reference as a back-matter resource. Each class names its counterpart in [lmodel/oscal](https://github.com/lmodel/oscal) in `broad_mappings`, because the OSCAL class is the more general one.
* **SP 800-53 Revision 5**: a requirement's `source_controls` carries the identifiers of the controls it is drawn from, such as `AC-02` and `AC-02(03)`, as the catalog lists them among the requirement's references. That is data in a document, not a mapping in the schema, and the schema binds no prefix for a model of SP 800-53; [lmodel/nist-sp-800-53](https://github.com/lmodel/nist-sp-800-53) is where that model is being built.
* **The publications SP 800-171 references**: `Sp800171Reference` names each by its short name, such as `SP 800-63-3` or `FIPS 140-3`, with the citation and the DOI the catalog gives it.

## Not modelled here

* The publication's chapters and appendices outside the requirements themselves, such as the introduction, the glossary and the tailoring criteria.
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

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle, in the Linked Open Knowledge Format (LOKF). Its domain schema is `.lokf/nist-sp-800-171.yaml`, which `lokf adapt` writes from `src/nist_sp_800_171/schema/nist_sp_800_171.yaml`. Edit the source, never the copy. A release carries the copy as `schema-<tag>-nist-sp-800-171.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

`just lokf-adapt` rewrites the copy, and `just lokf-adapt-check` says when it is stale. `project.justfile` names the classes the copy roots on `Concept`, and a concept may name any of them as its `type`. In Obsidian, add these classes to the KTL Registrar and KTL Curator plugins' *Known LOKF types* setting:

```text
Sp800171Family, Sp800171Requirement, Sp800171Parameter
```

A concept writes the publication's identifier in `family_number`, `requirement_id` or `odp_id`. A requirement's concept names its family's concept in `isPartOf`, and a parameter's concept names its requirement's. A name and a description are the concept's own `title` and `description`.

A host imports the copy beside LOKF's schema, `lokf.yaml`, and beside other adapt copies. LinkML merges them into one namespace, where the last definition of a name wins silently. So no class, enum or type shares a name with LOKF's or with the copies of slsa, github-actions, oscal, spdx and nist-sp-800-218. A slot shares a name only where it carries LOKF's meaning and Internationalized Resource Identifier (IRI), as `title` and `description` do, so `lokf adapt` folds the two into LOKF's and renames nothing. The copy shares no other key with the five neighbours, and `tests/test_schema_rules.py` fails on a new shared name.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)).

SP 800-171 and SP 800-171A are works of the United States Government and are not subject to copyright in the United States. The schema's descriptions are this project's own words. NIST's catalog in [src/nist_sp_800_171/schema/oscal-content/](src/nist_sp_800_171/schema/oscal-content) keeps NIST's licence beside it: see [NOTICE](NOTICE).

This is not an official NIST project, and its use implies no endorsement by NIST.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
