#!/usr/bin/env python3
"""
产业链依赖图谱构建器 (Industrial Chain Dependency Graph Builder)

从产品/行业输入出发，构建多层级物料依赖关系图谱。
支持从顶层产品 → 核心组件 → 关键零部件 → 原材料/卡脖子环节的反向追溯。

用法:
  python3 build_dependency_graph.py --product "NVIDIA H100 GPU" --depth 4
  python3 build_dependency_graph.py --industry "AI芯片" --output graph.json
"""

import json
import sys
import os

try:
    import networkx as nx
except ImportError:
    print("⚠️ networkx 未安装，运行: pip install networkx")
    sys.exit(1)


class DependencyGraphBuilder:
    """
    产业链依赖图谱构建器
    
    核心概念：
    - Node: 产品 / 组件 / 原材料
    - Edge: A → B 表示 A 依赖 B（B 是 A 的上游）
    - Node属性: tier (层级), market_share (市占率), gross_margin (毛利率),
                supplier_count (全球供应商数量), barrier (技术壁垒评级)
    """
    
    # 预置的科技硬件产业链模板数据
    # 这些是典型产业链结构，实际使用时会被实时搜索数据覆盖
    TEMPLATES = {
        "ai_gpu": {
            "name": "AI GPU 产业链",
            "root": "AI加速卡 (H100/B200)",
            "layers": [
                {  # Layer 1: 核心组件
                    "GPU芯片": {"suppliers": 2, "cr1": 80, "margin": 75, "barrier": "极高"},
                    "HBM3e高带宽内存": {"suppliers": 3, "cr1": 50, "margin": 55, "barrier": "极高"},
                    "CoWoS先进封装": {"suppliers": 1, "cr1": 95, "margin": 53, "barrier": "极高"},
                    "光模块/互联": {"suppliers": 5, "cr1": 30, "margin": 40, "barrier": "高"},
                },
                {  # Layer 2: GPU芯片 → 关键制程
                    "GPU芯片→5nm/3nm晶圆": {"suppliers": 2, "cr1": 60, "margin": 50, "barrier": "极高"},
                    "GPU芯片→EUV光刻": {"suppliers": 1, "cr1": 100, "margin": 52, "barrier": "极高"},
                    "GPU芯片→芯片设计IP": {"suppliers": 3, "cr1": 55, "margin": 95, "barrier": "高"},
                    "HBM3e→TSV硅通孔": {"suppliers": 3, "cr1": 45, "margin": 50, "barrier": "极高"},
                    "HBM3e→堆叠键合": {"suppliers": 2, "cr1": 60, "margin": 45, "barrier": "极高"},
                    "CoWoS→中介层(Interposer)": {"suppliers": 3, "cr1": 55, "margin": 42, "barrier": "极高"},
                },
                {  # Layer 3: 关键制程 → 核心材料
                    "5nm/3nm晶圆→高纯度硅片": {"suppliers": 3, "cr1": 50, "margin": 40, "barrier": "高"},
                    "5nm/3nm晶圆→光刻胶": {"suppliers": 2, "cr1": 60, "margin": 60, "barrier": "极高"},
                    "5nm/3nm晶圆→CMP抛光液": {"suppliers": 3, "cr1": 45, "margin": 45, "barrier": "高"},
                    "EUV光刻→光源系统": {"suppliers": 1, "cr1": 100, "margin": 55, "barrier": "极高"},
                    "EUV光刻→光学镜头组": {"suppliers": 2, "cr1": 65, "margin": 50, "barrier": "极高"},
                    "CoWoS→特种高频覆铜板(CCL)": {"suppliers": 3, "cr1": 50, "margin": 40, "barrier": "极高"},
                },
                {  # Layer 4: 核心材料 → 卡脖子环节
                    "光刻胶→光敏树脂": {"suppliers": 2, "cr1": 70, "margin": 65, "barrier": "极高"},
                    "光刻胶→光引发剂": {"suppliers": 2, "cr1": 55, "margin": 60, "barrier": "极高"},
                    "特种高频覆铜板→低损耗树脂": {"suppliers": 2, "cr1": 60, "margin": 55, "barrier": "极高"},
                    "特种高频覆铜板→玻璃纤维布": {"suppliers": 3, "cr1": 50, "margin": 35, "barrier": "高"},
                    "CMP抛光液→纳米磨料": {"suppliers": 2, "cr1": 55, "margin": 50, "barrier": "极高"},
                },
            ]
        },
        "humanoid_robot": {
            "name": "人形机器人产业链",
            "root": "人形机器人整机",
            "layers": [
                {
                    "谐波减速器/RV减速器": {"suppliers": 3, "cr1": 50, "margin": 45, "barrier": "极高"},
                    "空心杯电机": {"suppliers": 3, "cr1": 45, "margin": 40, "barrier": "高"},
                    "力矩传感器/六维力传感器": {"suppliers": 3, "cr1": 50, "margin": 55, "barrier": "极高"},
                    "AI推理芯片": {"suppliers": 3, "cr1": 45, "margin": 65, "barrier": "极高"},
                    "行星滚柱丝杠": {"suppliers": 2, "cr1": 55, "margin": 40, "barrier": "极高"},
                },
                {
                    "谐波减速器→柔性轴承": {"suppliers": 2, "cr1": 60, "margin": 50, "barrier": "极高"},
                    "谐波减速器→刚轮/柔轮精密加工": {"suppliers": 3, "cr1": 40, "margin": 35, "barrier": "高"},
                    "空心杯电机→高性能磁钢": {"suppliers": 3, "cr1": 45, "margin": 45, "barrier": "高"},
                    "力矩传感器→弹性体精密加工": {"suppliers": 2, "cr1": 55, "margin": 50, "barrier": "极高"},
                    "行星滚柱丝杠→高精度螺纹磨削": {"suppliers": 2, "cr1": 60, "margin": 45, "barrier": "极高"},
                },
            ]
        },
        "evtol": {
            "name": "低空经济/飞行汽车产业链",
            "root": "eVTOL飞行器整机",
            "layers": [
                {
                    "固态/半固态电池": {"suppliers": 5, "cr1": 25, "margin": 40, "barrier": "极高"},
                    "高功率密度电机": {"suppliers": 5, "cr1": 25, "margin": 35, "barrier": "高"},
                    "碳纤维复合材料结构件": {"suppliers": 5, "cr1": 30, "margin": 45, "barrier": "高"},
                    "飞控系统/航电": {"suppliers": 5, "cr1": 30, "margin": 55, "barrier": "极高"},
                },
                {
                    "固态电池→固态电解质": {"suppliers": 5, "cr1": 20, "margin": 50, "barrier": "极高"},
                    "固态电池→锂金属负极": {"suppliers": 3, "cr1": 40, "margin": 40, "barrier": "极高"},
                    "碳纤维复合材料→T1000级碳纤维": {"suppliers": 3, "cr1": 50, "margin": 45, "barrier": "极高"},
                    "碳纤维复合材料→特种树脂基体": {"suppliers": 3, "cr1": 45, "margin": 40, "barrier": "高"},
                },
            ]
        }
    }
    
    def __init__(self, industry_template: str = None):
        """
        初始化图谱构建器
        
        Args:
            industry_template: 预设行业模板名称 ('ai_gpu', 'humanoid_robot', 'evtol')
                              如果为 None，则构建自定义图谱
        """
        self.graph = nx.DiGraph()
        self.industry_template = industry_template
        self.analysis_results = {}
        
    def build_from_template(self, template_name: str) -> nx.DiGraph:
        """从预设模板构建依赖图谱"""
        template = self.TEMPLATES.get(template_name)
        if not template:
            raise ValueError(f"未知模板: {template_name}，可用: {list(self.TEMPLATES.keys())}")
        
        root = template["root"]
        self.graph.add_node(root, tier=0, type="终端产品")
        
        for layer_idx, layer in enumerate(template["layers"]):
            tier = layer_idx + 1
            for node_name, attrs in layer.items():
                # 解析 "A→B" 格式的上游关系
                if "→" in node_name:
                    parent, child = node_name.split("→", 1)
                    parent = parent.strip()
                    child = child.strip()
                    self.graph.add_node(child, 
                                       tier=tier,
                                       type="卡脖子环节" if tier >= 3 else ("核心零部件" if tier == 1 else "关键材料"),
                                       suppliers=attrs["suppliers"],
                                       cr1=attrs["cr1"],
                                       gross_margin=attrs["margin"],
                                       barrier_level=attrs["barrier"])
                    self.graph.add_edge(parent, child, relation="depends_on")
                    
                    # 连接父节点到根节点(如果父节点还不存在)
                    if parent not in self.graph:
                        self.graph.add_node(parent, tier=tier-1, type="核心组件")
                        # 尝试找到父节点的父节点
                        # 通过已添加的边来追溯
                else:
                    self.graph.add_node(node_name,
                                       tier=tier,
                                       type="核心组件",
                                       suppliers=attrs["suppliers"],
                                       cr1=attrs["cr1"],
                                       gross_margin=attrs["margin"],
                                       barrier_level=attrs["barrier"])
                    self.graph.add_edge(root, node_name, relation="depends_on")
        
        return self.graph
    
    def add_dependency_chain(self, chain: list):
        """
        手动添加依赖链
        例: add_dependency_chain(["AI服务器", "GPU", "CoWoS封装", "中介层", "覆铜板"])
        """
        for i in range(len(chain) - 1):
            parent = chain[i]
            child = chain[i + 1]
            if parent not in self.graph:
                self.graph.add_node(parent, tier=i, type="未知")
            if child not in self.graph:
                self.graph.add_node(child, tier=i+1, type="未知")
            self.graph.add_edge(parent, child, relation="depends_on")
    
    def set_node_attrs(self, node: str, **attrs):
        """设置节点属性（市占率、毛利率等）"""
        if node in self.graph:
            for k, v in attrs.items():
                self.graph.nodes[node][k] = v
    
    def to_dict(self) -> dict:
        """导出图谱为字典"""
        return {
            "nodes": [
                {"id": n, **self.graph.nodes[n]}
                for n in self.graph.nodes
            ],
            "edges": [
                {"from": u, "to": v, **self.graph.edges[u, v]}
                for u, v in self.graph.edges
            ]
        }
    
    def save(self, path: str):
        """保存图谱到JSON文件"""
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=2)
    
    def load(self, path: str):
        """从JSON文件加载图谱"""
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.graph = nx.DiGraph()
        for node in data["nodes"]:
            nid = node.pop("id")
            self.graph.add_node(nid, **node)
        for edge in data["edges"]:
            u = edge.pop("from")
            v = edge.pop("to")
            self.graph.add_edge(u, v, **edge)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="产业链依赖图谱构建器")
    parser.add_argument("--template", choices=list(DependencyGraphBuilder.TEMPLATES.keys()),
                       help="使用预设行业模板")
    parser.add_argument("--output", default="dependency_graph.json", help="输出JSON文件路径")
    parser.add_argument("--info", action="store_true", help="显示图谱统计信息")
    
    args = parser.parse_args()
    
    builder = DependencyGraphBuilder()
    
    if args.template:
        builder.build_from_template(args.template)
        builder.save(args.output)
        print(f"✅ 已构建 {builder.TEMPLATES[args.template]['name']}")
        print(f"   节点数: {builder.graph.number_of_nodes()}")
        print(f"   依赖边数: {builder.graph.number_of_edges()}")
        print(f"   已保存到: {args.output}")
    else:
        # 交互式构建
        print("=" * 60)
        print("产业链依赖图谱构建器 (Chokepoint Driller)")
        print("=" * 60)
        print("\n可用模板:", ", ".join(DependencyGraphBuilder.TEMPLATES.keys()))
        print("\n用法: python3 build_dependency_graph.py --template ai_gpu")
        print("\n自定义构建请通过Python API调用")


if __name__ == "__main__":
    main()
