> 历史样本记录：本文件不再作为默认模板或验收规则。当前流程见 framework.md 与 self_check.md。

# 人像生成 · 提示词优化沉淀

> 从几十张已出图里沉淀「哪些好 / 哪些差 / 好在哪 / 差在哪」，抽成可复用规则。

> 年龄适用说明：本页记录的是原有 18–22 岁甜妹风格样本，不是全年龄人像的准入限制，也不是所有模型或日常实拍的质量标准。日常实拍遵循 realism.md，不因肤色、眼型或年龄偏离样本而判定失败。其他年龄按用户要求创作；未成年人使用适龄、非色情的日常人像描述。

## 一、一句话结论

- **好图公式**：`圆润/鹅蛋脸 + 大而亮的双眼皮 + 白瓷皮 + 空气刘海 + 黑色长直发 + 柔和针织衫 + 温柔露齿笑 + 干净纯色背景 + 自然手势`
- **差图雷区**：`窄长脸/单眼皮/高颧骨`、`狐狸眼/挑眉`、`偏黄偏黑皮/雀斑`、`酒红/亚麻杂色发`、`张嘴狂笑/冷笑`、`深色紧身裙`、`模糊扭曲的手`

**核心结论：模型只擅长一类脸——"白净、圆润、大眼、年轻、甜"的清纯型。凡是往高级脸/特征脸/成熟脸/异色发肤偏的，几乎都翻车。**

## 二、正样本（好图）要点

圆润带婴儿肥的脸 · 大而亮双眼皮 · 白瓷肌 · 黑长直发 + 空气刘海 · 温柔露齿笑 ·
一手撩发一手放腿 · 米白宽松针织 · 暖米色纯色墙 · 五感高度统一无塑料感。

## 三、负样本雷词（来自真实翻车图）

| 图 | 雷词 |
|----|------|
| 窄长脸·单眼皮·28岁 | `LONG NARROW face`、`HIGH prominent cheekbones`、`MONOLID`、`slight smirk`、`head tilted`、`ash-brown`、`charcoal` |
| 暖蜜糖皮·24岁 | `honey-tan skin`、`FULL lips`、`wider face`、`bright infectious laugh`、`burgundy tint`、`gesturing mid-laugh`（手糊） |
| 狐狸眼·26岁 | `SLENDER OVAL`、`UPTURNED FOX eyes`、`high arched brows`、`sleek shoulder-length`（显老） |

## 四、提炼规则

### ✅ Do（好看来源，必须保留）
| 维度 | 规则 |
|------|------|
| 脸型 | 圆脸 / 柔和鹅蛋，饱满带婴儿肥 |
| 眼睛 | 大而亮双眼皮，眼神清亮 |
| 皮肤 | 白瓷肌 / 白皙通透，无雀斑瑕疵 |
| 年龄 | 按用户要求；18–22 岁仅为原样本风格 |
| 发型 | 黑/深棕长直发；空气刘海（强推） |
| 表情 | 温柔露齿笑 / 浅笑，自然亲和 |
| 服装 | 米白/米色/浅灰浅色针织，宽松柔和 |
| 背景 | 暖米/米白纯色墙，干净无杂物 |
| 手部 | 撩发 / 手放胸前 / 扶领（清晰不变形） |
| 妆容 | 伪素颜（零可见妆、原生裸感肌） |

### ❌ Don't（翻车原因，必须避免）
| 雷区 | 说明 |
|------|------|
| `LONG NARROW face` / 高颧骨 / 尖下颌 | 显老、凹陷、冷硬 |
| `MONOLID` 单眼皮 / 小眼 | 失去大眼美感 |
| `FOX eyes` 狐狸眼 / `arched brows` 挑眉 | 渲染不出高级感，反怪异 |
| `WARM` / `honey-tan` / 黄黑皮 | 偏离白净主线 |
| `freckles` 雀斑 | 减分（除非明确要） |
| 酒红/亚麻/灰棕 发色 | 杂色显没气色 |
| `infectious laugh` 狂笑 / `smirk` 冷笑 | 不优雅生硬 |
| `fitted dark dress` 深色紧身裙 | 漂移冷硬 |
| `motion` / `gesturing mid-laugh` 动态手势 | 手易糊易变形 |

## 五、黄金模板（可直接复用）

```
Half-body waist-up portrait of a beautiful [18-22]-year-old East Asian woman with
a SOFT ROUND face and full cheeks, LARGE bright double-eyelid eyes, FAIR porcelain
skin, gentle sweet smile showing teeth, long straight black hair with airy bangs,
wearing a [cream / beige / light-grey] knit sweater, one hand gently tucking hair
behind her ear, clean plain warm-beige wall background, warm soft light, soft grain,
shallow depth of field
```

**温和差异化变量（只在好看家族内部做区分，保证张张不同又不翻车）：**
- 脸型：`round` / `soft oval` / `slightly heart-shaped（保持柔和）`
- 发型：`airy bangs` / `soft side part` / `high ponytail with face-framing strands`
- 表情：`gentle smile showing teeth` / `soft closed smile` / `slight grin`
- 服装：`cream knit` / `beige cardigan` / `light-grey knit`
- 手部：`tucking hair` / `hand near collar` / `hand resting on chest`
- 年龄：全年龄；`18` / `20` / `22` 仅为原样本示例

## 六、重要提醒：差异化 ≠ 特征化

- 之前为"脸不重复"用了窄长脸/单眼皮/狐狸眼/异色肤发等**强特征**拉差异 → "够不同，但不好看"。
- **正确做法**：在"白净大眼甜妹"好看家族内部做**温和差异化**（脸型圆润度、发型、表情、年龄、服装微调）。
- 代价：她们是"同一类型下的不同漂亮女孩"，而非差异极大的人种脸。**优先保证好看，其次才是不同。**
- 若必须"大幅不同的人脸"：唯一可靠手段是**提供不同真人参考图，用图生图把脸钉死**，而非靠文字硬凑。
