# 🔬 Industry Deep Driller — 产业链深度钻探系统

> **Industry Chain Reverse Deep Drilling System**  
> An investment-banking-grade industry research framework fused with graph-theory-powered bottleneck (chokepoint) identification.

---

## 🎯 What Is This?

**Industry Deep Driller** is a comprehensive skill/system that combines:

1. **🏦 Investment Banking 6-Dimension Research Framework** (广度层 - Breadth Layer)  
   Covers: Industry Overview → Value Chain Analysis → Competitive Landscape → Growth Drivers → Risk Assessment → Investment Thesis

2. **🔬 Chokepoint Reverse Deep Drilling** (深度层 - Depth Layer)  
   A 4-step methodology to find the industry's "bottleneck" — the one or two global suppliers that have absolute pricing power and cannot be replaced.

```
Layer 1 (Breadth):  6-Dim Research → See the whole picture
                              ↓
Layer 2 (Depth):   4-Step Drilling → Find the chokepoint
```

---

## 🔧 Core Methodology

### Engine 1: 6-Dimension Industry Research

A complete industry analysis framework:

| Dimension | Focus | Output |
|-----------|-------|--------|
| ① Industry Definition | Market size, CAGR, life cycle | Industry essence in 1 sentence |
| ② Value Chain Deep Dive | Upstream/Midstream/Downstream | Who makes the most money & why |
| ③ Competitive Landscape | CR3/CR5/HHI, Porter's 5 Forces | Market concentration map |
| ④ Growth Drivers & Trends | Demand/Supply/Policy/Technology | Key variables that move the industry |
| ⑤ Risk Assessment | Industry/Policy/Competition/Macro | Risk matrix with probability × impact |
| ⑥ Investment Thesis | Rating, targets, catalysts | Actionable investment recommendations |

📖 **Detailed execution guide**: `references/research-framework.md`

---

### Engine 2: Chokepoint Reverse Deep Drilling

A 4-step "drilling" process to find the industry's bottleneck:

```
[Top-Level Demand] → [Core Hardware/Carrier] → [Key Process/Equipment] → [Exclusive Material/Soft Underbelly]
   (AI Model)             (GPU/Accelerator)           (Advanced Packaging/Lithography)     (Specialty Chemicals/Mask)
```

#### Step 1: BOM Decomposition (Agent A)
- Teardown reports → identify core components
- Filter out standardized parts (no investment value)
- Focus on **non-standardized, high-barrier** components

#### Step 2: Market Concentration Audit (Agent B)
- Query global CR1/CR3 for each component
- Red flag: CR1 > 70% (monopoly) 🔴; CR3 > 60% (oligopoly) 🟠
- Identify geographic concentration risk

#### Step 3: Financial & Pricing Power Verification (Agent C)
A true chokepoint MUST have:
- Gross Margin ≥ 50% → extreme pricing power
- Expansion Cycle ≥ 12 months → supply-side rigidity
- R&D Ratio ≥ 15% → sustained technological moat
- Patent barriers ✅

#### Step 4: Graph-Theory Quantification (Agent D)
Using **NetworkX** graph algorithms:
- **Betweenness Centrality** — the "throat" node that all paths must pass through
- **Structural Holes** — a node's control over its neighbors
- **PageRank** — weighted by importance of dependent nodes

**Chokepoint Score** = BC×0.30 + CR1×0.25 + Margin×0.20 + Barrier×0.15 + Scarcity×0.10

| Score | Rating | Investment Implication |
|-------|--------|------------------------|
| ≥ 0.70 | 🔴 Tier-1 Chokepoint (absolute monopoly) | Must study; find alternatives |
| ≥ 0.50 | 🟠 Tier-2 Chokepoint (oligopoly) | Core focus |
| ≥ 0.30 | 🟡 Tier-3 (high concentration) | Worth tracking |
| ≥ 0.15 | 🟢 Tier-4 (some monopoly features) | Monitor |
| < 0.15 | ⚪ Competitive | No need to track |

