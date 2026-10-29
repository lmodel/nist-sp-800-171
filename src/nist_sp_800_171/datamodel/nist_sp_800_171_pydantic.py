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


linkml_meta = LinkMLMeta({'annotations': {'cprt_framework_version': {'tag': 'cprt_framework_version',
                                                'value': 'SP_800_171_3_0_0'},
                     'oscal_content_commit': {'tag': 'oscal_content_commit',
                                              'value': 'f0de6d8d8c059d374f15e0ae07508d82e370fc1d'},
                     'oscal_content_tag': {'tag': 'oscal_content_tag',
                                           'value': 'v1.6.0'},
                     'publication_date': {'tag': 'publication_date',
                                          'value': '2024-05'}},
     'comments': ['The version is the revision of SP 800-171 the schema renders, '
                  "written as NIST's Cybersecurity and Privacy Reference Tool "
                  "numbers it (SP_800_171_3_0_0), and source is the publication's "
                  'digital object identifier. The catalog NIST publishes for that '
                  'revision in usnistgov/oscal-content, which carries the '
                  'assessment procedures of SP 800-171A Revision 3 as well, is '
                  'copied to src/nist_sp_800_171/schema/oscal-content/ at the tag '
                  'and commit in the annotations. '
                  'scripts/check_upstream_release.py reads the same pins and '
                  'reports when NIST publishes a newer revision or changes the '
                  "catalog. The catalog's own metadata version (1.1.0) numbers the "
                  "catalog, not the publication. The release tags are the schema's "
                  'own versions.',
                  'SP 800-171 is a work of the United States Government and is not '
                  'subject to copyright in the United States. The descriptions '
                  "here are this project's own words; NIST's text of each "
                  'requirement, discussion, parameter and assessment procedure '
                  'stays in the catalog copy.',
                  "NIST's catalog renders each family as an OSCAL group, each "
                  'security requirement as an OSCAL control of class requirement, '
                  'each statement item, discussion, assessment objective and '
                  'assessment method as a part, each organization-defined '
                  'parameter as a parameter, and each reference and source control '
                  'as a link to a back-matter resource. The broad_mappings name '
                  'those lmodel/oscal classes.'],
     'default_prefix': 'nist_sp_800_171',
     'default_range': 'string',
     'description': 'A LinkML model of NIST Special Publication 800-171 Revision '
                    '3, the security requirements for protecting controlled '
                    'unclassified information (CUI) in nonfederal systems and '
                    'organizations: its seventeen requirement families, each '
                    'security requirement with its statement, discussion, '
                    'references and source controls, the organization-defined '
                    'parameters (ODPs) a requirement leaves to the organization, '
                    'and the assessment objectives and methods that SP 800-171A '
                    'Revision 3 gives each requirement.',
     'id': 'https://w3id.org/lmodel/nist-sp-800-171',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'nist_sp_800_171',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_sp_800_171': {'prefix_prefix': 'nist_sp_800_171',
                                      'prefix_reference': 'https://w3id.org/lmodel/nist-sp-800-171/'},
                  'oscal': {'prefix_prefix': 'oscal',
                            'prefix_reference': 'https://w3id.org/lmodel/oscal/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/nist-sp-800-171',
                  'https://csrc.nist.gov/pubs/sp/800/171/r3/final',
                  'https://doi.org/10.6028/NIST.SP.800-171Ar3',
                  'https://csrc.nist.gov/projects/protecting-controlled-unclassified-information',
                  'https://github.com/usnistgov/oscal-content/tree/v1.6.0/nist.gov/SP800-171/rev3'],
     'source': 'https://doi.org/10.6028/NIST.SP.800-171r3',
     'source_file': 'src/nist_sp_800_171/schema/nist_sp_800_171.yaml',
     'title': 'Protecting Controlled Unclassified Information in Nonfederal '
              'Systems and Organizations (SP 800-171 Revision 3)',
     'types': {'sp800171_cited_publication_name': {'base': 'str',
                                                   'description': 'The short name '
                                                                  'SP 800-171 '
                                                                  'gives a '
                                                                  'publication it '
                                                                  'references: the '
                                                                  'series (SP, '
                                                                  'FIPS or IR) and '
                                                                  'the '
                                                                  "publication's "
                                                                  'number, with '
                                                                  'its revision or '
                                                                  'volume where '
                                                                  'the publication '
                                                                  'has one, such '
                                                                  'as SP 800-63-3, '
                                                                  'FIPS 140-3 and '
                                                                  'IR 7966.',
                                                   'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
                                                   'name': 'sp800171_cited_publication_name',
                                                   'pattern': '^(FIPS|IR|SP) '
                                                              '[1-9][0-9]*(-[0-9A-Z]+)*$',
                                                   'typeof': 'string',
                                                   'uri': 'xsd:string'},
               'sp800171_family_identifier': {'base': 'str',
                                              'description': "A family's number, "
                                                             'as SP 800-171 '
                                                             'Revision 3 numbers '
                                                             'its seventeen '
                                                             'families: 03, a dot '
                                                             'and two digits from '
                                                             '01 to 17, such as '
                                                             '03.01 for Access '
                                                             'Control.',
                                              'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
                                              'name': 'sp800171_family_identifier',
                                              'pattern': '^03\\.(0[1-9]|1[0-7])$',
                                              'typeof': 'string',
                                              'uri': 'xsd:string'},
               'sp800171_item_identifier': {'base': 'str',
                                            'description': 'The identifier of a '
                                                           'lettered item of a '
                                                           'requirement statement, '
                                                           'such as 03.01.01.a, or '
                                                           'of a numbered item '
                                                           'under it, such as '
                                                           '03.01.01.c.01.',
                                            'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
                                            'name': 'sp800171_item_identifier',
                                            'pattern': '^03\\.(0[1-9]|1[0-7])\\.(0[1-9]|[1-9][0-9])\\.[a-z](\\.(0[1-9]|[1-9][0-9]))?$',
                                            'typeof': 'string',
                                            'uri': 'xsd:string'},
               'sp800171_objective_identifier': {'base': 'str',
                                                 'description': 'An assessment '
                                                                "objective's "
                                                                'identifier, as SP '
                                                                '800-171A writes '
                                                                'it: A and the '
                                                                'identifier of the '
                                                                'requirement or '
                                                                'statement item it '
                                                                'assesses, such as '
                                                                'A.03.01.01.e, '
                                                                'with a two-digit '
                                                                'number in square '
                                                                'brackets when '
                                                                'that item has '
                                                                'several '
                                                                'objectives, such '
                                                                'as '
                                                                'A.03.01.01.b[01]. '
                                                                "NIST's catalog "
                                                                'writes the '
                                                                'bracketed number '
                                                                'as a dotted one, '
                                                                'A.03.01.01.b.01.',
                                                 'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
                                                 'name': 'sp800171_objective_identifier',
                                                 'pattern': '^A\\.03\\.(0[1-9]|1[0-7])\\.(0[1-9]|[1-9][0-9])(\\.[a-z](\\.(0[1-9]|[1-9][0-9]))?)?(\\[(0[1-9]|[1-9][0-9])\\])?$',
                                                 'typeof': 'string',
                                                 'uri': 'xsd:string'},
               'sp800171_odp_identifier': {'base': 'str',
                                           'description': 'An organization-defined '
                                                          "parameter's identifier, "
                                                          'as SP 800-171A writes '
                                                          'it: A, the '
                                                          "requirement's "
                                                          'identifier, ODP and the '
                                                          "parameter's two-digit "
                                                          'number in square '
                                                          'brackets, such as '
                                                          'A.03.01.01.ODP[01].',
                                           'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
                                           'name': 'sp800171_odp_identifier',
                                           'pattern': '^A\\.03\\.(0[1-9]|1[0-7])\\.(0[1-9]|[1-9][0-9])\\.ODP\\[(0[1-9]|[1-9][0-9])\\]$',
                                           'typeof': 'string',
                                           'uri': 'xsd:string'},
               'sp800171_requirement_identifier': {'base': 'str',
                                                   'description': 'A security '
                                                                  "requirement's "
                                                                  'identifier: its '
                                                                  "family's "
                                                                  'number, a dot '
                                                                  'and the '
                                                                  "requirement's "
                                                                  'two-digit '
                                                                  'number within '
                                                                  'the family, '
                                                                  'such as '
                                                                  '03.01.01.',
                                                   'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
                                                   'name': 'sp800171_requirement_identifier',
                                                   'pattern': '^03\\.(0[1-9]|1[0-7])\\.(0[1-9]|[1-9][0-9])$',
                                                   'typeof': 'string',
                                                   'uri': 'xsd:string'},
               'sp800171_source_control_identifier': {'base': 'str',
                                                      'description': 'The '
                                                                     'identifier '
                                                                     'of a control '
                                                                     'of SP 800-53 '
                                                                     'Revision 5 '
                                                                     "as NIST's "
                                                                     'catalog of '
                                                                     'SP 800-171 '
                                                                     'writes it: '
                                                                     "the family's "
                                                                     'two letters, '
                                                                     'a hyphen and '
                                                                     'the '
                                                                     "control's "
                                                                     'two-digit '
                                                                     'number, with '
                                                                     'a two-digit '
                                                                     'enhancement '
                                                                     'number in '
                                                                     'parentheses '
                                                                     'where it is '
                                                                     'one, such as '
                                                                     'AC-02 and '
                                                                     'AC-02(03).',
                                                      'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
                                                      'name': 'sp800171_source_control_identifier',
                                                      'pattern': '^[A-Z]{2}-(0[1-9]|[1-9][0-9])(\\((0[1-9]|[1-9][0-9])\\))?$',
                                                      'typeof': 'string',
                                                      'uri': 'xsd:string'}}} )

