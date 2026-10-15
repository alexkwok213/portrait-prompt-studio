# 文生图路线 · 句式粒度规范

> 适用于**不附参考照片**、纯靠文字生成的人像。与 `framework.md`（图生图 / 参考照片路线）是两条平行路线，各用各的规范：
> - 图生图 → `framework.md`：先看真实照片，写参考包与改编方案。
> - 文生图 → 本文件：直接写句式粒度提示词。**没有照片可看时，这是唯一入口，不是降级兜底。**

## 一、为什么要按句式写

标签流（逗号罗列形容词）与句式流（每个维度写成完整句子）可以覆盖同样的维度，但只有句式流渲染出的脸稳定。区别在于每句带了「状态」：光不只是"soft"，而是"从画面左侧经窗扩散、在鼻侧留下柔和阴影"；手不只是"hand near collar"，而是"右手搭在椅背上、指节松弛、手腕自然下垂"。

每个维度至少写 **主语 + 特征 + 状态**。

## 二、12 维度骨架

| # | 维度 | 怎么写 |
|---|------|-----------|
| 1 | 影像类型 + 质感 | 由场景决定，不要默认加胶片颗粒（见 realism.md §一） |
| 2 | 景别 | `waist-up half-body portrait`、`head-and-shoulders close-up` |
| 3 | 背景 | 写「排除法」：`completely empty with no environment, no props, no plants, no foreground elements` |
| 4 | 发型 | 长度 + 分缝 + 发束 + 落发位置 + 遮挡 + 光下高光 |
| 5 | 脸型 | 具体轮廓 + 婴儿肥/颧骨/下颌的实际状态 |
| 6 | 眉/眼/眼神 | 眼形 + 眼睑遮挡 + 眼神状态词（见下 §四） |
| 7 | 妆感 | 分层写，或明确写「无可见妆容、只有原生皮肤」 |
| 8 | 鼻/唇 | 鼻梁/鼻尖/鼻翼 + 上唇弧度 + 下唇 + 唇色与质感 |
| 9 | 耳饰/发饰 | 无耳饰时明确写 no earrings；发饰写清位置 |
| 10 | 服装 | 主件 + 领口 + 袖口 + 材质纹理 + 接触处褶皱 |
| 11 | **光位（最关键）** | 方向 + 硬度 + 色温 + 皮肤效果，四要素缺一不可 |
| 12 | 姿态与手部 | 身体朝向 + 支撑物 + 每只手接触什么 + 接触褶皱与阴影 |
| 13 | 表情一致性 | 眼睑、脸颊、鼻翼、嘴唇属于同一个反应 |
| 14 | 机位与景深 | 相机相对眼睛的高度与距离 + 对焦位置 + 清晰度沿距离变化 |

## 三、8 条硬规矩

1. 每个维度写成完整句子，不是逗号分隔的标签。
2. 眼神必须有状态词：直视镜头 / 微微失神 / 带笑意 / 安静聆听。**不必每次直视镜头。**
3. 光位必写 4 要素：方向 + 硬度 + 色温 + 皮肤效果（smooth highlights, natural gradients, no cast shadows）。
4. 背景写「排除法」，不只是「干净」。
5. 发型要有动态细节：落发位置 + 发梢在光下的高光。
6. 妆感分层写；儿童与日常写真直接写「无可见妆容」。
7. 质感层按场景取舍——**不要为了"高级"自动追加胶片颗粒、浅景深、金色轮廓光、奶油肤质**（realism.md §一）。手机日常照就写手机普通模式。
8. 技术词换视觉词：`photorealistic, sharp focus` → `soft grain, shallow depth of field`（仅在该场景确实需要时）。

## 四、句式升级写法

### 脸 / 眼 / 唇

