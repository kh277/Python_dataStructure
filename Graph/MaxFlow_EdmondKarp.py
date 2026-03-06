# Network Flow (Edmond-Karp) - O(V * E^2)

'''
유량 정보 capacity가 주어질 때, source -> sink로 가는 최대 유량 반환
'''

from collections import deque
INF = 1000000000


def BFS(capacity, source, sink, parent):
    visited = [False for _ in range(len(capacity))]

    q = deque([source])
    visited[source] = True

    while q:
        curV = q.popleft()

        for nextV in range(len(capacity)):
            # 용량이 남은 간선이 있는 경우
            if visited[nextV] == False and capacity[curV][nextV] > 0:
                q.append(nextV)
                visited[nextV] = True
                parent[nextV] = curV
                
                # sink에 도착할 경우
                if nextV == sink:
                    return True

    return False


def NetworkFlow(capacity, source, sink):
    parent = [-1 for _ in range(len(capacity))]
    maxFlow = 0
    
    # BFS로 증가 경로 탐색
    while BFS(capacity, source, sink, parent):
        # 증가 경로의 최소 용량 탐색
        pathFlow = INF
        s = sink
        while s != source:
            pathFlow = min(pathFlow, capacity[parent[s]][s])
            s = parent[s]

        # 경로에 따라 용량 업데이트
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= pathFlow
            capacity[v][u] += pathFlow
            v = parent[v]
        
        maxFlow += pathFlow

    return maxFlow