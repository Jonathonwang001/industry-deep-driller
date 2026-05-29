# 🔬 产业链深度钻探系统 — Industry Deep Driller

> **投行级行业研究** × **卡脖子反向钻探**  
> 一个融合了6维度行研框架和图算法量化瓶颈识别的完整方法论与工具集。

---

## 🎯 这是什么？

**产业链深度钻探系统** 将两个顶级方法论融合为一个完整的行业研究系统：

1. **🏦 投行6维度行研框架**（广度层）  
   覆盖：行业概览 → 产业链分析 → 竞争格局 → 驱动因素 → 风险评估 → 投资建议

2. **🔬 卡脖子反向深度钻探**（深度层）  
   四步法找到产业链的"命门"——全球只有一两家能做、替代成本极高、拥有绝对定价权的底层环节。

```
第一层（广度）：6维度行研 → 看清全貌
                              ↓
第二层（深度）：四步钻探 → 找到命门
```

---

## 🔧 核心方法论

### 引擎一：投行6维度行业研究

完整的行业分析框架：

| 维度 | 焦点 | 输出 |
|------|------|------|
| ① 行业定义与概览 | 市场规模、CAGR、生命周期 | 一句话行业本质 |
| ② 产业链深度拆解 | 上中下游、价值链分布 | 谁最赚钱、为什么 |
| ③ 竞争格局分析 | CR3/CR5/HHI、Porter五力 | 市场集中度地图 |
| ④ 驱动因素与趋势 | 需求/供给/政策/技术 | 最影响行业走向的1-2个变量 |
| ⑤ 风险评估 | 行业/政策/竞争/宏观 | 风险矩阵（概率×影响） |
| ⑥ 投资建议 | 评级、标的、催化剂 | 可操作的投资建议 |

📖 **详细执行指南**: `references/research-framework.md`  
📝 **输出示例**: `references/output-examples.md`

---

### 引擎二：卡脖子反向深度钻探

一个四步"钻探"流程，找到行业的瓶颈环节：

```
[顶层超级需求] → [核心硬件/载体] → [关键制程/设备] → [独家垄断材料/软肋]
  (AI大模型)         (GPU/加速卡)         (先进封装/光刻)       (特种化学品/掩膜版)
```

#### 第一步：BOM拆解（Agent A）
- 拆解报告 → 识别核心组件
- 过滤标准化零件（无投资价值）
- 聚焦**非标准化、高壁垒**环节

#### 第二步：市场集中度审计（Agent B）
- 查询全球CR1/CR3
- 标红垄断级：CR1 > 70% → 🔴；CR3 > 60% → 🟠
- 识别地域集中风险

#### 第三步：财务与定价权验证（Agent C）
真正的卡脖子环节必须同时满足：
- 毛利率 ≥ 50% → 极强定价权
- 扩产周期 ≥ 12个月 → 供给侧刚性
- 研发费用率 ≥ 15% → 持续技术壁垒
- 专利壁垒 ✅

#### 第四步：图论量化认证（Agent D）
使用 **NetworkX** 图算法：
- **介数中心性（Betweenness Centrality）** — 所有路径必经的节点 = 咽喉要道
- **结构洞（Structural Holes）** — 节点对上下游的控制力
- **PageRank** — 被重要节点依赖的权重

**卡脖子综合评分** = 介数×0.30 + CR1×0.25 + 毛利率×0.20 + 壁垒×0.15 + 稀缺度×0.10

| 评分 | 等级 | 投资含义 |
|------|------|----------|
| ≥ 0.70 | 🔴 一级·绝对垄断 | 必须研究，寻找替代方案 |
| ≥ 0.50 | 🟠 二级·寡头垄断 | 核心关注 |
| ≥ 0.30 | 🟡 三级·高集中度 | 值得跟踪 |
| ≥ 0.15 | 🟢 四级·有特征 | 关注 |
| < 0.15 | ⚪ 常规竞争 | 不追踪 |

