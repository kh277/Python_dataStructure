# 금광세그 (연속합 세그)

'''
각 노드는 [구간의 왼쪽 접두사 포함 최대 연속합, 구간의 오른쪽 접미사 포함 최대 연속합,
    구간 내 최대 연속합, 구간 내 총합] 저장.
'''

import io

input = io.BufferedReader(io.FileIO(0), 1<<18).readline
INF = 10**9


class Node:
    def __init__(self, preMax=0, sufMax=0, totMax=0, total=0):
        self.preMax = preMax
        self.sufMax = sufMax
        self.totMax = totMax
        self.total = total
    
    def addAll(self, value):
        self.preMax += value
        self.sufMax += value
        self.totMax += value
        self.total += value


# L노드 + R노드에서 최대 연속합 노드 처리 
def combine(L, R):
    return Node(max(L.preMax, L.total+R.preMax),
                max(R.sufMax, L.sufMax+R.total),
                max(L.totMax, R.totMax, L.sufMax+R.preMax),
                L.total+R.total)


# 세그먼트 트리 빌드
def build(N, A):
    tree = [Node() for _ in range(N*2)]
    for i in range(len(A)):
        tree[N+i].addAll(A[i])

    for i in range(N-1, 0, -1):
        tree[i] = combine(tree[i<<1], tree[i<<1 | 1])

    return tree


# 구간 [left, right]에서 가장 큰 연속합 출력
def query(N, tree, left, right):
    L = Node(-INF, -INF, -INF, 0)
    R = Node(-INF, -INF, -INF, 0)
    left += N
    right += N

    while left <= right:
        if left & 1:
            L = combine(L, tree[left])
            left += 1
        if ~right & 1:
            R = combine(tree[right], R)
            right -= 1

        left >>= 1
        right >>= 1

    return combine(L, R).totMax


# index번째 노드에 값 추가 및 노드 갱신
def update(N, tree, index, value):
    index += N
    tree[index].addAll(value)

    while index > 1:
        index >>= 1
        tree[index] = combine(tree[index<<1], tree[index<<1 | 1])


def main():
    N = int(input())
    treeSize = 1<<(N+1).bit_length
    A = list(map(int, input().split()))

    # 세그먼트 트리 기본 설정
    tree = build(treeSize, A)

    # 쿼리 처리
    pass


main()
