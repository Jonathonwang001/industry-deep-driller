#!/usr/bin/env python3
"""
卡脖子环节识别引擎 (Chokepoint / Bottleneck Detector)

基于 NetworkX 图算法，对产业链依赖图谱进行量化分析，
自动识别具有垄断特征的"卡脖子"节点。

核心指标:
1. 介数中心性 (Betweenness Centrality) — 所有依赖路径的必经程度
2. 出度 (Out-degree) — 该节点的上游依赖广度
3. 市场集中度 (CR1) — 全球最大供应商市占率
4. 毛利率 (Gross Margin) — 定价权代理指标
5. 综合卡脖子评分 (Chokepoint Score) — 加权综合评分

用法:
  python3 find_chokepoints.py --graph dependency_graph.json
  python3 find_chokepoints.py --graph dependency_graph.json --top 10
  python3 find_chokepoints.py --template ai_gpu --top 10
"""

import json
import sys
import math

try:
    import networkx as nx
except ImportError:
    print("⚠️ networkx 未安装，运行: pip install networkx")
    sys.exit(1)


class ChokepointDetector:
    """
    卡脖子环节识别引擎
    
    算法思想（投行分析方法论）:
    - 在图论中，介数中心性高的节点 = 产业链上的"咽喉要道"
    - 结合市占率、毛利率、技术壁垒 → 量化"卡脖子"程度
    - 这些节点就是推动需求暴增也无法快速扩产的瓶颈
    """
    
    # CR1 评分映射 (CR1 = 最大供应商市占率)
    CR1_SCORE = {
        100: 1.0,  # 独家垄断 → 满分
        90: 0.95,
        80: 0.9,
        70: 0.8,
        60: 0.7,
        50: 0.55,
        40: 0.4,
        30: 0.25,
        20: 0.15,
        10: 0.05,
        0: 0.0,
    }
    
    # 技术壁垒评分映射
    BARRIER_SCORE = {
        "极高": 1.0,
        "高": 0.65,
        "中": 0.35,
        "低": 0.1,
    }
    
    # 毛利率评分 (毛利率越高 → 定价权越强)
    @staticmethod
    def margin_to_score(margin: float) -> float:
        if margin >= 70: return 1.0
        if margin >= 60: return 0.9
        if margin >= 50: return 0.8
        if margin >= 40: return 0.6
        if margin >= 30: return 0.4
        if margin >= 20: return 0.2
        return 0.1
    
    def __init__(self, graph: nx.DiGraph):
        self.graph = graph
        self.betweenness = None
        self.chokepoints = []
        
    def compute_betweenness(self):
        """计算所有节点的介数中心性"""
        # 对于有向图，用有向图的介数中心性
        self.betweenness = nx.betweenness_centrality(self.graph)
        return self.betweenness
    
    def compute_pagerank(self):
        """计算PageRank作为补充指标（考虑上游供应商的重要性）"""
        return nx.pagerank(self.graph, alpha=0.85)
    
    def compute_structural_holes(self):
        """计算结构洞指标（节点对其邻居的控制力）"""
        # 使用有效规模(effective size)近似结构洞
        # 对于所有节点，计算其邻居间的连接程度
        structural_holes = {}
        for node in self.graph.nodes():
            neighbors = list(self.graph.successors(node)) + list(self.graph.predecessors(node))
            if len(neighbors) < 2:
                structural_holes[node] = 0
                continue
            ego_net = self.graph.subgraph(set(neighbors))
            # 有效规模 = n - 2t/n，其中 n=邻居数，t=邻居间边数
            n = len(neighbors)
            t = ego_net.number_of_edges()
            effective_size = n - (2 * t / n) if n > 0 else 0
            structural_holes[node] = effective_size / n if n > 0 else 0
        return structural_holes
    
    def compute_chokepoint_score(self, node: str) -> dict:
        """
        计算单个节点的综合卡脖子评分
        
        评分公式:
        Chokepoint Score = 
            Betweenness * 0.30
            + CR1_Score * 0.25
            + Margin_Score * 0.20
            + Barrier_Score * 0.15
            + Supplier_Scarcity * 0.10
        
        Returns:
            dict with breakdown of scores
        """
        attrs = self.graph.nodes[node]
        betweenness = self.betweenness.get(node, 0)
        
        # CR1 评分
        cr1 = attrs.get("cr1", 0)
        cr1_score = self._interpolate_cr1(cr1)
        
        # 毛利率评分
        margin = attrs.get("gross_margin", 0)
        margin_score = self.margin_to_score(margin)
        
        # 技术壁垒评分
        barrier = attrs.get("barrier_level", "中")
        barrier_score = self.BARRIER_SCORE.get(barrier, 0.35)
        
        # 供应商稀缺度 (supplier_count越低越稀缺)
        suppliers = attrs.get("suppliers", 10)
        scarcity_score = 1.0 / (1.0 + math.log(suppliers + 1, 10))
        
        # 加权综合评分
        score = (
            betweenness * 0.30 +
            cr1_score * 0.25 +
            margin_score * 0.20 +
            barrier_score * 0.15 +
            scarcity_score * 0.10
        )
        
        return {
            "node": node,
            "tier": attrs.get("tier", "?"),
            "type": attrs.get("type", "未知"),
            "score": round(score, 4),
            "betweenness": round(betweenness, 4),
            "cr1": cr1,
            "cr1_score": round(cr1_score, 4),
            "gross_margin": margin,
            "margin_score": round(margin_score, 4),
            "barrier_level": barrier,
            "barrier_score": round(barrier_score, 4),
            "suppliers": suppliers,
            "scarcity_score": round(scarcity_score, 4),
            "rating": self._get_rating(score),
        }
    
    def _interpolate_cr1(self, cr1: int) -> float:
        """CR1 评分插值计算"""
        thresholds = sorted(self.CR1_SCORE.keys(), reverse=True)
        for t in thresholds:
            if cr1 >= t:
                return self.CR1_SCORE[t]
        return 0.0
    
    def _get_rating(self, score: float) -> str:
        """根据评分给出卡脖子等级"""
        if score >= 0.7:
            return "🔴 一级卡脖子（全球唯一/绝对垄断）"
        elif score >= 0.5:
            return "🟠 二级卡脖子（寡头垄断/极高壁垒）"
        elif score >= 0.3:
            return "🟡 三级卡脖子（集中度高/高壁垒）"
        elif score >= 0.15:
            return "🟢 四级关注（有一定垄断特征）"
        else:
            return "⚪ 常规环节（充分竞争）"
    
    def detect_chokepoints(self, top_n: int = None) -> list:
        """检测卡脖子环节，返回排序列表"""
        # 先计算介数中心性
        if self.betweenness is None:
            self.compute_betweenness()
        
        # 计算所有节点的评分
        results = []
        for node in self.graph.nodes():
            attrs = self.graph.nodes[node]
            # 跳过终端产品节点
            if attrs.get("tier", 1) == 0:
                continue
            result = self.compute_chokepoint_score(node)
            results.append(result)
        
        # 按评分降序排列
        results.sort(key=lambda x: x["score"], reverse=True)
        
        if top_n:
            results = results[:top_n]
        
        self.chokepoints = results
        return results
    
    def generate_report(self, industry_name: str = None) -> str:
        """生成卡脖子分析报告 (Markdown格式)"""
        if not self.chokepoints:
            self.detect_chokepoints()
        
        lines = []
        lines.append(f"# 🔍 产业链卡脖子环节深度分析报告")
        if industry_name:
            lines.append(f"\n> 研究行业: **{industry_name}**")
        lines.append(f"\n> 图谱规模: {self.graph.number_of_nodes()} 节点, {self.graph.number_of_edges()} 条依赖边")
        
        # 统计概览
        ratings = {}
        for cp in self.chokepoints:
            rating_key = cp["rating"][:2]
            ratings[rating_key] = ratings.get(rating_key, 0) + 1
        
        lines.append(f"\n## 📊 卡脖子环节分布")
        lines.append("")
        lines.append("| 等级 | 数量 | 说明 |")
        lines.append("|------|------|------|")
        for rk in ["🔴", "🟠", "🟡", "🟢", "⚪"]:
            if rk in ratings:
                rk_desc = {
                    "🔴": "一级·绝对垄断",
                    "🟠": "二级·寡头垄断", 
                    "🟡": "三级·高集中度",
                    "🟢": "四级·有特征",
                    "⚪": "常规竞争",
                }
                lines.append(f"| {rk} | {ratings[rk]} | {rk_desc.get(rk, '')} |")
        
        # Top 卡脖子环节详细分析
        lines.append(f"\n## 🎯 Top Ranking 卡脖子环节")
        lines.append("")
        
        for i, cp in enumerate(self.chokepoints[:15]):
            lines.append(f"### {i+1}. {cp['node']} — {cp['rating']}")
            lines.append("")
            lines.append(f"| 指标 | 数值 | 权重 | 得分 |")
            lines.append(f"|------|------|------|------|")
            lines.append(f"| 介数中心性 | {cp['betweenness']:.4f} | 30% | {cp['betweenness']*0.3:.4f} |")
            lines.append(f"| CR1 市占率 | {cp['cr1']}% | 25% | {cp['cr1_score']:.4f} |")
            lines.append(f"| 毛利率 | {cp['gross_margin']}% | 20% | {cp['margin_score']:.4f} |")
            lines.append(f"| 技术壁垒 | {cp['barrier_level']} | 15% | {cp['barrier_score']:.4f} |")
            lines.append(f"| 供应商数量 | {cp['suppliers']}家 | 10% | {cp['scarcity_score']:.4f} |")
            lines.append(f"| **综合评分** | **{cp['score']:.4f}** | | |")
            lines.append("")
            
            # 投资含义
            implications = []
            if cp["cr1"] >= 70:
                implications.append("⚠️ 近乎垄断的供应商结构，下游几乎没有议价能力")
            if cp["gross_margin"] >= 50:
                implications.append(f"💰 超高毛利率({cp['gross_margin']}%)表明极强的定价权")
            if cp["barrier_level"] == "极高":
                implications.append("🏰 极高的技术壁垒，新进入者几乎不可能")
            if cp["betweenness"] >= 0.1:
                implications.append("🔗 所有产业路径的必经节点，替代成本极高")
            
            if implications:
                lines.append("**投资含义:**")
                for imp in implications:
                    lines.append(f"- {imp}")
                lines.append("")
        
        return "\n".join(lines)
    
    def to_dict(self) -> list:
        """导出为字典列表"""
        if not self.chokepoints:
            self.detect_chokepoints()
        return self.chokepoints
    
    def save_report(self, path: str, industry_name: str = None):
        """保存报告到文件"""
        report = self.generate_report(industry_name)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(report)
        return path


