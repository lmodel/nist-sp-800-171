/**
* The one status SP 800-171 Revision 3 states for a requirement. A requirement in force carries none.
*/
export enum Sp800171RequirementStatus {
    
    /** Revision 3 withdrew the requirement; other requirements incorporate or address what it required, or nothing does. */
    withdrawn = "withdrawn",
};
/**
* The three assessment methods of SP 800-171A.
*/
export enum Sp800171AssessmentMethodKind {
    
    /** Reviewing, inspecting, observing, studying or analysing assessment objects such as policies, plans, records and configurations. */
    examine = "examine",
    /** Holding discussions with people such as administrators and personnel with security responsibilities. */
    interview = "interview",
    /** Exercising mechanisms or processes under specified conditions and comparing the result with what is expected. */
    test = "test",
};
/**
* How many choices a selection parameter takes, as OSCAL states it.
*/
export enum Sp800171SelectionCount {
    
    /** Exactly one of the choices. */
    one = "one",
    /** One or more of the choices. */
    one_or_more = "one_or_more",
};


/**
 * One revision of SP 800-171 as a whole: its requirement families, each holding its security requirements, with the assessment procedures of the matching revision of SP 800-171A inside each requirement.
 */
export interface Sp800171Publication {
    /** The revision of SP 800-171 the document renders, as NIST numbers it, such as 3. */
    sp800171_revision: string,
    /** The requirement families, in the order SP 800-171 gives them. */
    requirement_families: Sp800171Family[],
}


/**
 * One of the seventeen families that SP 800-171 Revision 3 sorts its security requirements into, such as Access Control (03.01) or Supply Chain Risk Management (03.17).
 */
export interface Sp800171Family {
    /** The name SP 800-171 gives a family or a security requirement, such as Access Control or Account Management. */
    title: string,
    /** What the family or requirement is about, in the words of whoever records it. SP 800-171 gives a family no text of its own, and a requirement's own text goes in its statement, items and discussion. */
    description?: string,
    /** The family's number, such as 03.01. */
    family_number: string,
    /** The security requirements of the family, the withdrawn ones included, in the order SP 800-171 numbers them. A knowledge bundle relates a requirement to its family with isPartOf instead. */
    family_requirements?: Sp800171Requirement[],
}


/**
 * A security requirement of SP 800-171: a numbered, named requirement for protecting CUI, with its statement, discussion, references and source controls, the organization-defined parameters its statement leaves open, and the assessment objectives and methods SP 800-171A gives it. A requirement that Revision 3 withdrew keeps its number and says which requirements took its place.
 */
export interface Sp800171Requirement {
    /** The name SP 800-171 gives a family or a security requirement, such as Access Control or Account Management. */
    title?: string,
    /** What the family or requirement is about, in the words of whoever records it. SP 800-171 gives a family no text of its own, and a requirement's own text goes in its statement, items and discussion. */
    description?: string,
    /** The requirement's identifier, such as 03.01.01. */
    requirement_id: string,
    /** Withdrawn when Revision 3 withdrew the requirement. A requirement with no status is in force. */
    requirement_status?: string,
    /** For a withdrawn requirement, the requirements of Revision 3 that incorporate what it required, as the catalog states them. */
    incorporated_into_requirements?: string[],
    /** For a withdrawn requirement, the requirements of Revision 3 that address what it required, as the catalog states them. */
    addressed_by_requirements?: string[],
    /** The requirement statement when SP 800-171 writes it as one piece of text and not as lettered items. The catalog marks an organization-defined parameter in the text with an insert placeholder that names the parameter. */
    requirement_statement?: string,
    /** The lettered items of the requirement statement, in order, each with its numbered items where it has them. A requirement has either these or a statement, never both. */
    requirement_items?: Sp800171RequirementItem[],
    /** The requirement's discussion: SP 800-171's explanation of what the requirement means and how it relates to other requirements. */
    requirement_discussion?: string,
    /** The organization-defined parameters the requirement statement leaves to the organization, in the order SP 800-171A numbers them. */
    requirement_parameters?: Sp800171Parameter[],
    /** The assessment objectives SP 800-171A gives the requirement: the determination statements an assessor checks. */
    requirement_objectives?: Sp800171AssessmentObjective[],
    /** The assessment methods SP 800-171A gives the requirement, each with the objects it is applied to. */
    requirement_methods?: Sp800171AssessmentMethod[],
    /** The publications SP 800-171 lists under the requirement's references, each with its citation and address as the catalog gives them. */
    requirement_references?: Sp800171Reference[],
    /** The controls of SP 800-53 Revision 5 the requirement is drawn from, by their identifiers, as the catalog lists them among the requirement's references. The identifier is data; the schema maps nothing to a model of SP 800-53. */
    source_controls?: string[],
}


