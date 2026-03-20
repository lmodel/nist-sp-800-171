-- # Class: SP800171Document Description: Root wrapper for SP 800-171 catalog content
--     * Slot: id
--     * Slot: catalog_id Description: Root catalog payload
-- # Class: CatalogBody Description: Main catalog object
--     * Slot: id
--     * Slot: uuid Description: UUID for catalog, metadata, or resource element
--     * Slot: metadata_id Description: Catalog metadata
--     * Slot: back_matter_id Description: Back-matter references and resources
-- # Class: Metadata Description: OSCAL metadata section
--     * Slot: id
--     * Slot: title Description: Human-readable title
--     * Slot: published Description: Publication timestamp
--     * Slot: last_modified Description: Last modification timestamp
--     * Slot: version Description: Version identifier
--     * Slot: oscal_version Description: OSCAL version identifier
-- # Class: Role Description: Role definition
--     * Slot: uid
--     * Slot: id Description: Unique identifier for an element
--     * Slot: title Description: Human-readable title
--     * Slot: Metadata_id Description: Autocreated FK slot
-- # Class: Party Description: Party definition
--     * Slot: id
--     * Slot: uuid Description: UUID for catalog, metadata, or resource element
--     * Slot: type Description: Party type
--     * Slot: name Description: Name of a property, part, or party
--     * Slot: short_name Description: Short display name
--     * Slot: Metadata_id Description: Autocreated FK slot
-- # Class: Address Description: Postal address
--     * Slot: id
--     * Slot: city Description: City name
--     * Slot: state Description: State or region
--     * Slot: postal_code Description: Postal code
--     * Slot: Party_id Description: Autocreated FK slot
-- # Class: ResponsibleParty Description: Assignment of parties to a role
--     * Slot: id
--     * Slot: role_id Description: Assigned role identifier
--     * Slot: Metadata_id Description: Autocreated FK slot
-- # Class: BackMatter Description: OSCAL back-matter section
--     * Slot: id
-- # Class: Resource Description: Referenced resource
--     * Slot: id
--     * Slot: uuid Description: UUID for catalog, metadata, or resource element
--     * Slot: title Description: Human-readable title
--     * Slot: description Description: Resource description
--     * Slot: BackMatter_id Description: Autocreated FK slot
--     * Slot: citation_id Description: Citation details for a resource
-- # Class: Citation Description: Citation wrapper
--     * Slot: id
--     * Slot: text Description: Citation text
-- # Class: ResourceLink Description: Reference link for a resource
--     * Slot: id
--     * Slot: href Description: Link or resource reference
--     * Slot: media_type Description: Media type for a resource link
--     * Slot: Resource_id Description: Autocreated FK slot
-- # Abstract Class: CatalogElement Description: Base class for catalog elements with id, props, links, and parts
--     * Slot: uid
--     * Slot: id Description: Unique identifier for an element
-- # Class: IdentifiedElement Description: A catalog element with required id, title, and optional class/label
--     * Slot: uid
--     * Slot: title Description: Human-readable title
--     * Slot: _class Description: Classification of a catalog element (e.g. family, requirement, security_requirement)
--     * Slot: label Description: Human-readable label
--     * Slot: id Description: Unique identifier for an element
-- # Class: ControlGroup Description: A family group of security requirements
--     * Slot: uid
--     * Slot: title Description: Human-readable title
--     * Slot: _class Description: Classification of a catalog element (e.g. family, requirement, security_requirement)
--     * Slot: label Description: Human-readable label
--     * Slot: id Description: Unique identifier for an element
--     * Slot: CatalogBody_id Description: Autocreated FK slot
-- # Class: Control Description: A security requirement
--     * Slot: uid
--     * Slot: title Description: Human-readable title
--     * Slot: _class Description: Classification of a catalog element (e.g. family, requirement, security_requirement)
--     * Slot: label Description: Human-readable label
--     * Slot: id Description: Unique identifier for an element
--     * Slot: ControlGroup_uid Description: Autocreated FK slot
-- # Class: Parameter Description: An organization-defined parameter for a security requirement
--     * Slot: uid
--     * Slot: usage Description: Human-readable description of an organization-defined parameter's expected value
--     * Slot: title Description: Human-readable title
--     * Slot: _class Description: Classification of a catalog element (e.g. family, requirement, security_requirement)
--     * Slot: label Description: Human-readable label
--     * Slot: id Description: Unique identifier for an element
--     * Slot: Control_uid Description: Autocreated FK slot
-- # Class: Guideline Description: Additional prose guidance associated with a parameter
--     * Slot: id
--     * Slot: prose Description: Free-text prose content
--     * Slot: Parameter_uid Description: Autocreated FK slot
-- # Class: Property Description: A name-value property with optional namespace
--     * Slot: id
--     * Slot: name Description: Name of a property, part, or party
--     * Slot: value Description: Property value
--     * Slot: ns Description: Namespace URI for a property
--     * Slot: _class Description: Classification of a catalog element (e.g. family, requirement, security_requirement)
--     * Slot: Metadata_id Description: Autocreated FK slot
--     * Slot: CatalogElement_uid Description: Autocreated FK slot
--     * Slot: IdentifiedElement_uid Description: Autocreated FK slot
--     * Slot: ControlGroup_uid Description: Autocreated FK slot
--     * Slot: Control_uid Description: Autocreated FK slot
--     * Slot: Parameter_uid Description: Autocreated FK slot
--     * Slot: Part_uid Description: Autocreated FK slot
-- # Class: Link Description: Relationship link
--     * Slot: id
--     * Slot: href Description: Link or resource reference
--     * Slot: rel Description: Relationship type for a link
--     * Slot: Metadata_id Description: Autocreated FK slot
--     * Slot: CatalogElement_uid Description: Autocreated FK slot
--     * Slot: IdentifiedElement_uid Description: Autocreated FK slot
--     * Slot: ControlGroup_uid Description: Autocreated FK slot
--     * Slot: Control_uid Description: Autocreated FK slot
--     * Slot: Parameter_uid Description: Autocreated FK slot
--     * Slot: Part_uid Description: Autocreated FK slot
-- # Class: Part Description: Structured narrative part containing prose and optional nested parts. Used for statements, guidance, assessment-objectives, and assessment-methods.
--     * Slot: uid
--     * Slot: name Description: Name of a property, part, or party
--     * Slot: _class Description: Classification of a catalog element (e.g. family, requirement, security_requirement)
--     * Slot: prose Description: Free-text prose content
--     * Slot: id Description: Unique identifier for an element
--     * Slot: CatalogElement_uid Description: Autocreated FK slot
--     * Slot: IdentifiedElement_uid Description: Autocreated FK slot
--     * Slot: ControlGroup_uid Description: Autocreated FK slot
--     * Slot: Control_uid Description: Autocreated FK slot
--     * Slot: Parameter_uid Description: Autocreated FK slot
--     * Slot: Part_uid Description: Autocreated FK slot
-- # Class: Party_email_addresses
--     * Slot: Party_id Description: Autocreated FK slot
--     * Slot: email_addresses Description: Party email addresses
-- # Class: Address_addr_lines
--     * Slot: Address_id Description: Autocreated FK slot
--     * Slot: addr_lines Description: Address lines
-- # Class: ResponsibleParty_party_uuids
--     * Slot: ResponsibleParty_id Description: Autocreated FK slot
--     * Slot: party_uuids Description: Referenced party UUIDs

