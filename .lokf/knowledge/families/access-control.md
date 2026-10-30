---
type: Sp800171Family
id: https://w3id.org/lmodel/nist-sp-800-171/knowledge/families/access-control
title: Access Control
description: "The SP 800-171 family 03.01, Access Control: 16 security requirements in force, 03.01.01 Account Management to 03.01.22 Publicly Accessible Content, and six withdrawn, with 18 organization-defined parameters and 74 assessment objectives."
family_number: "03.01"
resource: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json
definedBy:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/references/sp-800-171
relatedTo:
  - https://w3id.org/lmodel/nist-sp-800-171/knowledge/glossary/family
sources:
  - id: nist_sp800-171_rev3_catalog.json
    resource: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json
    title: the group SP_800_171_03.01
generated:
  by: process:ktl-librarian
  at: "2026-10-30T01:13:03Z"
status: draft
---

# Access Control (03.01)

NIST's catalog renders the family as the group `SP_800_171_03.01`, titled Access Control, with 22 numbered requirements.[^nist_sp800-171_rev3_catalog.json] Its 16 requirements in force carry 18 organization-defined parameters and 74 assessment objectives:

- `03.01.01` Account Management
- `03.01.02` Access Enforcement
- `03.01.03` Information Flow Enforcement
- `03.01.04` Separation of Duties
- `03.01.05` Least Privilege
- `03.01.06` Least Privilege – Privileged Accounts
- `03.01.07` Least Privilege – Privileged Functions
- `03.01.08` Unsuccessful Logon Attempts
- `03.01.09` System Use Notification
- `03.01.10` Device Lock
- `03.01.11` Session Termination
- `03.01.12` Remote Access
- `03.01.16` Wireless Access
- `03.01.18` Access Control for Mobile Devices
- `03.01.20` Use of External Systems
- `03.01.22` Publicly Accessible Content

Revision 3 withdrew six of the family's requirements:

- `03.01.13`, addressed by `03.13.08`
- `03.01.14`, incorporated into `03.01.12`
- `03.01.15`, incorporated into `03.01.12`
- `03.01.17`, incorporated into `03.01.16`
- `03.01.19`, incorporated into `03.01.18`
- `03.01.21`, incorporated into `03.01.20`

[^nist_sp800-171_rev3_catalog.json]: src/nist_sp_800_171/schema/oscal-content/NIST_SP800-171_rev3_catalog.json, the group SP_800_171_03.01
