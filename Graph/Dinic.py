# Maximum Flow - Dinic 알고리즘 O(V^2 * E)

'''
Dinic의 DFS 부분을 non-recur 방식으로 구현했더니 더 느려졌음.
'''

from collections import deque
INF = 10000000


class Dinic:
    def __init__(self, size, source, sink):
        self.V = size
        self.graph = [[] for _ in range(size)]
        self.level = [-1] * size
        self.pointer = [0] * size
        self.source = source
        self.sink = sink


    def addEdge(self, start, end, cap, directed=True):
        self.graph[start].append([end, cap, len(self.graph[end])])
        self.graph[end].append([start, 0 if directed else cap, len(self.graph[start])-1])


    def BFS(self):
        level = [-1] * self.V
        level[self.source] = 0
        q = deque([self.source])

        while q:
            curV = q.popleft()
            for nextV, cap, _ in self.graph[curV]:
                if level[nextV] == -1 and cap > 0:
                    level[nextV] = level[curV] + 1
                    q.append(nextV)
        self.level = level

        return level[self.sink] != -1


    def DFS(self, curV, total):
        if curV == self.sink:
            return total

        while self.pointer[curV] < len(self.graph[curV]):
            i = self.pointer[curV]
            nextV, cap, revV = self.graph[curV][i]

            if self.level[nextV] == self.level[curV] + 1 and cap > 0:
                curFlow = self.DFS(nextV, min(total, cap))
                if curFlow > 0:
                    self.graph[curV][i][1] -= curFlow
                    self.graph[nextV][revV][1] += curFlow
                    return curFlow
            self.pointer[curV] += 1

        return 0


    def maxFlow(self):
        if self.source == -1 or self.sink == -1:
            return -1

        result = 0
        while self.BFS():
            self.pointer = [0] * self.V
            while True:
                curFlow = self.DFS(self.source, INF)
                if curFlow == 0:
                    break
                result += curFlow

        return result
