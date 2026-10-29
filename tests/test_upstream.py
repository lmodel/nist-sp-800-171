"""Checks that the schema renders the revision NIST's catalog publishes.

NIST publishes SP 800-171 Revision 3 as an OSCAL catalog in
usnistgov/oscal-content, with the assessment procedures of SP 800-171A
Revision 3 inside it, and src/nist_sp_800_171/schema/oscal-content/ holds the
copy that scripts/check_upstream_release.py pins. These tests read the copy
with the standard library alone, derive from it the Sp800171Publication the
schema describes, and hold that document to the validator and to the
publication's counts.
"""

import hashlib
import importlib.util
import json
import re
from functools import lru_cache
from pathlib import Path

import yaml
from linkml.validator import validate

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "nist_sp_800_171" / "schema" / "nist_sp_800_171.yaml"
COPY = ROOT / "src" / "nist_sp_800_171" / "schema" / "oscal-content"
CATALOG = COPY / "NIST_SP800-171_rev3_catalog.json"

# The catalog prefixes its identifiers: SP_800_171_ on a family or a
# requirement, SR- on a statement item, assessment-objective_DS- on an
# objective. A back-matter resource titled like an SP 800-53 control, AC-02
# or AC-02(03), is a source control; every other reference is a publication.
CONTROL = re.compile(r"^[A-Z]{2}-[0-9]{2}(\([0-9]{2}\))?$")

# What SP 800-171 Revision 3 holds: seventeen families and 130 numbered
# requirements, of which 97 are in force and 33 withdrawn; the organization-
# defined parameters, statement items, assessment objectives and methods
# of those in force; the publications they reference and the SP 800-53
# controls they are drawn from.
COUNTS = {
    "families": 17,
    "requirements": 130,
    "requirements in force": 97,
    "withdrawn requirements": 33,
    "incorporated-into links": 24,
    "addressed-by links": 17,
    "withdrawn with no successor": 6,
    "statement items": 252,
    "statements as one text": 29,
    "discussions": 97,
    "parameters": 88,
    "selection parameters": 3,
    "assessment objectives": 422,
    "assessment methods": 281,
    "references": 199,
    "cited publications": 65,
    "source control references": 157,
    "source controls": 155,
}
METHODS = {"examine": 95, "interview": 95, "test": 91}
# The requirements in force whose assessment procedures the catalog gives no
# method, or no test method; every other one has all three.
WITHOUT_METHODS = {"03.01.22", "03.14.03"}
WITHOUT_TEST = {"03.06.03", "03.06.04", "03.12.05", "03.15.01"}


