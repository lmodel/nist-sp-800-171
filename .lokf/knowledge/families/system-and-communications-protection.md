---
type: Sp800171Family
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/families/system-and-communications-protection
title: System and Communications Protection
description: "The SP 800-171 family 03.13, System and Communications Protection: 10 security requirements in force, 03.13.01 Boundary Protection to 03.13.15 Session Authenticity, and six withdrawn, with 4 organization-defined parameters and 24 assessment objectives."
family_number: "03.13"
resource: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/references/sp-800-171
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/glossary/family
sources:
  - id: nist_sp800-171_rev3_catalog.json
    resource: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json
    title: the group SP_800_171_03.13
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:13:03Z"
status: draft
---

# System and Communications Protection (03.13)

NIST's catalog renders the family as the group `SP_800_171_03.13`, titled System and Communications Protection, with 16 numbered requirements.[^nist_sp800-171_rev3_catalog.json] Its 10 requirements in force carry 4 organization-defined parameters and 24 assessment objectives:

- `03.13.01` Boundary Protection
- `03.13.04` Information in Shared System Resources
- `03.13.06` Network Communications – Deny by Default – Allow by Exception
- `03.13.08` Transmission and Storage Confidentiality
- `03.13.09` Network Disconnect
- `03.13.10` Cryptographic Key Establishment and Management
- `03.13.11` Cryptographic Protection
- `03.13.12` Collaborative Computing Devices and Applications
- `03.13.13` Mobile Code
- `03.13.15` Session Authenticity

Revision 3 withdrew six of the family's requirements:

- `03.13.02`, with no successor the catalog states
- `03.13.03`, addressed by `03.01.01`, `03.01.02`, `03.01.03`, `03.01.04`, `03.01.05`, `03.01.06`, `03.01.07`
- `03.13.05`, incorporated into `03.13.01`
- `03.13.07`, addressed by `03.01.12`, `03.04.02`, `03.04.06`
- `03.13.14`, with no successor the catalog states
- `03.13.16`, incorporated into `03.13.08`

[^nist_sp800-171_rev3_catalog.json]: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json, the group SP_800_171_03.13
