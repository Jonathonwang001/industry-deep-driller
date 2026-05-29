# Industry Deep Driller / 产业链深度钻探系统

> An investment-banking-grade industry research framework fused with graph-theory-powered bottleneck (chokepoint) identification.
> 
> 投行级6维度行业研究 × 卡脖子反向深度钻探。先看清全貌，再找到命门。

## 🎯 What It Does

A complete methodology + toolset for **deep industry chain analysis**:

1. **🏦 6-Dimension Industry Research** (Breadth Layer) — Market sizing, value chain, competitive landscape, growth drivers, risk, investment thesis
2. **🔬 4-Step Chokepoint Reverse Drilling** (Depth Layer) — BOM decomposition → concentration audit → financial verification → graph quantification
3. **🤖 4-Agent Collaborative Workflow** — Agent A (BOM) → Agent B (Concentration) → Agent C (Financial) → Agent D (Synthesis)

## 🔬 Core Innovation

```
[Top-Level Demand] → [Core Hardware] → [Key Process] → [Exclusive Material/Bottleneck]
   (AI Model)            (GPU/Accelerator)    (Advanced Packaging)      (Specialty Chemicals)
```

**Philosophy**: Don't 
The "bottleneck" is the node with:
- **Betweenness Centrality** > 0.3 (all paths must pass through it)
- **CR1** > 70% (monopoly / 寡头)
- **Gross Margin** > 50% (extreme pricing power)
- **Expansion Cycle** > 12 months (supply-side rigidity)

## 📂 Structure

```
industry-deep-driller/
├── SKILL.md                      ← Skill instruction (for AI agents)
├── scripts/
│   ├── build_dependency_graph.py ← Graph builder + 3 industry templates
│   ├── find_chokepoints.py      ← Chokepoint detection engine
│   └── reverse_drill_agent.py   ← 4-Agent workflow demo
└── references/
    ├── research-framework.md     ← 6-dimension research guide
    ├── methodology.md            ← 4-step drilling methodology
    ├── networkx_patterns.md     ← Graph algorithm reference
    ├── agent_workflow.md        ← Agent orchestration
    └── report_template.md       ← Investment-banking report template
```

## 🚀 Quick Start

```bash
# Build AI GPU industry chain graph
python3 scripts/build_dependency_graph.py --template ai_gpu --output chain.json

# Detect chokepoints
python3 scripts/find_chokepoints.py --graph chain.json --top 10

# Run full 4-Agent workflow
python3 scripts/reverse_drill_agent.py
```

## 🔬 Example Chokepoints Found

| Industry | Top Chokepoint | Score | Why |
|----------|-----------------|-------|-----|
| AI GPU | ASML EUV Lithography | 0.655 🔴 | 100% global market share |
| AI GPU | TSMC CoWoS Packaging | 0.649 🔴 | 95% market share, exclusive tech |
| Humanoid Robot | Harmonic Reducer | 0.58 🟠 | 50% CR1, extreme precision barrier |
| eVTOL | Solid-State Battery Electrolyte | 0.52 🟠 | 20% CR1, 24-month expansion |

## 🎯 Use Cases

- Industry chain deep-dive research
- Supply chain bottleneck identification
- BOM (Bill of Materials) reverse tracing
- Monopoly quantification using graph algorithms
- Investment-banking-grade industry reports
- "Pick-and-Shovel" strategy (find the "shovel seller" in a gold rush)

## 📖 Methodology Fusion

This system fuses methodologies from:

- **Investment Banking Research** (Goldman Sachs, Morgan Stanley, UBS)
- **Graph Theory / Network Science** (Betweenness centrality, structural holes)
- **Pick-and-Shovel Strategy** (Tiger Global, Coatue, Hillhouse)
- **Bottleneck Theory** (the shortest plank in the wooden bucket)
- **LLM Wiki Methodology** (structured knowledge management)
- **Universal Agent Skill** (universal agent workflow patterns)

## 📚 Documentation

All references are in `references/`:

| File | Content |
|------|---------|
| `research-framework.md` | 6-dimension industry research execution guide |
| `output-examples.md` | Sample industry research reports |
| `methodology.md` | Chokepoint 4-step drilling methodology |
| `networkx_patterns.md` | NetworkX graph algorithm code examples |
| `agent_workflow.md` | 4-Agent role definitions & orchestration |
| `report_template.md` | Chokepoint analysis report template (6000 words) |

## 🧪 Tested & Verified

- ✅ AI GPU industry chain (25 nodes, 21 edges) — identified EUV lithography, CoWoS as Tier-1 chokepoints
- ✅ Humanoid robot industry chain — identified harmonic reducers as key bottleneck
- ✅ eVTOL (low-altitude economy) industry chain — identified solid-state batteries as bottleneck
- ✅ 4-Agent workflow runs successfully end-to-end

## 🔗 Integration

This skill is designed for **OpenClaw** (AI agent framework):

```bash
# Install via ClawHub
clawhub install industry-deep-driller

# Or manually copy to ~/.qclaw/skills/
cp -r industry-deep-driller ~/.qclaw/skills/
```

Once installed, the AI agent will **automatically trigger** this skill when user requests match trigger keywords (产业链、卡脖子、chokepoint、bottleneck、reverse drilling, etc.).

## 📄 License

MIT License — free to use, modify, and distribute.

## 👤 Author

- **Created by**: QClaw AI Agent System (沐沐/MuMu)
- **For**: Jonathan (乔纳森)
- **Date**: 2026-05-30
- **Version**: v1.0.0

## ⭐ Star History

If you find this methodology/system useful, please give it a star! ⭐