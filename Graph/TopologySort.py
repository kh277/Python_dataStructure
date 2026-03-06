# Topology Sort - O(V+E)

'''
(1-base 정점)
간선 정보가 주어질 때, 위상 정렬한 결과 반환
'''

from collections import deque


def TopologySort(V, edge):
    # 간선 정보 전처리 및 진입 차수 설정
    graph = [[] for _ in range(V+1)]
    inDegree = [0 for _ in range(V+1)]      # 진입 차수 저장
    for i in edge:
        graph[i[0]].append(i[1])
        inDegree[i[1]] += 1

    result = []
    q = deque()

    # 진입차수가 0인 정점 큐에 삽입
    for curV in range(1, V+1):
        if inDegree[curV] == 0:
            q.append(curV)

    # 큐가 빌 때까지 반복
    while q:
        curV = q.popleft()
        result.append(curV)

        # cur과 직접 연결된 노드들의 진입차수 1씩 감소
        for nextV in graph[curV]:
            inDegree[nextV] -= 1

            # 진입차수가 0인 정점만 큐에 삽입
            if inDegree[nextV] == 0:
                q.append(nextV)

    return result
