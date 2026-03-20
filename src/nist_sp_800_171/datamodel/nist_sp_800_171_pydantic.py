from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.7.0"
version = "3.0.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'nist_sp_800_171',
     'default_range': 'string',
     'description': 'Electronic (LinkML) Version of Protecting Controlled '
                    'Unclassified Information in Nonfederal Systems and '
                    'Organizations',
     'id': 'https://w3id.org/lmodel/nist-sp-800-171',
     'imports': ['linkml:types'],
     'name': 'NIST-SP-800-171',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_sp_800_171': {'prefix_prefix': 'nist_sp_800_171',
                                      'prefix_reference': 'https://w3id.org/lmodel/nist-sp-800-171/'}},
     'source': 'https://doi.org/10.6028/NIST.SP.800-171r3',
     'source_file': 'src/nist_sp_800_171/schema/nist_sp_800_171.yaml',
     'subsets': {'nist_sp_800_171r3_catalog': {'description': 'NIST SP 800-171 '
                                                              'Catalog subset for '
                                                              'requirements and '
                                                              'assessment '
                                                              'procedures',
                                               'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
                                               'name': 'nist_sp_800_171r3_catalog'}}} )

class CatalogElementClassValue(str, Enum):
    """
    Allowed values for group and control class attributes
    """
    family = "family"
    requirement = "requirement"


class PartClassValue(str, Enum):
    """
    Allowed values for part class attributes
    """
    security_requirement = "security_requirement"


class AssessmentMethodValue(str, Enum):
    """
    Allowed values for assessment method property values
    """
    EXAMINE = "EXAMINE"
    INTERVIEW = "INTERVIEW"
    TEST = "TEST"



class Role(ConfiguredBaseModel):
    """
    Role definition
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
         'in_subset': ['nist_sp_800_171r3_catalog']})

    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Role', 'Resource', 'IdentifiedElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })


class CatalogElement(ConfiguredBaseModel):
    """
    Base class for catalog elements with id, props, links, and parts
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
         'in_subset': ['nist_sp_800_171r3_catalog']})

    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts providing prose, statements, guidance, assessment objectives and methods""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_171r3_catalog']} })


class IdentifiedElement(CatalogElement):
    """
    A catalog element with required id, title, and optional class/label
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
         'in_subset': ['nist_sp_800_171r3_catalog'],
         'slot_usage': {'_class': {'name': '_class',
                                   'range': 'CatalogElementClassValue'}}})

    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Role', 'Resource', 'IdentifiedElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="_class", description="""Classification of a catalog element (e.g. family, requirement, security_requirement)""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property', 'Part'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement'], 'in_subset': ['nist_sp_800_171r3_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts providing prose, statements, guidance, assessment objectives and methods""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_171r3_catalog']} })


class ControlGroup(IdentifiedElement):
    """
    A family group of security requirements
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
         'in_subset': ['nist_sp_800_171r3_catalog']})

    controls: Optional[list[Control]] = Field(default=None, description="""List of security requirements in a family group""", json_schema_extra = { "linkml_meta": {'domain_of': ['ControlGroup'], 'in_subset': ['nist_sp_800_171r3_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Role', 'Resource', 'IdentifiedElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="_class", description="""Classification of a catalog element (e.g. family, requirement, security_requirement)""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property', 'Part'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement'], 'in_subset': ['nist_sp_800_171r3_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts providing prose, statements, guidance, assessment objectives and methods""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_171r3_catalog']} })


class Control(IdentifiedElement):
    """
    A security requirement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
         'in_subset': ['nist_sp_800_171r3_catalog']})

    params: Optional[list[Parameter]] = Field(default=None, description="""List of organization-defined parameters for a requirement""", json_schema_extra = { "linkml_meta": {'domain_of': ['Control'], 'in_subset': ['nist_sp_800_171r3_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Role', 'Resource', 'IdentifiedElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="_class", description="""Classification of a catalog element (e.g. family, requirement, security_requirement)""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property', 'Part'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement'], 'in_subset': ['nist_sp_800_171r3_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts providing prose, statements, guidance, assessment objectives and methods""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_171r3_catalog']} })


