# 🔬 产业链深度钻探系统 v2.0 — Industry Deep Driller

> **投行级行业研究** × **卡脖子反向钻探** × **六大脑自进化**  
> 三模式独立分离 · 图算法量化瓶颈 · 越用越精准

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.0-red.svg)](https://github.com/Jonathonwang001/industry-deep-driller)
[![Python](https://img.shields.io/badge/python-3.8%2B-green.svg)](https://www.python.org/)
[![NetworkX](https://img.shields.io/badge/NetworkX-3.0%2B-orange.svg)](https://networkx.org/)

---

## 🎯 这是什么

**产业链深度钻探系统** 是一个融合了四大技术栈 + 六大脑自进化方法论的产业链分析工具集。

四个技术来源：
- 🧬 [liuhuanyong/ProductKnowledgeGraph](https://github.com/liuhuanyong/ProductKnowledgeGraph) — 产品知识图谱构建
- 🔗 [Aminer-Cloud/KG-Construction](https://github.com/Aminer-Cloud/KG-Construction) — 知识图谱构建工具集
- 📊 [networkx/networkx](https://github.com/networkx/networkx) — 图算法库
- 🤖 [geekan/MetaGPT](https://github.com/geekan/MetaGPT) / [microsoft/autogen](https://github.com/microsoft/autogen) — 多Agent框架

六条方法论驱动自迭代：
- 🧠 **self-improving** — 每次分析后自动记录，每周自检模式准确度
- 🧠 **mem0** — 跨会话记忆用户偏好、数据源状态、分析结论
- 🧠 **openclaw-project-iteration** — 模板库持续扩展（新产业链→新模板）
- 🧠 **ragflow-dataset-ingest** — 产业链图谱自动同步知识库
- 🧠 **universal-agent-skill** — 多Agent工作流精准编排
- 🧠 **LLM wiki** — 所有结构化输出遵循统一规范

---

## 🚦 三大独立模式（v2.0 核心升级）

**v1.0 问题**：引擎绑定——用户说"找卡脖子"也会输出市场规模、投资评级等行研噪声。

**v2.0 解决**：三模式独立分离，按需精准输出。

```
🔴 纯钻探模式           🟡 标准行研模式           🔵 双引擎深度模式
触发："找卡脖子"        触发："分析行业"          触发："分析行业+找卡脖子"
执行：BOM拆解+CR1+图论    执行：6维度完整行研       执行：行研+嵌入钻探
跳过：财务/行研/投资      跳过：钻探/图论            输出：全量
```

### 🔴 纯钻探模式

**触发词**：卡脖子、瓶颈、chokepoint、bottleneck、反向钻探、反向追溯、供应链瓶颈、BOM拆解

**执行四步**：
1. 📋 BOM拆解 → 2. 🔍 节点CR1集中度 → 3. 📊 图论量化 → 4. 🏆 卡脖子排名

**评分公式**（v2.0 去财务权重）：
```
Chokepoint Score = 介数中心性×0.40 + CR1×0.35 + 技术壁垒×0.15 + 稀缺度×0.10
```

| 评分 | 等级 | 含义 |
|------|------|------|
| ≥0.70 | 🔴 T0 绝对瓶颈 | 全球唯一，替代方案>3年 |
| ≥0.55 | 🟠 T1 核心瓶颈 | 寡头垄断 |
| ≥0.35 | 🟡 T2 显著瓶颈 | 龙头明确 |
| ≥0.20 | 🟢 T3 潜在瓶颈 | 有特征 |
| <0.20 | ⚪ 非瓶颈 | 竞争充分 |

**输出**：≤1500字，纯产业链结构 + 瓶颈地图，不含投资建议

### 🟡 标准行研模式

**触发词**：产业链、行业分析、赛道分析、行研、行业研究、行业报告、市场格局、竞争格局（不含卡脖子关键词）

**执行六维度**：
① 行业概览 → ② 产业链拆解 → ③ 竞争格局（含Porter五力）→ ④ 驱动因素（含PEST分析）→ ⑤ 风险评估（含风险矩阵）→ ⑥ 投资建议（含标的推荐+估值参考）

### 🔵 双引擎深度模式

**触发词**：行研关键词 + 卡脖子关键词同时出现

5个维度行研 + 在维度二"产业链拆解"中嵌入纯钻探四步法。

---

## 🧬 六大脑深度嵌入方式

这六条方法**不是贴在表面**，而是像器官一样长在技能内部：

| 🧠 大脑 | 嵌入位置 | 触发时机 | 效果 |
|---------|----------|----------|------|
| **self-improving** | 决策流结束点 | 每次分析后 + 每周自检 | 误判率>10%→自动升级关键词规则 |
| **mem0** | 三个记忆锚点 | (1)用户偏好 (2)数据源变化 (3)分析结论 | 跨会话记忆，越用越懂你 |
| **openclaw-project-iteration** | 模板评估器 | 每次完成产业链分析后 | 满足条件自动扩展模板库 |
| **ragflow-dataset-ingest** | 图谱导出钩子 | 图谱构建完成时 | 产业链数据自动同步知识库 |
| **universal-agent-skill** | Agent编排器 | 模式判断完成后 | lightweight/完整模式自动切换 |
| **LLM wiki** | 输出格式化器 | 报告生成结束时 | 统一结构、统一来源标注、统一传播力分级 |

### self-improving 详细触发

```python
# 伪代码（已内置到 SKILL.md 决策流）
每次分析后:
  memory/YYYY-MM-DD.md.append(分析摘要, 模式, 满意度)

每周一:
  last_7_days_misjudgment_rate = 统计误判次数 / 总分析次数
  if last_7_days_misjudgment_rate > 0.10:
      触发关键词匹配规则升级
      记录到 LEARNINGS.md
```

### mem0 三大记忆锚点

```
锚点1: 用户偏好
  "主人明确偏好：卡脖子=纯钻探（非行研），不需要财务数据"
  
锚点2: 数据源状态
  "2026-05-30: 英为财情超时、FRED API不可用、腾讯qt.gtimg.cn正常"
  
锚点3: 分析结论回测
  "2026-05-30: AI GPU纯钻探→EUV光刻胶T1瓶颈→3个月后验证准确度"
```

---

## 🔧 核心脚本

| 脚本 | 功能 | 命令 |
|------|------|------|
| `build_dependency_graph.py` | 构建产业链图谱 | `--template ai_gpu` |
| `find_chokepoints.py` | 卡脖子评分引擎 | `--graph chain.json --top 10` |
| `reverse_drill_agent.py` | 多Agent钻探工作流 | `--lightweight` 切换纯钻探模式 |

```bash
# 🔴 纯钻探 — 找AI GPU产业链卡脖子（跳过财务）
python3 scripts/reverse_drill_agent.py --template ai_gpu --lightweight

# 🔵 完整双引擎 — 含财务验证
python3 scripts/reverse_drill_agent.py --template ai_gpu

# 自定义产业链
python3 scripts/build_dependency_graph.py --template ai_gpu --output my_chain.json
python3 scripts/find_chokepoints.py --graph my_chain.json --top 15
```

---

## 📊 预设行业模板

| 模板 | 名称 | 钻探路径 | 节点数 | 边数 |
|------|------|----------|--------|------|
| `ai_gpu` | AI GPU产业链 | H100 → EUV光刻 → 光刻胶 | 25 | 21 |
| `humanoid_robot` | 人形机器人 | 整机 → 减速器 → 轴承 | 22 | 18 |
| `evtol` | 低空经济 | eVTOL → 固态电池 → 锂金属负极 | 20 | 16 |

---

## 📁 文件结构

```
industry-deep-driller/
├── SKILL.md                        ← 核心指令（1.4万字，含决策树+模式入口）
├── README.md                       ← 中英双语 README
├── README_ZH.md                    ← 本文件（纯中文）
├── ABOUT.md                        ← GitHub 项目描述
├── LICENSE                         ← MIT 开源协议
├── scripts/
│   ├── build_dependency_graph.py   ← 图谱构建器
│   ├── find_chokepoints.py         ← 卡脖子评分
│   └── reverse_drill_agent.py      ← 四Agent工作流
└── references/
    ├── research-framework.md       ← 6维度行研执行指南
    ├── output-examples.md          ← 行研报告输出示例
    ├── methodology.md              ← 卡脖子方法论
    ├── networkx_patterns.md        ← 图算法参考
    ├── agent_workflow.md           ← Agent编排
    └── report_template.md          ← 纯钻探报告模板
```

---

## 🚀 快速开始

```bash
# 克隆
git clone https://github.com/Jonathonwang001/industry-deep-driller.git
cd industry-deep-driller

# 安装依赖
pip install networkx

# 🔴 纯钻探 — 找AI GPU卡脖子（财务验证自动跳过）
python3 scripts/reverse_drill_agent.py --template ai_gpu --lightweight
```

---

## 📐 版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-05-30 | 初始版本：双引擎架构 + 四Agent工作流 + 3套行业模板 |
| **v2.0** | **2026-05-30** | 🔴 三模式独立分离 + 🧬 六大脑深度嵌入 + 纯钻探评分去毛利率权重 |

---

## 📄 许可

MIT License — 见 [LICENSE](LICENSE)

---

**Made with 🖤 by 沐沐 & 乔纳森大人 | v2.0 — 三模式独立 · 六大脑进化**