#!/usr/bin/env python3
"""Read-only Daldal repository inventory. Prints metadata, never config contents.

Usage: python inspect_repository.py REPO [--mode summary|catalog|history] [--query TEXT]
Catalog extraction is lexical navigation, not a Java/JS semantic call graph.
History includes all locally available refs; no fetch, checkout, build, or DB calls.
"""
import argparse
import collections
import json
import pathlib
import re
import subprocess
import sys
import xml.etree.ElementTree as ET


def git(root, *args):
    result = subprocess.run(["git", "-c", "core.quotepath=false", "-C", str(root), *args], capture_output=True, timeout=60)
    if result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace").strip())
    return result.stdout.decode("utf-8", errors="replace")


def inventory(root):
    files = git(root, "ls-files", "-z").split("\0")
    files = [p for p in files if p]
    sources = [p for p in files if p.startswith("src/") and pathlib.PurePosixPath(p).suffix in {".java", ".xml", ".js", ".jsx", ".ts", ".tsx", ".html"} and not any(s in p for s in ("/assets/", "/static/lib/", "/static/vendor/", "/static/js/ckeditor5/", "/static/js/flatpickr/", ".min."))]
    return files, sources


def catalog(root, sources):
    out = {"controllers": [], "mappers": [], "frontend": [], "errors": [], "scannedFiles": 0, "scannedLines": 0}
    for path in sources:
        try:
            content = (root / path).read_text(encoding="utf-8-sig")
        except (OSError, UnicodeError) as exc:
            out["errors"].append({"path": path, "error": type(exc).__name__})
            continue
        out["scannedFiles"] += 1
        out["scannedLines"] += content.count("\n") + 1
        if path.endswith("Controller.java"):
            mappings = []
            for match in re.finditer(r"@(Request|Get|Post|Put|Delete|Patch)Mapping\s*(?:\(([^;]*?)\))?", content, re.S):
                args = re.findall(r'"([^"\r\n]*)"', match.group(2) or "")
                mappings.append({"kind": match.group(1), "paths": args, "line": content.count("\n", 0, match.start()) + 1})
            out["controllers"].append({"path": path, "mappings": mappings})
        if path.endswith(".xml") and "/mapper/" in path:
            try:
                node = ET.fromstring(content)
            except ET.ParseError as exc:
                out["errors"].append({"path": path, "error": "XML:" + str(exc)})
                continue
            for child in node:
                if child.tag not in {"select", "insert", "update", "delete", "sql"}:
                    continue
                sql = " ".join(child.itertext())
                symbol = child.get("id", "")
                match = re.search(r'\bid\s*=\s*[\"\x27]' + re.escape(symbol) + r'[\"\x27]', content)
                out["mappers"].append({"path": path, "namespace": node.get("namespace"), "id": symbol, "kind": child.tag, "line": content.count("\n", 0, match.start()) + 1 if match else None, "tables": sorted(set(re.findall(r"\bTB_[A-Z0-9_]+\b", sql, re.I))), "parameters": sorted(set(re.findall(r"[#\$]\{([^},]+)", sql))), "includes": [i.get("refid") for i in child.iter("include")]})
        if path.endswith((".js", ".jsx", ".ts", ".tsx")) and any(x in path for x in ("/services/", "/routers/", "/store/", "/hooks/", "/hook/")):
            calls = [{"method": m.group(1), "url": m.group(2), "line": content.count("\n", 0, m.start()) + 1} for m in re.finditer(r"\.(get|post|put|patch|delete)\s*\(\s*['\"`]([^'\"`\n]+)", content) if m.group(2).startswith(("/", "http", "${"))]
            calls += [{"method": m.group(1), "url": m.group(2), "line": content.count("\n", 0, m.start()) + 1} for m in re.finditer(r"requestApi\s*\(\s*['\"](GET|POST|PUT|PATCH|DELETE)['\"]\s*,\s*['\"`]([^'\"`\n]+)", content)]
            exports = sorted(set(re.findall(r"export\s+(?:default\s+)?(?:async\s+)?(?:function|const|class)\s+(\w+)", content)))
            out["frontend"].append({"path": path, "calls": calls, "exports": exports})
    return out


def history(root):
    reachable = set(git(root, "rev-list", "HEAD").splitlines())
    raw = git(root, "log", "--all", "--date=short", "--format=%x1e%H%x1f%ad%x1f%s", "--name-only")
    commits = []
    for block in raw.split("\x1e"):
        if not block.strip():
            continue
        lines = block.strip().splitlines()
        fields = lines[0].split("\x1f", 2)
        if len(fields) != 3:
            continue
        commits.append({"sha": fields[0], "date": fields[1], "subject": fields[2], "reachableFromHead": fields[0] in reachable, "files": [x for x in lines[1:] if x.strip()]})
    return commits


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=pathlib.Path)
    parser.add_argument("--mode", choices=["summary", "catalog", "history"], default="summary")
    parser.add_argument("--query", default="")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=0, help="History page size; zero returns all matching commits")
    args = parser.parse_args()
    root = args.repo.resolve(strict=True)
    files, sources = inventory(root)
    out = {"repo": root.name, "head": git(root, "rev-parse", "HEAD").strip(), "branch": git(root, "branch", "--show-current").strip(), "status": git(root, "status", "--short").splitlines(), "trackedFiles": len(files), "sourceCandidates": len(sources), "localCommitCount": int(git(root, "rev-list", "--count", "--all")), "shallow": git(root, "rev-parse", "--is-shallow-repository").strip() == "true"}
    if args.mode == "catalog":
        out["catalog"] = catalog(root, sources)
        if args.query:
            for category in ("controllers", "mappers", "frontend"):
                out["catalog"][category] = [x for x in out["catalog"][category] if args.query.lower() in json.dumps(x, ensure_ascii=False).lower()]
    elif args.mode == "history":
        out["commits"] = history(root)
        if args.query:
            out["commits"] = [x for x in out["commits"] if args.query.lower() in json.dumps(x, ensure_ascii=False).lower()]
        out["totalMatches"] = len(out["commits"])
        out["commits"] = out["commits"][args.offset:args.offset + args.limit if args.limit else None]
    else:
        out["sourceGroups"] = dict(collections.Counter("/".join(p.split("/")[:5]) for p in sources))
    print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
