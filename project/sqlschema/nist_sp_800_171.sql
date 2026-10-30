-- # Class: Sp800171Publication Description: One revision of SP 800-171 as a whole: its requirement families, each holding its security requirements, with the assessment procedures of the matching revision of SP 800-171A inside each requirement.
--     * Slot: id
--     * Slot: sp800171_revision Description: The revision of SP 800-171 the document renders, as NIST numbers it, such as 3.
-- # Class: Sp800171Family Description: One of the seventeen families that SP 800-171 Revision 3 sorts its security requirements into, such as Access Control (03.01) or Supply Chain Risk Management (03.17).
--     * Slot: id
--     * Slot: title Description: The name SP 800-171 gives a family or a security requirement, such as Access Control or Account Management.
--     * Slot: description Description: What the family or requirement is about, in the words of whoever records it. SP 800-171 gives a family no text of its own, and a requirement's own text goes in its statement, items and discussion.
--     * Slot: family_number Description: The family's number, such as 03.01.
--     * Slot: Sp800171Publication_id Description: Autocreated FK slot
-- # Class: Sp800171Requirement Description: A security requirement of SP 800-171: a numbered, named requirement for protecting CUI, with its statement, discussion, references and source controls, the organization-defined parameters its statement leaves open, and the assessment objectives and methods SP 800-171A gives it. A requirement that Revision 3 withdrew keeps its number and says which requirements took its place.
--     * Slot: id
--     * Slot: title Description: The name SP 800-171 gives a family or a security requirement, such as Access Control or Account Management.
--     * Slot: description Description: What the family or requirement is about, in the words of whoever records it. SP 800-171 gives a family no text of its own, and a requirement's own text goes in its statement, items and discussion.
--     * Slot: requirement_id Description: The requirement's identifier, such as 03.01.01.
--     * Slot: requirement_status Description: Withdrawn when Revision 3 withdrew the requirement. A requirement with no status is in force.
--     * Slot: requirement_statement Description: The requirement statement when SP 800-171 writes it as one piece of text and not as lettered items. The catalog marks an organization-defined parameter in the text with an insert placeholder that names the parameter.
--     * Slot: requirement_discussion Description: The requirement's discussion: SP 800-171's explanation of what the requirement means and how it relates to other requirements.
--     * Slot: Sp800171Family_id Description: Autocreated FK slot
-- # Class: Sp800171RequirementItem Description: One item of a requirement statement: a lettered item such as 03.01.01.a, or a numbered item under a lettered one such as 03.01.01.c.01.
--     * Slot: id
--     * Slot: requirement_item_id Description: The item's identifier, such as 03.01.01.a.
--     * Slot: requirement_item_text Description: What the item requires. The catalog marks an organization-defined parameter in the text with an insert placeholder that names the parameter.
--     * Slot: Sp800171Requirement_id Description: Autocreated FK slot
--     * Slot: Sp800171RequirementItem_id Description: Autocreated FK slot
-- # Class: Sp800171Parameter Description: An organization-defined parameter (ODP): a value, such as a time period or a frequency, that a requirement statement leaves to the organization, with the guideline SP 800-171A gives for defining it. A few parameters are a selection among choices instead of a value.
--     * Slot: id
--     * Slot: odp_id Description: The parameter's identifier, such as A.03.01.01.ODP[01].
--     * Slot: odp_label Description: What kind of value the parameter takes, such as time period or frequency, or SELECTED PARAMETER VALUES for a selection.
--     * Slot: odp_usage Description: How the requirement statement names the parameter, such as organization-defined time period.
--     * Slot: odp_guideline Description: The determination SP 800-171A gives for the parameter: what the organization must have defined, such as the time period for account inactivity before disabling is defined.
--     * Slot: odp_selection_count Description: How many of the choices a selection takes.
--     * Slot: Sp800171Requirement_id Description: Autocreated FK slot
-- # Class: Sp800171AssessmentObjective Description: An assessment objective of SP 800-171A: one determination statement that an assessor checks, tied to the requirement or to one item of its statement.
--     * Slot: id
--     * Slot: requirement_objective_id Description: The objective's identifier, such as A.03.01.01.b[01].
--     * Slot: requirement_determination Description: The determination statement: what the assessor determines is the case, such as system accounts are created in accordance with organizational policy, procedures, prerequisites, and criteria.
--     * Slot: assessed_requirement_item Description: The statement item the objective assesses, such as 03.01.01.b. Absent when the objective assesses a requirement whose statement is one piece of text.
--     * Slot: Sp800171Requirement_id Description: Autocreated FK slot
-- # Class: Sp800171AssessmentMethod Description: One of the three assessment methods SP 800-171A applies to a requirement, examine, interview or test, with the assessment objects (documents, people, processes or mechanisms) it is applied to.
--     * Slot: id
--     * Slot: requirement_method_kind Description: Which method it is.
--     * Slot: Sp800171Requirement_id Description: Autocreated FK slot
-- # Class: Sp800171Reference Description: A publication that SP 800-171 lists under a requirement's references, by the short name the publication gives it, with the full citation and the address NIST's catalog gives it.
--     * Slot: id
--     * Slot: cited_publication Description: The publication's short name, such as SP 800-63-3.
--     * Slot: cited_publication_citation Description: The full citation, as the catalog's back matter gives it.
--     * Slot: cited_publication_url Description: The publication's address, which the catalog gives as its digital object identifier at doi.org.
--     * Slot: Sp800171Requirement_id Description: Autocreated FK slot
-- # Class: Sp800171Requirement_incorporated_into_requirements
--     * Slot: Sp800171Requirement_id Description: Autocreated FK slot
--     * Slot: incorporated_into_requirements Description: For a withdrawn requirement, the requirements of Revision 3 that incorporate what it required, as the catalog states them.
-- # Class: Sp800171Requirement_addressed_by_requirements
--     * Slot: Sp800171Requirement_id Description: Autocreated FK slot
--     * Slot: addressed_by_requirements Description: For a withdrawn requirement, the requirements of Revision 3 that address what it required, as the catalog states them.
-- # Class: Sp800171Requirement_source_controls
--     * Slot: Sp800171Requirement_id Description: Autocreated FK slot
--     * Slot: source_controls Description: The controls of SP 800-53 Revision 5 the requirement is drawn from, by their identifiers, as the catalog lists them among the requirement's references. The identifier is data; the schema maps nothing to a model of SP 800-53.
-- # Class: Sp800171Parameter_odp_choices
--     * Slot: Sp800171Parameter_id Description: Autocreated FK slot
--     * Slot: odp_choices Description: For a selection, the choices SP 800-171 offers, in its order. A choice may itself carry an insert placeholder naming another parameter.
-- # Class: Sp800171AssessmentMethod_requirement_method_objects
--     * Slot: Sp800171AssessmentMethod_id Description: Autocreated FK slot
--     * Slot: requirement_method_objects Description: The assessment objects, one entry each, in the order SP 800-171A lists them, such as access control policy and procedures or system administrators.

