#!/usr/bin/env python3
"""Render and check the Claude/Codex catalogs from one set of release pins."""

import argparse
import json
from pathlib import Path
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def render(catalog):
    entries = catalog["plugins"]
    names = [entry["name"] for entry in entries]
    if len(names) != len(set(names)):
        raise ValueError("duplicate plugin names")
    claude = {"name": catalog["name"], "description": catalog["description"], "owner": {"name": "Dankosik", "url": "https://github.com/Dankosik"}, "plugins": []}
    codex = {"name": catalog["name"], "interface": {"displayName": catalog["displayName"]}, "plugins": []}
    for entry in entries:
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", entry["name"]):
            raise ValueError("invalid plugin name")
        if not re.fullmatch(r"[0-9a-f]{40}", entry["sha"]):
            raise ValueError("plugin source must use a full immutable commit")
        if not re.fullmatch(r"https://github\.com/[A-Za-z0-9-]+/[A-Za-z0-9_.-]+", entry["repository"]):
            raise ValueError("unexpected repository URL")
        if not re.fullmatch(r"\d+\.\d+\.\d+", entry["version"]):
            raise ValueError("invalid package version")
        pin = {"ref": "v" + entry["version"], "sha": entry["sha"]}
        claude_source = {"source": "github", "repo": entry["repository"].removeprefix("https://github.com/"), **pin}
        if claude_path := entry.get("claudePath"):
            if not re.fullmatch(r"[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*", claude_path) or any(part in {".", ".."} for part in claude_path.split("/")):
                raise ValueError("invalid Claude plugin subdirectory")
            claude_source = {"source": "git-subdir", "url": entry["repository"] + ".git", "path": claude_path, **pin}
        claude["plugins"].append({"name": entry["name"], "source": claude_source, "description": entry["description"], "category": "development"})
        codex_source = {"source": "url", "url": entry["repository"] + ".git", **pin}
        if codex_path := entry.get("codexPath"):
            if not re.fullmatch(r"[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*", codex_path) or any(part in {".", ".."} for part in codex_path.split("/")):
                raise ValueError("invalid Codex plugin subdirectory")
            codex_source = {"source": "git-subdir", "url": entry["repository"] + ".git", "path": codex_path, **pin}
        codex["plugins"].append({"name": entry["name"], "source": codex_source, "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "category": "Productivity"})
    return {".claude-plugin/marketplace.json": claude, ".agents/plugins/marketplace.json": codex}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["sync", "check"])
    parser.add_argument("--remote", action="store_true")
    args = parser.parse_args()
    catalog = json.loads((ROOT / "catalog.json").read_text())
    for relative, expected in render(catalog).items():
        path = ROOT / relative
        if args.command == "sync":
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(expected, indent=2) + "\n")
        elif json.loads(path.read_text()) != expected:
            raise ValueError("catalog drift: " + relative)
    if args.remote:
        for entry in catalog["plugins"]:
            repo = entry["repository"].removeprefix("https://github.com/")
            url = "https://raw.githubusercontent.com/" + repo + "/" + entry["sha"] + "/plugin.json"
            with urllib.request.urlopen(url, timeout=30) as response:
                package = json.load(response)
            if package["name"] != entry["name"] or package["version"] != entry["version"]:
                raise ValueError("remote package identity mismatch: " + entry["name"])
            if claude_path := entry.get("claudePath"):
                url = "https://raw.githubusercontent.com/" + repo + "/" + entry["sha"] + "/" + claude_path + "/.claude-plugin/plugin.json"
                with urllib.request.urlopen(url, timeout=30) as response:
                    native = json.load(response)
                if native["name"] != entry["name"] or native["version"] != entry["version"]:
                    raise ValueError("remote Claude package identity mismatch: " + entry["name"])
            if codex_path := entry.get("codexPath"):
                url = "https://raw.githubusercontent.com/" + repo + "/" + entry["sha"] + "/" + codex_path + "/.codex-plugin/plugin.json"
                with urllib.request.urlopen(url, timeout=30) as response:
                    native = json.load(response)
                if native["name"] != entry["name"] or native["version"] != entry["version"]:
                    raise ValueError("remote Codex package identity mismatch: " + entry["name"])
    print(f"Validated {len(catalog['plugins'])} pinned plugins in both native catalogs")


if __name__ == "__main__":
    main()
