---
type: Sp800171Family
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/families/audit-and-accountability
title: Audit and Accountability
description: "The SP 800-171 family 03.03, Audit and Accountability: 8 security requirements in force, 03.03.01 Event Logging to 03.03.08 Protection of Audit Information, and one withdrawn, with 6 organization-defined parameters and 30 assessment objectives."
family_number: "03.03"
resource: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/references/sp-800-171
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/glossary/family
sources:
  - id: nist_sp800-171_rev3_catalog.json
    resource: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json
    title: the group SP_800_171_03.03
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:13:03Z"
status: draft
---

# Audit and Accountability (03.03)

NIST's catalog renders the family as the group `SP_800_171_03.03`, titled Audit and Accountability, with 9 numbered requirements.[^nist_sp800-171_rev3_catalog.json] Its 8 requirements in force carry 6 organization-defined parameters and 30 assessment objectives:

- `03.03.01` Event Logging
- `03.03.02` Audit Record Content
- `03.03.03` Audit Record Generation
- `03.03.04` Response to Audit Logging Process Failures
- `03.03.05` Audit Record Review, Analysis, and Reporting
- `03.03.06` Audit Record Reduction and Report Generation
- `03.03.07` Time Stamps
- `03.03.08` Protection of Audit Information

Revision 3 withdrew one of the family's requirements:

- `03.03.09`, incorporated into `03.03.08`

[^nist_sp800-171_rev3_catalog.json]: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json, the group SP_800_171_03.03
