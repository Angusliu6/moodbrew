# ☕ MoodBrew — a coffee mood compass

*A coffee that meets you where you are.* Open-source ChatGPT skill for choosing coffee by mood and flavor, reading photographed coffee menus/bean bags, exploring origins, guided tasting, and building a portable tasting journal.

[中文](README.md) · [Installation / 安装](docs/INSTALL.md) · [Skill source](skills/moodbrew/SKILL.md) · [Journal schema](skills/moodbrew/references/coffee-journal.schema.json)

## What it does

- **Match your mood**: distinguish how you feel now vs how you want to feel; recommend a coffee style and explain its sensory match, without claiming caffeine changes emotions predictably.
- **Read a coffee photo**: identify visible bean names, origin, roast, process and flavor notes from a menu or package. Do not fabricate hidden details or claim an unlabeled cup reveals its farm.
- **Explain origin stories responsibly**: geographic context, processing choices, and possible flavor characteristics; distinguish label statements, verifiable facts, and typical regional tendencies.
- **Guide sensory exploration**: sweetness, acidity, bitterness, mouthfeel, finish, returning sweetness and aroma.
- **Keep a portable journal**: optional JSON export/import of user-confirmed entries; derive a tentative taste portrait from genuine records, not fabricated history.

## Quick start

Install the skills-only plugin from its owner-provided ChatGPT plugin page, then talk naturally and attach a photo. This README does **not** claim a standalone chat link installs any skill. Without installation you can still ask regular ChatGPT to use a similar coffee mood framework, but it is not the packaged workflow.

Example: “I feel contemplative and want a full-bodied black coffee with a long chocolate finish. What should I try?”

## Data truthfulness and privacy

**The skills-only plugin has no persistent database or cloud sync.** Asking it to “remember this coffee” can produce an entry for export; reliable cross-conversation history requires bringing your saved journal back into chat, or an independently available recorded source. Do not put real people’s mood logs, precise locations or images in public GitHub. All bundled journal examples are fictitious.

Optional offline CLI (Python standard library only):

```bash
python3 tools/journal.py init my-coffee.json
python3 tools/journal.py add my-coffee.json entry.json
python3 tools/journal.py list my-coffee.json
python3 tools/journal.py summary my-coffee.json
```

Run checks: `python3 -m unittest discover -s tests -v`.

MIT license. Contributions welcome; please avoid personal data and unlicensed photographs.
