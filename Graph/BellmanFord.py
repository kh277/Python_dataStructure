# Bellman-Ford - O(VE)

'''
(1-base 정점)
간선 정보가 주어질 때, 한 정점에서 다른 모든 정점까지의 최단 거리 반환.
음수 간선이 섞여도 사용 가능
'''

INF = 1000000000


def BellmanFord(V, E, edge, start):
    DP = [INF for _ in range(V+1)]
    DP[start] = 0

    for i in range(V):
        for j in range(E):
            curStart, curEnd, curDist = edge[j]

            # curEnd까지 거리 갱신이 가능한 경우
            if DP[curStart] != INF:
                DP[curEnd] = min(DP[curEnd], DP[curStart] + curDist)

                # 마지막 정점에 대해서도 갱신 -> 음수 순환이 존재하는 그래프
                if i == V-1:
                    return [-1]

    return DP[1:]
