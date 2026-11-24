# Project Governance

## Maintainer Structure

- **Project Steward (`Divinari`):** Holds final operational, legal, trademark, security, and release authority across Divinari repositories (`CODEOWNERS`), maintaining clean-room separation between open repositories and commercial infrastructure.
- **Language Leads *(Community Role)*:** Trusted bilingual linguists or native speakers appointed per language code (`tl`, `ceb`, `ilo`, `hil`, etc.) to review vocabulary accuracy, register labels, and regional nuance.
- **Cultural Advisors *(Community Role)*:** Educators, elders, or community historians consulted on heritage packs, script conventions, and Indigenous Data Ethics compliance.
- **Technical Maintainers:** Maintain JSON Schemas, CI validators, encoding checks, and air-gapped downstream integration scripts.

## Repository Authority

No automated community Pull Request writes directly to production Divinari servers, databases, or mobile/web releases. All production imports pass manual human copyright and quality review downstream.
