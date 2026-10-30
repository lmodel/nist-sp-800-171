---
type: Sp800171Family
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/families/media-protection
title: Media Protection
description: "The SP 800-171 family 03.08, Media Protection: 7 security requirements in force, 03.08.01 Media Storage to 03.08.09 System Backup – Cryptographic Protection, and two withdrawn, with 1 organization-defined parameters and 15 assessment objectives."
family_number: "03.08"
resource: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/references/sp-800-171
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/glossary/family
sources:
  - id: nist_sp800-171_rev3_catalog.json
    resource: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json
    title: the group SP_800_171_03.08
generated:
  by: process:ktl-librarian
  at: "2026-10-30T08:32:20Z"
status: draft
---

# Media Protection (03.08)

NIST's catalog renders the family as the group `SP_800_171_03.08`, titled Media Protection, with 9 numbered requirements.[^nist_sp800-171_rev3_catalog.json] Its 7 requirements in force carry 1 organization-defined parameters and 15 assessment objectives:

- `03.08.01` Media Storage
- `03.08.02` Media Access
- `03.08.03` Media Sanitization
- `03.08.04` Media Marking
- `03.08.05` Media Transport
- `03.08.07` Media Use
- `03.08.09` System Backup – Cryptographic Protection

Revision 3 withdrew two of the family's requirements:

- `03.08.06`, incorporated into `03.13.08` as NIST's catalog gives it; SP 800-171 and SP 800-171A say that `03.13.08` addresses it
- `03.08.08`, incorporated into `03.08.07`

[^nist_sp800-171_rev3_catalog.json]: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json, the group SP_800_171_03.08
