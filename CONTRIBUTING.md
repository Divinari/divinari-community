# Contributing to `divinari-community`

Thank you for helping build an open, inclusive ecosystem for language preservation and heritage education!

## Important Scope Boundaries

1. **Proprietary Platform Remains Private:** Divinari's mobile/web application source code, backend services, billing logic, and AI Teacher prompts are maintained privately and are outside this repository.
2. **No Automatic App Deployment:** Merging a Pull Request into `divinari-community` updates public community documentation and governance only—it does **not** deploy directly to `divinari.app` or mobile releases.
3. **No Unapproved Endorsements:** Do not add external institution, church, NGO, or university names as confirmed partners without documented written authorization.

## How to Contribute

1. Open an issue using `.github/ISSUE_TEMPLATE/` (language request, volunteer reviewer application, or partnership inquiry) or fork the repository for documentation improvements.
2. Ensure all markdown files use UTF-8 (without BOM), NFC Unicode normalization, and Unix LF (`\n`) line endings.
3. Sign off every commit under the **Developer Certificate of Origin (DCO 1.1)** (`git commit -s`):

```text
Developer Certificate of Origin
Version 1.1

Copyright (C) 2004, 2006 The Linux Foundation and its contributors.

By making a contribution to this project, I certify that:
(a) The contribution was created in whole or in part by me and I have the
    right to submit it under the open source license indicated in the file; or
(b) The contribution is based upon previous work that, to the best of my
    knowledge, is covered under an appropriate open source license and I have
    the right under that license to submit that work with modifications; or
(c) The contribution was provided directly to me by some other person who
    certified (a), (b) or (c) and I have not modified it.
(d) I understand and agree that this project and the contribution are public
    and that a record of the contribution (including all personal information
    I submit with it, including my sign-off) is maintained indefinitely and may
    be redistributed consistent with this project or the open source license(s)
    involved.
```

Example commit trailer:
```text
Signed-off-by: Your Name <you@example.org>
```

## Review Process

All pull requests require review from `.github/CODEOWNERS` maintainers and must pass automated formatting and clean-room lint checks before merge.