CREATE TABLE "Metadata" (
	id INTEGER NOT NULL,
	title TEXT,
	published TEXT,
	last_modified TEXT,
	version TEXT,
	oscal_version TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Metadata_id" ON "Metadata" (id);

CREATE TABLE "BackMatter" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_BackMatter_id" ON "BackMatter" (id);

CREATE TABLE "Citation" (
	id INTEGER NOT NULL,
	text TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Citation_id" ON "Citation" (id);

CREATE TABLE "CatalogElement" (
	uid INTEGER NOT NULL,
	id TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_CatalogElement_uid" ON "CatalogElement" (uid);

CREATE TABLE "IdentifiedElement" (
	uid INTEGER NOT NULL,
	title TEXT,
	_class VARCHAR(11),
	label TEXT,
	id TEXT,
	PRIMARY KEY (uid)
);
CREATE INDEX "ix_IdentifiedElement_uid" ON "IdentifiedElement" (uid);

CREATE TABLE "CatalogBody" (
	id INTEGER NOT NULL,
	uuid TEXT,
	metadata_id INTEGER,
	back_matter_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(metadata_id) REFERENCES "Metadata" (id),
	FOREIGN KEY(back_matter_id) REFERENCES "BackMatter" (id)
);
CREATE INDEX "ix_CatalogBody_id" ON "CatalogBody" (id);

CREATE TABLE "Role" (
	uid INTEGER NOT NULL,
	id TEXT,
	title TEXT,
	"Metadata_id" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("Metadata_id") REFERENCES "Metadata" (id)
);
CREATE INDEX "ix_Role_uid" ON "Role" (uid);

CREATE TABLE "Party" (
	id INTEGER NOT NULL,
	uuid TEXT,
	type TEXT,
	name TEXT,
	short_name TEXT,
	"Metadata_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Metadata_id") REFERENCES "Metadata" (id)
);
CREATE INDEX "ix_Party_id" ON "Party" (id);

CREATE TABLE "ResponsibleParty" (
	id INTEGER NOT NULL,
	role_id TEXT,
	"Metadata_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Metadata_id") REFERENCES "Metadata" (id)
);
CREATE INDEX "ix_ResponsibleParty_id" ON "ResponsibleParty" (id);

CREATE TABLE "Resource" (
	id INTEGER NOT NULL,
	uuid TEXT,
	title TEXT,
	description TEXT,
	"BackMatter_id" INTEGER,
	citation_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("BackMatter_id") REFERENCES "BackMatter" (id),
	FOREIGN KEY(citation_id) REFERENCES "Citation" (id)
);
CREATE INDEX "ix_Resource_id" ON "Resource" (id);

CREATE TABLE "SP800171Document" (
	id INTEGER NOT NULL,
	catalog_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(catalog_id) REFERENCES "CatalogBody" (id)
);
CREATE INDEX "ix_SP800171Document_id" ON "SP800171Document" (id);

CREATE TABLE "Address" (
	id INTEGER NOT NULL,
	city TEXT,
	state TEXT,
	postal_code TEXT,
	"Party_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Party_id") REFERENCES "Party" (id)
);
CREATE INDEX "ix_Address_id" ON "Address" (id);