📖 **详细方法论**: `references/methodology.md`  
📊 **图算法参考**: `references/networkx_patterns.md`

---

## 🚀 快速开始

### 依赖

```bash
pip install networkx  # 图算法依赖
```

### 使用内置行业模板

```bash
# 构建AI GPU产业链图谱
python3 scripts/build_dependency_graph.py --template ai_gpu --output ai_gpu_chain.json

# 检测卡脖子环节
python3 scripts/find_chokepoints.py --graph ai_gpu_chain.json --top 10 --output report.md

# 运行完整四Agent工作流演示
python3 scripts/reverse_drill_agent.py
```

### 可用模板

| 模板 | 行业 | 核心卡脖子路径 |
|----------|----------|----------------------|
| `ai_gpu` | AI GPU产业链 | H100 → EUV光刻 → 光刻胶 → 光敏树脂 |
| `humanoid_robot` | 人形机器人产业链 | 整机 → 减速器 → 轴承 → 精密加工 |
| `evtol` | 低空经济产业链 | eVTOL → 固态电池 → 锂金属负极 |

---

## 📂 文件结构

```
industry-deep-driller/
├── README.md                          ← 英文说明文档
├── README_ZH.md                      ← 中文说明文档（本文件）
├── ABOUT.md                          ← GitHub About（显示在仓库主页）
├── SKILL.md                          ← Skill指令文件（OpenClaw/ClawHub用）
├── LICENSE                           ← MIT许可证
├── scripts/
│   ├── build_dependency_graph.py     ← 图谱构建器 + 3套行业模板
│   ├── find_chokepoints.py          ← 卡脖子评分引擎
│   └── reverse_drill_agent.py       ← 四Agent协作工作流
└── references/
    ├── research-framework.md         ← 6维度行研详细执行指南
    ├── output-examples.md            ← 行研报告输出示例
    ├── methodology.md                ← 卡脖子四步钻探方法论
    ├── networkx_patterns.md         ← NetworkX图算法代码参考
    ├── agent_workflow.md            ← 四Agent角色配置与编排
    └── report_template.md           ← 卡脖子分析报告模板
```

---

## 🔬 四Agent工作流

分析一个具体产品或行业时，四个"Agent"协作：

```
Agent A (BOM拆解员)
   ↓ 识别核心组件
Agent B (市场集中度审计员)
   ↓ 计算CR1/CR3，标记垄断
Agent C (财务定价权评估员)
   ↓ 验证毛利率、扩产周期、专利壁垒
Agent D (卡脖子综合评级员)
   ↓ 构建图谱，计算介数中心性，给出最终评级
```

每个Agent的输出作为输入传递给下一个Agent——确保**不遗漏任何卡脖子环节**。

📖 **Agent配置详情**: `references/agent_workflow.md`

---

## 📊 示例：AI GPU产业链分析

对NVIDIA H100 GPU运行完整工作流后：

```
==========================================
🔬 产业链反向深度钻探报告
==========================================

Top 卡脖子环节:
  1. EUV光刻制程             评分: 0.6552 🟠 二级
  2. CoWoS先进封装           评分: 0.6489 🟠 二级
  3. GPU核心芯片 (5nm)       评分: 0.6192 🟠 二级
  4. 低损耗树脂               评分: 0.4696 🟡 三级
  5. HBM3e高带宽内存          评分: 0.4688 🟡 三级
  ...
```

**关键洞察**: 
- **ASML (EUV光刻)** 拥有**100%全球市场份额** — 真正的绝对卡脖子环节
- **台积电 (CoWoS封装)** 拥有**95%市场份额** — 另一个卡脖子环节
- **GPU芯片** CR1达85% — 英伟达近乎垄断

---

## 🎯 适用场景

本系统/方法论适用于：

1. **产业链深度研究**（找到真正的瓶颈）
2. **供应链瓶颈识别**（卡脖子 / bottleneck分析）
3. **BOM（物料清单）反向追溯**
4. **垄断度量化**（图算法）
5. **投行级行业深度报告**
6. **识别"卖铲人"机会**（Pick-and-Shovel策略）