class Parameter(IdentifiedElement):
    """
    An organization-defined parameter for a security requirement
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
         'in_subset': ['nist_sp_800_171r3_catalog']})

    usage: Optional[str] = Field(default=None, description="""Human-readable description of an organization-defined parameter's expected value""", json_schema_extra = { "linkml_meta": {'domain_of': ['Parameter'], 'in_subset': ['nist_sp_800_171r3_catalog']} })
    guidelines: Optional[list[Guideline]] = Field(default=None, description="""List of guidelines for a parameter""", json_schema_extra = { "linkml_meta": {'domain_of': ['Parameter'], 'in_subset': ['nist_sp_800_171r3_catalog']} })
    title: Optional[str] = Field(default=None, description="""Human-readable title""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'Role', 'Resource', 'IdentifiedElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    class_: Optional[CatalogElementClassValue] = Field(default=None, alias="_class", description="""Classification of a catalog element (e.g. family, requirement, security_requirement)""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property', 'Part'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    label: Optional[str] = Field(default=None, description="""Human-readable label""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement'], 'in_subset': ['nist_sp_800_171r3_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts providing prose, statements, guidance, assessment objectives and methods""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_171r3_catalog']} })


class Guideline(ConfiguredBaseModel):
    """
    Additional prose guidance associated with a parameter
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
         'in_subset': ['nist_sp_800_171r3_catalog']})

    prose: Optional[str] = Field(default=None, description="""Free-text prose content""", json_schema_extra = { "linkml_meta": {'domain_of': ['Guideline', 'Part'], 'in_subset': ['nist_sp_800_171r3_catalog']} })


class Property(ConfiguredBaseModel):
    """
    A name-value property with optional namespace
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
         'in_subset': ['nist_sp_800_171r3_catalog']})

    name: Optional[str] = Field(default=None, description="""Name of a property, part, or party""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party', 'Property', 'Part'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    value: Optional[str] = Field(default=None, description="""Property value""", json_schema_extra = { "linkml_meta": {'domain_of': ['Property'], 'in_subset': ['nist_sp_800_171r3_catalog']} })
    ns: Optional[str] = Field(default=None, description="""Namespace URI for a property""", json_schema_extra = { "linkml_meta": {'domain_of': ['Property'], 'in_subset': ['nist_sp_800_171r3_catalog']} })
    class_: Optional[str] = Field(default=None, alias="_class", description="""Classification of a catalog element (e.g. family, requirement, security_requirement)""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property', 'Part'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })


class Link(ConfiguredBaseModel):
    """
    Relationship link
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
         'in_subset': ['nist_sp_800_171r3_catalog']})

    href: Optional[str] = Field(default=None, description="""Link or resource reference""", json_schema_extra = { "linkml_meta": {'domain_of': ['ResourceLink', 'Link'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    rel: Optional[str] = Field(default=None, description="""Relationship type for a link""", json_schema_extra = { "linkml_meta": {'domain_of': ['Link'], 'in_subset': ['nist_sp_800_171r3_catalog']} })


class Part(CatalogElement):
    """
    Structured narrative part containing prose and optional nested parts. Used for statements, guidance, assessment-objectives, and assessment-methods.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
         'in_subset': ['nist_sp_800_171r3_catalog'],
         'slot_usage': {'_class': {'name': '_class', 'range': 'PartClassValue'}}})

    name: Optional[str] = Field(default=None, description="""Name of a property, part, or party""", json_schema_extra = { "linkml_meta": {'domain_of': ['Party', 'Property', 'Part'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    class_: Optional[PartClassValue] = Field(default=None, alias="_class", description="""Classification of a catalog element (e.g. family, requirement, security_requirement)""", json_schema_extra = { "linkml_meta": {'domain_of': ['IdentifiedElement', 'Property', 'Part'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    prose: Optional[str] = Field(default=None, description="""Free-text prose content""", json_schema_extra = { "linkml_meta": {'domain_of': ['Guideline', 'Part'], 'in_subset': ['nist_sp_800_171r3_catalog']} })
    id: Optional[str] = Field(default=None, description="""Unique identifier for an element""", json_schema_extra = { "linkml_meta": {'domain_of': ['Role', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    props: Optional[list[Property]] = Field(default=None, description="""List of properties""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    links: Optional[list[Link]] = Field(default=None, description="""List of links and relationships""", json_schema_extra = { "linkml_meta": {'domain_of': ['Metadata', 'CatalogElement'],
         'in_subset': ['nist_sp_800_171r3_catalog']} })
    parts: Optional[list[Part]] = Field(default=None, description="""Nested parts providing prose, statements, guidance, assessment objectives and methods""", json_schema_extra = { "linkml_meta": {'domain_of': ['CatalogElement'], 'in_subset': ['nist_sp_800_171r3_catalog']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Role.model_rebuild()
CatalogElement.model_rebuild()
IdentifiedElement.model_rebuild()
ControlGroup.model_rebuild()
Control.model_rebuild()
Parameter.model_rebuild()
Guideline.model_rebuild()
Property.model_rebuild()
Link.model_rebuild()
Part.model_rebuild()
