from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE_ROOT = ROOT / "release-site"
INDEX_PATH = SITE_ROOT / "index.html"
class LocalReferenceParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.references: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.references.append(value)


def main() -> None:
    html = INDEX_PATH.read_text(encoding="utf-8")
    required_text = [
        "Nunulo",
        "邀请制多人测试",
        "邀请制测试环境已上线",
        "首轮线上多人验收已通过",
        "尚未公开正式发布",
        "下载 0.2.0 测试 APK",
        "SHA-256",
        "/app/",
        "/admin/",
        "https://github.com/Nunulo",
        "com.lumokato.nunulo",
        "0.2.0-test.1",
        "https://github.com/nunulo/nunulo-android/releases/download/v0.2.0-test.1/nunulo-android.apk",
        "https://github.com/nunulo/nunulo-android/releases/download/v0.2.0-test.1/nunulo-android.sha256",
    ]
    for value in required_text:
        if value not in html:
            raise SystemExit(f"current status missing from index.html: {value}")

    forbidden_text = ["0.1.0-personal.2", "暂无受支持 APK", "当前只把本人私人记录", "原位升级", "尚未正式上线"]
    for value in forbidden_text:
        if value in html:
            raise SystemExit(f"obsolete release claim remains in index.html: {value}")

    reference_parser = LocalReferenceParser()
    reference_parser.feed(html)
    for reference in reference_parser.references:
        if reference.startswith(("#", "/", "http://", "https://", "mailto:")):
            continue
        target = (SITE_ROOT / reference).resolve()
        if not target.is_file():
            raise SystemExit(f"missing local release-site reference: {reference}")

    stale_artifacts = [*SITE_ROOT.rglob("*.apk"), *SITE_ROOT.rglob("*.sha256")]
    if stale_artifacts:
        raise SystemExit(f"obsolete release artifacts remain: {', '.join(str(path) for path in stale_artifacts)}")

    print("multi-user trial release site verified")


if __name__ == "__main__":
    main()
