# Segment Tree (비재귀 구현)

'''
점 업데이트, 구간 쿼리를 O(logN)에 처리하기 위한 자료구조

build() : 배열 A를 기반으로 세그먼트 트리 생성, O(N)
update() : A의 i번째 원소값 수정 및 전파, O(logN)
query() : 구간 [l, r]의 총합 도출, O(logN)
'''

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