def load_graph_from_json(path: str) -> nx.DiGraph:
    """从JSON文件加载图谱"""
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    G = nx.DiGraph()
    for node in data["nodes"]:
        nid = node.pop("id")
        G.add_node(nid, **node)
    for edge in data["edges"]:
        u = edge.pop("from")
        v = edge.pop("to")
        G.add_edge(u, v, **edge)
    
    return G


def main():
    import argparse
    parser = argparse.ArgumentParser(description="卡脖子环节识别引擎")
    parser.add_argument("--graph", help="依赖图谱JSON文件路径")
    parser.add_argument("--template", help="直接使用预设模板 (ai_gpu/humanoid_robot/evtol)")
    parser.add_argument("--top", type=int, default=15, help="返回Top N个卡脖子环节")
    parser.add_argument("--output", help="输出Markdown报告路径")
    parser.add_argument("--json", help="输出JSON结果路径")
    
    args = parser.parse_args()
    
    if args.template:
        # 从模板构建
        sys.path.insert(0, os.path.dirname(__file__))
        from build_dependency_graph import DependencyGraphBuilder
        builder = DependencyGraphBuilder()
        builder.build_from_template(args.template)
        G = builder.graph
    elif args.graph:
        G = load_graph_from_json(args.graph)
    else:
        print("请指定 --graph 或 --template 参数")
        sys.exit(1)
    
    detector = ChokepointDetector(G)
    chokepoints = detector.detect_chokepoints(args.top)
    
    # 输出到终端
    print("=" * 70)
    print("🔍 产业链卡脖子环节分析结果")
    print("=" * 70)
    print()
    for i, cp in enumerate(chokepoints):
        bar = "█" * int(cp["score"] * 20)
        print(f"{i+1:2d}. {cp['node']:<30s} {cp['rating']}")
        print(f"    评分: {cp['score']:.4f} {bar}")
        print(f"    介数: {cp['betweenness']:.4f} | CR1: {cp['cr1']}% | 毛利: {cp['gross_margin']}% | 壁垒: {cp['barrier_level']} | 供应商: {cp['suppliers']}家")
        print()
    
    # 保存报告
    if args.output:
        industry_name = args.template if args.template else "自定义产业链"
        detector.save_report(args.output, industry_name)
        print(f"✅ 报告已保存到: {args.output}")
    
    # 保存JSON
    if args.json:
        with open(args.json, 'w', encoding='utf-8') as f:
            json.dump(chokepoints, f, ensure_ascii=False, indent=2)
        print(f"✅ JSON结果已保存到: {args.json}")


if __name__ == "__main__":
    import os
    main()