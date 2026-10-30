# Auto generated from nist_sp_800_171.yaml by pythongen.py version: 0.0.1
# Schema: nist_sp_800_171
#
# id: https://w3id.org/lmodel/nist-sp-800-171
# description: A LinkML model of NIST Special Publication 800-171 Revision 3, the security requirements for protecting controlled unclassified information (CUI) in nonfederal systems and organizations: its seventeen requirement families, each security requirement with its statement, discussion, references and source controls, the organization-defined parameters (ODPs) a requirement leaves to the organization, and the assessment objectives and methods that SP 800-171A Revision 3 gives each requirement.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String, Uri
from linkml_runtime.utils.metamodelcore import URI

metamodel_version = "1.12.0"
version = "3.0.0"

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_SP_800_171 = CurieNamespace('nist_sp_800_171', 'https://w3id.org/lmodel/nist-sp-800-171/')
OSCAL = CurieNamespace('oscal', 'https://w3id.org/lmodel/oscal/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NIST_SP_800_171


# Types
class Sp800171FamilyIdentifier(String):
    """ A family's number, as SP 800-171 Revision 3 numbers its seventeen families: 03, a dot and two digits from 01 to 17, such as 03.01 for Access Control. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sp800171_family_identifier"
    type_model_uri = NIST_SP_800_171.Sp800171FamilyIdentifier


class Sp800171RequirementIdentifier(String):
    """ A security requirement's identifier: its family's number, a dot and the requirement's two-digit number within the family, such as 03.01.01. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sp800171_requirement_identifier"
    type_model_uri = NIST_SP_800_171.Sp800171RequirementIdentifier


class Sp800171ItemIdentifier(String):
    """ The identifier of a lettered item of a requirement statement, such as 03.01.01.a, or of a numbered item under it, such as 03.01.01.c.01. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sp800171_item_identifier"
    type_model_uri = NIST_SP_800_171.Sp800171ItemIdentifier


class Sp800171OdpIdentifier(String):
    """ An organization-defined parameter's identifier, as SP 800-171A writes it: A, the requirement's identifier, ODP and the parameter's two-digit number in square brackets, such as A.03.01.01.ODP[01]. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sp800171_odp_identifier"
    type_model_uri = NIST_SP_800_171.Sp800171OdpIdentifier


class Sp800171ObjectiveIdentifier(String):
    """ An assessment objective's identifier, as SP 800-171A writes it: A and the identifier of the requirement or statement item it assesses, such as A.03.01.01.e, with a two-digit number in square brackets when that item has several objectives, such as A.03.01.01.b[01]. NIST's catalog writes the bracketed number as a dotted one, A.03.01.01.b.01. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sp800171_objective_identifier"
    type_model_uri = NIST_SP_800_171.Sp800171ObjectiveIdentifier


class Sp800171SourceControlIdentifier(String):
    """ The identifier of a control of SP 800-53 Revision 5 as NIST's catalog of SP 800-171 writes it: the family's two letters, a hyphen and the control's two-digit number, with a two-digit enhancement number in parentheses where it is one, such as AC-02 and AC-02(03). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sp800171_source_control_identifier"
    type_model_uri = NIST_SP_800_171.Sp800171SourceControlIdentifier


class Sp800171CitedPublicationName(String):
    """ The short name SP 800-171 gives a publication it references: the series (SP, FIPS or IR) and the publication's number, with the number of a part or volume where the publication has one, such as SP 800-57-1, SP 800-160-1, IR 8011-2 or FIPS 140-3. The short name leaves out the publication's revision, which the citation and the address carry: SP 800-53 stands for Revision 5. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "sp800171_cited_publication_name"
    type_model_uri = NIST_SP_800_171.Sp800171CitedPublicationName


# Class references



@dataclass(repr=False)
class Sp800171Publication(YAMLRoot):
    """
    One revision of SP 800-171 as a whole: its requirement families, each holding its security requirements, with the
    assessment procedures of the matching revision of SP 800-171A inside each requirement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_171["Publication"]
    class_class_curie: ClassVar[str] = "nist_sp_800_171:Publication"
    class_name: ClassVar[str] = "Sp800171Publication"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_171.Sp800171Publication

    sp800171_revision: str = None
    requirement_families: Union[Union[dict, "Sp800171Family"], list[Union[dict, "Sp800171Family"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.sp800171_revision):
            self.MissingRequiredField("sp800171_revision")
        if not isinstance(self.sp800171_revision, str):
            self.sp800171_revision = str(self.sp800171_revision)

        if self._is_empty(self.requirement_families):
            self.MissingRequiredField("requirement_families")
        self._normalize_inlined_as_list(slot_name="requirement_families", slot_type=Sp800171Family, key_name="title", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sp800171Family(YAMLRoot):
    """
    One of the seventeen families that SP 800-171 Revision 3 sorts its security requirements into, such as Access
    Control (03.01) or Supply Chain Risk Management (03.17).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_171["Family"]
    class_class_curie: ClassVar[str] = "nist_sp_800_171:Family"
    class_name: ClassVar[str] = "Sp800171Family"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_171.Sp800171Family

    title: str = None
    family_number: Union[str, Sp800171FamilyIdentifier] = None
    description: Optional[str] = None
    family_requirements: Optional[Union[Union[dict, "Sp800171Requirement"], list[Union[dict, "Sp800171Requirement"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.family_number):
            self.MissingRequiredField("family_number")
        if not isinstance(self.family_number, Sp800171FamilyIdentifier):
            self.family_number = Sp800171FamilyIdentifier(self.family_number)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="family_requirements", slot_type=Sp800171Requirement, key_name="requirement_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sp800171Requirement(YAMLRoot):
    """
    A security requirement of SP 800-171: a numbered, named requirement for protecting CUI, with its statement,
    discussion, references and source controls, the organization-defined parameters its statement leaves open, and the
    assessment objectives and methods SP 800-171A gives it. A requirement that Revision 3 withdrew keeps its number
    and says which requirements took its place.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_171["Requirement"]
    class_class_curie: ClassVar[str] = "nist_sp_800_171:Requirement"
    class_name: ClassVar[str] = "Sp800171Requirement"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_171.Sp800171Requirement

    requirement_id: Union[str, Sp800171RequirementIdentifier] = None
    title: Optional[str] = None
    description: Optional[str] = None
    requirement_status: Optional[Union[str, "Sp800171RequirementStatus"]] = None
    incorporated_into_requirements: Optional[Union[Union[str, Sp800171RequirementIdentifier], list[Union[str, Sp800171RequirementIdentifier]]]] = empty_list()
    addressed_by_requirements: Optional[Union[Union[str, Sp800171RequirementIdentifier], list[Union[str, Sp800171RequirementIdentifier]]]] = empty_list()
    requirement_statement: Optional[str] = None
    requirement_items: Optional[Union[Union[dict, "Sp800171RequirementItem"], list[Union[dict, "Sp800171RequirementItem"]]]] = empty_list()
    requirement_discussion: Optional[str] = None
    requirement_parameters: Optional[Union[Union[dict, "Sp800171Parameter"], list[Union[dict, "Sp800171Parameter"]]]] = empty_list()
    requirement_objectives: Optional[Union[Union[dict, "Sp800171AssessmentObjective"], list[Union[dict, "Sp800171AssessmentObjective"]]]] = empty_list()
    requirement_methods: Optional[Union[Union[dict, "Sp800171AssessmentMethod"], list[Union[dict, "Sp800171AssessmentMethod"]]]] = empty_list()
    requirement_references: Optional[Union[Union[dict, "Sp800171Reference"], list[Union[dict, "Sp800171Reference"]]]] = empty_list()
    source_controls: Optional[Union[Union[str, Sp800171SourceControlIdentifier], list[Union[str, Sp800171SourceControlIdentifier]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.requirement_id):
            self.MissingRequiredField("requirement_id")
        if not isinstance(self.requirement_id, Sp800171RequirementIdentifier):
            self.requirement_id = Sp800171RequirementIdentifier(self.requirement_id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.requirement_status is not None and not isinstance(self.requirement_status, Sp800171RequirementStatus):
            self.requirement_status = Sp800171RequirementStatus(self.requirement_status)

        if not isinstance(self.incorporated_into_requirements, list):
            self.incorporated_into_requirements = [self.incorporated_into_requirements] if self.incorporated_into_requirements is not None else []
        self.incorporated_into_requirements = [v if isinstance(v, Sp800171RequirementIdentifier) else Sp800171RequirementIdentifier(v) for v in self.incorporated_into_requirements]

        if not isinstance(self.addressed_by_requirements, list):
            self.addressed_by_requirements = [self.addressed_by_requirements] if self.addressed_by_requirements is not None else []
        self.addressed_by_requirements = [v if isinstance(v, Sp800171RequirementIdentifier) else Sp800171RequirementIdentifier(v) for v in self.addressed_by_requirements]

        if self.requirement_statement is not None and not isinstance(self.requirement_statement, str):
            self.requirement_statement = str(self.requirement_statement)

        self._normalize_inlined_as_list(slot_name="requirement_items", slot_type=Sp800171RequirementItem, key_name="requirement_item_id", keyed=False)

        if self.requirement_discussion is not None and not isinstance(self.requirement_discussion, str):
            self.requirement_discussion = str(self.requirement_discussion)

        self._normalize_inlined_as_list(slot_name="requirement_parameters", slot_type=Sp800171Parameter, key_name="odp_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="requirement_objectives", slot_type=Sp800171AssessmentObjective, key_name="requirement_objective_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="requirement_methods", slot_type=Sp800171AssessmentMethod, key_name="requirement_method_kind", keyed=False)

        self._normalize_inlined_as_list(slot_name="requirement_references", slot_type=Sp800171Reference, key_name="cited_publication", keyed=False)

        if not isinstance(self.source_controls, list):
            self.source_controls = [self.source_controls] if self.source_controls is not None else []
        self.source_controls = [v if isinstance(v, Sp800171SourceControlIdentifier) else Sp800171SourceControlIdentifier(v) for v in self.source_controls]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sp800171RequirementItem(YAMLRoot):
    """
    One item of a requirement statement: a lettered item such as 03.01.01.a, or a numbered item under a lettered one
    such as 03.01.01.c.01.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_171["RequirementItem"]
    class_class_curie: ClassVar[str] = "nist_sp_800_171:RequirementItem"
    class_name: ClassVar[str] = "Sp800171RequirementItem"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_171.Sp800171RequirementItem

    requirement_item_id: Union[str, Sp800171ItemIdentifier] = None
    requirement_item_text: str = None
    requirement_subitems: Optional[Union[Union[dict, "Sp800171RequirementItem"], list[Union[dict, "Sp800171RequirementItem"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.requirement_item_id):
            self.MissingRequiredField("requirement_item_id")
        if not isinstance(self.requirement_item_id, Sp800171ItemIdentifier):
            self.requirement_item_id = Sp800171ItemIdentifier(self.requirement_item_id)

        if self._is_empty(self.requirement_item_text):
            self.MissingRequiredField("requirement_item_text")
        if not isinstance(self.requirement_item_text, str):
            self.requirement_item_text = str(self.requirement_item_text)

        self._normalize_inlined_as_list(slot_name="requirement_subitems", slot_type=Sp800171RequirementItem, key_name="requirement_item_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sp800171Parameter(YAMLRoot):
    """
    An organization-defined parameter (ODP): a value, such as a time period or a frequency, that a requirement
    statement leaves to the organization, with the guideline SP 800-171A gives for defining it. A few parameters are a
    selection among choices instead of a value.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_171["Parameter"]
    class_class_curie: ClassVar[str] = "nist_sp_800_171:Parameter"
    class_name: ClassVar[str] = "Sp800171Parameter"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_171.Sp800171Parameter

    odp_id: Union[str, Sp800171OdpIdentifier] = None
    odp_label: str = None
    odp_usage: Optional[str] = None
    odp_guideline: Optional[str] = None
    odp_choices: Optional[Union[str, list[str]]] = empty_list()
    odp_selection_count: Optional[Union[str, "Sp800171SelectionCount"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.odp_id):
            self.MissingRequiredField("odp_id")
        if not isinstance(self.odp_id, Sp800171OdpIdentifier):
            self.odp_id = Sp800171OdpIdentifier(self.odp_id)

        if self._is_empty(self.odp_label):
            self.MissingRequiredField("odp_label")
        if not isinstance(self.odp_label, str):
            self.odp_label = str(self.odp_label)

        if self.odp_usage is not None and not isinstance(self.odp_usage, str):
            self.odp_usage = str(self.odp_usage)

        if self.odp_guideline is not None and not isinstance(self.odp_guideline, str):
            self.odp_guideline = str(self.odp_guideline)

        if not isinstance(self.odp_choices, list):
            self.odp_choices = [self.odp_choices] if self.odp_choices is not None else []
        self.odp_choices = [v if isinstance(v, str) else str(v) for v in self.odp_choices]

        if self.odp_selection_count is not None and not isinstance(self.odp_selection_count, Sp800171SelectionCount):
            self.odp_selection_count = Sp800171SelectionCount(self.odp_selection_count)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sp800171AssessmentObjective(YAMLRoot):
    """
    An assessment objective of SP 800-171A: one determination statement that an assessor checks, tied to the
    requirement or to one item of its statement.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_171["AssessmentObjective"]
    class_class_curie: ClassVar[str] = "nist_sp_800_171:AssessmentObjective"
    class_name: ClassVar[str] = "Sp800171AssessmentObjective"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_171.Sp800171AssessmentObjective

    requirement_objective_id: Union[str, Sp800171ObjectiveIdentifier] = None
    requirement_determination: str = None
    assessed_requirement_item: Optional[Union[str, Sp800171ItemIdentifier]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.requirement_objective_id):
            self.MissingRequiredField("requirement_objective_id")
        if not isinstance(self.requirement_objective_id, Sp800171ObjectiveIdentifier):
            self.requirement_objective_id = Sp800171ObjectiveIdentifier(self.requirement_objective_id)

        if self._is_empty(self.requirement_determination):
            self.MissingRequiredField("requirement_determination")
        if not isinstance(self.requirement_determination, str):
            self.requirement_determination = str(self.requirement_determination)

        if self.assessed_requirement_item is not None and not isinstance(self.assessed_requirement_item, Sp800171ItemIdentifier):
            self.assessed_requirement_item = Sp800171ItemIdentifier(self.assessed_requirement_item)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sp800171AssessmentMethod(YAMLRoot):
    """
    One of the three assessment methods SP 800-171A applies to a requirement, examine, interview or test, with the
    assessment objects (documents, people, processes or mechanisms) it is applied to.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_171["AssessmentMethod"]
    class_class_curie: ClassVar[str] = "nist_sp_800_171:AssessmentMethod"
    class_name: ClassVar[str] = "Sp800171AssessmentMethod"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_171.Sp800171AssessmentMethod

    requirement_method_kind: Union[str, "Sp800171AssessmentMethodKind"] = None
    requirement_method_objects: Union[str, list[str]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.requirement_method_kind):
            self.MissingRequiredField("requirement_method_kind")
        if not isinstance(self.requirement_method_kind, Sp800171AssessmentMethodKind):
            self.requirement_method_kind = Sp800171AssessmentMethodKind(self.requirement_method_kind)

        if self._is_empty(self.requirement_method_objects):
            self.MissingRequiredField("requirement_method_objects")
        if not isinstance(self.requirement_method_objects, list):
            self.requirement_method_objects = [self.requirement_method_objects] if self.requirement_method_objects is not None else []
        self.requirement_method_objects = [v if isinstance(v, str) else str(v) for v in self.requirement_method_objects]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sp800171Reference(YAMLRoot):
    """
    A publication that SP 800-171 lists under a requirement's references, by the short name the publication gives it,
    with the full citation and the address NIST's catalog gives it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_171["Reference"]
    class_class_curie: ClassVar[str] = "nist_sp_800_171:Reference"
    class_name: ClassVar[str] = "Sp800171Reference"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_171.Sp800171Reference

    cited_publication: Union[str, Sp800171CitedPublicationName] = None
    cited_publication_citation: str = None
    cited_publication_url: Union[str, URI] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.cited_publication):
            self.MissingRequiredField("cited_publication")
        if not isinstance(self.cited_publication, Sp800171CitedPublicationName):
            self.cited_publication = Sp800171CitedPublicationName(self.cited_publication)

        if self._is_empty(self.cited_publication_citation):
            self.MissingRequiredField("cited_publication_citation")
        if not isinstance(self.cited_publication_citation, str):
            self.cited_publication_citation = str(self.cited_publication_citation)

        if self._is_empty(self.cited_publication_url):
            self.MissingRequiredField("cited_publication_url")
        if not isinstance(self.cited_publication_url, URI):
            self.cited_publication_url = URI(self.cited_publication_url)

        super().__post_init__(**kwargs)


# Enumerations
class Sp800171RequirementStatus(EnumDefinitionImpl):
    """
    The one status SP 800-171 Revision 3 states for a requirement. A requirement in force carries none.
    """
    withdrawn = PermissibleValue(
        text="withdrawn",
        description="""Revision 3 withdrew the requirement; other requirements incorporate or address what it required, or nothing does.""")

    _defn = EnumDefinition(
        name="Sp800171RequirementStatus",
        description="The one status SP 800-171 Revision 3 states for a requirement. A requirement in force carries none.",
    )

class Sp800171AssessmentMethodKind(EnumDefinitionImpl):
    """
    The three assessment methods of SP 800-171A.
    """
    examine = PermissibleValue(
        text="examine",
        description="""Reviewing, inspecting, observing, studying or analysing assessment objects such as policies, plans, records and configurations.""")
    interview = PermissibleValue(
        text="interview",
        description="""Holding discussions with people such as administrators and personnel with security responsibilities.""")
    test = PermissibleValue(
        text="test",
        description="""Exercising mechanisms or processes under specified conditions and comparing the result with what is expected.""")

    _defn = EnumDefinition(
        name="Sp800171AssessmentMethodKind",
        description="The three assessment methods of SP 800-171A.",
    )

class Sp800171SelectionCount(EnumDefinitionImpl):
    """
    How many choices a selection parameter takes, as OSCAL states it.
    """
    one = PermissibleValue(
        text="one",
        description="Exactly one of the choices.")
    one_or_more = PermissibleValue(
        text="one_or_more",
        description="One or more of the choices.")

    _defn = EnumDefinition(
        name="Sp800171SelectionCount",
        description="How many choices a selection parameter takes, as OSCAL states it.",
    )

# Slots
class slots:
    pass

slots.title = Slot(uri=SCHEMA.name, name="title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_SP_800_171.title, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_SP_800_171.description, domain=None, range=Optional[str])

slots.sp800171Publication__sp800171_revision = Slot(uri=NIST_SP_800_171.sp800171_revision, name="sp800171Publication__sp800171_revision", curie=NIST_SP_800_171.curie('sp800171_revision'),
                   model_uri=NIST_SP_800_171.sp800171Publication__sp800171_revision, domain=None, range=str,
                   pattern=re.compile(r'^[1-9][0-9]*$'))

slots.sp800171Publication__requirement_families = Slot(uri=NIST_SP_800_171.requirement_families, name="sp800171Publication__requirement_families", curie=NIST_SP_800_171.curie('requirement_families'),
                   model_uri=NIST_SP_800_171.sp800171Publication__requirement_families, domain=None, range=Union[Union[dict, Sp800171Family], list[Union[dict, Sp800171Family]]])

slots.sp800171Family__family_number = Slot(uri=NIST_SP_800_171.family_number, name="sp800171Family__family_number", curie=NIST_SP_800_171.curie('family_number'),
                   model_uri=NIST_SP_800_171.sp800171Family__family_number, domain=None, range=Union[str, Sp800171FamilyIdentifier])

slots.sp800171Family__family_requirements = Slot(uri=NIST_SP_800_171.family_requirements, name="sp800171Family__family_requirements", curie=NIST_SP_800_171.curie('family_requirements'),
                   model_uri=NIST_SP_800_171.sp800171Family__family_requirements, domain=None, range=Optional[Union[Union[dict, Sp800171Requirement], list[Union[dict, Sp800171Requirement]]]])

slots.sp800171Requirement__requirement_id = Slot(uri=NIST_SP_800_171.requirement_id, name="sp800171Requirement__requirement_id", curie=NIST_SP_800_171.curie('requirement_id'),
                   model_uri=NIST_SP_800_171.sp800171Requirement__requirement_id, domain=None, range=Union[str, Sp800171RequirementIdentifier])

slots.sp800171Requirement__requirement_status = Slot(uri=NIST_SP_800_171.requirement_status, name="sp800171Requirement__requirement_status", curie=NIST_SP_800_171.curie('requirement_status'),
                   model_uri=NIST_SP_800_171.sp800171Requirement__requirement_status, domain=None, range=Optional[Union[str, "Sp800171RequirementStatus"]])

slots.sp800171Requirement__incorporated_into_requirements = Slot(uri=NIST_SP_800_171.incorporated_into_requirements, name="sp800171Requirement__incorporated_into_requirements", curie=NIST_SP_800_171.curie('incorporated_into_requirements'),
                   model_uri=NIST_SP_800_171.sp800171Requirement__incorporated_into_requirements, domain=None, range=Optional[Union[Union[str, Sp800171RequirementIdentifier], list[Union[str, Sp800171RequirementIdentifier]]]])

slots.sp800171Requirement__addressed_by_requirements = Slot(uri=NIST_SP_800_171.addressed_by_requirements, name="sp800171Requirement__addressed_by_requirements", curie=NIST_SP_800_171.curie('addressed_by_requirements'),
                   model_uri=NIST_SP_800_171.sp800171Requirement__addressed_by_requirements, domain=None, range=Optional[Union[Union[str, Sp800171RequirementIdentifier], list[Union[str, Sp800171RequirementIdentifier]]]])

slots.sp800171Requirement__requirement_statement = Slot(uri=NIST_SP_800_171.requirement_statement, name="sp800171Requirement__requirement_statement", curie=NIST_SP_800_171.curie('requirement_statement'),
                   model_uri=NIST_SP_800_171.sp800171Requirement__requirement_statement, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\s*\S'))

slots.sp800171Requirement__requirement_items = Slot(uri=NIST_SP_800_171.requirement_items, name="sp800171Requirement__requirement_items", curie=NIST_SP_800_171.curie('requirement_items'),
                   model_uri=NIST_SP_800_171.sp800171Requirement__requirement_items, domain=None, range=Optional[Union[Union[dict, Sp800171RequirementItem], list[Union[dict, Sp800171RequirementItem]]]])

slots.sp800171Requirement__requirement_discussion = Slot(uri=NIST_SP_800_171.requirement_discussion, name="sp800171Requirement__requirement_discussion", curie=NIST_SP_800_171.curie('requirement_discussion'),
                   model_uri=NIST_SP_800_171.sp800171Requirement__requirement_discussion, domain=None, range=Optional[str],
                   pattern=re.compile(r'^\s*\S'))

slots.sp800171Requirement__requirement_parameters = Slot(uri=NIST_SP_800_171.requirement_parameters, name="sp800171Requirement__requirement_parameters", curie=NIST_SP_800_171.curie('requirement_parameters'),
                   model_uri=NIST_SP_800_171.sp800171Requirement__requirement_parameters, domain=None, range=Optional[Union[Union[dict, Sp800171Parameter], list[Union[dict, Sp800171Parameter]]]])

slots.sp800171Requirement__requirement_objectives = Slot(uri=NIST_SP_800_171.requirement_objectives, name="sp800171Requirement__requirement_objectives", curie=NIST_SP_800_171.curie('requirement_objectives'),
                   model_uri=NIST_SP_800_171.sp800171Requirement__requirement_objectives, domain=None, range=Optional[Union[Union[dict, Sp800171AssessmentObjective], list[Union[dict, Sp800171AssessmentObjective]]]])

slots.sp800171Requirement__requirement_methods = Slot(uri=NIST_SP_800_171.requirement_methods, name="sp800171Requirement__requirement_methods", curie=NIST_SP_800_171.curie('requirement_methods'),
                   model_uri=NIST_SP_800_171.sp800171Requirement__requirement_methods, domain=None, range=Optional[Union[Union[dict, Sp800171AssessmentMethod], list[Union[dict, Sp800171AssessmentMethod]]]])

slots.sp800171Requirement__requirement_references = Slot(uri=NIST_SP_800_171.requirement_references, name="sp800171Requirement__requirement_references", curie=NIST_SP_800_171.curie('requirement_references'),
                   model_uri=NIST_SP_800_171.sp800171Requirement__requirement_references, domain=None, range=Optional[Union[Union[dict, Sp800171Reference], list[Union[dict, Sp800171Reference]]]])

slots.sp800171Requirement__source_controls = Slot(uri=NIST_SP_800_171.source_controls, name="sp800171Requirement__source_controls", curie=NIST_SP_800_171.curie('source_controls'),
                   model_uri=NIST_SP_800_171.sp800171Requirement__source_controls, domain=None, range=Optional[Union[Union[str, Sp800171SourceControlIdentifier], list[Union[str, Sp800171SourceControlIdentifier]]]])

slots.sp800171RequirementItem__requirement_item_id = Slot(uri=NIST_SP_800_171.requirement_item_id, name="sp800171RequirementItem__requirement_item_id", curie=NIST_SP_800_171.curie('requirement_item_id'),
                   model_uri=NIST_SP_800_171.sp800171RequirementItem__requirement_item_id, domain=None, range=Union[str, Sp800171ItemIdentifier])

slots.sp800171RequirementItem__requirement_item_text = Slot(uri=NIST_SP_800_171.requirement_item_text, name="sp800171RequirementItem__requirement_item_text", curie=NIST_SP_800_171.curie('requirement_item_text'),
                   model_uri=NIST_SP_800_171.sp800171RequirementItem__requirement_item_text, domain=None, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.sp800171RequirementItem__requirement_subitems = Slot(uri=NIST_SP_800_171.requirement_subitems, name="sp800171RequirementItem__requirement_subitems", curie=NIST_SP_800_171.curie('requirement_subitems'),
                   model_uri=NIST_SP_800_171.sp800171RequirementItem__requirement_subitems, domain=None, range=Optional[Union[Union[dict, Sp800171RequirementItem], list[Union[dict, Sp800171RequirementItem]]]])

slots.sp800171Parameter__odp_id = Slot(uri=NIST_SP_800_171.odp_id, name="sp800171Parameter__odp_id", curie=NIST_SP_800_171.curie('odp_id'),
                   model_uri=NIST_SP_800_171.sp800171Parameter__odp_id, domain=None, range=Union[str, Sp800171OdpIdentifier])

slots.sp800171Parameter__odp_label = Slot(uri=NIST_SP_800_171.odp_label, name="sp800171Parameter__odp_label", curie=NIST_SP_800_171.curie('odp_label'),
                   model_uri=NIST_SP_800_171.sp800171Parameter__odp_label, domain=None, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.sp800171Parameter__odp_usage = Slot(uri=NIST_SP_800_171.odp_usage, name="sp800171Parameter__odp_usage", curie=NIST_SP_800_171.curie('odp_usage'),
                   model_uri=NIST_SP_800_171.sp800171Parameter__odp_usage, domain=None, range=Optional[str])

slots.sp800171Parameter__odp_guideline = Slot(uri=NIST_SP_800_171.odp_guideline, name="sp800171Parameter__odp_guideline", curie=NIST_SP_800_171.curie('odp_guideline'),
                   model_uri=NIST_SP_800_171.sp800171Parameter__odp_guideline, domain=None, range=Optional[str])

slots.sp800171Parameter__odp_choices = Slot(uri=NIST_SP_800_171.odp_choices, name="sp800171Parameter__odp_choices", curie=NIST_SP_800_171.curie('odp_choices'),
                   model_uri=NIST_SP_800_171.sp800171Parameter__odp_choices, domain=None, range=Optional[Union[str, list[str]]])

slots.sp800171Parameter__odp_selection_count = Slot(uri=NIST_SP_800_171.odp_selection_count, name="sp800171Parameter__odp_selection_count", curie=NIST_SP_800_171.curie('odp_selection_count'),
                   model_uri=NIST_SP_800_171.sp800171Parameter__odp_selection_count, domain=None, range=Optional[Union[str, "Sp800171SelectionCount"]])

slots.sp800171AssessmentObjective__requirement_objective_id = Slot(uri=NIST_SP_800_171.requirement_objective_id, name="sp800171AssessmentObjective__requirement_objective_id", curie=NIST_SP_800_171.curie('requirement_objective_id'),
                   model_uri=NIST_SP_800_171.sp800171AssessmentObjective__requirement_objective_id, domain=None, range=Union[str, Sp800171ObjectiveIdentifier])

slots.sp800171AssessmentObjective__requirement_determination = Slot(uri=NIST_SP_800_171.requirement_determination, name="sp800171AssessmentObjective__requirement_determination", curie=NIST_SP_800_171.curie('requirement_determination'),
                   model_uri=NIST_SP_800_171.sp800171AssessmentObjective__requirement_determination, domain=None, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.sp800171AssessmentObjective__assessed_requirement_item = Slot(uri=NIST_SP_800_171.assessed_requirement_item, name="sp800171AssessmentObjective__assessed_requirement_item", curie=NIST_SP_800_171.curie('assessed_requirement_item'),
                   model_uri=NIST_SP_800_171.sp800171AssessmentObjective__assessed_requirement_item, domain=None, range=Optional[Union[str, Sp800171ItemIdentifier]])

slots.sp800171AssessmentMethod__requirement_method_kind = Slot(uri=NIST_SP_800_171.requirement_method_kind, name="sp800171AssessmentMethod__requirement_method_kind", curie=NIST_SP_800_171.curie('requirement_method_kind'),
                   model_uri=NIST_SP_800_171.sp800171AssessmentMethod__requirement_method_kind, domain=None, range=Union[str, "Sp800171AssessmentMethodKind"])

slots.sp800171AssessmentMethod__requirement_method_objects = Slot(uri=NIST_SP_800_171.requirement_method_objects, name="sp800171AssessmentMethod__requirement_method_objects", curie=NIST_SP_800_171.curie('requirement_method_objects'),
                   model_uri=NIST_SP_800_171.sp800171AssessmentMethod__requirement_method_objects, domain=None, range=Union[str, list[str]],
                   pattern=re.compile(r'^\s*\S'))

slots.sp800171Reference__cited_publication = Slot(uri=NIST_SP_800_171.cited_publication, name="sp800171Reference__cited_publication", curie=NIST_SP_800_171.curie('cited_publication'),
                   model_uri=NIST_SP_800_171.sp800171Reference__cited_publication, domain=None, range=Union[str, Sp800171CitedPublicationName])

slots.sp800171Reference__cited_publication_citation = Slot(uri=NIST_SP_800_171.cited_publication_citation, name="sp800171Reference__cited_publication_citation", curie=NIST_SP_800_171.curie('cited_publication_citation'),
                   model_uri=NIST_SP_800_171.sp800171Reference__cited_publication_citation, domain=None, range=str)

slots.sp800171Reference__cited_publication_url = Slot(uri=NIST_SP_800_171.cited_publication_url, name="sp800171Reference__cited_publication_url", curie=NIST_SP_800_171.curie('cited_publication_url'),
                   model_uri=NIST_SP_800_171.sp800171Reference__cited_publication_url, domain=None, range=Union[str, URI],
                   pattern=re.compile(r'^https://doi\.org/10\.[0-9]+/\S+$'))

slots.Sp800171Family_title = Slot(uri=SCHEMA.name, name="Sp800171Family_title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_SP_800_171.Sp800171Family_title, domain=Sp800171Family, range=str)