CREATE TABLE "ResourceLink" (
	id INTEGER NOT NULL,
	href TEXT,
	media_type TEXT,
	"Resource_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Resource_id") REFERENCES "Resource" (id)
);
CREATE INDEX "ix_ResourceLink_id" ON "ResourceLink" (id);

CREATE TABLE "ControlGroup" (
	uid INTEGER NOT NULL,
	title TEXT,
	_class VARCHAR(11),
	label TEXT,
	id TEXT,
	"CatalogBody_id" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("CatalogBody_id") REFERENCES "CatalogBody" (id)
);
CREATE INDEX "ix_ControlGroup_uid" ON "ControlGroup" (uid);

CREATE TABLE "Party_email_addresses" (
	"Party_id" INTEGER,
	email_addresses TEXT,
	PRIMARY KEY ("Party_id", email_addresses),
	FOREIGN KEY("Party_id") REFERENCES "Party" (id)
);
CREATE INDEX "ix_Party_email_addresses_email_addresses" ON "Party_email_addresses" (email_addresses);
CREATE INDEX "ix_Party_email_addresses_Party_id" ON "Party_email_addresses" ("Party_id");

CREATE TABLE "ResponsibleParty_party_uuids" (
	"ResponsibleParty_id" INTEGER,
	party_uuids TEXT,
	PRIMARY KEY ("ResponsibleParty_id", party_uuids),
	FOREIGN KEY("ResponsibleParty_id") REFERENCES "ResponsibleParty" (id)
);
CREATE INDEX "ix_ResponsibleParty_party_uuids_ResponsibleParty_id" ON "ResponsibleParty_party_uuids" ("ResponsibleParty_id");
CREATE INDEX "ix_ResponsibleParty_party_uuids_party_uuids" ON "ResponsibleParty_party_uuids" (party_uuids);

CREATE TABLE "Control" (
	uid INTEGER NOT NULL,
	title TEXT,
	_class VARCHAR(11),
	label TEXT,
	id TEXT,
	"ControlGroup_uid" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("ControlGroup_uid") REFERENCES "ControlGroup" (uid)
);
CREATE INDEX "ix_Control_uid" ON "Control" (uid);

