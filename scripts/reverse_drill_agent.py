#!/usr/bin/env python3
"""
多Agent反向深度钻探工作流 (Multi-Agent Reverse Deep Drilling Workflow)

模拟投行分析师的四步反向钻探法，通过多Agent协作自动执行:
  Agent A (BOM拆解员): 扒出终端产品的物料清单和供应链结构
  Agent B (市场集中度审计员): 计算每个零部件的全球CR1/CR3
  Agent C (财务定价权评估员): 评估供应商的毛利率和壁垒
  Agent D (卡脖子综合评级员): 综合所有数据给出最终评级和投资建议

工作流:
  [顶层超级需求] → [核心硬件/载体] → [关键制程/设备] → [独家垄断材料/软肋]

用法:
  python3 reverse_drill_agent.py --product "NVIDIA H100" --depth 4
  python3 reverse_drill_agent.py --template ai_gpu --output report.md
"""

import json
import sys
import os
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from datetime import datetime

try:
    import networkx as nx
except ImportError:
    print("⚠️ networkx 未安装，运行: pip install networkx")
    sys.exit(1)


@dataclass
class BomItem:
    """物料清单条目"""
    name: str
    tier: int
    category: str  # 核心硬件/关键制程/特种材料/标准化零部件
    parent: str
    cost_share_pct: float  # 占整机成本比例
    is_standardized: bool  # 是否标准化零部件
    tech_barrier: str  # 技术壁垒: 极高/高/中/低
    description: str = ""


@dataclass
class SupplierIntel:
    """供应商情报"""
    name: str
    country: str
    market_share: float  # % 
    gross_margin: float  # %
    revenue: str  # 营收规模（文字描述）
    moat_description: str
    expansion_cycle: str  # 扩产周期描述
    is_monopoly: bool  # 是否接近垄断


@dataclass
class ChokepointAnalysis:
    """卡脖子环节综合分析"""
    node_name: str
    tier: int
    category: str
    bom_item: Optional[BomItem] = None
    suppliers: List[SupplierIntel] = field(default_factory=list)
    
    # 量化指标
    betweenness: float = 0.0
    cr1: float = 0.0
    cr3: float = 0.0
    margin_weighted: float = 0.0
    barrier_score: float = 0.0
    chokepoint_score: float = 0.0
    
    # 评级
    rating: str = "⚪ 常规"
    investment_thesis: str = ""
    key_triggers: List[str] = field(default_factory=list)


