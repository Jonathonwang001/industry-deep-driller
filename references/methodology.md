# 产业链反向深度钻探方法论 (Chokepoint Methodology)

## 理论来源

这套方法论来自顶级投行（Goldman Sachs, Morgan Stanley, UBS）和买方机构（Tiger Global, Coatue, Hillhouse）的行业研究实践。核心思想源于：

- **Michael Porter 五力模型** — 供应商议价权分析
- **Network Theory** — 介数中心性和结构洞理论
- **Pick-and-Shovel Strategy** — 卖铲人策略（淘金热中卖铲子的人最赚钱）
- **Bottleneck Theory** — 木桶最短的那块木板

## 完整四步钻探法

### Step 1: BOM 拆解 (Bill of Materials Decomposition)

**目标**：从终端产品出发，识别所有需要"非标准化"工艺的零部件。

**数据源优先级**：
1. iFixit 拆解报告 (`ifixit.com/Teardown`)
2. TechInsights / Chipworks 芯片分析
3. 行业拆解报告（中泰证券、天风证券等）
4. 供应商路演/招股书中的客户信息
5. 专利引用关系（谁引用了谁的专利）

**过滤规则**：
- ✅ 保留：非标准化、有独特工艺、有专利壁垒
- ❌ 剔除：标准化零部件（电容、电阻、螺丝）
- ❌ 剔除：成本占比 < 2% 的零部件（除非是单一来源）

**搜索策略**：
```
serper "[产品名] BOM teardown cost breakdown"
serper "[产品名] 拆解 核心零部件 成本"
web_fetch "ifixit.com/Teardown/[产品名]"
```

### Step 2: 市场集中度审计 (Market Concentration Audit)

**目标**：量化每个核心环节的供应商集中度。

**关键指标**：
- CR1：最大供应商市占率（>70% = 🔴垄断）
- CR3：前三供应商市占率（>60% = 🟠寡头）
- HHI：赫芬达尔指数（>2500 = 高度集中）
- 地域集中度：单一国家/地区依赖风险

**数据源**：
1. Omdia、Yole Développement、IC Insights 行业报告
2. 供应商年报（市占率相关披露）
3. 行业协会数据（SEMI, SIA 等）
4. 海关进出口数据（判断进口依赖度）

**搜索策略**：
```
serper "global [component] market share 2025 ranking"
serper "[component] supplier market share CR1 CR3"
web_fetch "omdia.com / yole.fr"  ← 行业权威
```

### Step 3: 财务与定价权验证 (Financial & Pricing Power Verification)

**目标**：确认卡脖子环节 → 供应商是否真正具备"巨头离不开的底层命门"特征。

**关键财务指标**：

| 指标 | 阈值 | 含义 |
|------|------|------|
| 毛利率 (Gross Margin) | ≥ 50% | 极强定价权，客户不敢压价 |
| 扩产周期 (Expansion Cycle) | ≥ 12个月 | 供给侧刚性，需求暴增时必然涨价 |
| 研发费用率 (R&D Ratio) | ≥ 15% | 持续技术投入，壁垒不会短期消亡 |
| 预收款占比 | 高 | 卖方市场特征 |
| 客户集中度 | 分散 | 不依赖单一大客户 |

**数据源**：
1. 上市公司年报/季报（Wind, Bloomberg, 东方财富）
2. 招股说明书中的竞争格局章节
3. 专利数据库（Google Patents, WIPO）
4. 行业深度报告中的毛利率对比

**搜索策略**：
```
serper "[company] gross margin annual report 2025"
web_fetch "cninfo.com.cn" (巨潮资讯·年报)
finance API: Finnhub company profile + financials
```

### Step 4: 图论量化认证 (Graph Theory Quantification)

**目标**：使用网络科学方法，从图论角度认证"咽喉要道"。

**核心指标**：

1. **介数中心性 (Betweenness Centrality)**
   ```
   BC(v) = Σ σ_st(v) / σ_st
   其中 σ_st 是 s→t 的最短路径数，σ_st(v) 是通过 v 的路径数
   ```
   - 物理含义：所有产业链依赖路径必须经过这个节点的概率
   - 投资含义：BC越高的节点 = 越不可替代

2. **结构洞 (Structural Holes)**
   - 有效规模 (Effective Size) = n - 2t/n
   - 投资含义：高结构洞节点对上下游有极强控制力

3. **PageRank**
   - 考虑被重要节点依赖的权重
   - 投资含义：识别"被关键环节依赖的关键环节"

**工具**：
```bash
python3 scripts/find_chokepoints.py --graph chain.json --top 15
```

### Step 5: 综合投资建议 (Investment Synthesis)

**信号评级算法**：

| 信号 | 权重 | 阈值 |
|------|------|------|
| 介数中心性 | 30% | BC > 0.1 |
| CR1市占率 | 25% | CR1 > 70% |
| 毛利率 | 20% | Margin > 50% |
| 技术壁垒 | 15% | "极高" |
| 供应商稀缺度 | 10% | < 3家 |

**最终评级**：
- ≥ 0.70 → 🔴 一级卡脖子·绝对垄断（全球唯一，不可替代）
- ≥ 0.50 → 🟠 二级卡脖子·寡头垄断（2-3家，极难替代）
- ≥ 0.30 → 🟡 三级卡脖子·高集中度（有垄断特征但可替代）
- ≥ 0.15 → 🟢 四级·有特征（值得关注）
- < 0.15 → ⚪ 常规竞争

## 适用行业

这套方法论最适合以下行业（技术壁垒高、供应链长、存在垄断环节）：

1. **先进半导体** — AI GPU → 先进封装 → 光刻 → 特种化学品
2. **低空经济/eVTOL** — 飞行器 → 固态电池 → 碳纤维 → 特种材料
3. **人形机器人** — 整机 → 减速器 → 电机 → 传感器
4. **光通信/光模块** — 光模块 → 光芯片 → 化合物半导体
5. **新能源车** — 整车 → 动力电池 → 正极材料 → 锂盐
6. **创新药** — 药物 → 靶点 → 合成路径 → 关键中间体

## 不适用场景

- 充分竞争的消费品行业（如服装、食品）
- 供应链短的行业（如软件/SaaS）
- 主要依赖品牌溢价而非技术壁垒的行业（如奢侈品）

## 持续迭代

遵循 universal-agent-skill 和 self-improving 方法论：

1. 每次分析后记录关键发现到 memory/
2. 发现新的数据源立即更新本文档
3. 发现具有高BC但之前忽略的环节 → 拓展现有模板
4. 每月回顾：行业模板是否仍然准确
