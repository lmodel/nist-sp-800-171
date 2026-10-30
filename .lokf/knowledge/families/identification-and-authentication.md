---
type: Sp800171Family
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/families/identification-and-authentication
title: Identification and Authentication
description: "The SP 800-171 family 03.05, Identification and Authentication: 8 security requirements in force, 03.05.01 User Identification and Authentication to 03.05.12 Authenticator Management, and four withdrawn, with 8 organization-defined parameters and 36 assessment objectives."
family_number: "03.05"
resource: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/references/sp-800-171
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/glossary/family
sources:
  - id: nist_sp800-171_rev3_catalog.json
    resource: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json
    title: the group SP_800_171_03.05
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:13:03Z"
status: draft
---

# Identification and Authentication (03.05)

NIST's catalog renders the family as the group `SP_800_171_03.05`, titled Identification and Authentication, with 12 numbered requirements.[^nist_sp800-171_rev3_catalog.json] Its 8 requirements in force carry 8 organization-defined parameters and 36 assessment objectives:

- `03.05.01` User Identification and Authentication
- `03.05.02` Device Identification and Authentication
- `03.05.03` Multi-Factor Authentication
- `03.05.04` Replay-Resistant Authentication
- `03.05.05` Identifier Management
- `03.05.07` Password Management
- `03.05.11` Authentication Feedback
- `03.05.12` Authenticator Management

Revision 3 withdrew four of the family's requirements:

- `03.05.06`, with no successor the catalog states
- `03.05.08`, with no successor the catalog states
- `03.05.09`, with no successor the catalog states
- `03.05.10`, incorporated into `03.05.07`

[^nist_sp800-171_rev3_catalog.json]: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json, the group SP_800_171_03.05
