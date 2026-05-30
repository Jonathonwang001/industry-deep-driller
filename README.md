# 🔬 产业链深度钻探系统 v2.0 — Industry Deep Driller

> **投行级行业研究 × 卡脖子反向钻探 × 六大脑持续学习**  
> 三模式独立分离 | 图算法量化瓶颈 | self-improving + mem0 + LLM wiki 驱动迭代

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.0-red.svg)](https://github.com/Jonathonwang001/industry-deep-driller/releases)
[![Python](https://img.shields.io/badge/python-3.8%2B-green.svg)](https://www.python.org/)
[![NetworkX](https://img.shields.io/badge/NetworkX-3.0%2B-orange.svg)](https://networkx.org/)

---

## 🎯 这是什么 / What Is This?

**产业链深度钻探系统** 是一个融合了**投行级6维度行研框架** + **图论量化卡脖子识别** + **六大自进化方法论**的完整产业分析工具集。

三个独立引擎，按需精准输出：

```
🔴 纯钻探模式          🟡 标准行研模式          🔵 双引擎深度模式
"找AI GPU的卡脖子"     "分析AI芯片行业"        "分析AI芯片行业，找找卡脖子环节"
→ BOM拆解+集中度+图论   → 完整6维度投行行研     → 行研报告 + 嵌入钻探
→ 不含财务/行研噪声      → 不含钻探             → 全量输出
```

---

## 🚦 三大独立模式 / Three Independent Modes

| 模式 | 触发关键词 | 执行 | 跳过 |
|------|----------|------|------|
| 🔴 **纯钻探** | 卡脖子、瓶颈、chokepoint、反向钻探 | 产业链图谱 → BOM拆解 → 节点CR1 → 图论量化 | 市场规模、竞争格局、投资评级、财务验证 |
| 🟡 **标准行研** | 产业链、行业分析、赛道（无瓶颈词） | 6维度完整行业研究 | BOM拆解、图论量化、卡脖子评分 |
| 🔵 **双引擎** | 行研关键词 + 瓶颈关键词 | 6维度行研 → 嵌入卡脖子钻探 | — |

> ⚠️ **模式互斥**：每个模式独立运行，模式判断在第一步完成，然后坚定不移执行到底。

<details>
<summary>📖 详细内容 / Expand for details</summary>

### 🔴 纯钻探模式 (Chokepoint Pure Drilling)

**评分公式**（去财务权重）:
```
Chokepoint Score = Betweenness×0.40 + CR1×0.35 + Barrier×0.15 + Scarcity×0.10
```

- T0（≥0.70）: 绝对瓶颈 — 全球唯一，替代方案>3年
- T1（≥0.55）: 核心瓶颈 — 寡头垄断，替换成本极高
- T2（≥0.35）: 显著瓶颈 — 龙头明确
- T3（≥0.20）: 潜在瓶颈 — 有特征但验证不足
- ⚪（<0.20）: 非瓶颈

**输出**：≤1500字，纯产业链结构 + 瓶颈定位，不含投资建议

### 🟡 标准行研模式 (Standard 6-Dim Research)

**六维度**：① 行业概览 → ② 产业链拆解 → ③ 竞争格局 → ④ 驱动因素 → ⑤ 风险评估 → ⑥ 投资建议

输出包含：Porter五力分析、PEST分析、风险矩阵、标的推荐、估值参考

### 🔵 双引擎深度模式 (Dual Engine Deep Dive)

5个维度行研 + 在维度二"产业链拆解"中嵌入纯钻探四步法

</details>

---

## 🧬 六大脑持续学习 / Six Self-Evolving Brains

这个 skill **不是静态的**。六条方法论深度嵌入决策流，让它会自我迭代：

| 🧠 大脑 | 嵌入方式 | 效果 |
|---------|----------|------|
| **self-improving** | 每次分析后自动记录关键发现；每周检查模式判断准确度，误判率>10% → 触发升级 | 越用越准 |
| **mem0** | 三个记忆锚点：(1)用户偏好(2)数据源可用性(3)分析结论→3个月后回测验证 | 跨会话记忆 |
| **openclaw-project-iteration** | 每完成一个产业链分析 → 评估是否值得加入预设模板库 | 模板库持续扩展 |
| **ragflow-dataset-ingest** | 产业链图谱 + 卡脖子发现 → 自动同步到RAGFlow数据集 | 知识图谱积累 |
| **universal-agent-skill** | 多Agent工作流纯钻探/完整模式自动切换；Agent C（财务）在lightweight模式下自动休眠 | 精准模式匹配 |
| **LLM wiki** | 所有结构化知识输出遵循 `docs/wiki/SCHEMA.md` 规范 | 一致性输出 |

<details>
<summary>📖 六大脑详细说明 / Expand for details</summary>

### 🧠 self-improving — 自迭代

```
时间触发器:
  - 每次分析后 → 记录到 memory/YYYY-MM-DD.md
  - 每周一 → 检查模式判断准确度
  - 误判率>10% → 升级关键词匹配规则
  - 发现错误 → 立即写入 LEARNINGS.md
```

### 🧠 mem0 — 记忆增强

```
记忆锚点:
  - 用户偏好记忆: 主人偏好卡脖子=纯钻探（非行研）
  - 数据源记忆: 哪些API当前可用/不可用
  - 结论记忆: 关键卡脖子判断→3个月后回测验证
```

### 🧠 openclaw-project-iteration — 模板扩展

```
模板扩展标准:
  1. 产业链有≥5个可识别的瓶颈节点
  2. 有完整的BOM拆解数据
  3. 有至少3个供应商的CR1数据
  满足以上 → 加入预设模板库
```

### 🧠 ragflow-dataset-ingest — 知识库同步

```
自动同步内容:
  - 产业链图谱（节点+边）
  - 卡脖子评级结果
  - 供应商集中度数据
  - 关键发现摘要
```

### 🧠 universal-agent-skill — 多Agent编排

```
Agent编排决策:
  - lightweight=True → A(拆解) → B(集中度) → D(图论) | C休眠
  - lightweight=False → A → B → C(财务) → D(综合)
```

### 🧠 LLM wiki — 结构化知识规范

```
输出规范:
  - 所有报告遵循统一格式模板
  - 数据来源标注规范: [来源: 机构名, YYYY-MM]
  - 事实/推断/猜测三级区分
  - 结构化表格占比≥60%
```

</details>

---

## 🔧 核心脚本 / Core Scripts

| 脚本 | 功能 | 用法 |
|------|------|------|
| `build_dependency_graph.py` | 构建产业链图谱 | `--template ai_gpu/humanoid_robot/evtol` |
| `find_chokepoints.py` | 卡脖子评分引擎 | `--graph chain.json --top 10` |
| `reverse_drill_agent.py` | 多Agent钻探工作流 | `--template ai_gpu --lightweight` |

```bash
# 🔴 纯钻探（财务验证自动跳过）
python3 scripts/reverse_drill_agent.py --template ai_gpu --lightweight

# 🔵 完整双引擎
python3 scripts/reverse_drill_agent.py --template ai_gpu

# 构建自己的产业链图谱
python3 scripts/build_dependency_graph.py --template ai_gpu --output my_chain.json
python3 scripts/find_chokepoints.py --graph my_chain.json --top 15
```

---

## 📐 纯钻探评分公式 / Pure Drilling Scoring

```
v1.0 (旧): BC×0.30 + CR1×0.25 + Margin×0.20 + Barrier×0.15 + Scarcity×0.10
v2.0 (新): BC×0.40 + CR1×0.35 + Barrier×0.15 + Scarcity×0.10
            ↑ 介数↑    ↑ 集中度↑    ✂️去毛利 ✂️
```

纯钻探的哲学：**不论赚多少钱，只论不可替代性。**

---

## 📊 预设行业模板 / Pre-built Templates

| 模板 | 名称 | 钻探路径 |
|------|------|----------|
| `ai_gpu` | AI GPU产业链 | H100 → EUV光刻 → 光刻胶 → 光敏树脂 |
| `humanoid_robot` | 人形机器人 | 整机 → 减速器 → 轴承 |
| `evtol` | 低空经济 | eVTOL → 固态电池 → 锂金属负极 |

---

## 📁 文件结构 / File Structure

```
industry-deep-driller/
├── SKILL.md              ← 核心指令（模式入口+决策树）
├── README.md             ← 本文件（中英双语）
├── README_ZH.md          ← 中文完整版
├── ABOUT.md              ← GitHub 项目描述
├── LICENSE               ← MIT 开源协议
├── scripts/
│   ├── build_dependency_graph.py    ← 产业链图谱构建器
│   ├── find_chokepoints.py          ← 卡脖子评分引擎
│   └── reverse_drill_agent.py       ← 多Agent工作流
└── references/
    ├── research-framework.md         ← 6维度行研执行指南
    ├── output-examples.md            ← 行研报告输出示例
    ├── methodology.md                ← 卡脖子方法论
    ├── networkx_patterns.md          ← 图算法参考
    ├── agent_workflow.md             ← Agent编排配置
    └── report_template.md            ← 纯钻探报告模板
```

---

## 🚀 快速开始 / Quick Start

```bash
# 克隆
git clone https://github.com/Jonathonwang001/industry-deep-driller.git
cd industry-deep-driller

# 安装依赖
pip install networkx

# 🔴 纯钻探 — 找AI GPU产业链卡脖子
python3 scripts/reverse_drill_agent.py --template ai_gpu --lightweight

# 🟡 标准行研 — 这个需要 LLM 配合，用 skill 调用
# 在 OpenClaw 中说："用 industry-deep-driller 分析人形机器人行业"

# 🔵 双引擎 — 行研 + 钻探
# 在 OpenClaw 中说："用 industry-deep-driller 深入分析AI芯片行业，找出卡脖子环节"
```

---

## 🧪 融合的技术栈 / Integrated Tech Stack

| 技术 | 来源仓库 | 应用 |
|------|----------|------|
| 产品知识图谱构建 | [liuhuanyong/ProductKnowledgeGraph](https://github.com/liuhuanyong/ProductKnowledgeGraph) | BOM拆解 + 供应链映射 |
| 知识图谱构建工具集 | [Aminer-Cloud/KG-Construction](https://github.com/Aminer-Cloud/KG-Construction) | 产业链节点关系建模 |
| 图算法库 | [networkx/networkx](https://github.com/networkx/networkx) | 介数中心性 + PageRank + 结构洞分析 |
| 多Agent框架 | [geekan/MetaGPT](https://github.com/geekan/MetaGPT) / [microsoft/autogen](https://github.com/microsoft/autogen) | 四Agent工作流编排 |

---

## 📐 版本历史 / Version History

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-05-30 | 初始版本：双引擎架构（引擎绑定） |
| **v2.0** | **2026-05-30** | 🔴 三模式独立分离 + 六大脑深度嵌入 + 纯钻探评分去除毛利率权重 |

---

## 📄 许可 / License

MIT License — 见 [LICENSE](LICENSE)

---

**Made with 🖤 by 沐沐 & 乔纳森大人 | v2.0 — 三模式独立 | 六大脑自进化**