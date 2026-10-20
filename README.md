# ☕ MoodBrew · 心情咖啡图谱

**今天的心情，适合哪一杯？** | *Find a coffee that meets you where you are.*

[English](README_EN.md) · [30 秒上手](docs/INSTALL.md) · [核心 Skill](skills/moodbrew/SKILL.md) · [日志结构](skills/moodbrew/references/coffee-journal.schema.json)

在咖啡店面对一排耶加雪菲、Guji、肯尼亚、哥伦比亚、日晒、水洗、蜜处理、瑰夏，看到风味标签却不知道选哪一杯？MoodBrew 是一个以 **心情 × 咖啡风味 × 品鉴记忆** 为核心的开源 ChatGPT Skill。

> 不只推荐好喝的咖啡，更想推荐**符合今天心情**的咖啡。

## ✨ 可以做什么

| 场景 | 你可以说 | MoodBrew 怎么做 |
| --- | --- | --- |
| 🫶 按心情选 | “今天想沉思，喝有长余韵的美式” | 根据想要的体验给出主推荐和备选 |
| 📷 拍照看懂 | 上传店内菜单、豆袋或咖啡卡 | 读取真实可见选项，比较风味、产区和处理法 |
| 🌍 产区漫游 | “Guji 日晒为什么和肯尼亚水洗不同？” | 讲清地理与工艺，并标注推测、常见趋势和可核实事实 |
| 👅 引导品鉴 | “入口酸，后来甜，这是什么感觉？” | 理解甜、酸、苦、醇厚、余韵、回甘 |
| 📓 记录每杯 | “记录今天这杯，酸度 4，心情不错” | 形成经用户核实的可导出 JSON 品鉴条目 |
| 🧭 味觉人格 | “我之前喝过什么？想试不一样的” | 仅根据**实际有据可查的**记录归纳偏好，寻找陌生风味 |

## 🚀 30 秒开始（非技术用户）