CREATE TABLE "Sp800171Publication" (
	id INTEGER NOT NULL,
	sp800171_revision TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Sp800171Publication_id" ON "Sp800171Publication" (id);

CREATE TABLE "Sp800171Family" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	family_number TEXT NOT NULL,
	"Sp800171Publication_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Sp800171Publication_id") REFERENCES "Sp800171Publication" (id)
);
CREATE INDEX "ix_Sp800171Family_id" ON "Sp800171Family" (id);

CREATE TABLE "Sp800171Requirement" (
	id INTEGER NOT NULL,
	title TEXT,
	description TEXT,
	requirement_id TEXT NOT NULL,
	requirement_status VARCHAR(9),
	requirement_statement TEXT,
	requirement_discussion TEXT,
	"Sp800171Family_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Sp800171Family_id") REFERENCES "Sp800171Family" (id)
);
CREATE INDEX "ix_Sp800171Requirement_id" ON "Sp800171Requirement" (id);

CREATE TABLE "Sp800171RequirementItem" (
	id INTEGER NOT NULL,
	requirement_item_id TEXT NOT NULL,
	requirement_item_text TEXT NOT NULL,
	"Sp800171Requirement_id" INTEGER,
	"Sp800171RequirementItem_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Sp800171Requirement_id") REFERENCES "Sp800171Requirement" (id),
	FOREIGN KEY("Sp800171RequirementItem_id") REFERENCES "Sp800171RequirementItem" (id)
);
CREATE INDEX "ix_Sp800171RequirementItem_id" ON "Sp800171RequirementItem" (id);

CREATE TABLE "Sp800171Parameter" (
	id INTEGER NOT NULL,
	odp_id TEXT NOT NULL,
	odp_label TEXT NOT NULL,
	odp_usage TEXT,
	odp_guideline TEXT,
	odp_selection_count VARCHAR(11),
	"Sp800171Requirement_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Sp800171Requirement_id") REFERENCES "Sp800171Requirement" (id)
);
CREATE INDEX "ix_Sp800171Parameter_id" ON "Sp800171Parameter" (id);

CREATE TABLE "Sp800171AssessmentObjective" (
	id INTEGER NOT NULL,
	requirement_objective_id TEXT NOT NULL,
	requirement_determination TEXT NOT NULL,
	assessed_requirement_item TEXT,
	"Sp800171Requirement_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Sp800171Requirement_id") REFERENCES "Sp800171Requirement" (id)
);
CREATE INDEX "ix_Sp800171AssessmentObjective_id" ON "Sp800171AssessmentObjective" (id);

