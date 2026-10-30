# About nist-sp-800-171

This page is for anyone reading the [LinkML](https://linkml.io) schema's
elements: it says how they are named and what the model leaves out.

Special Publication (SP) 800-171 sorts its security requirements into
families. A requirement has a number, a name, a statement, a discussion and
references, and the statement may leave values, the organization-defined
parameters (ODPs), to the organization. SP 800-171A gives each requirement
assessment objectives, the determination statements an assessor checks, and
the examine, interview and test methods with their assessment objects. The
schema gives each of these a class, and holds the families under one
publication document.

Element names are the schema's own. Classes carry the `Sp800171` prefix
(`Sp800171Family`, `Sp800171Requirement`) so they can be imported beside other
vocabularies. Slots are snake_case, and each is qualified with the
publication's own noun (`requirement_discussion`, `odp_guideline`) so that
none shares a name with a neighbouring schema. The identifiers keep the forms
the National Institute of Standards and Technology (NIST) gives them: `03.01`
for a family, `03.01.01` for a requirement, `03.01.01.a` for a statement
item, `A.03.01.01.ODP[01]` for a parameter and `A.03.01.01.b[01]` for an
assessment objective. NIST's catalog writes an objective's bracketed number
as a dotted one, and the schema's test turns it back. Every element is in the
`nist_sp_800_171:` namespace (`https://w3id.org/lmodel/nist-sp-800-171/`).

The descriptions are this project's own words. NIST's own text of each
requirement, discussion, parameter and assessment procedure stays in NIST's
catalog, which the repository keeps beside the schema.

## What is left out

The schema models the requirements of Revision 3 and the procedures of
SP 800-171A Revision 3 as NIST's catalog carries them. A withdrawn requirement
records its number, its status and the requirements that took its place, and
nothing of what it once required. The schema holds none of the publication's
prose outside the requirements, nothing of SP 800-172's enhanced requirements,
and none of the catalog's own metadata.

## Where NIST's catalog departs from the publication

The schema renders what NIST's catalog states, and the catalog departs from
the two publications in three places. `tests/test_upstream.py` holds each as
`KNOWN_DEPARTURES`, so a corrected catalog fails the test and is noticed. The
page numbers are the publications' printed ones.

- SP 800-171A Revision 3 gives requirement `03.01.22` the examine, interview
  and test methods (page 21); the catalog gives it none.
- SP 800-171A Revision 3 gives requirement `03.14.03` the same three methods
  (page 86); the catalog gives it none. So the catalog holds 281 assessment
  methods and the publication 287.
- SP 800-171 Revision 3 (page 47) and SP 800-171A Revision 3 (page 60) say
  that `03.13.08` addresses the withdrawn requirement `03.08.06`; the catalog
  says that `03.13.08` incorporates it. So the catalog has 24
  incorporated-into and 17 addressed-by links and the publication 23 and 18.

Both NIST's text and its catalog number the two objectives of item
`03.01.12.d` with one digit, `A.03.01.12.d[1]`; the schema writes them with
two, `A.03.01.12.d[01]`, as it writes every other objective.

## Reference

- [Special Publication 800-171 Revision 3 on NIST's site](https://csrc.nist.gov/pubs/sp/800/171/r3/final)
- [Special Publication 800-171A Revision 3](https://doi.org/10.6028/NIST.SP.800-171Ar3)
- [The project for protecting controlled unclassified information](https://csrc.nist.gov/projects/protecting-controlled-unclassified-information)
- [NIST's SP 800-171 catalog in the Open Security Controls Assessment Language](https://github.com/usnistgov/oscal-content/tree/v1.6.0/nist.gov/SP800-171/rev3)
