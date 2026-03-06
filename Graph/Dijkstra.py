# Dijkstra - O((V+E)logV)

'''
(1-base 정점)
간선 정보가 주어질 때, 한 정점에서 다른 모든 정점까지의 최단 거리 반환.
음수 간선이 섞인 경우 사용 불가
'''

import heapq
INF = 10**8


def Dijkstra(V, edge, start):
    # 간선 정보 전처리
    graph = [[] for _ in range(V+1)]
    for startV, endV, cost in edge:
        graph[startV].append([endV, cost])

    distance = [INF for _ in range(V+1)]

    # 시작 정점 처리
    pq = []     # (시작 정점으로부터의 거리, 목표 정점) 형태로 저장
    distance[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        curDist, curV = heapq.heappop(pq)

        # 갱신할 필요가 없는 경우 (저장된 비용 < 계산한 비용)
        if distance[curV] < curDist:
            continue

        # 현재 탐색한 정점과 이어전 간선들에 대해서
        for nextV, tempDist in graph[curV]:
            nextDist = curDist + tempDist

            # 갱신이 가능한 경우 (저장된 비용 > 계산한 비용)
            if nextDist < distance[nextV]:
                distance[nextV] = nextDist
                heapq.heappush(pq, (nextDist, nextV))

    return distance[1:]