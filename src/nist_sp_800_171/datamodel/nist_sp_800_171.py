# Auto generated from nist_sp_800_171.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-03-20T17:11:34
# Schema: NIST-SP-800-171
#
# id: https://w3id.org/lmodel/nist-sp-800-171
# description: Electronic (LinkML) Version of Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations
# license: https://creativecommons.org/publicdomain/zero/1.0/

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

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = "3.0.0"

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_SP_800_171 = CurieNamespace('nist_sp_800_171', 'https://w3id.org/lmodel/nist-sp-800-171/')
DEFAULT_ = NIST_SP_800_171


# Types

# Class references



SP800171Document = Any

CatalogBody = Any

Metadata = Any

@dataclass(repr=False)
class Role(YAMLRoot):
    """
    Role definition
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_171["Role"]
    class_class_curie: ClassVar[str] = "nist_sp_800_171:Role"
    class_name: ClassVar[str] = "Role"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_171.Role

    id: Optional[str] = None
    title: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        super().__post_init__(**kwargs)


Party = Any

Address = Any

ResponsibleParty = Any

BackMatter = Any

Resource = Any

Citation = Any

ResourceLink = Any

@dataclass(repr=False)
class CatalogElement(YAMLRoot):
    """
    Base class for catalog elements with id, props, links, and parts
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_171["CatalogElement"]
    class_class_curie: ClassVar[str] = "nist_sp_800_171:CatalogElement"
    class_name: ClassVar[str] = "CatalogElement"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_171.CatalogElement

    id: Optional[str] = None
    props: Optional[Union[Union[dict, "Property"], list[Union[dict, "Property"]]]] = empty_list()
    links: Optional[Union[Union[dict, "Link"], list[Union[dict, "Link"]]]] = empty_list()
    parts: Optional[Union[Union[dict, "Part"], list[Union[dict, "Part"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if not isinstance(self.props, list):
            self.props = [self.props] if self.props is not None else []
        self.props = [v if isinstance(v, Property) else Property(**as_dict(v)) for v in self.props]

        if not isinstance(self.links, list):
            self.links = [self.links] if self.links is not None else []
        self.links = [v if isinstance(v, Link) else Link(**as_dict(v)) for v in self.links]

        if not isinstance(self.parts, list):
            self.parts = [self.parts] if self.parts is not None else []
        self.parts = [v if isinstance(v, Part) else Part(**as_dict(v)) for v in self.parts]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class IdentifiedElement(CatalogElement):
    """
    A catalog element with required id, title, and optional class/label
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_171["IdentifiedElement"]
    class_class_curie: ClassVar[str] = "nist_sp_800_171:IdentifiedElement"
    class_name: ClassVar[str] = "IdentifiedElement"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_171.IdentifiedElement

    title: Optional[str] = None
    _class: Optional[Union[str, "CatalogElementClassValue"]] = None
    label: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self._class is not None and not isinstance(self._class, CatalogElementClassValue):
            self._class = CatalogElementClassValue(self._class)

        if self.label is not None and not isinstance(self.label, str):
            self.label = str(self.label)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ControlGroup(IdentifiedElement):
    """
    A family group of security requirements
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_171["ControlGroup"]
    class_class_curie: ClassVar[str] = "nist_sp_800_171:ControlGroup"
    class_name: ClassVar[str] = "ControlGroup"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_171.ControlGroup

    controls: Optional[Union[Union[dict, "Control"], list[Union[dict, "Control"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.controls, list):
            self.controls = [self.controls] if self.controls is not None else []
        self.controls = [v if isinstance(v, Control) else Control(**as_dict(v)) for v in self.controls]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Control(IdentifiedElement):
    """
    A security requirement
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_171["Control"]
    class_class_curie: ClassVar[str] = "nist_sp_800_171:Control"
    class_name: ClassVar[str] = "Control"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_171.Control

    params: Optional[Union[Union[dict, "Parameter"], list[Union[dict, "Parameter"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.params, list):
            self.params = [self.params] if self.params is not None else []
        self.params = [v if isinstance(v, Parameter) else Parameter(**as_dict(v)) for v in self.params]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Parameter(IdentifiedElement):
    """
    An organization-defined parameter for a security requirement
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_171["Parameter"]
    class_class_curie: ClassVar[str] = "nist_sp_800_171:Parameter"
    class_name: ClassVar[str] = "Parameter"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_171.Parameter

    usage: Optional[str] = None
    guidelines: Optional[Union[Union[dict, "Guideline"], list[Union[dict, "Guideline"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.usage is not None and not isinstance(self.usage, str):
            self.usage = str(self.usage)

        if not isinstance(self.guidelines, list):
            self.guidelines = [self.guidelines] if self.guidelines is not None else []
        self.guidelines = [v if isinstance(v, Guideline) else Guideline(**as_dict(v)) for v in self.guidelines]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Guideline(YAMLRoot):
    """
    Additional prose guidance associated with a parameter
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_171["Guideline"]
    class_class_curie: ClassVar[str] = "nist_sp_800_171:Guideline"
    class_name: ClassVar[str] = "Guideline"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_171.Guideline

    prose: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.prose is not None and not isinstance(self.prose, str):
            self.prose = str(self.prose)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Property(YAMLRoot):
    """
    A name-value property with optional namespace
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_171["Property"]
    class_class_curie: ClassVar[str] = "nist_sp_800_171:Property"
    class_name: ClassVar[str] = "Property"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_171.Property

    name: Optional[str] = None
    value: Optional[str] = None
    ns: Optional[str] = None
    _class: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.value is not None and not isinstance(self.value, str):
            self.value = str(self.value)

        if self.ns is not None and not isinstance(self.ns, str):
            self.ns = str(self.ns)

        if self._class is not None and not isinstance(self._class, str):
            self._class = str(self._class)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Link(YAMLRoot):
    """
    Relationship link
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_171["Link"]
    class_class_curie: ClassVar[str] = "nist_sp_800_171:Link"
    class_name: ClassVar[str] = "Link"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_171.Link

    href: Optional[str] = None
    rel: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.href is not None and not isinstance(self.href, str):
            self.href = str(self.href)

        if self.rel is not None and not isinstance(self.rel, str):
            self.rel = str(self.rel)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Part(CatalogElement):
    """
    Structured narrative part containing prose and optional nested parts. Used for statements, guidance,
    assessment-objectives, and assessment-methods.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_SP_800_171["Part"]
    class_class_curie: ClassVar[str] = "nist_sp_800_171:Part"
    class_name: ClassVar[str] = "Part"
    class_model_uri: ClassVar[URIRef] = NIST_SP_800_171.Part

    name: Optional[str] = None
    _class: Optional[Union[str, "PartClassValue"]] = None
    prose: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self._class is not None and not isinstance(self._class, PartClassValue):
            self._class = PartClassValue(self._class)

        if self.prose is not None and not isinstance(self.prose, str):
            self.prose = str(self.prose)

        super().__post_init__(**kwargs)


# Enumerations
class CatalogElementClassValue(EnumDefinitionImpl):
    """
    Allowed values for group and control class attributes
    """
    family = PermissibleValue(text="family")
    requirement = PermissibleValue(text="requirement")

    _defn = EnumDefinition(
        name="CatalogElementClassValue",
        description="Allowed values for group and control class attributes",
    )

class PartClassValue(EnumDefinitionImpl):
    """
    Allowed values for part class attributes
    """
    security_requirement = PermissibleValue(text="security_requirement")

    _defn = EnumDefinition(
        name="PartClassValue",
        description="Allowed values for part class attributes",
    )

class AssessmentMethodValue(EnumDefinitionImpl):
    """
    Allowed values for assessment method property values
    """
    EXAMINE = PermissibleValue(text="EXAMINE")
    INTERVIEW = PermissibleValue(text="INTERVIEW")
    TEST = PermissibleValue(text="TEST")

    _defn = EnumDefinition(
        name="AssessmentMethodValue",
        description="Allowed values for assessment method property values",
    )

# Slots
class slots:
    pass

slots.catalog = Slot(uri=NIST_SP_800_171.catalog, name="catalog", curie=NIST_SP_800_171.curie('catalog'),
                   model_uri=NIST_SP_800_171.catalog, domain=None, range=Optional[Union[dict, CatalogBody]])

slots.metadata = Slot(uri=NIST_SP_800_171.metadata, name="metadata", curie=NIST_SP_800_171.curie('metadata'),
                   model_uri=NIST_SP_800_171.metadata, domain=None, range=Optional[Union[dict, Metadata]])

slots.groups = Slot(uri=NIST_SP_800_171.groups, name="groups", curie=NIST_SP_800_171.curie('groups'),
                   model_uri=NIST_SP_800_171.groups, domain=None, range=Optional[Union[Union[dict, ControlGroup], list[Union[dict, ControlGroup]]]])

slots.controls = Slot(uri=NIST_SP_800_171.controls, name="controls", curie=NIST_SP_800_171.curie('controls'),
                   model_uri=NIST_SP_800_171.controls, domain=None, range=Optional[Union[Union[dict, Control], list[Union[dict, Control]]]])

slots.params = Slot(uri=NIST_SP_800_171.params, name="params", curie=NIST_SP_800_171.curie('params'),
                   model_uri=NIST_SP_800_171.params, domain=None, range=Optional[Union[Union[dict, Parameter], list[Union[dict, Parameter]]]])

slots.props = Slot(uri=NIST_SP_800_171.props, name="props", curie=NIST_SP_800_171.curie('props'),
                   model_uri=NIST_SP_800_171.props, domain=None, range=Optional[Union[Union[dict, Property], list[Union[dict, Property]]]])

slots.guidelines = Slot(uri=NIST_SP_800_171.guidelines, name="guidelines", curie=NIST_SP_800_171.curie('guidelines'),
                   model_uri=NIST_SP_800_171.guidelines, domain=None, range=Optional[Union[Union[dict, Guideline], list[Union[dict, Guideline]]]])

slots.links = Slot(uri=NIST_SP_800_171.links, name="links", curie=NIST_SP_800_171.curie('links'),
                   model_uri=NIST_SP_800_171.links, domain=None, range=Optional[Union[Union[dict, Link], list[Union[dict, Link]]]])

slots.parts = Slot(uri=NIST_SP_800_171.parts, name="parts", curie=NIST_SP_800_171.curie('parts'),
                   model_uri=NIST_SP_800_171.parts, domain=None, range=Optional[Union[Union[dict, Part], list[Union[dict, Part]]]])

slots.id = Slot(uri=NIST_SP_800_171.id, name="id", curie=NIST_SP_800_171.curie('id'),
                   model_uri=NIST_SP_800_171.id, domain=None, range=Optional[str])

slots.uuid = Slot(uri=NIST_SP_800_171.uuid, name="uuid", curie=NIST_SP_800_171.curie('uuid'),
                   model_uri=NIST_SP_800_171.uuid, domain=None, range=Optional[str])

slots.title = Slot(uri=NIST_SP_800_171.title, name="title", curie=NIST_SP_800_171.curie('title'),
                   model_uri=NIST_SP_800_171.title, domain=None, range=Optional[str])

slots.published = Slot(uri=NIST_SP_800_171.published, name="published", curie=NIST_SP_800_171.curie('published'),
                   model_uri=NIST_SP_800_171.published, domain=None, range=Optional[str])

slots.version = Slot(uri=NIST_SP_800_171.version, name="version", curie=NIST_SP_800_171.curie('version'),
                   model_uri=NIST_SP_800_171.version, domain=None, range=Optional[str])

slots.last_modified = Slot(uri=NIST_SP_800_171.last_modified, name="last-modified", curie=NIST_SP_800_171.curie('last_modified'),
                   model_uri=NIST_SP_800_171.last_modified, domain=None, range=Optional[str])

slots.oscal_version = Slot(uri=NIST_SP_800_171.oscal_version, name="oscal-version", curie=NIST_SP_800_171.curie('oscal_version'),
                   model_uri=NIST_SP_800_171.oscal_version, domain=None, range=Optional[str])

slots._class = Slot(uri=NIST_SP_800_171._class, name="_class", curie=NIST_SP_800_171.curie('_class'),
                   model_uri=NIST_SP_800_171._class, domain=None, range=Optional[str])

slots.label = Slot(uri=NIST_SP_800_171.label, name="label", curie=NIST_SP_800_171.curie('label'),
                   model_uri=NIST_SP_800_171.label, domain=None, range=Optional[str])

slots.name = Slot(uri=NIST_SP_800_171.name, name="name", curie=NIST_SP_800_171.curie('name'),
                   model_uri=NIST_SP_800_171.name, domain=None, range=Optional[str])

slots.value = Slot(uri=NIST_SP_800_171.value, name="value", curie=NIST_SP_800_171.curie('value'),
                   model_uri=NIST_SP_800_171.value, domain=None, range=Optional[str])

slots.ns = Slot(uri=NIST_SP_800_171.ns, name="ns", curie=NIST_SP_800_171.curie('ns'),
                   model_uri=NIST_SP_800_171.ns, domain=None, range=Optional[str])

slots.prose = Slot(uri=NIST_SP_800_171.prose, name="prose", curie=NIST_SP_800_171.curie('prose'),
                   model_uri=NIST_SP_800_171.prose, domain=None, range=Optional[str])

slots.usage = Slot(uri=NIST_SP_800_171.usage, name="usage", curie=NIST_SP_800_171.curie('usage'),
                   model_uri=NIST_SP_800_171.usage, domain=None, range=Optional[str])

slots.remarks = Slot(uri=NIST_SP_800_171.remarks, name="remarks", curie=NIST_SP_800_171.curie('remarks'),
                   model_uri=NIST_SP_800_171.remarks, domain=None, range=Optional[str])

slots.roles = Slot(uri=NIST_SP_800_171.roles, name="roles", curie=NIST_SP_800_171.curie('roles'),
                   model_uri=NIST_SP_800_171.roles, domain=None, range=Optional[Union[Union[dict, Role], list[Union[dict, Role]]]])

slots.parties = Slot(uri=NIST_SP_800_171.parties, name="parties", curie=NIST_SP_800_171.curie('parties'),
                   model_uri=NIST_SP_800_171.parties, domain=None, range=Optional[Union[Union[dict, Party], list[Union[dict, Party]]]])

slots.responsible_parties = Slot(uri=NIST_SP_800_171.responsible_parties, name="responsible-parties", curie=NIST_SP_800_171.curie('responsible_parties'),
                   model_uri=NIST_SP_800_171.responsible_parties, domain=None, range=Optional[Union[Union[dict, ResponsibleParty], list[Union[dict, ResponsibleParty]]]])

slots.role_id = Slot(uri=NIST_SP_800_171.role_id, name="role-id", curie=NIST_SP_800_171.curie('role_id'),
                   model_uri=NIST_SP_800_171.role_id, domain=None, range=Optional[str])

slots.party_uuids = Slot(uri=NIST_SP_800_171.party_uuids, name="party-uuids", curie=NIST_SP_800_171.curie('party_uuids'),
                   model_uri=NIST_SP_800_171.party_uuids, domain=None, range=Optional[Union[str, list[str]]])

slots.type = Slot(uri=NIST_SP_800_171.type, name="type", curie=NIST_SP_800_171.curie('type'),
                   model_uri=NIST_SP_800_171.type, domain=None, range=Optional[str])

slots.short_name = Slot(uri=NIST_SP_800_171.short_name, name="short-name", curie=NIST_SP_800_171.curie('short_name'),
                   model_uri=NIST_SP_800_171.short_name, domain=None, range=Optional[str])

slots.email_addresses = Slot(uri=NIST_SP_800_171.email_addresses, name="email-addresses", curie=NIST_SP_800_171.curie('email_addresses'),
                   model_uri=NIST_SP_800_171.email_addresses, domain=None, range=Optional[Union[str, list[str]]])

slots.addresses = Slot(uri=NIST_SP_800_171.addresses, name="addresses", curie=NIST_SP_800_171.curie('addresses'),
                   model_uri=NIST_SP_800_171.addresses, domain=None, range=Optional[Union[Union[dict, Address], list[Union[dict, Address]]]])

slots.addr_lines = Slot(uri=NIST_SP_800_171.addr_lines, name="addr-lines", curie=NIST_SP_800_171.curie('addr_lines'),
                   model_uri=NIST_SP_800_171.addr_lines, domain=None, range=Optional[Union[str, list[str]]])

slots.city = Slot(uri=NIST_SP_800_171.city, name="city", curie=NIST_SP_800_171.curie('city'),
                   model_uri=NIST_SP_800_171.city, domain=None, range=Optional[str])

slots.state = Slot(uri=NIST_SP_800_171.state, name="state", curie=NIST_SP_800_171.curie('state'),
                   model_uri=NIST_SP_800_171.state, domain=None, range=Optional[str])

slots.postal_code = Slot(uri=NIST_SP_800_171.postal_code, name="postal-code", curie=NIST_SP_800_171.curie('postal_code'),
                   model_uri=NIST_SP_800_171.postal_code, domain=None, range=Optional[str])

slots.back_matter = Slot(uri=NIST_SP_800_171.back_matter, name="back-matter", curie=NIST_SP_800_171.curie('back_matter'),
                   model_uri=NIST_SP_800_171.back_matter, domain=None, range=Optional[Union[dict, BackMatter]])

slots.resources = Slot(uri=NIST_SP_800_171.resources, name="resources", curie=NIST_SP_800_171.curie('resources'),
                   model_uri=NIST_SP_800_171.resources, domain=None, range=Optional[Union[Union[dict, Resource], list[Union[dict, Resource]]]])

slots.citation = Slot(uri=NIST_SP_800_171.citation, name="citation", curie=NIST_SP_800_171.curie('citation'),
                   model_uri=NIST_SP_800_171.citation, domain=None, range=Optional[Union[dict, Citation]])

slots.text = Slot(uri=NIST_SP_800_171.text, name="text", curie=NIST_SP_800_171.curie('text'),
                   model_uri=NIST_SP_800_171.text, domain=None, range=Optional[str])

slots.description = Slot(uri=NIST_SP_800_171.description, name="description", curie=NIST_SP_800_171.curie('description'),
                   model_uri=NIST_SP_800_171.description, domain=None, range=Optional[str])

slots.rlinks = Slot(uri=NIST_SP_800_171.rlinks, name="rlinks", curie=NIST_SP_800_171.curie('rlinks'),
                   model_uri=NIST_SP_800_171.rlinks, domain=None, range=Optional[Union[Union[dict, ResourceLink], list[Union[dict, ResourceLink]]]])

slots.media_type = Slot(uri=NIST_SP_800_171.media_type, name="media-type", curie=NIST_SP_800_171.curie('media_type'),
                   model_uri=NIST_SP_800_171.media_type, domain=None, range=Optional[str])

slots.href = Slot(uri=NIST_SP_800_171.href, name="href", curie=NIST_SP_800_171.curie('href'),
                   model_uri=NIST_SP_800_171.href, domain=None, range=Optional[str])

slots.rel = Slot(uri=NIST_SP_800_171.rel, name="rel", curie=NIST_SP_800_171.curie('rel'),
                   model_uri=NIST_SP_800_171.rel, domain=None, range=Optional[str])

slots.IdentifiedElement__class = Slot(uri=NIST_SP_800_171._class, name="IdentifiedElement__class", curie=NIST_SP_800_171.curie('_class'),
                   model_uri=NIST_SP_800_171.IdentifiedElement__class, domain=IdentifiedElement, range=Optional[Union[str, "CatalogElementClassValue"]])

slots.Part__class = Slot(uri=NIST_SP_800_171._class, name="Part__class", curie=NIST_SP_800_171.curie('_class'),
                   model_uri=NIST_SP_800_171.Part__class, domain=Part, range=Optional[Union[str, "PartClassValue"]])
