# NetworkX 产业链图算法参考手册

## 核心概念

产业链依赖图 = 有向无环图 (DAG)：
- **节点 (Node)**：产品、零部件、材料、工艺
- **边 (Edge)**：A → B 表示 A 依赖 B（B 是 A 的供应商/上游）
- **方向**：从终端产品（下游）指向原材料/设备（上游）

```
AI服务器 → GPU → EUV光刻 → ASML光刻机 → 蔡司光学镜头
                                    → 光源系统
                  → TSMC 5nm晶圆 → 光刻胶
```

## 1. 介数中心性 (Betweenness Centrality)

### 数学定义

```
BC(v) = Σ_{s≠v≠t} σ_st(v) / σ_st
```

其中 σ_st 是从节点 s 到节点 t 的最短路径总数，σ_st(v) 是通过节点 v 的路径数。

### 产业链含义

- **高BC值** = 几乎所有依赖路径都经过这个节点
- ASML（全球唯一EUV光刻机）在所有涉及先进制程的产业链中BC值都极高
- 如果删掉BC=0.5的节点，50%的依赖路径会断裂

### 代码示例

```python
import networkx as nx

G = nx.DiGraph()
# ... 构建图谱 ...

# 有向图的介数中心性
bc = nx.betweenness_centrality(G)

# 标准化到 [0, 1] 区间
sorted_nodes = sorted(bc.items(), key=lambda x: x[1], reverse=True)

# 找出top 5 "咽喉要道"
for node, score in sorted_nodes[:5]:
    print(f"🔴 {node}: BC = {score:.4f}")
```

### 阈值参考

| BC值 | 含义 | 投资建议 |
|------|------|----------|
| > 0.3 | 极度集中，所有路径必经 | 🔴 必须研究，寻找替代方案 |
| 0.1-0.3 | 高度依赖 | 🟠 核心关注 |
| 0.01-0.1 | 替代路径存在但不多 | 🟡 关注 |
| < 0.01 | 去中心化，竞争充分 | ⚪ 不追踪 |

## 2. 结构洞 (Structural Holes)

### 概念

结构洞理论（Ronald Burt）：节点在网络中连接两个或多个互相不连接的分支时，该节点拥有信息优势和控制权。

### 计算方法：有效规模 (Effective Size)

```python
def structural_holes(G, node):
    """
    计算节点的有效规模（结构洞代理指标）
    
    原理: 如果该节点的邻居之间没有连接，
         则该节点对邻居有更大的控制力
    """
    neighbors = set(G.successors(node)) | set(G.predecessors(node))
    n = len(neighbors)
    
    if n < 2:
        return 0
    
    # 计算邻居子图中边的数量
    sub = G.subgraph(neighbors)
    t = sub.number_of_edges()
    
    # 有效规模 = n - 平均冗余度
    # 邻居间连接越多 → 冗余越高 → 有效规模越小
    effective_size = n - (2 * t / n) if n > 0 else 0
    
    # 标准化
    return effective_size / n if n > 0 else 0
```

### 产业链含义

- 高结构洞 = 作为"独木桥"连接上下游
- 例如：CoWoS封装连接GPU芯片和HBM内存，结构洞值极高
- 结构洞越高的节点，越能掌握上下游的命门

## 3. PageRank

### 产业链应用

PageRank不仅考虑"谁被依赖"，还考虑"被谁依赖"——被重要节点依赖的节点更重要。

```python
pr = nx.pagerank(G, alpha=0.85)

# 加入卡脖子评分的PageRank加权版本
# 被高CR1节点依赖 → 更高权重
personalization = {n: G.nodes[n].get('cr1', 0) / 100 for n in G.nodes}
pr_weighted = nx.pagerank(G, alpha=0.85, personalization=personalization)
```

## 4. 反向路径查询

### 从终端产品反向追溯

```python
def reverse_drill(G, start_node, max_depth=4):
    """
    从终端产品出发，反向追溯所有上游依赖
    
    返回: {层级: [上游节点列表]}
    """
    visited = {start_node: 0}
    layers = {0: [start_node]}
    queue = [(start_node, 0)]
    
    while queue and queue[0][1] < max_depth:
        node, depth = queue.pop(0)
        next_depth = depth + 1
        
        for parent in G.predecessors(node):
            if parent not in visited:
                visited[parent] = next_depth
                if next_depth not in layers:
                    layers[next_depth] = []
                layers[next_depth].append(parent)
                queue.append((parent, next_depth))
    
    return layers
```

## 5. 卡脖子综合评分公式

```python
def chokepoint_score(G, node):
    """
    综合评分 = 多维度加权
    
    Formula:
    score = BC * 0.30 + CR1 * 0.25 + Margin * 0.20 + Barrier * 0.15 + Scarcity * 0.10
    """
    attrs = G.nodes[node]
    
    # 介数中心性 (0-1)
    bc = nx.betweenness_centrality(G).get(node, 0)
    
    # CR1 评分 (0-1)
    cr1 = attrs.get('cr1', 0) / 100.0
    
    # 毛利率评分 (0-1)，用max(70%, ...)做上限
    margin = min(attrs.get('gross_margin', 0) / 70.0, 1.0)
    
    # 技术壁垒评分
    barrier_map = {'极高': 1.0, '高': 0.65, '中': 0.35, '低': 0.1}
    barrier = barrier_map.get(attrs.get('barrier_level', '中'), 0.35)
    
    # 供应商稀缺度 (0-1)，suppliers越少越稀缺
    suppliers = attrs.get('suppliers', 5)
    scarcity = 1.0 / max(suppliers, 1)
    
    return (
        bc * 0.30 +
        cr1 * 0.25 +
        margin * 0.20 +
        barrier * 0.15 +
        scarcity * 0.10
    )
```

## 6. 批量分析示例

```python
# 一个完整的产业链分析pipeline
from build_dependency_graph import DependencyGraphBuilder
from find_chokepoints import ChokepointDetector

# 1. 构建图谱
builder = DependencyGraphBuilder()
builder.build_from_template('ai_gpu')

# 2. 检测卡脖子
detector = ChokepointDetector(builder.graph)
detector.compute_betweenness()  # 计算介数中心性
detector.compute_pagerank()     # 计算PageRank

# 3. 综合评分
results = detector.detect_chokepoints(top_n=10)

# 4. 可视化输出
for cp in results:
    print(f"{cp['node']}: {cp['score']:.4f} ({cp['rating']})")
```