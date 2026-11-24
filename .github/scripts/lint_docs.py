# SPDX-License-Identifier: Apache-2.0
"""Clean-room documentation, UTF-8/NFC/LF encoding, and YAML hygiene checker for divinari-community."""

import pathlib
import sys
import unicodedata
import yaml

ROOT = pathlib.Path(__file__).resolve().parents[2]
SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", ".venv"}


def main() -> int:
    errors: list[str] = []
    for path in sorted(ROOT.rglob("*")):
        if any(part in SKIP_DIRS for part in path.parts) or path.is_dir():
            continue
        raw = path.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            errors.append(f"{path.relative_to(ROOT)}: contains UTF-8 BOM")
            continue
        if b"\r\n" in raw:
            errors.append(f"{path.relative_to(ROOT)}: contains CRLF line endings")
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{path.relative_to(ROOT)}: invalid UTF-8 ({exc})")
            continue
        if text != unicodedata.normalize("NFC", text):
            errors.append(f"{path.relative_to(ROOT)}: text is not NFC normalized")
        if text and not text.endswith("\n"):
            errors.append(f"{path.relative_to(ROOT)}: missing trailing newline")
        if path.suffix in {".yml", ".yaml"}:
            try:
                yaml.safe_load(text)
            except yaml.YAMLError as exc:
                errors.append(f"{path.relative_to(ROOT)}: invalid YAML ({exc})")

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1
    print("All community docs and YAML templates passed clean-room hygiene checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