| 部位 | 标签流 | 句式粒度 |
|------|-----------|---------|
| 脸型 | soft and rounded | soft and rounded with full baby-fat cheeks, a small gently rounded chin, smooth full temples |
| 眉 | naturally straight | naturally straight soft eyebrows with a gentle arch and fine natural hairs |
| 眼 | large dark-brown eyes | upper eyelid crease clearly visible, lower eyelid softly defined, lashes fine and separated one by one, ordinary iris proportion |
| 鼻 | short and straight | short and straight with a delicate small rounded tip, softly flared nostrils |
| 唇 | full and softly parted | upper lip gently curved, tinted healthy natural rose with a light moist gloss catching the light |
| 皮肤 | fair porcelain | even fair skin with faint natural color variation across the cheeks and nose, no visible pores added |

### 服装

- 标签流：`cream oversized knit sweater`
- 句式粒度：`cream oversized knit sweater with soft ribbed texture and relaxed drop-shoulder fit that drapes over her shoulders, knit fibers clearly visible and slightly fuzzy at the cuffs`

### 姿态与手部

- 标签流：`hand raised to tuck a strand behind her ear`
- 句式粒度：动作三要素 = **身体朝向 + 头部倾斜 + 每只手的位置与手指状态**，并加 `both hands visible in frame with natural relaxed spacing and no distortion`。这句显著降低手部崩坏。

## 五、表情写成一个正在发生的瞬间

不要固定成「整齐牙齿 + 弯曲嘴角」。写清这个表情因何而起：

```
刚听到摄影师说了一句玩笑，笑容正在出现——眼睑随之微微收窄，
脸颊自然提起，嘴角两侧略微不对称，嘴唇分开露出小而整齐的牙齿。
```

眼睑、脸颊、鼻翼、嘴唇的变化必须属于**同一个**反应。也可以捕捉交流中安静聆听的瞬间（嘴部放松、目光不在镜头上），微笑不是必选项。

## 六、脸部模板化的修正顺序

连续生成都出现同样的圆脸、亮眼、均匀肤色和标准微笑时，**不要追加「真实、不磨皮」这类泛化否定词**。按顺序处理：

1. **先减**：去掉「甜美、大眼、精致、完美」这类理想化组合。
2. **再挑少量普通特征**：眼睑形状、正常虹膜比例、鼻基底、唇形、自然表情、轻微自然不对称。
3. **不要用加瑕疵代替真实感**：夸张毛孔、雀斑、丑化都不是解法。
4. **改一处最相关的约束**后重试（脸 → 光 → 姿态 → 景深，按需选一），不要一次全改。

需要**完全不同的人脸**时，文字不可靠——改用图生图 + 有权使用的真实参考照片（`framework.md` 路线）。

## 七、中文叙事模式

用户要求中文提示词时，全文中文，300–600 字。同样的维度覆盖要求，但中文字数与英文词数不可混算——按需计数后再交付。

## 八、填充分块骨架（文生图）

```
[景别] portrait photograph, [由场景决定的成像特征].
The subject is a [年龄] [身份], [镜头与构图],
[支撑关系或姿态起点], against [背景],
completely empty with no environment, no props, no plants and no foreground elements.
[发型：分缝、长度、发束、落发位置、遮挡].
Her face shape is [具体轮廓]. [眉]. [眼形 + 眼睑遮挡 + 眼神状态].
[鼻]. [唇]. [耳饰或明确写无]. [服装：主件、材质、接触处褶皱].
[表情：因何而起，眼睑/脸颊/鼻翼/嘴唇的同向变化].
[姿态与手部：身体朝向、支撑物、每只手接触什么、褶皱与接触阴影].
[光位：来源 + 方向 + 硬度/扩散 + 色温 + 皮肤效果 + 具体阴影位置].
[机位与景深：相对眼睛的高度与距离、对焦位置、清晰度沿距离变化].
No text, logos or watermark.
```

## 九、禁止事项

- 不写 `masterpiece / best quality` 等质量标签串，不用 `(x:1.2)` 权重语法，不用逗号堆砌的 tag soup。
- 中英文保持同一场景——不要中文写居家、英文末尾却追加无环境影棚。
- 不用抽象口号代替具体内容（`高级感`、`自然真实`、`人物背景融合`）。
- 不把每个人固定成「正面、直视、交叠双手、浅景深」的同一姿态；也不把五官、笑容、机位、姿势、景深每次复制成同一组合。