**A. 真正安装 Skill**：使用获得授权的 [MoodBrew ChatGPT 插件页面](https://chatgpt.com/plugins/plugins_6ad6dcb04d0c81918a0a7ef5cadbfb5f)；按页面指引添加或启用。目前该插件由维护者以**私人插件**方式创建，不保证每位仓库访客都能安装，后续公开分享需单独配置。

**B. 不安装先体验**：[▶ 点击这里，在普通 ChatGPT 试试心情选咖啡](https://chatgpt.com/?q=%E8%AF%B7%E5%BD%93%E6%88%91%E7%9A%84%20MoodBrew%20%E5%92%96%E5%95%A1%E9%A3%8E%E5%91%B3%E5%90%91%E5%AF%BC%E3%80%82%E5%85%88%E9%97%AE%E6%88%91%E4%BB%8A%E5%A4%A9%E7%9A%84%E5%BF%83%E6%83%85%E5%92%8C%E6%83%B3%E8%A6%81%E7%9A%84%E7%8A%B6%E6%80%81%EF%BC%8C%E5%86%8D%E7%BB%93%E5%90%88%E7%94%9C%E6%84%9F%E3%80%81%E9%85%B8%E5%BA%A6%E3%80%81%E8%8B%A6%E5%91%B3%E3%80%81%E9%86%87%E5%8E%9A%E5%BA%A6%E3%80%81%E5%9B%9E%E7%94%98%E5%92%8C%E4%BD%99%E9%9F%B5%E7%BB%99%E6%88%91%E6%8E%A8%E8%8D%90%E4%B8%80%E6%9D%AF%E5%92%96%E5%95%A1%EF%BC%9B%E5%A6%82%E6%9C%89%E8%8F%9C%E5%8D%95%E6%88%96%E8%B1%86%E8%A2%8B%E7%85%A7%E7%89%87%EF%BC%8C%E4%BC%98%E5%85%88%E6%AF%94%E8%BE%83%E7%85%A7%E7%89%87%E4%B8%AD%E7%9A%84%E7%9C%9F%E5%AE%9E%E9%80%89%E9%A1%B9%EF%BC%8C%E4%B8%8D%E7%BC%96%E9%80%A0%E5%BA%84%E5%9B%AD%E4%BF%A1%E6%81%AF%E3%80%82)。这是预填问题的普通 ChatGPT 对话，**不是 Skill 安装，也不保证加载本仓库的指令**。

可以直接这样开场：

> 今天很想静下来学习，想要醇厚的口感和悠长余韵，最好不太酸。推荐哪杯？

> 我在咖啡店拍了菜单，请从照片里实际能看清的咖啡豆中推荐一种，同时讲讲它的产区、处理法与可能的风味。

> 刚喝完一杯咖啡，帮我记录下来，慢慢建立我的味觉人格。

更多操作与安装说明：[docs/INSTALL.md](docs/INSTALL.md)。

## 🎨 咖啡情绪风味图谱

| 心境 / 想要的感官体验 | 可探索的风味方向 |
| --- | --- |
| 🌙 沉静思考 | 坚果、黑巧克力，较饱满的口感、柔和酸质、长余韵 |
| ☀️ 清爽明朗 | 柑橘、花香，较明亮的酸质和轻盈口感 |
| 🫶 温柔松弛 | 低苦、自然甜感、顺滑的奶咖，也可考虑低因或脱因 |
| 🔥 坚定出发 | 强烈烘焙香、饱满的触感和清晰的苦甜对比 |
| 🌱 好奇探索 | 花果香、日晒或蜜处理，以及过去没有体验过的产区 |

这些是可供选择的**风味与心境联想**，不是声称咖啡能保证改变情绪、治疗焦虑、提高专注度或提供持续数小时的能量。

## 📷 为什么照片讲解不会“编故事”？

- **照片上能看见的**：可按咖啡袋/菜单标签讲解原产国、区域、庄园（仅在明确标注时）、处理法、烘焙和店家描述的风味。
- **常见风味倾向**：解释海拔、品种、处理法、气候等可能的影响，但不以某个地区的典型描述替代这一袋豆子的真实记录。
- **需要查证的内容**：具体庄园历史、微气候、竞赛奖项或最新店内价格。无法核实就直接说明不确定。
- **一杯没有标注的黑咖啡照片**：不能凭颜色和表面油脂可靠地识别产区、品种或庄园。

## 📓 记录每杯，慢慢形成味觉人格

核心记录字段：日期、咖啡与处理法、当时心情及期望心境、冲煮方式、甜感 / 酸度 / 苦味 / 醇厚度 / 余韵 / 回甘 / 香气的主观评分、喝后感受和证据来源。可以标注 `planned` / `ordered` / `tasted`，不会把“打算买”冒充“喝过”。

**重要限制**：这是 **skills-only** 实现，没有私人云数据库，没有后台自动保存功能。对话里的“记下了”只代表形成待保存的记录；想跨聊天准确查看历史，请保留导出的 JSON 文件，下次再上传或引用真实可用的数据。绝不凭空杜撰已喝过的咖啡。

示例数据（完全虚构）：[examples/example-journal.json](examples/example-journal.json)。

### 进阶用户：用离线工具管理品鉴历史

无需 API Key，无需额外 Python 依赖，日志仅保存在自己的电脑中：

```bash
python3 tools/journal.py init my-coffee.json
python3 tools/journal.py add my-coffee.json entry.json
python3 tools/journal.py list my-coffee.json
python3 tools/journal.py summary my-coffee.json
python3 tools/journal.py export my-coffee.json my-backup.json
```

`entry.json` 为单杯记录对象，格式参见示例日志里的 `entries[0]`。请不要把私人咖啡/心情记录放进公开仓库。

## 🧪 开发与测试

```bash
python3 -m unittest discover -s tests -v
python3 tools/journal.py validate examples/example-journal.json
```

上述命令仅验证离线日志；[15 个人工行为评估用例](evals/scenarios.json) 供日后模型对话测试，**并不代表已跑通自动化模型评测**。

### 项目结构

```text
moodbrew/
├── plugin.json
├── SKILL.md                         # 便于 GitHub 用户直接阅读
├── skills/moodbrew/
│   ├── SKILL.md                     # 插件实际使用的技能说明
│   └── references/                  # 心情、产区、品鉴与记录格式
├── docs/INSTALL.md
├── examples/example-journal.json
├── evals/scenarios.json
├── tools/journal.py
└── tests/test_journal.py
```

## 🛣 Roadmap

- [x] 心情与风味的对话推荐
- [x] 咖啡菜单和豆袋照片的证据优先讲解
- [x] 产区与处理法知识，避免虚构庄园信息
- [x] 可导出的味觉人格 / 品鉴 JSON、离线 CLI
- [x] 数据校验单元测试与人工行为测试清单
- [ ] 选择性授权的私人云端同步（需独立服务器与隐私设计）
- [ ] 图形化风味雷达、跨月味觉趋势、盲测挑战
- [ ] 支持更多语言的产区资料

## License & Contributing

[MIT License](LICENSE)。欢迎提交 Issue、PR 和可验证的产区知识，但不要提交含他人信息、真实情绪记录或未获授权照片的材料。
