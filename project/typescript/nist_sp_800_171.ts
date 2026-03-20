/**
* Allowed values for group and control class attributes
*/
export enum CatalogElementClassValue {
    
    family = "family",
    requirement = "requirement",
};
/**
* Allowed values for part class attributes
*/
export enum PartClassValue {
    
    security_requirement = "security_requirement",
};
/**
* Allowed values for assessment method property values
*/
export enum AssessmentMethodValue {
    
    EXAMINE = "EXAMINE",
    INTERVIEW = "INTERVIEW",
    TEST = "TEST",
};
/**
* Cardinality constraint for parameter selection
*/
export enum HowManyValue {
    
    one = "one",
    one_or_more = "one-or-more",
};


/**
 * Root wrapper for SP 800-171 catalog content
 */
export interface SP800171Document {
    /** Root catalog payload */
    catalog?: CatalogBody,
}


/**
 * Main catalog object
 */
export interface CatalogBody {
    /** UUID for catalog, metadata, or resource element */
    uuid?: string,
    /** Catalog metadata */
    metadata?: Metadata,
    /** List of requirement family groups in the catalog */
    groups?: ControlGroup[],
    /** Back-matter references and resources */
    back_matter?: BackMatter,
}


/**
 * OSCAL metadata section
 */
export interface Metadata {
    /** Human-readable title */
    title?: string,
    /** Publication timestamp */
    published?: string,
    /** Last modification timestamp */
    last_modified?: string,
    /** Version identifier */
    version?: string,
    /** OSCAL version identifier */
    oscal_version?: string,
    /** List of properties */
    props?: Property[],
    /** List of links and relationships */
    links?: Link[],
    /** Roles used in metadata */
    roles?: Role[],
    /** Parties used in metadata */
    parties?: Party[],
    /** Responsible party assignments */
    responsible_parties?: ResponsibleParty[],
}


/**
 * Role definition
 */
export interface Role {
    /** Unique identifier for an element */
    id?: string,
    /** Human-readable title */
    title?: string,
}


/**
 * Party definition
 */
export interface Party {
    /** UUID for catalog, metadata, or resource element */
    uuid?: string,
    /** Party type */
    type?: string,
    /** Name of a property, part, or party */
    name?: string,
    /** Short display name */
    short_name?: string,
    /** Party email addresses */
    email_addresses?: string[],
    /** Postal addresses */
    addresses?: Address[],
}


/**
 * Postal address
 */
export interface Address {
    /** Address lines */
    addr_lines?: string[],
    /** City name */
    city?: string,
    /** State or region */
    state?: string,
    /** Postal code */
    postal_code?: string,
}


/**
 * Assignment of parties to a role
 */
export interface ResponsibleParty {
    /** Assigned role identifier */
    role_id?: string,
    /** Referenced party UUIDs */
    party_uuids?: string[],
}


/**
 * OSCAL back-matter section
 */
export interface BackMatter {
    /** Back-matter resources */
    resources?: Resource[],
}


/**
 * Referenced resource
 */
export interface Resource {
    /** UUID for catalog, metadata, or resource element */
    uuid?: string,
    /** Human-readable title */
    title?: string,
    /** Resource description */
    description?: string,
    /** Citation details for a resource */
    citation?: Citation,
    /** Resource links */
    rlinks?: ResourceLink[],
}


/**
 * Citation wrapper
 */
export interface Citation {
    /** Citation text */
    text?: string,
}


/**
 * Reference link for a resource
 */
export interface ResourceLink {
    /** Link or resource reference */
    href?: string,
    /** Media type for a resource link */
    media_type?: string,
}


/**
 * Base class for catalog elements with id, props, links, and parts
 */
export interface CatalogElement {
    /** Unique identifier for an element */
    id?: string,
    /** List of properties */
    props?: Property[],
    /** List of links and relationships */
    links?: Link[],
    /** Nested parts providing prose, statements, guidance, assessment objectives and methods */
    parts?: Part[],
}


/**
 * A catalog element with required id, title, and optional class/label
 */
export interface IdentifiedElement extends CatalogElement {
    /** Human-readable title */
    title?: string,
    /** Classification of a catalog element (e.g. family, requirement, security_requirement) */
    class?: string,
    /** Human-readable label */
    label?: string,
}


/**
 * A family group of security requirements
 */
export interface ControlGroup extends IdentifiedElement {
    /** List of security requirements in a family group */
    controls?: Control[],
}


/**
 * A security requirement
 */
export interface Control extends IdentifiedElement {
    /** List of organization-defined parameters for a requirement */
    params?: Parameter[],
}


/**
 * An organization-defined parameter for a security requirement
 */
export interface Parameter extends IdentifiedElement {
    /** Human-readable description of an organization-defined parameter's expected value */
    usage?: string,
    /** List of guidelines for a parameter */
    guidelines?: Guideline[],
    /** Selection constraints for an organization-defined parameter */
    select?: ParameterSelection,
}


/**
 * Selection constraints specifying allowed values for a parameter
 */
export interface ParameterSelection {
    /** Cardinality constraint for parameter selection choices */
    how_many?: string,
    /** List of allowed values for a parameter selection */
    choice?: string[],
}


/**
 * Additional prose guidance associated with a parameter
 */
export interface Guideline {
    /** Free-text prose content */
    prose?: string,
}


/**
 * A name-value property with optional namespace
 */
export interface Property {
    /** Name of a property, part, or party */
    name?: string,
    /** Property value */
    value?: string,
    /** Namespace URI for a property */
    ns?: string,
    /** Classification of a catalog element (e.g. family, requirement, security_requirement) */
    class?: string,
}


/**
 * Relationship link
 */
export interface Link {
    /** Link or resource reference */
    href?: string,
    /** Relationship type for a link */
    rel?: string,
}


/**
 * Structured narrative part containing prose and optional nested parts. Used for statements, guidance, assessment-objectives, and assessment-methods.
 */
export interface Part extends CatalogElement {
    /** Name of a property, part, or party */
    name?: string,
    /** Classification of a catalog element (e.g. family, requirement, security_requirement) */
    class?: string,
    /** Free-text prose content */
    prose?: string,
}