/**
 * One item of a requirement statement: a lettered item such as 03.01.01.a, or a numbered item under a lettered one such as 03.01.01.c.01.
 */
export interface Sp800171RequirementItem {
    /** The item's identifier, such as 03.01.01.a. */
    requirement_item_id: string,
    /** What the item requires. The catalog marks an organization-defined parameter in the text with an insert placeholder that names the parameter. */
    requirement_item_text: string,
    /** The numbered items under a lettered item, in order. */
    requirement_subitems?: Sp800171RequirementItem[],
}


/**
 * An organization-defined parameter (ODP): a value, such as a time period or a frequency, that a requirement statement leaves to the organization, with the guideline SP 800-171A gives for defining it. A few parameters are a selection among choices instead of a value.
 */
export interface Sp800171Parameter {
    /** The parameter's identifier, such as A.03.01.01.ODP[01]. */
    odp_id: string,
    /** What kind of value the parameter takes, such as time period or frequency, or SELECTED PARAMETER VALUES for a selection. */
    odp_label: string,
    /** How the requirement statement names the parameter, such as organization-defined time period. */
    odp_usage?: string,
    /** The determination SP 800-171A gives for the parameter: what the organization must have defined, such as the time period for account inactivity before disabling is defined. */
    odp_guideline?: string,
    /** For a selection, the choices SP 800-171 offers, in its order. A choice may itself carry an insert placeholder naming another parameter. */
    odp_choices?: string[],
    /** How many of the choices a selection takes. */
    odp_selection_count?: string,
}


/**
 * An assessment objective of SP 800-171A: one determination statement that an assessor checks, tied to the requirement or to one item of its statement.
 */
export interface Sp800171AssessmentObjective {
    /** The objective's identifier, such as A.03.01.01.b[01]. */
    requirement_objective_id: string,
    /** The determination statement: what the assessor determines is the case, such as system accounts are created in accordance with organizational policy, procedures, prerequisites, and criteria. */
    requirement_determination: string,
    /** The statement item the objective assesses, such as 03.01.01.b. Absent when the objective assesses a requirement whose statement is one piece of text. */
    assessed_requirement_item?: string,
}


/**
 * One of the three assessment methods SP 800-171A applies to a requirement, examine, interview or test, with the assessment objects (documents, people, processes or mechanisms) it is applied to.
 */
export interface Sp800171AssessmentMethod {
    /** Which method it is. */
    requirement_method_kind: string,
    /** The assessment objects, one entry each, in the order SP 800-171A lists them, such as access control policy and procedures or system administrators. */
    requirement_method_objects: string[],
}


/**
 * A publication that SP 800-171 lists under a requirement's references, by the short name the publication gives it, with the full citation and the address NIST's catalog gives it.
 */
export interface Sp800171Reference {
    /** The publication's short name, such as SP 800-63-3. */
    cited_publication: string,
    /** The full citation, as the catalog's back matter gives it. */
    cited_publication_citation: string,
    /** The publication's address, which the catalog gives as its digital object identifier at doi.org. */
    cited_publication_url: string,
}