class Sp800171RequirementStatus(str, Enum):
    """
    The one status SP 800-171 Revision 3 states for a requirement. A requirement in force carries none.
    """
    withdrawn = "withdrawn"
    """
    Revision 3 withdrew the requirement; other requirements incorporate or address what it required, or nothing does.
    """


class Sp800171AssessmentMethodKind(str, Enum):
    """
    The three assessment methods of SP 800-171A.
    """
    examine = "examine"
    """
    Reviewing, inspecting, observing, studying or analysing assessment objects such as policies, plans, records and configurations.
    """
    interview = "interview"
    """
    Holding discussions with people such as administrators and personnel with security responsibilities.
    """
    test = "test"
    """
    Exercising mechanisms or processes under specified conditions and comparing the result with what is expected.
    """


class Sp800171SelectionCount(str, Enum):
    """
    How many choices a selection parameter takes, as OSCAL states it.
    """
    one = "one"
    """
    Exactly one of the choices.
    """
    one_or_more = "one_or_more"
    """
    One or more of the choices.
    """



class Sp800171Publication(ConfiguredBaseModel):
    """
    One revision of SP 800-171 as a whole: its requirement families, each holding its security requirements, with the assessment procedures of the matching revision of SP 800-171A inside each requirement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Catalog'],
         'class_uri': 'nist_sp_800_171:Publication',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
         'see_also': ['https://csrc.nist.gov/pubs/sp/800/171/r3/final'],
         'tree_root': True})

    sp800171_revision: str = Field(default=..., description="""The revision of SP 800-171 the document renders, as NIST numbers it, such as 3.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Publication']} })
    requirement_families: list[Sp800171Family] = Field(default=..., description="""The requirement families, in the order SP 800-171 gives them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Publication']} })

    @field_validator('sp800171_revision')
    def pattern_sp800171_revision(cls, v):
        pattern=re.compile(r"^[1-9][0-9]*$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid sp800171_revision format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid sp800171_revision format: {v}"
            raise ValueError(err_msg)
        return v


class Sp800171Family(ConfiguredBaseModel):
    """
    One of the seventeen families that SP 800-171 Revision 3 sorts its security requirements into, such as Access Control (03.01) or Supply Chain Risk Management (03.17).
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Group'],
         'class_uri': 'nist_sp_800_171:Family',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
         'see_also': ['https://csrc.nist.gov/pubs/sp/800/171/r3/final'],
         'slot_usage': {'title': {'name': 'title', 'required': True}}})

    title: str = Field(default=..., description="""The name SP 800-171 gives a family or a security requirement, such as Access Control or Account Management.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['Sp800171Family', 'Sp800171Requirement'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the family or requirement is about, in the words of whoever records it. SP 800-171 gives a family no text of its own, and a requirement's own text goes in its statement, items and discussion.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['Sp800171Family', 'Sp800171Requirement'],
         'slot_uri': 'schema:description'} })
    family_number: str = Field(default=..., description="""The family's number, such as 03.01.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Family']} })
    family_requirements: Optional[list[Sp800171Requirement]] = Field(default=None, description="""The security requirements of the family, the withdrawn ones included, in the order SP 800-171 numbers them. A knowledge bundle relates a requirement to its family with isPartOf instead.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Family']} })


class Sp800171Requirement(ConfiguredBaseModel):
    """
    A security requirement of SP 800-171: a numbered, named requirement for protecting CUI, with its statement, discussion, references and source controls, the organization-defined parameters its statement leaves open, and the assessment objectives and methods SP 800-171A gives it. A requirement that Revision 3 withdrew keeps its number and says which requirements took its place.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Control'],
         'class_uri': 'nist_sp_800_171:Requirement',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
         'see_also': ['https://csrc.nist.gov/pubs/sp/800/171/r3/final']})

    title: Optional[str] = Field(default=None, description="""The name SP 800-171 gives a family or a security requirement, such as Access Control or Account Management.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['Sp800171Family', 'Sp800171Requirement'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the family or requirement is about, in the words of whoever records it. SP 800-171 gives a family no text of its own, and a requirement's own text goes in its statement, items and discussion.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['Sp800171Family', 'Sp800171Requirement'],
         'slot_uri': 'schema:description'} })
    requirement_id: str = Field(default=..., description="""The requirement's identifier, such as 03.01.01.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Requirement']} })
    requirement_status: Optional[Sp800171RequirementStatus] = Field(default=None, description="""Withdrawn when Revision 3 withdrew the requirement. A requirement with no status is in force.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Requirement']} })
    incorporated_into_requirements: Optional[list[str]] = Field(default=None, description="""For a withdrawn requirement, the requirements of Revision 3 that incorporate what it required, as the catalog states them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Requirement']} })
    addressed_by_requirements: Optional[list[str]] = Field(default=None, description="""For a withdrawn requirement, the requirements of Revision 3 that address what it required, as the catalog states them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Requirement']} })
    requirement_statement: Optional[str] = Field(default=None, description="""The requirement statement when SP 800-171 writes it as one piece of text and not as lettered items. The catalog marks an organization-defined parameter in the text with an insert placeholder that names the parameter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Requirement']} })
    requirement_items: Optional[list[Sp800171RequirementItem]] = Field(default=None, description="""The lettered items of the requirement statement, in order, each with its numbered items where it has them. A requirement has either these or a statement, never both.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Requirement']} })
    requirement_discussion: Optional[str] = Field(default=None, description="""The requirement's discussion: SP 800-171's explanation of what the requirement means and how it relates to other requirements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Requirement']} })
    requirement_parameters: Optional[list[Sp800171Parameter]] = Field(default=None, description="""The organization-defined parameters the requirement statement leaves to the organization, in the order SP 800-171A numbers them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Requirement']} })
    requirement_objectives: Optional[list[Sp800171AssessmentObjective]] = Field(default=None, description="""The assessment objectives SP 800-171A gives the requirement: the determination statements an assessor checks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Requirement']} })
    requirement_methods: Optional[list[Sp800171AssessmentMethod]] = Field(default=None, description="""The assessment methods SP 800-171A gives the requirement, each with the objects it is applied to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Requirement']} })
    requirement_references: Optional[list[Sp800171Reference]] = Field(default=None, description="""The publications SP 800-171 lists under the requirement's references, each with its citation and address as the catalog gives them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Requirement']} })
    source_controls: Optional[list[str]] = Field(default=None, description="""The controls of SP 800-53 Revision 5 the requirement is drawn from, by their identifiers, as the catalog lists them among the requirement's references. The identifier is data; the schema maps nothing to a model of SP 800-53.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Requirement']} })

    @field_validator('requirement_statement')
    def pattern_requirement_statement(cls, v):
        pattern=re.compile(r"\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid requirement_statement format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid requirement_statement format: {v}"
            raise ValueError(err_msg)
        return v

    @field_validator('requirement_discussion')
    def pattern_requirement_discussion(cls, v):
        pattern=re.compile(r"\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid requirement_discussion format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid requirement_discussion format: {v}"
            raise ValueError(err_msg)
        return v


class Sp800171RequirementItem(ConfiguredBaseModel):
    """
    One item of a requirement statement: a lettered item such as 03.01.01.a, or a numbered item under a lettered one such as 03.01.01.c.01.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Part'],
         'class_uri': 'nist_sp_800_171:RequirementItem',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
         'see_also': ['https://csrc.nist.gov/pubs/sp/800/171/r3/final']})

    requirement_item_id: str = Field(default=..., description="""The item's identifier, such as 03.01.01.a.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171RequirementItem']} })
    requirement_item_text: str = Field(default=..., description="""What the item requires. The catalog marks an organization-defined parameter in the text with an insert placeholder that names the parameter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171RequirementItem']} })
    requirement_subitems: Optional[list[Sp800171RequirementItem]] = Field(default=None, description="""The numbered items under a lettered item, in order.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171RequirementItem']} })

    @field_validator('requirement_item_text')
    def pattern_requirement_item_text(cls, v):
        pattern=re.compile(r"\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid requirement_item_text format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid requirement_item_text format: {v}"
            raise ValueError(err_msg)
        return v


class Sp800171Parameter(ConfiguredBaseModel):
    """
    An organization-defined parameter (ODP): a value, such as a time period or a frequency, that a requirement statement leaves to the organization, with the guideline SP 800-171A gives for defining it. A few parameters are a selection among choices instead of a value.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:OscalParameter'],
         'class_uri': 'nist_sp_800_171:Parameter',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
         'see_also': ['https://doi.org/10.6028/NIST.SP.800-171Ar3']})

    odp_id: str = Field(default=..., description="""The parameter's identifier, such as A.03.01.01.ODP[01].""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Parameter']} })
    odp_label: str = Field(default=..., description="""What kind of value the parameter takes, such as time period or frequency, or SELECTED PARAMETER VALUES for a selection.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Parameter']} })
    odp_usage: Optional[str] = Field(default=None, description="""How the requirement statement names the parameter, such as organization-defined time period.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Parameter']} })
    odp_guideline: Optional[str] = Field(default=None, description="""The determination SP 800-171A gives for the parameter: what the organization must have defined, such as the time period for account inactivity before disabling is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Parameter']} })
    odp_choices: Optional[list[str]] = Field(default=None, description="""For a selection, the choices SP 800-171 offers, in its order. A choice may itself carry an insert placeholder naming another parameter.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Parameter']} })
    odp_selection_count: Optional[Sp800171SelectionCount] = Field(default=None, description="""How many of the choices a selection takes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Parameter']} })

    @field_validator('odp_label')
    def pattern_odp_label(cls, v):
        pattern=re.compile(r"\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid odp_label format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid odp_label format: {v}"
            raise ValueError(err_msg)
        return v


class Sp800171AssessmentObjective(ConfiguredBaseModel):
    """
    An assessment objective of SP 800-171A: one determination statement that an assessor checks, tied to the requirement or to one item of its statement.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Part'],
         'class_uri': 'nist_sp_800_171:AssessmentObjective',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
         'see_also': ['https://doi.org/10.6028/NIST.SP.800-171Ar3']})

    requirement_objective_id: str = Field(default=..., description="""The objective's identifier, such as A.03.01.01.b[01].""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171AssessmentObjective']} })
    requirement_determination: str = Field(default=..., description="""The determination statement: what the assessor determines is the case, such as system accounts are created in accordance with organizational policy, procedures, prerequisites, and criteria.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171AssessmentObjective']} })
    assessed_requirement_item: Optional[str] = Field(default=None, description="""The statement item the objective assesses, such as 03.01.01.b. Absent when the objective assesses a requirement whose statement is one piece of text.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171AssessmentObjective']} })

    @field_validator('requirement_determination')
    def pattern_requirement_determination(cls, v):
        pattern=re.compile(r"\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid requirement_determination format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid requirement_determination format: {v}"
            raise ValueError(err_msg)
        return v


class Sp800171AssessmentMethod(ConfiguredBaseModel):
    """
    One of the three assessment methods SP 800-171A applies to a requirement, examine, interview or test, with the assessment objects (documents, people, processes or mechanisms) it is applied to.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Part'],
         'class_uri': 'nist_sp_800_171:AssessmentMethod',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
         'see_also': ['https://doi.org/10.6028/NIST.SP.800-171Ar3']})

    requirement_method_kind: Sp800171AssessmentMethodKind = Field(default=..., description="""Which method it is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171AssessmentMethod']} })
    requirement_method_objects: list[str] = Field(default=..., description="""The assessment objects, one entry each, in the order SP 800-171A lists them, such as access control policy and procedures or system administrators.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171AssessmentMethod']} })

    @field_validator('requirement_method_objects')
    def pattern_requirement_method_objects(cls, v):
        pattern=re.compile(r"\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.match(element):
                    err_msg = f"Invalid requirement_method_objects format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.match(v):
            err_msg = f"Invalid requirement_method_objects format: {v}"
            raise ValueError(err_msg)
        return v


class Sp800171Reference(ConfiguredBaseModel):
    """
    A publication that SP 800-171 lists under a requirement's references, by the short name the publication gives it, with the full citation and the address NIST's catalog gives it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Resource'],
         'class_uri': 'nist_sp_800_171:Reference',
         'from_schema': 'https://w3id.org/lmodel/nist-sp-800-171',
         'see_also': ['https://csrc.nist.gov/pubs/sp/800/171/r3/final']})

    cited_publication: str = Field(default=..., description="""The publication's short name, such as SP 800-63-3.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Reference']} })
    cited_publication_citation: Optional[str] = Field(default=None, description="""The full citation, as the catalog's back matter gives it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Reference']} })
    cited_publication_url: Optional[str] = Field(default=None, description="""The publication's address, which the catalog gives as its digital object identifier.""", json_schema_extra = { "linkml_meta": {'domain_of': ['Sp800171Reference']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Sp800171Publication.model_rebuild()
Sp800171Family.model_rebuild()
Sp800171Requirement.model_rebuild()
Sp800171RequirementItem.model_rebuild()
Sp800171Parameter.model_rebuild()
Sp800171AssessmentObjective.model_rebuild()
Sp800171AssessmentMethod.model_rebuild()
Sp800171Reference.model_rebuild()
