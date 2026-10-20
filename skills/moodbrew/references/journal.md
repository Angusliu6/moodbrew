# Portable journal / coffee history

**Never promise invisible persistence**. The portable `coffee-journal.schema.json` is the source of truth when uploaded. A user message or the current chat can be treated as a *candidate* entry, not an externally saved record. Log entries should come from the user's own actual experience, not generated tasting notes.

## Suggested conversation

- "我喝完了，想记录" → "是哪杯？今天喝完最明显的一个感觉是什么？" If exact drink is in current chat, don't ask again.
- Draft a succinct human-readable log and let user confirm or correct if uncertain.
- Add `entry_id`, ISO date (`YYYY-MM-DD` if only local calendar day is known), optional time when known, bean/roaster/venue if disclosed, brew, taste axes that user rated, mood before, mood sought, personal reaction, novelty, source information confidence; unknowns null/omitted.
- If user asks for an actual backup, create an updated JSON file using tools actually available and provide a download link when a file is created. If tools cannot write a file, print valid JSON in a fenced code block so user can save it manually. For non-technical users, offer a simple "导出我的咖啡档案" request.
- Merge uploads by `entry_id`; preserve original entries and add only new entries, never overwrite divergent records silently. Avoid recording today's purchase as "tasted" unless user says they tasted it. No invented dates or stores.

## Core fields

```
{
  "schema_version": "1.0.0",
  "profile": {"display_name": null, "preferences": {}, "updated_at": null},
  "entries": [
    {
      "entry_id": "local-2026-01-10-a1", "date": "2026-01-10", "status": "tasted",
      "coffee": {"name": "Example washed Guji", "origin_country": "Ethiopia", "region": "Guji", "process": "washed"},
      "brew": {"method": "pour-over"},
      "mood": {"before": "curious", "desired": "bright", "after": null},
      "ratings": {"sweetness": 3, "acidity": 4, "bitterness": 1, "body": 2, "finish": 3, "after_sweetness": null, "aroma": 4, "overall": 4},
      "notes": "Floral / citrus, clean finish", "evidence": "self_report"
    }
  ]
}
```

`ratings` keys have 1–5 scales (null for unknown). `finish` denotes duration; `notes` and `finish_character` denote quality. For unknown farm do not populate it. Dates should not silently assume the user's locale/time zone; if user says "今天" use known local date when available, otherwise ask or leave explicit date unfilled until confirmed. Venue and precise locations are optional; don't collect them unprompted. Photos are *not* stored in this JSON by default.

## History analysis

When asked "我之前喝过什么" and a journal is present, present dated timeline in descending order, **only** real entries; include number, place/bean, mood and standout impression. If no diary available say "目前这段对话里能确定的是...; 其他历史需要你导入咖啡档案". Never conjure old logs from memory.

For taste portrait: count total *tasted* entries, report evidence strength (1–2 tentative, 3–5 emerging, >5 broader sample but still personal), preferences (liked/disliked), flavor axes, comfort zone and novelty. Avoid inferring a stable personality type or medical mood trajectory. When novel recommendations are requested, respect restrictions, use already tried origins as a negative signal only if user wants something different, and explain what is new.

## Privacy and retention

This plugin does not have a database. Diary exports are kept wherever the user saves them. Advise not to commit private diary, identifiable locations, photos, or emotional notes to **public GitHub**. Users own logs and can edit/delete JSON backups. Never say data is encrypted, synchronized, backed up, or permanently saved by this skill unless those operations actually occurred.