📖 **Detailed methodology**: `references/methodology.md`  
📊 **NetworkX patterns**: `references/networkx_patterns.md`

---

## 🚀 Quick Start

### Prerequisites

```bash
pip install networkx  # Graph algorithms
```

### Use Pre-built Industry Templates

```bash
# Build AI GPU industry chain graph
python3 scripts/build_dependency_graph.py --template ai_gpu --output ai_gpu_chain.json

# Detect chokepoints
python3 scripts/find_chokepoints.py --graph ai_gpu_chain.json --top 10 --output report.md

# Run full 4-Agent workflow demo
python3 scripts/reverse_drill_agent.py
```

### Available Templates

| Template | Industry | Core Chokepoint Path |
|----------|----------|----------------------|
| `ai_gpu` | AI GPU Industry Chain | H100 → EUV Lithography → Photoresist → Photosensitizer |
| `humanoid_robot` | Humanoid Robot Industry Chain | Robot → Harmonic Reducer → Flex Bearing → Precision Machining |
| `evtol` | eVTOL (Low-Altitude Economy) | eVTOL → Solid-State Battery → Solid Electrolyte → Lithium Metal Anode |

---

## 📂 File Structure

```
industry-deep-driller/
├── README.md                          ← You are here (English)
├── README_ZH.md                      ← 中文版说明文档
├── ABOUT.md                          ← GitHub About (displayed on repo main page)
├── SKILL.md                          ← Skill instruction file (for OpenClaw/ClawHub)
├── LICENSE                           ← MIT License
├── scripts/
│   ├── build_dependency_graph.py     ← Graph builder + 3 industry templates
│   ├── find_chokepoints.py          ← Chokepoint detection engine
│   └── reverse_drill_agent.py       ← 4-Agent collaborative workflow
└── references/
    ├── research-framework.md         ← 6-dimension research execution guide
    ├── output-examples.md            ← Sample industry research reports
    ├── methodology.md                ← Chokepoint 4-step drilling methodology
    ├── networkx_patterns.md         ← NetworkX graph algorithm reference
    ├── agent_workflow.md            ← 4-Agent role configuration
    └── report_template.md           ← Chokepoint analysis report template
```

---

## 🔬 The 4-Agent Workflow

When analyzing a specific product/industry, four "agents" collaborate:

```
Agent A (BOM Decomposer)
   ↓ Identifies core components
Agent B (Market Concentration Auditor)
   ↓ Calculates CR1/CR3, flags monopolies
Agent C (Financial & Pricing Power Assessor)
   ↓ Verifies margin, expansion cycle, patent moat
Agent D (Chokepoint Synthesis & Grader)
   ↓ Builds graph, computes betweenness, gives final rating
```

Each agent's output feeds into the next — a pipeline ensuring **no chokepoint is missed**.

📖 **Agent configuration details**: `references/agent_workflow.md`

---

## 📊 Example: AI GPU Industry Chain Analysis

After running the full workflow on NVIDIA H100 GPU:

```
==========================================
🔬 Industry Chain Reverse Deep Drilling Report
==========================================

Top Chokepoints:
  1. EUV Lithography Process        Score: 0.6552 🟠 Tier-2
  2. CoWoS Advanced Packaging       Score: 0.6489 🟠 Tier-2
  3. GPU Core Chip (5nm)           Score: 0.6192 🟠 Tier-2
  4. Low-Loss Resin                Score: 0.4696 🟡 Tier-3
  5. HBM3e High-Bandwidth Memory  Score: 0.4688 🟡 Tier-3
  ...
```

**Key insight**: ASML (EUV lithography) has **100% global market share** — a true absolute chokepoint. TSMC's CoWoS packaging has **95% market share** — another chokepoint.

---

## 🎯 Use Cases

This system/methodology is designed for:

1. **Industry chain deep-dive research** (find the real bottlenecks)
2. **Supply chain bottleneck identification** (chokepoint / bottleneck analysis)
3. **BOM (Bill of Materials) reverse tracing**
4. **Monopoly quantification using graph algorithms**
5. **Investment-banking-grade industry research reports**
6. **Identifying "shovel sellers" (Pick-and-Shovel strategy)**

