# Bipartite Matching (Ford-Fulkerson) - O(VE)

'''
(1-base 정점)
[시작 정점 번호, 끝 정점 번호] 형태의 간선 정보가 주어지고,
A그룹의 정점과 B그룹의 정점을 1개 매칭할 수 있다고 할 때, 생성할 수 있는 최대 이분 매칭의 수
'''

# B에서 curV과 연결될 수 있는지 여부 체크
def DFS(curV, graph, visited, matchB):
    for nextV in graph[curV]:
        if visited[nextV] == True:
            continue
        visited[nextV] = True

        # nextV가 매칭되지 않았거나, 다른 정점과 매칭시킬 수 있다면 -> 연결
        if matchB[nextV] == 0 or DFS(matchB[nextV], graph, visited, matchB):
            matchB[nextV] = curV
            return True

    return False


def Ford_Fulkerson(numA, numB, edge):
    # 간선 정보 전처리
    graph = [[] for _ in range(numA+1)]
    for curS, curE in edge:
        graph[curS].append(curE)

    matchB = [0 for _ in range(numB+1)]
    result = 0

    for curV in range(1, numA+1):
        if DFS(curV, graph, [False for _ in range(numB+1)], matchB):
            result += 1

    return result