def _watch():
    spec = importlib.util.spec_from_file_location(
        "watch", ROOT / "scripts" / "check_upstream_release.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _blob_sha(path):
    data = path.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


@lru_cache(maxsize=1)
def _header():
    return yaml.safe_load(SCHEMA.read_text())


@lru_cache(maxsize=1)
def _catalog():
    return json.loads(CATALOG.read_text(encoding="utf-8"))["catalog"]


def _prop(element, name):
    return next(p["value"] for p in element.get("props", []) if p["name"] == name)


def _has_prop(element, name, value=None):
    return any(
        p["name"] == name and (value is None or p["value"] == value)
        for p in element.get("props", [])
    )


def _number(catalog_id):
    """The publication's identifier inside a catalog one: 03.01.01 from
    SP_800_171_03.01.01, 03.01.01.a from SR-03.01.01.a."""
    return catalog_id.rpartition("_")[2].removeprefix("SR-")


def _items(parts):
    return [
        {
            "requirement_item_id": _number(part["id"]),
            "requirement_item_text": part["prose"],
            **(
                {"requirement_subitems": _items(part["parts"])}
                if part.get("parts")
                else {}
            ),
        }
        for part in parts
        if part["name"] == "item"
    ]


def _parameter(param):
    entry = {"odp_id": _prop(param, "label"), "odp_label": param["label"]}
    if "usage" in param:
        entry["odp_usage"] = param["usage"]
    if "guidelines" in param:
        (guideline,) = param["guidelines"]
        entry["odp_guideline"] = guideline["prose"]
    if "select" in param:
        entry["odp_choices"] = param["select"]["choice"]
        entry["odp_selection_count"] = param["select"]["how-many"].replace("-", "_")
    return entry


def _objective(part, requirement_id):
    """The publication's form of an objective: A, the item it assesses and,
    when the catalog's identifier runs one dotted number past that item, the
    number in square brackets."""
    (link,) = [l["href"] for l in part["links"] if l["rel"] == "assessment-for"]
    assessed = _number(link.lstrip("#"))
    catalog_id = part["id"].removeprefix("assessment-objective_DS-A.")
    if catalog_id == assessed:
        objective_id = f"A.{assessed}"
    else:
        assert catalog_id.startswith(assessed + "."), part["id"]
        split = catalog_id[len(assessed) + 1 :]
        assert split.isdigit(), part["id"]
        objective_id = f"A.{assessed}[{int(split):02d}]"
    entry = {
        "requirement_objective_id": objective_id,
        "requirement_determination": part["prose"],
    }
    if assessed != requirement_id:
        entry["assessed_requirement_item"] = assessed
    return entry


def _method(part):
    (objects,) = part["parts"]
    return {
        "requirement_method_kind": _prop(part, "method").lower(),
        "requirement_method_objects": objects["prose"].split("\n\n"),
    }


def _requirement(control, resources):
    requirement_id = _number(control["id"])
    entry = {"requirement_id": requirement_id}
    if _has_prop(control, "label"):
        entry["title"] = control["title"]
    if _has_prop(control, "status", "withdrawn"):
        entry["requirement_status"] = "withdrawn"
    for rel, key in (
        ("incorporated_into", "incorporated_into_requirements"),
        ("addressed_by", "addressed_by_requirements"),
    ):
        targets = [l["href"] for l in control.get("links", []) if l["rel"] == rel]
        if targets:
            entry[key] = targets
    for part in control.get("parts", []):
        if part["name"] == "statement":
            if "prose" in part:
                entry["requirement_statement"] = part["prose"]
            else:
                entry["requirement_items"] = _items(part["parts"])
        elif part["name"] == "guidance":
            entry["requirement_discussion"] = part["prose"]
        elif part["name"] == "assessment-objective":
            entry.setdefault("requirement_objectives", []).append(
                _objective(part, requirement_id)
            )
        elif part["name"] == "assessment-method":
            entry.setdefault("requirement_methods", []).append(_method(part))
    if control.get("params"):
        entry["requirement_parameters"] = [_parameter(p) for p in control["params"]]
    for link in control.get("links", []):
        if link["rel"] != "reference":
            continue
        resource = resources[link["href"].lstrip("#")]
        if CONTROL.match(resource["title"]):
            entry.setdefault("source_controls", []).append(resource["title"])
        else:
            (rlink,) = resource["rlinks"]
            entry.setdefault("requirement_references", []).append(
                {
                    "cited_publication": resource["title"],
                    "cited_publication_citation": resource["citation"]["text"],
                    "cited_publication_url": rlink["href"],
                }
            )
    return entry


def derive(catalog):
    """The Sp800171Publication that the catalog's groups, controls, parts,
    parameters and links describe, in the schema's terms."""
    resources = {r["uuid"]: r for r in catalog["back-matter"]["resources"]}
    families = []
    for group in catalog["groups"]:
        assert group["class"] == "family", group["id"]
        requirements = []
        for control in group["controls"]:
            assert control["class"] == "requirement", control["id"]
            assert not control.get("controls"), control["id"]
            requirements.append(_requirement(control, resources))
        families.append(
            {
                "family_number": _number(group["id"]),
                "title": group["title"],
                "family_requirements": requirements,
            }
        )
    return {
        "sp800171_revision": _header()["version"].split(".")[0],
        "requirement_families": families,
    }


@lru_cache(maxsize=1)
def _publication():
    return derive(_catalog())


def _requirements():
    return [
        r for f in _publication()["requirement_families"] for r in f["family_requirements"]
    ]


def _in_force():
    return [r for r in _requirements() if "requirement_status" not in r]


def _withdrawn():
    return [r for r in _requirements() if r.get("requirement_status") == "withdrawn"]


def _count_items(items):
    return sum(1 + _count_items(i.get("requirement_subitems", [])) for i in items)


def test_copy_matches_the_pinned_blobs():
    """Every copied file has the git object hash the watch pins, so the copy
    is the file NIST published at the pinned commit, and nothing else is in
    the folder."""
    pinned = _watch().PINNED_BLOBS
    assert {p.name for p in COPY.iterdir()} == set(pinned)
    for name, (_source, sha) in pinned.items():
        assert _blob_sha(COPY / name) == sha, name


def test_header_pins_match_the_watch():
    """The header records the release, commit and publication the watch
    checks."""
    watch = _watch()
    header = _header()
    notes = header["annotations"]
    assert notes["oscal_content_tag"] == watch.PINNED_TAG
    assert notes["oscal_content_commit"] == watch.PINNED_COMMIT
    assert header["source"] == f"https://doi.org/{watch.PINNED_DOI}"
    tree = f"https://github.com/usnistgov/oscal-content/tree/{watch.PINNED_TAG}/"
    assert tree + watch.PINNED_PATH.rpartition("/")[0] in header["see_also"]


def test_catalog_is_the_pinned_revision():
    """The copy is NIST's final catalog of the revision in the header, by the
    identifier NIST's reference tool gives that revision. The catalog's own
    metadata version numbers the catalog, not the publication."""
    metadata = _catalog()["metadata"]
    version = _header()["version"]
    identifier = "SP_800_171_" + version.replace(".", "_")
    assert _header()["annotations"]["cprt_framework_version"] == identifier
    assert _prop(metadata, "framework-version-identifier") == identifier
    assert _prop(metadata, "publication-status") == "Final"
    assert metadata["version"] != version


def test_derived_publication_validates():
    """The whole of Revision 3, as the catalog gives it, is a valid
    Sp800171Publication."""
    report = validate(_publication(), str(SCHEMA), "Sp800171Publication")
    assert not report.results, [r.message for r in report.results][:10]


def test_counts_match_the_publication():
    """The derived document holds what the publication holds."""
    in_force, withdrawn = _in_force(), _withdrawn()
    references = [r for q in in_force for r in q.get("requirement_references", [])]
    sources = [s for q in in_force for s in q.get("source_controls", [])]
    counted = {
        "families": len(_publication()["requirement_families"]),
        "requirements": len(_requirements()),
        "requirements in force": len(in_force),
        "withdrawn requirements": len(withdrawn),
        "incorporated-into links": sum(
            len(q.get("incorporated_into_requirements", [])) for q in withdrawn
        ),
        "addressed-by links": sum(
            len(q.get("addressed_by_requirements", [])) for q in withdrawn
        ),
        "withdrawn with no successor": sum(
            1
            for q in withdrawn
            if "incorporated_into_requirements" not in q
            and "addressed_by_requirements" not in q
        ),
        "statement items": sum(
            _count_items(q.get("requirement_items", [])) for q in in_force
        ),
        "statements as one text": sum(
            1 for q in in_force if "requirement_statement" in q
        ),
        "discussions": sum(1 for q in in_force if "requirement_discussion" in q),
        "parameters": sum(len(q.get("requirement_parameters", [])) for q in in_force),
        "selection parameters": sum(
            1
            for q in in_force
            for p in q.get("requirement_parameters", [])
            if "odp_choices" in p
        ),
        "assessment objectives": sum(
            len(q.get("requirement_objectives", [])) for q in in_force
        ),
        "assessment methods": sum(
            len(q.get("requirement_methods", [])) for q in in_force
        ),
        "references": len(references),
        "cited publications": len({r["cited_publication"] for r in references}),
        "source control references": len(sources),
        "source controls": len(set(sources)),
    }
    assert counted == COUNTS
    methods = [m for q in in_force for m in q.get("requirement_methods", [])]
    assert {
        kind: sum(1 for m in methods if m["requirement_method_kind"] == kind)
        for kind in METHODS
    } == METHODS


def test_requirements_in_force_are_complete():
    """Every requirement in force has a title, a statement or items but not
    both, a discussion, at least one source control and at least one
    assessment objective; all but the listed ones have the three assessment
    methods; and every selection parameter has its choices."""
    for q in _in_force():
        rid = q["requirement_id"]
        assert "title" in q, rid
        assert ("requirement_statement" in q) != ("requirement_items" in q), rid
        assert "requirement_discussion" in q, rid
        assert q.get("source_controls"), rid
        assert q.get("requirement_objectives"), rid
        kinds = {m["requirement_method_kind"] for m in q.get("requirement_methods", [])}
        if rid in WITHOUT_METHODS:
            assert not kinds, rid
        elif rid in WITHOUT_TEST:
            assert kinds == {"examine", "interview"}, rid
        else:
            assert kinds == set(METHODS), rid
        for p in q.get("requirement_parameters", []):
            assert ("odp_choices" in p) == ("odp_selection_count" in p), p["odp_id"]


def test_withdrawn_requirements_are_bare():
    """A withdrawn requirement carries its number, its status and, where the
    catalog states them, the requirements that took its place, and nothing
    else; each of those requirements is in force."""
    in_force = {q["requirement_id"] for q in _in_force()}
    for q in _withdrawn():
        assert set(q) <= {
            "requirement_id",
            "requirement_status",
            "incorporated_into_requirements",
            "addressed_by_requirements",
        }, q["requirement_id"]
        successors = q.get("incorporated_into_requirements", []) + q.get(
            "addressed_by_requirements", []
        )
        assert set(successors) <= in_force, q["requirement_id"]
        assert not (
            "incorporated_into_requirements" in q and "addressed_by_requirements" in q
        ), q["requirement_id"]


def test_identifiers_nest_and_are_unique():
    """Each identifier starts with the identifier of what holds it, which no
    pattern in the schema can check, and none repeats within its kind."""
    seen = {"family": [], "requirement": [], "item": [], "odp": [], "objective": []}
    for family in _publication()["requirement_families"]:
        seen["family"].append(family["family_number"])
        for q in family["family_requirements"]:
            rid = q["requirement_id"]
            assert rid.startswith(family["family_number"] + "."), rid
            seen["requirement"].append(rid)
            items = []

            def collect(entries, parent):
                for item in entries:
                    assert item["requirement_item_id"].startswith(parent + "."), rid
                    items.append(item["requirement_item_id"])
                    collect(item.get("requirement_subitems", []), item["requirement_item_id"])

            collect(q.get("requirement_items", []), rid)
            seen["item"] += items
            for p in q.get("requirement_parameters", []):
                assert p["odp_id"].startswith(f"A.{rid}.ODP["), p["odp_id"]
                seen["odp"].append(p["odp_id"])
            for o in q.get("requirement_objectives", []):
                assert o["requirement_objective_id"].startswith(f"A.{rid}"), rid
                if "assessed_requirement_item" in o:
                    assert o["assessed_requirement_item"] in items, o
                seen["objective"].append(o["requirement_objective_id"])
    for kind, values in seen.items():
        assert len(values) == len(set(values)), kind


def test_placeholders_name_the_requirements_own_parameters():
    """An insert placeholder in a statement, an item or an objective names a
    parameter of the same requirement, by the catalog's dotted form of the
    parameter's identifier."""
    placeholder = re.compile(r"\{\{\s*insert: param, (A\.[0-9.]+\.ODP\.[0-9]+)\s*\}\}")
    for q in _in_force():
        own = {
            p["odp_id"].replace("[", ".").rstrip("]")
            for p in q.get("requirement_parameters", [])
        }
        text = json.dumps(q)
        named = set(placeholder.findall(text))
        assert named <= own, (q["requirement_id"], named - own)