CREATE TABLE "Sp800171AssessmentMethod" (
	id INTEGER NOT NULL,
	requirement_method_kind VARCHAR(9) NOT NULL,
	"Sp800171Requirement_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Sp800171Requirement_id") REFERENCES "Sp800171Requirement" (id)
);
CREATE INDEX "ix_Sp800171AssessmentMethod_id" ON "Sp800171AssessmentMethod" (id);

CREATE TABLE "Sp800171Reference" (
	id INTEGER NOT NULL,
	cited_publication TEXT NOT NULL,
	cited_publication_citation TEXT NOT NULL,
	cited_publication_url TEXT NOT NULL,
	"Sp800171Requirement_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("Sp800171Requirement_id") REFERENCES "Sp800171Requirement" (id)
);
CREATE INDEX "ix_Sp800171Reference_id" ON "Sp800171Reference" (id);

CREATE TABLE "Sp800171Requirement_incorporated_into_requirements" (
	"Sp800171Requirement_id" INTEGER,
	incorporated_into_requirements TEXT,
	PRIMARY KEY ("Sp800171Requirement_id", incorporated_into_requirements),
	FOREIGN KEY("Sp800171Requirement_id") REFERENCES "Sp800171Requirement" (id)
);
CREATE INDEX "ix_Sp800171Requirement_incorporated_into_requirements_Sp800171Requirement_id" ON "Sp800171Requirement_incorporated_into_requirements" ("Sp800171Requirement_id");
CREATE INDEX "ix_Sp800171Requirement_incorporated_into_requirements_incorporated_into_requirements" ON "Sp800171Requirement_incorporated_into_requirements" (incorporated_into_requirements);

CREATE TABLE "Sp800171Requirement_addressed_by_requirements" (
	"Sp800171Requirement_id" INTEGER,
	addressed_by_requirements TEXT,
	PRIMARY KEY ("Sp800171Requirement_id", addressed_by_requirements),
	FOREIGN KEY("Sp800171Requirement_id") REFERENCES "Sp800171Requirement" (id)
);
CREATE INDEX "ix_Sp800171Requirement_addressed_by_requirements_addressed_by_requirements" ON "Sp800171Requirement_addressed_by_requirements" (addressed_by_requirements);
CREATE INDEX "ix_Sp800171Requirement_addressed_by_requirements_Sp800171Requirement_id" ON "Sp800171Requirement_addressed_by_requirements" ("Sp800171Requirement_id");

CREATE TABLE "Sp800171Requirement_source_controls" (
	"Sp800171Requirement_id" INTEGER,
	source_controls TEXT,
	PRIMARY KEY ("Sp800171Requirement_id", source_controls),
	FOREIGN KEY("Sp800171Requirement_id") REFERENCES "Sp800171Requirement" (id)
);
CREATE INDEX "ix_Sp800171Requirement_source_controls_source_controls" ON "Sp800171Requirement_source_controls" (source_controls);
CREATE INDEX "ix_Sp800171Requirement_source_controls_Sp800171Requirement_id" ON "Sp800171Requirement_source_controls" ("Sp800171Requirement_id");

CREATE TABLE "Sp800171Parameter_odp_choices" (
	"Sp800171Parameter_id" INTEGER,
	odp_choices TEXT,
	PRIMARY KEY ("Sp800171Parameter_id", odp_choices),
	FOREIGN KEY("Sp800171Parameter_id") REFERENCES "Sp800171Parameter" (id)
);
CREATE INDEX "ix_Sp800171Parameter_odp_choices_Sp800171Parameter_id" ON "Sp800171Parameter_odp_choices" ("Sp800171Parameter_id");
CREATE INDEX "ix_Sp800171Parameter_odp_choices_odp_choices" ON "Sp800171Parameter_odp_choices" (odp_choices);

CREATE TABLE "Sp800171AssessmentMethod_requirement_method_objects" (
	"Sp800171AssessmentMethod_id" INTEGER,
	requirement_method_objects TEXT NOT NULL,
	PRIMARY KEY ("Sp800171AssessmentMethod_id", requirement_method_objects),
	FOREIGN KEY("Sp800171AssessmentMethod_id") REFERENCES "Sp800171AssessmentMethod" (id)
);
CREATE INDEX "ix_Sp800171AssessmentMethod_requirement_method_objects_requirement_method_objects" ON "Sp800171AssessmentMethod_requirement_method_objects" (requirement_method_objects);
CREATE INDEX "ix_Sp800171AssessmentMethod_requirement_method_objects_Sp800171AssessmentMethod_id" ON "Sp800171AssessmentMethod_requirement_method_objects" ("Sp800171AssessmentMethod_id");
