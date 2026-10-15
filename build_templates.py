#!/usr/bin/env python3
"""从 templates/*/template.md 解析元素表与两版提示词，注入 assets/template_browser.html。

用法：python3 build_templates.py
生成后在浏览器打开 assets/template_browser.html 即可浏览模板。
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TPL_DIR = ROOT / "templates"
HTML = ROOT / "assets" / "template_browser.html"

ROW_RE = re.compile(r"^\|\s*(E\d+)\s*\|(.+)$")
PROTECTED_RE = re.compile(r"受保护")
# 兼容带编号的标题：「## 中文提示词」和「## 八、中文提示词」
FENCE_RE = re.compile(
    r"##\s*(?:[一二三四五六七八九十]+\s*、)?中文提示词\s*\n(.*?)"
    r"\n##\s*(?:[一二三四五六七八九十]+\s*、)?English prompt\s*\n(.*?)(?=\n##\s|\Z)",
    re.S,
)


def parse(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    fm = re.search(r"^---\n(.*?)\n---\n", text, re.S)
    if not fm:
        return None
    front = fm.group(1)

    body = text[fm.end():]
    m = FENCE_RE.search(body)
    if not m:
        raise SystemExit(f"{path.name}: 找不到「中文提示词 / English prompt」两节")
    zh, en = m.group(1).strip(), m.group(2).strip()

    elements = []
    for line in body.splitlines():
        row = ROW_RE.match(line)
        if not row:
            continue
        cells = [c.strip() for c in row.group(2).split("|")]
        if len(cells) < 4:
            raise SystemExit(f"{path.name}: 元素表列数不足（需 4 列：# / 元素 / 当前值 / 可替换为）→ {line}")
        # 切分后 cells[0] 是元素名（E 编号已由 ROW_RE 捕获），故索引整体左移一位
        elements.append({
            "id": row.group(1),
            "name": cells[0],
            "value": cells[1],
            "alt": cells[2],
            "protected": bool(PROTECTED_RE.search(cells[0])),
        })

    if not elements:
        raise SystemExit(f"{path.name}: 元素表为空")

    slug = re.search(r"^name:\s*(\S+)", front, re.M)
    source = re.search(r"^source:\s*(.+)$", front, re.M)
    identity = re.search(r"^new_identity:\s*(.+)$", front, re.M)

    preview = path.parent / "preview.png"
    return {
        "id": slug.group(1) if slug else path.parent.name,
        "title": path.parent.name,
        "meta": (source.group(1).strip() if source else ""),
        "sourceNote": ("新身份：" + identity.group(1).strip() if identity else ""),
        "preview": f"../templates/{path.parent.name}/preview.png" if preview.exists() else "",
        "elements": elements,
        "zh": zh,
        "en": en,
    }


def main() -> None:
    tpls = []
    for md in sorted(TPL_DIR.glob("*/template.md")):
        t = parse(md)
        if t:
            tpls.append(t)

    if not tpls:
        raise SystemExit("templates/ 下没有找到 template.md")

    # 照片库目录不该有 template.md；有子目录缺 template.md 说明文件被误删或误移，
    # 必须报出来而不是静默跳过——静默跳过会让模板悄悄从库里消失。
    PHOTOS_DIRNAME = "photos"
    for d in sorted(p for p in TPL_DIR.iterdir() if p.is_dir()):
        if d.name == PHOTOS_DIRNAME:
            continue
        if not (d / "template.md").exists():
            print(f"⚠️跳过 {d.name}/：没有 template.md（若确认不再使用，请删掉这个目录）")

    loaded = {p.parent.name for p in TPL_DIR.glob("*/template.md")}
    for extra in TPL_DIR.glob("*.md"):
        if extra.name != "index.md":
            print(f"⚠️ templates/{extra.name} 不在任何模板目录里")

    print(f"已加载模板目录: {', '.join(sorted(loaded))}\n")

    html = HTML.read_text(encoding="utf-8")
    payload = json.dumps(tpls, ensure_ascii=False)
    marker = "const TEMPLATES = window.__TEMPLATES__ || [];"
    if marker in html:
        # lambda 作 replacement：payload 里的 \n 转义不能走 re.sub 的转义解析，
        # 否则 JSON 里的 \n 会被替换成真实换行，导致整个 JSON 失效。
        html = re.sub(re.escape(marker),
                      lambda _m: "const TEMPLATES = " + payload + ";",
                      html)
    else:
        raise SystemExit(f"{HTML.name} 里找不到注入标记：{marker}")

    HTML.write_text(html, encoding="utf-8")
    print(f"已注入 {len(tpls)} 个模板 → {HTML}")
    for t in tpls:
        print(f"  - {t['id']}（{len(t['elements'])} 个元素）")


if __name__ == "__main__":
    main()