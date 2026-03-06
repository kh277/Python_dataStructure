# Segment Tree (비재귀 구현)

from array import array
ARRAY_TYPE = 'i'


# 크기가 N인 세그먼트 트리 빌드
def build(N, A):
    tree = array(ARRAY_TYPE, [0]) * (N*2)
    for i in range(len(A)):
        tree[N+i] = A[i]

    for i in range(N-1, 0, -1):
        tree[i] = tree[i<<1] + tree[i<<1 | 1]

    return tree


# index번째 값을 value로 변경
def update(N, tree, index, value):
    index += N
    tree[index] = value
    
    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1]


# 0-base, 구간 [left, right]의 전체 합을 구하는 쿼리
def query(N, tree, left, right):
    result = 0
    left += N
    right += N

    while left <= right:
        if left & 1:
            result += tree[left]
            left += 1
        if ~right & 1:
            result += tree[right]
            right -= 1
        left >>= 1
        right >>= 1

    return result
