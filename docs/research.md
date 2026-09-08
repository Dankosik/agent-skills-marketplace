# Distribution research — 2026-09-08

The source format remains Agent Skills: one SKILL.md per independent skill,
with the same content on all installation paths. Agent Plugins 1.0.0 adds a
portable root plugin manifest; native Claude and Codex manifests are thin
adapters. They do not require separate copies of the instructions.
[Agent Skills](https://agentskills.io/specification),
[Agent Plugins](https://agent-plugins.org/plugin-authors/manifest).

## Concrete reference: mattpocock/skills

Inspected source revision `3cca18b368ae95cdbdebbff572ccafa662551015` and current
GitHub release metadata. The repository uses a native Claude manifest and a
marketplace file. Its private package.json carries version 1.2.3, Changesets
creates version PRs/tags, and a script synchronizes the Claude manifest version.
The npm package is private: npm is used for maintainer tooling, not as the skill
payload registry. The latest observed release was v1.2.3 on 2026-08-06; those
observed releases were not marked immutable.

The README offers a managed Claude plugin and editable standalone installation
through Skills CLI, and warns that both together duplicate the skills. It
documents official Claude marketplace availability. The inspected repository
does not contain a native Codex plugin manifest; it documents the standalone
route for Codex and other hosts.
[Source](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015),
[release](https://github.com/mattpocock/skills/releases/tag/v1.2.3).

Our packs adopt the separation of content, package version, native wrapper and
installation channel. They do not need Changesets/npm tooling to publish a few
static packs; their root plugin.json is the version authority. A small helper
synchronizes native views and builds the archive. CI uses the official skill
reference validator and published plugin schema instead of creating a competing
skill format.

## Versions and updates

Each pack has an independent SemVer sequence. Names, paths, scope, invocation
expectations and required environment form its public contract. A changed
description can affect activation; Markdown edits are not automatically PATCH.
There is no new version stamp in every SKILL.md on each package release.

GitHub immutable releases protect the release tag and assets after publication.
All assets are uploaded to a draft first. Consumers can pin a release tag or full
SHA; the author catalog pins both the human-readable ref and exact commit.
[GitHub release immutability](https://docs.github.com/en/code-security/concepts/supply-chain-security/immutable-releases).

Skills CLI uses `owner/repo#ref` for a Git ref. `skills@1.5.25` names the
installer version; it does not name the skill-pack version. GitHub CLI's preview
`gh skill install --pin` offers another source-tracked installation route.
Use one manager per installed copy. Standalone project files plus their
provenance record can be reviewed and rolled back with Git.
[Skills CLI](https://github.com/vercel-labs/skills),
[GitHub CLI](https://cli.github.com/manual/gh_skill_install).

## Native marketplaces

Claude's marketplace file supports remote repositories and full SHA pins.
The native plugin version affects caching; it must change when a new release
changes package contents. Do not duplicate that version in the marketplace entry.
[Claude marketplace reference](https://code.claude.com/docs/en/plugin-marketplaces).

Codex has its own repo marketplace format at `.agents/plugins/marketplace.json`
and native `.codex-plugin/plugin.json` metadata. Git-backed entries can point to
separate root plugins with refs/SHAs. Local/author marketplaces are separate from
the universal public Plugins Directory shared by ChatGPT and Codex.
[OpenAI packaging](https://developers.openai.com/plugins/build/plugins).

## Reviewed public catalogs

Anthropic's normal submission goes through the Console or eligible organization
form. Approved third-party submissions land in the community marketplace, which
users add separately. The official marketplace is curated at Anthropic's
discretion; there is no application process guaranteeing inclusion there.
[Anthropic submission process](https://code.claude.com/docs/en/plugins#submit-your-plugin-to-the-community-marketplace).

OpenAI accepts skills-only plugins through its submission portal. It requires
Apps Management write access, a verified developer/business identity, listing
and policy URLs, logo, five positive and three negative cases, availability,
and policy attestations. Submission starts review. After approval, the developer
publishes to the universal directory. A qualifying Claude skills archive can
also be uploaded and converted by that portal.
[OpenAI submission](https://developers.openai.com/plugins/deploy/submission),
[Claude archive import](https://developers.openai.com/plugins/guides/submit-claude-plugin).

Publishing GitHub releases or this catalog does not complete either review
process. Installation/discovery checks are also distinct from model-behavior
evaluations. The submitted pack instructions must remain minimal and accurately
describe their capabilities, without claiming nonexistent tools or services.
