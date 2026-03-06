# Strongly Connected Component (Tarjan's algothihm) - O(V+E)

'''
(1-base 정점)
간선 정보가 주어질 때, SCC를 이루는 점들끼리 리스트로 묶어 반환

구현체는 아래 링크를 참조했음
https://stackoverflow.com/questions/46511682/non-recursive-version-of-tarjans-algorithm
'''


def SCC(V, edge):
    # 간선 전처리
    graph = [[] for _ in range(V+1)]
    for s, e in edge:
        graph[s].append(e)

    result = []
    stack = []
    low = dict()
    callStack = []

    for curV in range(len(graph)):
        callStack.append((curV, 0, len(low)))

        # DFS 처리
        while callStack:
            curV, pi, num = callStack.pop()

            # 노드를 처음 방문하는 경우
            if pi == 0:
                if curV in low:
                    continue
                low[curV] = num
                stack.append(curV)
            
            # 재방문한 경우
            if pi > 0:
                low[curV] = min(low[curV], low[graph[curV][pi-1]])
            
            # 인접 노드 처리
            if pi < len(graph[curV]):
                callStack.append((curV, pi+1, num))
                callStack.append((graph[curV][pi], 0, len(low)))
                continue

            # 모든 인접 노드 처리가 끝난 경우
            if num == low[curV]:
                comp = []
                while True:
                    comp.append(stack.pop())
                    low[comp[-1]] = len(graph)
                    if comp[-1] == curV:
                        break
                result.append(comp)

    # 0번 정점 SCC 제외
    return result[1:]
