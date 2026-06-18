# Skill-Suite Router 架构

版本：`0.5.0`

本仓库采用 **平级独立 skill + suite router + registry** 的架构。

## 为什么不是把所有 skill 塞进一个 skill 里面？

因为每个 journal skill 和 component skill 都应该可以被单独发现、单独安装、单独调用、单独测试。`ieee-skill-suite` 是总控入口，但不是唯一真正的 skill。

## 推荐结构

```text
skills/
├── ieee-skill-suite/          # 总控 router
├── ieee-journal-router/  # 期刊 router
├── ieee-component-router/# 论文组件 router
├── ieee-submission-router/# 投稿流程 router
├── <component-skill>/
└── <journal-adapter>/
```

## 两种安装模式

- **Full Suite Mode**：安装多个平级 skill，适合高级用户。
- **Compact Suite Mode**：安装 `dist/compact-suite/ieee-skill-suite/` 这一个 skill，适合想要一个入口管理全部模块的用户。

## 路由依据

- `resources/skill_registry.json`
- `resources/journal_registry.json`
- `resources/component_registry.json`
- `resources/submission_registry.json`
- `resources/routing_rules.json`
