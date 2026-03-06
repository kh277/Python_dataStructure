# Floyd-Warshall - O(V^3)

'''
(1-base 정점)
정점 간 거리가 저장된 인접 행렬이 주어질 때, 모든 정점 간 최단 거리 구하기
'''

INF = 10**8

def FloydWarshall(V, graph):
    # 자신으로의 거리는 0 처리
    for curV in range(1, V+1):
        graph[curV][curV] = 0

    # start -> end로 갈 때, mid를 거쳐 가는 것이 더 효율적인지 판단
    for midV in range(1, V+1):
        for startV in range(1, V+1):
            for endV in range(1, V+1):
                graph[startV][endV] = min(graph[startV][endV], graph[startV][midV] + graph[midV][endV])

    # 간선 정보가 INF인 값은 -1로 변환
    for startV in range(V+1):
        for endV in range(V+1):
            if graph[startV][endV] == INF:
                graph[startV][endV] = -1

    # 0번 정점은 제외하고 출력
    return [graph[i][1:] for i in range(1, V+1)]