**Trigger keywords** (for AI agent integration):
- 中文: 产业链、卡脖子、反向钻探、chokepoint、bottleneck、供应链分析、垄断分析、产业链图谱、BOM拆解、行业瓶颈
- English: `industry chain`, `chokepoint`, `bottleneck`, `reverse drilling`, `supply chain analysis`, `monopoly analysis`, `BOM teardown`

---

## 🔗 Integration with AI Agents (OpenClaw)

This skill is designed to be installed in **OpenClaw** (an AI agent framework):

```bash
# Install via ClawHub
clawhub install industry-deep-driller

# Or manually copy to ~/.qclaw/skills/
cp -r industry-deep-driller ~/.qclaw/skills/
```

Once installed, the AI agent will **automatically trigger** this skill when the user's request matches the trigger keywords above.

---

## 📚 Methodology Sources

This system fuses methodologies from:

- **Investment Banking Research** (Goldman Sachs, Morgan Stanley, UBS) — 6-dimension framework
- **Graph Theory / Network Science** — Betweenness centrality, structural holes
- **Pick-and-Shovel Strategy** (Tiger Global, Coatue, Hillhouse) — find the "shovel seller" in a gold rush
- **Bottleneck Theory** — identify the shortest plank in the wooden bucket
- **LLM Wiki Methodology** — structured knowledge management
- **Universal Agent Skill** — universal agent workflow patterns

---

## 🧪 Tested & Verified

- ✅ AI GPU industry chain (25 nodes, 21 edges) — successfully identified EUV lithography, CoWoS packaging as Tier-2 chokepoints
- ✅ Humanoid robot industry chain — identified harmonic reducers, hollow-cup motors as key bottlenecks
- ✅ eVTOL (low-altitude economy) industry chain — identified solid-state batteries, carbon fiber composites as bottlenecks
- ✅ 4-Agent workflow runs successfully end-to-end

---

## 📖 Documentation

All references are in the `references/` directory:

| File | Content |
|------|---------|
| `research-framework.md` | 6-dimension industry research execution guide (detailed) |
| `output-examples.md` | Sample industry research reports (for format reference) |
| `methodology.md` | Chokepoint 4-step drilling methodology (detailed) |
| `networkx_patterns.md` | NetworkX graph algorithm code examples |
| `agent_workflow.md` | 4-Agent role definitions, prompts, orchestration |
| `report_template.md` | Chokepoint analysis report template (6000-word structure) |

---

## 🔒 Data Discipline (Iron Rules)

1. **All key data must cite sources and timestamps**
2. **Cannot obtain = "⚠️ 待验证" (pending verification)** — never fabricate data
3. **Distinguish**: Fact → Inference (⚠️ 推测) → Guess (⚠️ 猜测)
4. **Cross-verify core data with ≥ 2 sources**
5. **Prefer 2025/2026 data** (most recent available)

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 👤 Author & Contact

- **Created by**: QClaw AI Agent System (沐沐/MuMu)
- **For**: Jonathan (乔纳森)
- **Date**: 2026-05-30
- **Version**: v1.0.0

---

## 🔗 Related Projects

- [OpenClaw](https://github.com/openclaw/openclaw) — the AI agent framework this skill is designed for
- [ProductKnowledgeGraph](https://github.com/liuhuanyong/ProductKnowledgeGraph) — product knowledge graph (reference)
- [KG-Construction](https://github.com/Aminer-Cloud/KG-Construction) — knowledge graph construction (reference)
- [networkx](https://github.com/networkx/networkx) — graph algorithms (core dependency)
- [MetaGPT](https://github.com/geekan/MetaGPT) — multi-agent framework (methodology reference)
- [AutoGen](https://github.com/microsoft/autogen) — multi-agent framework (methodology reference)

---

## ⭐ Star History

If you find this methodology/system useful, please give it a star! ⭐