CREATE TABLE "Address_addr_lines" (
	"Address_id" INTEGER,
	addr_lines TEXT,
	PRIMARY KEY ("Address_id", addr_lines),
	FOREIGN KEY("Address_id") REFERENCES "Address" (id)
);
CREATE INDEX "ix_Address_addr_lines_Address_id" ON "Address_addr_lines" ("Address_id");
CREATE INDEX "ix_Address_addr_lines_addr_lines" ON "Address_addr_lines" (addr_lines);

CREATE TABLE "Parameter" (
	uid INTEGER NOT NULL,
	usage TEXT,
	title TEXT,
	_class VARCHAR(11),
	label TEXT,
	id TEXT,
	"Control_uid" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("Control_uid") REFERENCES "Control" (uid)
);
CREATE INDEX "ix_Parameter_uid" ON "Parameter" (uid);

CREATE TABLE "Guideline" (
	id INTEGER NOT NULL,
	prose TEXT,
	"Parameter_uid" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Parameter_uid") REFERENCES "Parameter" (uid)
);
CREATE INDEX "ix_Guideline_id" ON "Guideline" (id);

CREATE TABLE "Part" (
	uid INTEGER NOT NULL,
	name TEXT,
	_class VARCHAR(20),
	prose TEXT,
	id TEXT,
	"CatalogElement_uid" INTEGER,
	"IdentifiedElement_uid" INTEGER,
	"ControlGroup_uid" INTEGER,
	"Control_uid" INTEGER,
	"Parameter_uid" INTEGER,
	"Part_uid" INTEGER,
	PRIMARY KEY (uid),
	FOREIGN KEY("CatalogElement_uid") REFERENCES "CatalogElement" (uid),
	FOREIGN KEY("IdentifiedElement_uid") REFERENCES "IdentifiedElement" (uid),
	FOREIGN KEY("ControlGroup_uid") REFERENCES "ControlGroup" (uid),
	FOREIGN KEY("Control_uid") REFERENCES "Control" (uid),
	FOREIGN KEY("Parameter_uid") REFERENCES "Parameter" (uid),
	FOREIGN KEY("Part_uid") REFERENCES "Part" (uid)
);
CREATE INDEX "ix_Part_uid" ON "Part" (uid);

CREATE TABLE "Property" (
	id INTEGER NOT NULL,
	name TEXT,
	value TEXT,
	ns TEXT,
	_class TEXT,
	"Metadata_id" INTEGER,
	"CatalogElement_uid" INTEGER,
	"IdentifiedElement_uid" INTEGER,
	"ControlGroup_uid" INTEGER,
	"Control_uid" INTEGER,
	"Parameter_uid" INTEGER,
	"Part_uid" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Metadata_id") REFERENCES "Metadata" (id),
	FOREIGN KEY("CatalogElement_uid") REFERENCES "CatalogElement" (uid),
	FOREIGN KEY("IdentifiedElement_uid") REFERENCES "IdentifiedElement" (uid),
	FOREIGN KEY("ControlGroup_uid") REFERENCES "ControlGroup" (uid),
	FOREIGN KEY("Control_uid") REFERENCES "Control" (uid),
	FOREIGN KEY("Parameter_uid") REFERENCES "Parameter" (uid),
	FOREIGN KEY("Part_uid") REFERENCES "Part" (uid)
);
CREATE INDEX "ix_Property_id" ON "Property" (id);

CREATE TABLE "Link" (
	id INTEGER NOT NULL,
	href TEXT,
	rel TEXT,
	"Metadata_id" INTEGER,
	"CatalogElement_uid" INTEGER,
	"IdentifiedElement_uid" INTEGER,
	"ControlGroup_uid" INTEGER,
	"Control_uid" INTEGER,
	"Parameter_uid" INTEGER,
	"Part_uid" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Metadata_id") REFERENCES "Metadata" (id),
	FOREIGN KEY("CatalogElement_uid") REFERENCES "CatalogElement" (uid),
	FOREIGN KEY("IdentifiedElement_uid") REFERENCES "IdentifiedElement" (uid),
	FOREIGN KEY("ControlGroup_uid") REFERENCES "ControlGroup" (uid),
	FOREIGN KEY("Control_uid") REFERENCES "Control" (uid),
	FOREIGN KEY("Parameter_uid") REFERENCES "Parameter" (uid),
	FOREIGN KEY("Part_uid") REFERENCES "Part" (uid)
);
CREATE INDEX "ix_Link_id" ON "Link" (id);
