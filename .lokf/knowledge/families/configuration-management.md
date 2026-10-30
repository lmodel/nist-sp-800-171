---
type: Sp800171Family
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/families/configuration-management
title: Configuration Management
description: "The SP 800-171 family 03.04, Configuration Management: 10 security requirements in force, 03.04.01 Baseline Configuration to 03.04.12 System and Component Configuration for High-Risk Areas, and two withdrawn, with 12 organization-defined parameters and 49 assessment objectives."
family_number: "03.04"
resource: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/references/sp-800-171
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/glossary/family
sources:
  - id: nist_sp800-171_rev3_catalog.json
    resource: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json
    title: the group SP_800_171_03.04
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:13:03Z"
status: draft
---

# Configuration Management (03.04)

NIST's catalog renders the family as the group `SP_800_171_03.04`, titled Configuration Management, with 12 numbered requirements.[^nist_sp800-171_rev3_catalog.json] Its 10 requirements in force carry 12 organization-defined parameters and 49 assessment objectives:

- `03.04.01` Baseline Configuration
- `03.04.02` Configuration Settings
- `03.04.03` Configuration Change Control
- `03.04.04` Impact Analyses
- `03.04.05` Access Restrictions for Change
- `03.04.06` Least Functionality
- `03.04.08` Authorized Software – Allow by Exception
- `03.04.10` System Component Inventory
- `03.04.11` Information Location
- `03.04.12` System and Component Configuration for High-Risk Areas

Revision 3 withdrew two of the family's requirements:

- `03.04.07`, incorporated into `03.04.06` and `03.04.08`
- `03.04.09`, addressed by `03.01.05`, `03.01.06`, `03.01.07`, `03.04.08`, `03.12.03`

[^nist_sp800-171_rev3_catalog.json]: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json, the group SP_800_171_03.04
