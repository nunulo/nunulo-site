from __future__ import annotations

import argparse
import re
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE_ROOT = ROOT / "release-site"
INDEX_PATH = SITE_ROOT / "index.html"
DOWNLOADS_ROOT = SITE_ROOT / "public" / "downloads"


class LocalReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.references.append(value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--require-apk", action="store_true")
    args = parser.parse_args()

    html = INDEX_PATH.read_text(encoding="utf-8")
    checksum_files = list(DOWNLOADS_ROOT.glob("*.sha256"))
    if len(checksum_files) != 1:
        raise SystemExit("release site must contain exactly one SHA-256 manifest")
    checksum_text = checksum_files[0].read_text(encoding="utf-8").strip()
    match = re.fullmatch(r"([0-9a-f]{64})  ([A-Za-z0-9._-]+\.apk)", checksum_text)
    if match is None:
        raise SystemExit("invalid SHA-256 manifest format")
    digest, apk_name = match.groups()
    version = apk_name.removeprefix("nunulo-android-").removesuffix(".apk")

    required_text = [
        "Nunulo",
        version,
        digest,
        "com.lumokato.nunulo",
        f"./public/downloads/{apk_name}",
    ]
    for value in required_text:
        if value not in html:
            raise SystemExit(f"release metadata missing from index.html: {value}")

    reference_parser = LocalReferenceParser()
    reference_parser.feed(html)
    for reference in reference_parser.references:
        if reference.startswith(("#", "http://", "https://", "mailto:")):
            continue
        target = (SITE_ROOT / reference).resolve()
        if target.suffix == ".apk" and not args.require_apk:
            continue
        if not target.is_file():
            raise SystemExit(f"missing local release-site reference: {reference}")

    apk_path = DOWNLOADS_ROOT / apk_name
    if args.require_apk:
        import hashlib

        if not apk_path.is_file():
            raise SystemExit(f"missing release APK: {apk_name}")
        actual = hashlib.sha256(apk_path.read_bytes()).hexdigest()
        if actual != digest:
            raise SystemExit(f"APK SHA-256 mismatch: expected {digest}, got {actual}")

    print(f"release site verified: {version}")


if __name__ == "__main__":
    main()
