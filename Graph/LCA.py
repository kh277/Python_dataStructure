# LCA - O(logN)

'''
(1-base 정점)
두 정점의 LCA(최소 공통 조상)을 logN에 구함
'''

class LCA():
    def __init__(self, N, graph, root):
        self.N = N
        self.LOG = N.bit_length()
        self.graph = graph
        self.depth = [0] * (N+1)
        self.DP = [[0] * self.LOG for _ in range(N+1)]

        self.DFS(root)
        self.calDP()


    # 각 정점별 depth 계산
    def DFS(self, root):
        visited = [0] * (self.N+1)

        stack = []
        stack.append([root, 0])
        self.depth[root] = 0
        visited[root] = 1

        while stack:
            curV, curDepth = stack.pop()

            for nextV in self.graph[curV]:
                if visited[nextV] == 0:
                    self.DP[nextV][0] = curV
                    self.depth[nextV] = curDepth+1
                    visited[nextV] ^= 1
                    stack.append([nextV, curDepth+1])


    # DP 테이블 채우기
    def calDP(self):
        for x in range(1, self.LOG):
            for y in range(1, self.N+1):
                self.DP[y][x] = self.DP[self.DP[y][x-1]][x-1]


    # LCA 계산
    def LCA(self, startV, endV):
        if self.depth[startV] < self.depth[endV]:
            startV, endV = endV, startV

        gap = self.depth[startV] - self.depth[endV]
        index = 0
        while gap:
            if gap & 1:
                startV = self.DP[startV][index]
            gap >>= 1
            index += 1

        if startV == endV:
            return startV

        for i in range(self.LOG-1, -1, -1):
            if self.DP[startV][i] != self.DP[endV][i]:
                startV = self.DP[startV][i]
                endV = self.DP[endV][i]

        return self.DP[startV][0]
