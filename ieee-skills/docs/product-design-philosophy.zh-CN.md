# 产品设计理念（中文）

`ieee-skills` 的目标不是做几个提示词，而是做成一个可以发布到 GitHub 的产品级 academic skill 仓库。

## 核心定位

这个仓库服务 IEEE Transactions/Journals-style 论文写作、润色、审稿模拟、返修回复、投稿包检查和模板学习。它的核心原则是：**写作可以被增强，但事实、实验、引用、声明和合规不能被编造。**

## 为什么这样设计

1. **完整 skill unit**：每个 skill 都是一个完整文件夹，包含 `SKILL.md`、references、checklists、examples。这参考了 `nature-skills` 的安装思路：可复用单元是整个 skill 文件夹，而不是单个 `SKILL.md`。
2. **Core + Adapter 架构**：通用能力放在 core skills；具体期刊风格、审稿风险和结构偏好放在 journal adapters。
3. **官方依据可追溯**：仓库单独维护 `docs/official-source-map.md`，说明设计参考了哪些官方材料、每个材料影响了哪些 skill。
4. **论文模板语料合法化**：只放开放获取/CC BY 或官方模板文档；不把付费论文或版权不明论文塞进仓库。
5. **模板论文只学结构**：模板论文用于学习 section 组织、摘要密度、图表功能、实验呈现和讨论方式，不用于复制句子。
6. **质量门禁**：每个 skill 都有 reviewer-risk matrix、quality gates、refusal behavior 和 official-source verification。

## 与普通 prompt 仓库的区别

普通 prompt 仓库解决“怎么写一句话”；这个仓库解决“怎么把一篇论文按目标出版社/期刊要求组织成可投稿、可返修、可解释、可验证的完整工作流”。