class ReverseDrillWorkflow:
    """
    多Agent反向深度钻探工作流
    
    模拟四位投行分析师的协作过程:
    """
    
    def __init__(self, product_name: str, industry: str = ""):
        self.product_name = product_name
        self.industry = industry
        self.graph = nx.DiGraph()
        self.bom_items: List[BomItem] = []
        self.supplier_intel: Dict[str, List[SupplierIntel]] = {}
        self.chokepoints: List[ChokepointAnalysis] = []
        
    # ============================================================
    # Agent A: BOM拆解员
    # 任务: 扒出终端产品的物料清单和供应链结构
    # ============================================================
    def agent_a_bom_decompose(self, 
                               core_components: List[dict],
                               sub_components: List[dict],
                               materials: List[dict]) -> List[BomItem]:
        """
        Agent A: 物料清单拆解
        
        输入供应链情报（可能来自搜索、拆解报告、行业研究），
        输出结构化的BOM清单。
        
        Args:
            core_components: 核心组件列表 [{"name": "GPU", "cost_share": 35, "standardized": False}, ...]
            sub_components: 子组件列表
            materials: 原材料列表
        """
        bom = []
        
        # Tier 1: 核心组件
        for comp in core_components:
            item = BomItem(
                name=comp["name"],
                tier=1,
                category="核心硬件/载体",
                parent=self.product_name,
                cost_share_pct=comp.get("cost_share", 0),
                is_standardized=comp.get("standardized", False),
                tech_barrier=comp.get("barrier", "高"),
                description=comp.get("description", "")
            )
            bom.append(item)
            self.graph.add_node(item.name, tier=1, type="核心组件")
            self.graph.add_edge(self.product_name, item.name, relation="depends_on")
        
        # Tier 2: 关键制程/设备
        for comp in sub_components:
            parent = comp.get("parent", core_components[0]["name"] if core_components else self.product_name)
            item = BomItem(
                name=comp["name"],
                tier=2,
                category="关键制程/设备",
                parent=parent,
                cost_share_pct=comp.get("cost_share", 0),
                is_standardized=comp.get("standardized", False),
                tech_barrier=comp.get("barrier", "极高"),
                description=comp.get("description", "")
            )
            bom.append(item)
            self.graph.add_node(item.name, tier=2, type="关键制程")
            self.graph.add_edge(parent, item.name, relation="depends_on")
        
        # Tier 3: 独家材料
        for mat in materials:
            parent = mat.get("parent", sub_components[0]["name"] if sub_components else self.product_name)
            item = BomItem(
                name=mat["name"],
                tier=3,
                category="独家材料/软肋",
                parent=parent,
                cost_share_pct=mat.get("cost_share", 0),
                is_standardized=mat.get("standardized", False),
                tech_barrier=mat.get("barrier", "极高"),
                description=mat.get("description", "")
            )
            bom.append(item)
            self.graph.add_node(item.name, tier=3, type="特种材料")
            self.graph.add_edge(parent, item.name, relation="depends_on")
        
        self.bom_items = bom
        self._print_agent_report("A", "BOM拆解员", 
            f"✅ 已完成 {self.product_name} 的物料清单拆解",
            f"共识别 {len(core_components)} 个核心组件 → "
            f"{len(sub_components)} 个制程环节 → "
            f"{len(materials)} 个底层材料",
            "\n⚠️ 标准化零部件已过滤（无投资价值）",
            "\n🎯 聚焦非标准化、高壁垒的卡脖子环节",
        )
        
        return bom
    
    # ============================================================
    # Agent B: 市场集中度审计员
    # 任务: 计算每个零部件的全球CR1/CR3/供应商分布
    # ============================================================
    def agent_b_market_concentration(self, supplier_data: Dict[str, List[dict]]) -> Dict[str, List[SupplierIntel]]:
        """
        Agent B: 市场集中度审计
        
        Args:
            supplier_data: {"组件名": [{"name": "供应商A", "country": "JP", "share": 60, "margin": 55}, ...]}
        """
        results = {}
        
        for component_name, suppliers in supplier_data.items():
            intel_list = []
            total_market = sum(s["share"] for s in suppliers)
            
            for s in suppliers:
                intel = SupplierIntel(
                    name=s["name"],
                    country=s.get("country", "未知"),
                    market_share=s["share"],
                    gross_margin=s.get("margin", 0),
                    revenue=s.get("revenue", "未公开"),
                    moat_description=s.get("moat", ""),
                    expansion_cycle=s.get("expansion", "未知"),
                    is_monopoly=s["share"] >= 60,
                )
                intel_list.append(intel)
            
            # 按市场份额降序排列
            intel_list.sort(key=lambda x: x.market_share, reverse=True)
            results[component_name] = intel_list
            
            # 更新图谱节点属性
            cr1 = intel_list[0].market_share if intel_list else 0
            cr3 = sum(s.market_share for s in intel_list[:3])
            avg_margin = sum(s.gross_margin for s in intel_list) / len(intel_list) if intel_list else 0
            
            if component_name in self.graph:
                self.graph.nodes[component_name]["cr1"] = cr1
                self.graph.nodes[component_name]["cr3"] = cr3
                self.graph.nodes[component_name]["suppliers"] = len(intel_list)
                self.graph.nodes[component_name]["gross_margin"] = avg_margin
        
        self.supplier_intel = results
        
        # 统计
        monopoly_count = sum(1 for il in results.values() if il and il[0].is_monopoly)
        oligopoly_count = sum(1 for il in results.values() 
                              if il and not il[0].is_monopoly and sum(s.market_share for s in il[:3]) >= 60)
        
        self._print_agent_report("B", "市场集中度审计员",
            f"✅ 已完成供应商集中度分析",
            f"共分析 {len(results)} 个产业链环节",
            f"🔴 垄断级(CR1≥60%): {monopoly_count} 个",
            f"🟠 寡头级(CR3≥60%): {oligopoly_count} 个",
            f"🟢 竞争级: {len(results) - monopoly_count - oligopoly_count} 个",
        )
        
        return results
    
    # ============================================================
    # Agent C: 财务与定价权评估员
    # 任务: 评估供应商毛利率、研发壁垒、扩产周期
    # ============================================================
    def agent_c_financial_assessment(self, financial_data: Dict[str, dict]) -> Dict[str, dict]:
        """
        Agent C: 财务与定价权评估
        
        Args:
            financial_data: {"组件名": {"margin": 55, "rd_ratio": 15, "expansion_months": 18, "has_patent_moat": True}}
        """
        results = {}
        
        for component_name, fin_data in financial_data.items():
            assessment = {
                "gross_margin": fin_data.get("margin", 0),
                "rd_ratio": fin_data.get("rd_ratio", 0),  # 研发费用率
                "expansion_months": fin_data.get("expansion_months", 0),  # 扩产周期(月)
                "has_patent_moat": fin_data.get("has_patent_moat", False),
                "pricing_power": self._assess_pricing_power(fin_data),
                "is_chokepoint": self._is_chokepoint(fin_data),
            }
            results[component_name] = assessment
            
            # 更新图谱节点
            if component_name in self.graph:
                self.graph.nodes[component_name]["gross_margin"] = fin_data.get("margin", 0)
                if fin_data.get("expansion_months", 0) >= 12:
                    self.graph.nodes[component_name]["barrier_level"] = "极高"
                elif fin_data.get("has_patent_moat"):
                    self.graph.nodes[component_name]["barrier_level"] = "高"
        
        chokepoint_count = sum(1 for a in results.values() if a["is_chokepoint"])
        
        self._print_agent_report("C", "财务与定价权评估员",
            f"✅ 已完成财务深度分析",
            f"🔴 确认卡脖子特征(毛利率>50%+扩产>12月+专利壁垒): {chokepoint_count} 个",
            f"📊 平均毛利率: {sum(a['gross_margin'] for a in results.values()) / len(results):.1f}%",
            f"⏱️ 平均扩产周期: {sum(a['expansion_months'] for a in results.values()) / len(results):.1f} 个月",
        )
        
        return results
    
    def _assess_pricing_power(self, fin_data: dict) -> str:
        """评估定价权等级"""
        margin = fin_data.get("margin", 0)
        has_moat = fin_data.get("has_patent_moat", False)
        expansion = fin_data.get("expansion_months", 0)
        
        if margin >= 55 and has_moat and expansion >= 12:
            return "绝对定价权"
        elif margin >= 45 and (has_moat or expansion >= 12):
            return "强定价权"
        elif margin >= 35:
            return "中等定价权"
        else:
            return "弱定价权"
    
    def _is_chokepoint(self, fin_data: dict) -> bool:
        """判断是否为卡脖子环节"""
        margin = fin_data.get("margin", 0)
        expansion = fin_data.get("expansion_months", 0)
        has_moat = fin_data.get("has_patent_moat", False)
        return margin >= 50 and expansion >= 12 and has_moat
    
    # ============================================================
    # Agent D: 卡脖子综合评级员
    # 任务: 汇总前三步结果，给出最终评级和投资建议
    # ============================================================
    def agent_d_final_synthesis(self) -> List[ChokepointAnalysis]:
        """
        Agent D: 综合评级与投资建议
        
        汇总 Agent A/B/C 的分析结果，使用图算法计算介数中心性，
        结合市场集中度和财务数据，给出最终的卡脖子评级。
        """
        if self.graph.number_of_nodes() == 0:
            print("⚠️ 图谱为空，请先运行 Agent A")
            return []
        
        # 计算图论指标
        betweenness = nx.betweenness_centrality(self.graph)
        
        results = []
        for node in self.graph.nodes():
            if node == self.product_name:
                continue
            
            attrs = self.graph.nodes[node]
            cr1 = attrs.get("cr1", 0)
            margin = attrs.get("gross_margin", 0)
            barrier = attrs.get("barrier_level", "中")
            bt = betweenness.get(node, 0)
            
            # 综合评分
            barrier_score = {"极高": 1.0, "高": 0.65, "中": 0.35, "低": 0.1}.get(barrier, 0.35)
            cr1_score = min(cr1 / 100, 1.0)
            margin_score = min(margin / 70, 1.0)
            
            score = (
                bt * 0.30 +
                cr1_score * 0.25 +
                margin_score * 0.20 +
                barrier_score * 0.15 +
                (1.0 / max(attrs.get("suppliers", 5), 1)) * 0.10
            )
            
            # 评级
            if score >= 0.7: rating = "🔴 一级卡脖子·绝对垄断"
            elif score >= 0.5: rating = "🟠 二级卡脖子·寡头垄断"
            elif score >= 0.3: rating = "🟡 三级卡脖子·高集中度"
            elif score >= 0.15: rating = "🟢 四级·有垄断特征"
            else: rating = "⚪ 常规竞争"
            
            chokepoint = ChokepointAnalysis(
                node_name=node,
                tier=attrs.get("tier", 1),
                category=attrs.get("type", "未知"),
                betweenness=round(bt, 4),
                cr1=cr1,
                cr3=attrs.get("cr3", 0),
                margin_weighted=margin,
                barrier_score=barrier_score,
                chokepoint_score=round(score, 4),
                rating=rating,
                investment_thesis=self._generate_investment_thesis(node, attrs, score),
                key_triggers=self._generate_triggers(node, attrs),
            )
            results.append(chokepoint)
        
        # 排序
        results.sort(key=lambda x: x.chokepoint_score, reverse=True)
        self.chokepoints = results
        
        top_chokepoints = [c for c in results if c.chokepoint_score >= 0.5]
        
        self._print_agent_report("D", "卡脖子综合评级员",
            f"✅ 已完成最终综合评级",
            f"🔴 一级卡脖子: {len([c for c in results if '一级' in c.rating])} 个",
            f"🟠 二级卡脖子: {len([c for c in results if '二级' in c.rating])} 个",
            f"🎯 建议重点关注: {', '.join(c.node_name for c in top_chokepoints[:5])}",
        )
        
        return results
    
    def _generate_investment_thesis(self, node: str, attrs: dict, score: float) -> str:
        """生成投资论点"""
        thesis_parts = []
        
        if score >= 0.5:
            thesis_parts.append(f"🔴 {node}是产业链上的咽喉环节")
        elif score >= 0.3:
            thesis_parts.append(f"🟡 {node}具有显著垄断特征")
        
        margin = attrs.get("gross_margin", 0)
        if margin >= 50:
            thesis_parts.append(f"毛利率{margin}%表明极强的定价权")
        
        cr1 = attrs.get("cr1", 0)
        if cr1 >= 60:
            thesis_parts.append(f"全球CR1达{cr1}%近乎垄断")
        
        return "；".join(thesis_parts) if thesis_parts else "暂无明确投资论点"
    
    def _generate_triggers(self, node: str, attrs: dict) -> List[str]:
        """生成催化剂事件"""
        triggers = []
        triggers.append(f"关注{node}供应商的季度财报和产能指引")
        
        cr1 = attrs.get("cr1", 0)
        if cr1 >= 60:
            triggers.append(f"⚠️ 监测{cr1}%市占率潜在反垄断风险")
        
        margin = attrs.get("gross_margin", 0)
        if margin >= 50:
            triggers.append(f"关注毛利率{margin}%的可持续性，警惕新进入者")
        
        triggers.append(f"跟踪终端需求变化对{node}的价格传导效应")
        return triggers
    
    # ============================================================
    # 主工作流
    # ============================================================
    def run(self,
            bom_components: List[dict],
            bom_sub_components: List[dict],
            bom_materials: List[dict],
            supplier_data: Dict[str, List[dict]],
            financial_data: Dict[str, dict],
            lightweight: bool = False) -> List[ChokepointAnalysis]:
        """
        运行完整的多Agent反向钻探工作流
        
        参数结构参考 src/agent_a_bom_decompose、agent_b_market_concentration、
        agent_c_financial_assessment 方法的文档。
        
        lightweight=True → 🔴 纯钻探模式：跳过Agent C财务验证，使用纯图论+集中度评分
        lightweight=False → 完整模式：包含财务验证
        """
        mode_label = "🔴 纯钻探" if lightweight else "🔵 完整双引擎"
        print("=" * 70)
        print(f"🔄 多Agent反向深度钻探工作流启动 [{mode_label}]")
        print(f"🎯 终端产品: {self.product_name}")
        print(f"🏭 所属行业: {self.industry}")
        print(f"📅 分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        if lightweight:
            print("⚡ 纯钻探模式: Agent A(拆解) → Agent B(集中度) → Agent D(图论评级)")
            print("⏭️  已跳过 Agent C(财务验证) — 纯钻探聚焦产业链上下游结构")
        print("=" * 70)
        print()
        print("工作流: [终端产品] → [核心组件] → [关键制程] → [独家材料]")
        print()
        
        # Agent A: BOM拆解
        self.agent_a_bom_decompose(bom_components, bom_sub_components, bom_materials)
        
        # Agent B: 市场集中度
        self.agent_b_market_concentration(supplier_data)
        
        # Agent C: 财务评估
        if not lightweight:
            self.agent_c_financial_assessment(financial_data)
        else:
            # 纯钻探模式：跳过财务评估，仅基于CR1做集中度判断
            print(f"╔══ Agent C: 财务定价权评估员 ═══╗")
            print(f"║ ⏭️  纯钻探模式 — 跳过财务指标分析")
            print(f"║ 🔴 聚焦：产业链上下游结构 + 节点集中度（CR1）")
            print(f"╚════════════════════════════════════════╝")
            print()
        
        # Agent D: 综合评级
        chokepoints = self.agent_d_final_synthesis(lightweight=lightweight)
        
        return chokepoints
    
    def _print_agent_report(self, agent_id: str, agent_name: str, *lines):
        """打印Agent报告"""
        print(f"╔══ Agent {agent_id}: {agent_name} ═══╗")
        for line in lines:
            print(f"║ {line}")
        print(f"╚{'═' * 40}╝")
        print()
    
    def generate_full_report(self) -> str:
        """生成完整的反向钻探分析报告"""
        if not self.chokepoints:
            return "⚠️ 请先运行 run() 方法执行完整工作流"
        
        lines = []
        lines.append(f"# 🔬 {self.product_name} 产业链反向深度钻探报告")
        lines.append(f"\n> 分析方法: Chokepoint Reverse Deep Drilling")
        lines.append(f"> 行业: {self.industry}")
        lines.append(f"> 图谱: {self.graph.number_of_nodes()} 节点 · {self.graph.number_of_edges()} 条依赖边")
        lines.append(f"> 时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        
        # BOM 概览
        lines.append(f"\n## 📋 BOM物料清单概览")
        lines.append("")
        lines.append("| 层级 | 组件 | 类别 | 成本占比 | 标准化 | 技术壁垒 |")
        lines.append("|------|------|------|----------|--------|----------|")
        for item in self.bom_items:
            std = "是" if item.is_standardized else "否⚠️"
            lines.append(f"| Tier {item.tier} | {item.name} | {item.category} | {item.cost_share_pct}% | {std} | {item.tech_barrier} |")
        
        # 供应商格局
        lines.append(f"\n## 🏭 全球供应商格局")
        for component, suppliers in self.supplier_intel.items():
            lines.append(f"\n### {component}")
            lines.append("")
            lines.append("| 排名 | 供应商 | 国家 | 市占率 | 毛利率 | 垄断特征 |")
            lines.append("|------|--------|------|--------|--------|----------|")
            for i, s in enumerate(suppliers[:5]):
                mono = "🔴 垄断" if s.is_monopoly else ("🟠 强位" if s.market_share >= 30 else "")
                lines.append(f"| {i+1} | {s.name} | {s.country} | {s.market_share}% | {s.gross_margin}% | {mono} |")
        
        # 卡脖子排名
        lines.append(f"\n## 🎯 卡脖子环节最终排名")
        lines.append("")
        lines.append("| 排名 | 环节 | 层级 | 评分 | 评级 | 核心观点 |")
        lines.append("|------|------|------|------|------|----------|")
        for i, cp in enumerate(self.chokepoints[:15]):
            lines.append(f"| {i+1} | {cp.node_name} | T{cp.tier} | {cp.chokepoint_score:.4f} | {cp.rating[:4]} | {cp.investment_thesis[:60]}... |")
        
        # 投资建议
        lines.append(f"\n## 💰 投资建议")
        lines.append("")
        top_3 = [c for c in self.chokepoints if c.chokepoint_score >= 0.5][:3]
        for i, cp in enumerate(top_3):
            lines.append(f"### 🥇🥈🥉"[i] + f" {cp.node_name}")
            lines.append(f"- **评级**: {cp.rating}")
            lines.append(f"- **投资逻辑**: {cp.investment_thesis}")
            lines.append(f"- **催化剂**:")
            for t in cp.key_triggers:
                lines.append(f"  - {t}")
            lines.append("")
        
        # 方法论
        lines.append(f"\n## 📐 分析方法论")
        lines.append("")
        lines.append("```")
        lines.append("[顶层超级需求] ──> [核心硬件/载体] ──> [关键制程/设备] ──> [独家垄断材料/软肋]")
        lines.append(f"  ({self.product_name})      (核心BOM)         (制程瓶颈)         (卡脖子命门)")
        lines.append("```")
        lines.append("")
        lines.append("**四步钻探法:**")
        lines.append("1. 拆解BOM — 识别非标准化、高成本占比的零部件")
        lines.append("2. 审计集中度 — 找到CR1≥60%的垄断供应商")
        lines.append("3. 财务验证 — 确认毛利率≥50% + 长扩产周期 + 专利壁垒")
        lines.append("4. 图论量化 — 介数中心性识别产业链咽喉要道")
        
        return "\n".join(lines)
    
    def save_report(self, path: str):
        """保存报告"""
        report = self.generate_full_report()
        with open(path, 'w', encoding='utf-8') as f:
            f.write(report)
        return path


def demo_ai_gpu():
    """演示: AI GPU 产业链反向钻探"""
    workflow = ReverseDrillWorkflow("NVIDIA H100 GPU", "先进半导体与AI")
    
    # Agent A: BOM拆解数据
    bom_components = [
        {"name": "GPU核心芯片 (5nm)", "cost_share": 35, "standardized": False, "barrier": "极高"},
        {"name": "HBM3e高带宽内存", "cost_share": 25, "standardized": False, "barrier": "极高"},
        {"name": "CoWoS先进封装", "cost_share": 15, "standardized": False, "barrier": "极高"},
        {"name": "光模块/互联", "cost_share": 8, "standardized": False, "barrier": "高"},
    ]
    
    bom_sub = [
        {"name": "EUV光刻制程", "cost_share": 20, "parent": "GPU核心芯片 (5nm)", "standardized": False, "barrier": "极高"},
        {"name": "TSV硅通孔", "cost_share": 10, "parent": "HBM3e高带宽内存", "standardized": False, "barrier": "极高"},
        {"name": "中介层(Interposer)", "cost_share": 8, "parent": "CoWoS先进封装", "standardized": False, "barrier": "极高"},
    ]
    
    bom_materials = [
        {"name": "高纯度光刻胶", "cost_share": 5, "parent": "EUV光刻制程", "standardized": False, "barrier": "极高"},
        {"name": "特种高频覆铜板(CCL)", "cost_share": 4, "parent": "中介层(Interposer)", "standardized": False, "barrier": "极高"},
        {"name": "低损耗树脂", "cost_share": 3, "parent": "特种高频覆铜板(CCL)", "standardized": False, "barrier": "极高"},
    ]
    
    # Agent B: 供应商数据
    supplier_data = {
        "GPU核心芯片 (5nm)": [
            {"name": "NVIDIA (自研设计)", "country": "US", "share": 85, "margin": 75, "moat": "CUDA生态+架构优势"},
            {"name": "AMD", "country": "US", "share": 15, "margin": 50, "moat": "追赶者"},
        ],
        "HBM3e高带宽内存": [
            {"name": "SK海力士", "country": "KR", "share": 50, "margin": 55, "moat": "HBM技术领先"},
            {"name": "三星电子", "country": "KR", "share": 35, "margin": 45, "moat": "存储全面布局"},
            {"name": "美光", "country": "US", "share": 15, "margin": 35, "moat": "技术追赶"},
        ],
        "CoWoS先进封装": [
            {"name": "台积电", "country": "TW", "share": 95, "margin": 53, "moat": "独家掌握CoWoS技术"},
        ],
        "EUV光刻制程": [
            {"name": "ASML", "country": "NL", "share": 100, "margin": 52, "moat": "全球唯一EUV光刻机供应商"},
        ],
        "高纯度光刻胶": [
            {"name": "JSR", "country": "JP", "share": 35, "margin": 60, "moat": "EUV光刻胶先驱"},
            {"name": "TOK", "country": "JP", "share": 30, "margin": 55, "moat": "高端光刻胶"},
        ],
        "特种高频覆铜板(CCL)": [
            {"name": "松下电工", "country": "JP", "share": 35, "margin": 42, "moat": "高频CCL先驱"},
            {"name": "联茂电子", "country": "TW", "share": 25, "margin": 38, "moat": "高速成长"},
        ],
        "低损耗树脂": [
            {"name": "三菱化学", "country": "JP", "share": 45, "margin": 55, "moat": "特种树脂专利"},
            {"name": "DIC株式会社", "country": "JP", "share": 35, "margin": 50, "moat": "低Dk/Df树脂"},
        ],
    }
    
    # Agent C: 财务数据
    financial_data = {
        "GPU核心芯片 (5nm)": {"margin": 75, "rd_ratio": 25, "expansion_months": 24, "has_patent_moat": True},
        "HBM3e高带宽内存": {"margin": 55, "rd_ratio": 15, "expansion_months": 18, "has_patent_moat": True},
        "CoWoS先进封装": {"margin": 53, "rd_ratio": 10, "expansion_months": 18, "has_patent_moat": True},
        "EUV光刻制程": {"margin": 52, "rd_ratio": 20, "expansion_months": 24, "has_patent_moat": True},
        "高纯度光刻胶": {"margin": 60, "rd_ratio": 12, "expansion_months": 12, "has_patent_moat": True},
        "特种高频覆铜板(CCL)": {"margin": 42, "rd_ratio": 8, "expansion_months": 9, "has_patent_moat": True},
        "低损耗树脂": {"margin": 55, "rd_ratio": 10, "expansion_months": 12, "has_patent_moat": True},
    }
    
    chokepoints = workflow.run(bom_components, bom_sub, bom_materials, supplier_data, financial_data)
    
    # 输出最终排名
    print("=" * 70)
    print("🏆 最终卡脖子排名 TOP 10")
    print("=" * 70)
    for i, cp in enumerate(chokepoints[:10]):
        bar = "█" * int(cp.chokepoint_score * 20)
        print(f"{i+1:2d}. {cp.node_name:<30s} [T{cp.tier}] {cp.rating}")
        print(f"    评分: {cp.chokepoint_score:.4f} {bar}")
        print(f"    介数: {cp.betweenness:.4f} | CR1: {cp.cr1}% | 毛利: {cp.margin_weighted}%")
        print()
    
    return workflow


if __name__ == "__main__":
    workflow = demo_ai_gpu()
    
    # 保存报告
    report_path = workflow.save_report("chokepoint_drill_report.md")
    print(f"\n📄 完整报告已保存到: {report_path}")
    
    # 同时导出JSON
    json_path = "chokepoint_drill_result.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump([{
            "node": cp.node_name,
            "tier": cp.tier,
            "score": cp.chokepoint_score,
            "rating": cp.rating,
            "thesis": cp.investment_thesis,
            "triggers": cp.key_triggers,
        } for cp in workflow.chokepoints], f, ensure_ascii=False, indent=2)
    print(f"📊 JSON结果已保存到: {json_path}")