**触发词**（用于AI Agent集成）：
- 中文: 产业链、卡脖子、反向钻探、chokepoint、bottleneck、供应链分析、垄断分析、产业链图谱、BOM拆解、行业瓶颈、产业深度
- 英文: `industry chain`, `chokepoint`, `bottleneck`, `reverse drilling`, `supply chain analysis`, `monopoly analysis`, `BOM teardown`

---

## 🔗 与AI Agent集成（OpenClaw）

本 Skill 设计用于安装在 **OpenClaw**（AI Agent框架）中：

```bash
# 通过ClawHub安装
clawhub install industry-deep-driller

# 或手动复制到 ~/.qclaw/skills/
cp -r industry-deep-driller ~/.qclaw/skills/
```

安装后，当用户请求匹配上述触发词时，AI Agent会**自动触发**本Skill。

---

## 📚 方法论来源

本系统融合了以下方法论：

- **投行行研框架**（Goldman Sachs, Morgan Stanley, UBS）— 6维度框架
- **图论/网络科学**（Betweenness Centrality, Structural Holes）
- **卖铲人策略**（Tiger Global, Coatue, Hillhouse）— 找到"淘金热中卖铲子的人"
- **瓶颈理论** — 木桶最短的那块木板
- **LLM Wiki方法论** — 结构化知识管理
- **Universal Agent Skill** — 通用Agent工作流模式

---

## 🧪 测试验证

- ✅ AI GPU产业链（25节点，21条边）— 成功识别EUV光刻、CoWoS封装为二级卡脖子
- ✅ 人形机器人产业链 — 识别减速器、空心杯电机为关键瓶颈
- ✅ 低空经济产业链（eVTOL）— 识别固态电池、碳纤维复合材料为瓶颈
- ✅ 四Agent工作流端到端成功运行

---

## 📖 文档

所有参考文档均在 `references/` 目录：

| 文件 | 内容 |
|------|---------|
| `research-framework.md` | 6维度行业研究执行指南（详细） |
| `output-examples.md` | 行研报告输出示例（格式参考） |
| `methodology.md` | 卡脖子四步钻探方法论（详细） |
| `networkx_patterns.md` | NetworkX图算法代码示例 |
| `agent_workflow.md` | 四Agent角色定义、提示词、编排 |
| `report_template.md` | 卡脖子分析报告模板（6000字结构） |

---

## 🔒 数据纪律（铁律）

1. **所有关键数据必须标注来源和时间**
2. **无法获取的直接注明"⚠️ 待验证"，绝不编造**
3. **区分**：事实 → 推断（⚠️ 推测） → 猜测（⚠️ 猜测）
4. **核心数据至少两个来源交叉验证**
5. **优先使用2025/2026年数据**（最新可用）

---

## 📄 许可证

MIT许可证 — 自由使用、修改和分发。

---

## 👤 作者与联系

- **创建者**: QClaw AI Agent System (沐沐/MuMu)
- **用于**: Jonathan (乔纳森)
- **日期**: 2026-05-30
- **版本**: v1.0.0

---

## 🔗 相关项目

- [OpenClaw](https://github.com/openclaw/openclaw) — 本Skill设计的AI Agent框架
- [ProductKnowledgeGraph](https://github.com/liuhuanyong/ProductKnowledgeGraph) — 产品知识图谱（参考）
- [KG-Construction](https://github.com/Aminer-Cloud/KG-Construction) — 知识图谱构建（参考）
- [networkx](https://github.com/networkx/networkx) — 图算法（核心依赖）
- [MetaGPT](https://github.com/geekan/MetaGPT) — 多Agent框架（方法论参考）
- [AutoGen](https://github.com/microsoft/autogen) — 多Agent框架（方法论参考）

---

## ⭐ Star History

如果您觉得这个方法论/系统有用，请给它一个星！⭐
