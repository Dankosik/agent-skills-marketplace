# Dankosik Skills

One author marketplace for focused engineering skills and Super Review.
The catalog points to immutable release commits; packages stay in their own
repositories. The four language packs contain only skills. Super Review uses
native host tools plus your configured model and GitHub access.

| Pack | Skills | Focus |
| --- | ---: | --- |
| [Java Backend Skills](https://github.com/Dankosik/java-backend-skills) | 15 | Java and Spring |
| [Fastify Backend Skills](https://github.com/Dankosik/fastify-backend-skills) | 15 | TypeScript and Fastify |
| [Go Backend Skills](https://github.com/Dankosik/golang-backend-skills) | 16 | Go backend development |
| [Rust CLI Skills](https://github.com/Dankosik/rust-cli-skills) | 16 | Rust command-line utilities |
| [Super Review](https://github.com/Dankosik/super-review) | 1 | Go, TypeScript, Rust, and Java readability and maintainability |

## Claude Code

```sh
claude plugin marketplace add Dankosik/agent-skills-marketplace
claude plugin install java-backend-skills@dankosik-skills
```

Replace the plugin name with any pack in the table. Inside a session, use
`/plugin marketplace add` and `/plugin install` instead. Native skills are
namespaced, for example `/java-backend-skills:java-implement`. Super Review uses
`/super-review:review <PR URL>` and requires Node.js 20+, GitHub CLI, and working
Claude Code model access.

## Codex

```sh
codex plugin marketplace add Dankosik/agent-skills-marketplace
codex plugin add rust-cli-skills@dankosik-skills
```

The author marketplace is a selectable plugin source where supported. Start a
new task after installing. Current verified command surfaces: Codex CLI 0.153.4
and Claude Code 2.1.280. See each pack's distribution guide for update behavior.

## Standalone skills and other clients

Install into a project with the Skills CLI:

```sh
npx skills@1.5.25 add "Dankosik/java-backend-skills#v1.0.0" --agent codex --skill '*' --copy
npx skills@1.5.25 add "Dankosik/fastify-backend-skills#v1.0.0" --agent codex --skill '*' --copy
npx skills@1.5.25 add "Dankosik/golang-backend-skills#v1.0.0" --agent codex --skill '*' --copy
npx skills@1.5.25 add "Dankosik/rust-cli-skills#v1.0.0" --agent codex --skill '*' --copy
```

Choose one or more packs and replace `'*'` with individual skill names when
appropriate. Use the installer-supported agent name for a different client.
Node.js >=22.20.0 is needed by this installer, not by the skills. Preserve the
installed files and lock record in Git for a reproducible project environment.
Use one installation manager per copy; installing both native and standalone
copies can duplicate skills.

GitHub CLI 2.97.0 has a preview alternative:

```sh
gh skill install Dankosik/golang-backend-skills go-implement --pin v1.0.0 --agent codex --scope project
```

## Updates

`catalog.json` owns the pack versions and exact source SHAs. The Claude and
Codex marketplace files are derived from it. Each pack releases independently.
An optional `claudePath` selects a native Claude package inside its repository.
An optional `codexPath` selects a native Codex package, including its host-specific
MCP configuration. Both subdirectories are verified at the same immutable pin.
After an upstream release, change the corresponding pin, run
`python3 scripts/catalog.py sync`, and review the update. CI checks both catalog
representations and the remote package identities.

Consumers explicitly refresh the catalog and update the selected native plugin,
or install a newer fixed standalone release on a project branch. For a frozen
catalog, check out this marketplace's release tag locally and register that
local root. Do not silently replace published tags or release assets.

## Public directories and submission

This repository is an **author-maintained marketplace** that users can add
immediately. It does not imply approval or automatic inclusion in Anthropic's
official/community catalogs or OpenAI's universal Plugins Directory.

[Distribution research](docs/research.md) explains the verified examples and
platform differences. [Submission handoff](docs/submission.md) lists the public
portals and owner-controlled steps. Each pack includes an upload-ready archive,
logo, listing copy, privacy/support links and eight proposed review scenarios.

[MIT license](LICENSE).
