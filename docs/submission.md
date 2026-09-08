# Public-directory submission handoff

The author marketplace is available independently of provider review. The four
pack releases include upload-ready archives, file hashes, logos, listing fields,
privacy/support information and eight proposed test scenarios in each
`docs/submission.md`. Those proposed model scenarios are not labeled as executed
packaging tests.

## OpenAI

Open [the plugin portal](https://platform.openai.com/plugins). Sign in to the
publishing organization. Its owner has the required access; other submitters
need **Apps Management: Write**. Complete individual or business verification,
select that identity, and choose **Skills only** for each pack.

Upload the corresponding release ZIP. Use its submission packet for listing,
prompts and the required five positive/three negative cases. Confirm the actual
publisher identity, support details, availability regions and policy attestations.
Do not invent credentials: these packs have no account integration or MCP server.
Submit for review, resolve any scan/reviewer feedback, and publish through the
portal after approval.

[Official instructions](https://developers.openai.com/plugins/deploy/submission).

## Anthropic

Individual authors can use [Claude Console](https://platform.claude.com/plugins/submit).
An eligible Team/Enterprise organization with directory-management access can
use [the organization form](https://claude.ai/admin-settings/directory/submissions/plugins/new).
Supply the released plugin repository/version and the prepared listing materials.

The review includes native manifest validation and automated safety screening.
Community catalog publication may lag approval until its next sync. The official
catalog is separately curated by Anthropic; the ordinary form cannot guarantee
that placement.

[Official instructions](https://code.claude.com/docs/en/plugins#submit-your-plugin-to-the-community-marketplace).

## Owner actions

Authentication, verified identity, availability choices and legal/policy
attestations remain with the publisher. A GitHub username or local plugin
installation does not establish them. No provider submission has been marked
approved merely because a release exists. Keep approval/publication status
separate from the source releases and this independently usable author catalog.
