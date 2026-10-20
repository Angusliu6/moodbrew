# MoodBrew 安装和手机使用 / Installation

## A. 非技术用户：ChatGPT 插件页面（推荐）

1. 点击项目维护者提供的 **MoodBrew · 心情咖啡图谱** 插件链接。
2. 在 ChatGPT 里按页面提供的 **添加/安装/启用** 操作（具体按钮因版本、设备、权限而异）。
3. 发：“今天想喝一杯和我心情同频的咖啡。” 或上传咖啡菜单照片。
4. 喝完后说：“记录刚刚这一杯，并帮我导出 JSON 品鉴档案。” 把它保存在自己的设备，下次上传继续。

目前由维护者创建的插件属于**私人插件**，并不表示任何 GitHub 访客都已获授权安装。公开安装需另行发布或分享。

**公开 README 或 ChatGPT 预填问题链接不是自动安装按钮。** 若没有安装权限，使用 B 方式。

## B. 不安装也能简单体验

[▶ 点击这里开始普通 ChatGPT 对话](https://chatgpt.com/?q=请当我的咖啡风味向导，根据今天心情推荐咖啡)（不是 Skill 安装）。也可直接复制：

> 请当我的咖啡风味向导。先根据我今天的心情与想要的心境推荐咖啡；有菜单、豆袋照片就优先读取真实备选；只陈述有依据的产区和庄园信息；喝完帮我整理酸、甜、苦、质地、余韵、回甘以及心情的品鉴日志；没有保存文件就不要声称历史已经永久储存。

## C. 进阶用户：从源码构建插件

仓库遵循 Agent Plugins 1.0：根目录 `plugin.json` 与 `skills/moodbrew/SKILL.md` 和其 `references/`。将 `plugin.json` 与 `skills/` 放进单一 ZIP；通过具有插件创建权限的 ChatGPT 账户或工作区的插件创建流程上传。

```text
moodbrew/
  plugin.json
  skills/moodbrew/
    SKILL.md
    references/
      mood-mapping.md
      photo-and-origin.md
      tasting-guidance.md
      journal.md
      coffee-journal.schema.json
```

安装不意味着有后台自动保存：请保存每次导出的 JSON，下次重新上传。私人心情、位置及照片不要提交到公开仓库。
