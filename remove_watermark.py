#!/usr/bin/env python3
"""裁掉生成图右下角的「AI生成」水印，用背景渐变重建被覆盖区域。

背景处理：本模型的输出即使写了 `no watermark` 也仍会加水印，三种否定词写法
全部无效（见 references/template-workflow.md）。所以后期处理是唯一可靠手段。

关键点：**不要用单一颜色填**。影棚背景本身有渐变，填纯色会留下一块明显的
方块（实测过）。正确做法是从被覆盖区域的**上边缘和左边缘**取真实像素，
沿两个方向线性插值重建渐变，再做6px 羽化混合消除接缝。

用法：
    python3 remove_watermark.py 输入.png [-o 输出.png]
默认输出到 <输入名>-clean.png。
"""
from __future__ import annotations

import argparse
import pathlib
import sys

try:
    from PIL import Image, ImageDraw
except ImportError:
    sys.exit("需要 Pillow：pip install Pillow")

# 水印位置（占整图比例，实测右下角 26% 宽× 8.5% 高）
REGION_W = 0.26
REGION_H = 0.085
FEATHER = 6  # 上边缘羽化像素


def rebuild(img):
    w, h = img.size
    rw, rh = int(w * REGION_W), int(h * REGION_H)
    x0, y0 = w - rw, h - rh

    # 从未被覆盖的两个边缘取真实背景像素
    top_row = [img.getpixel((x, y0 - 2)) for x in range(x0, w)]
    left_col = [img.getpixel((x0 - 2, y)) for y in range(y0, h)]
    base = img.getpixel((x0 - 2, y0 - 2))

    overlay = Image.new("RGB", (w, h), base)
    od = overlay.load()
    for j, y in enumerate(range(y0, h)):
        ty = j / max(rh - 1, 1)
        # 以左上角基色为起点，沿横向按 top 走向延伸，沿纵向按 left 走向过渡
        ty_col = left_col[min(j, len(left_col) - 1)]
        for i, x in enumerate(range(x0, w)):
            top = top_row[min(i, len(top_row) - 1)]
            fx = i / max(rw - 1, 1)
            r = int(base[0] * (1 - fx) * (1 - ty) + top[0] * fx * (1 - ty) + ty_col[0] * ty)
            g = int(base[1] * (1 - fx) * (1 - ty) + top[1] * fx * (1 - ty) + ty_col[1] * ty)
            b = int(base[2] * (1 - fx) * (1 - ty) + top[2] * fx * (1 - ty) + ty_col[2] * ty)
            od[x, y] = (min(r, 255), min(g, 255), min(b, 255))

    # 上下左右四边都羽化，避免任何硬边
    mask = Image.new("L", (w, h), 0)
    md = ImageDraw.Draw(mask)
    for i in range(rh):
        md.line([(x0, y0 + i), (w, y0 + i)], fill=255 if i >= FEATHER else int(255 * i / FEATHER))
    for i in range(rw):
        md.line([(x0 + i, y0), (x0 + i, h)], fill=255 if i >= FEATHER else int(255 * i / FEATHER))

    img.paste(overlay, (0, 0), mask)
    return img


def main() -> None:
    ap = argparse.ArgumentParser(description="裁掉右下角水印并重建背景渐变")
    ap.add_argument("image", type=pathlib.Path)
    ap.add_argument("-o", "--out", type=pathlib.Path, default=None)
    args = ap.parse_args()

    if not args.image.exists():
        sys.exit(f"文件不存在：{args.image}")

    out = args.out or args.image.with_name(args.image.stem + "-clean.png")
    img = Image.open(args.image).convert("RGB")
    rebuild(img).save(out, "PNG")
    print(f"{args.image.name} → {out.name}（{out.stat().st_size // 1024} KB）")


if __name__ == "__main__":
    main()