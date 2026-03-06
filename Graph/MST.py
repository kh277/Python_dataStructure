# Minimum Spanning Tree (Kruskal) - O(ElogE)

'''
(1-base 정점)
간선 정보가 주어질 때, 가장 적은 비용으로 모든 정점을 연결하는 트리 및 비용 반환
'''

# x의 루트 정점을 탐색
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])

    return parent[x]


# a 트리와 b 트리 병합
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    parent[max(a, b)] = min(a, b)


def Kruskal(V, graph):
    totalCost = 0
    resultGraph = []

    # 부모 정점 초기화
    parent = [i for i in range(V+1)]

    # [startV, endV, cost] 순서에서 cost 기준으로 정렬
    graph.sort(key= lambda x: x[2])

    # 그리디하게 간선 선택
    for cur in graph:
        startV, endV, cost = cur
        if find(parent, startV) != find(parent, endV):
            union(parent, startV, endV)
            totalCost += cost
            resultGraph.append(cur)

    return totalCost, resultGraph
