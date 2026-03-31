# Segment Tree on walk (세그먼트 트리 + 이분 탐색)

'''
세그먼트 트리에 이분 탐색을 적용해 앞에서부터 k번째 원소를 O(logN)에 구하는 자료구조.
kth()를 사용하기 위해서는 세그먼트 트리의 size가 반드시 2의 제곱수여야 함.

build() : 배열 A를 기반으로 세그먼트 트리 생성, O(N)
update() : 세그먼트 트리를 이용해 배열의 특정 인덱스에 값 추가/제거, O(logN)
query() : 세그먼트 트리를 이용해 배열의 [l, r] 구간에 존재하는 원소의 개수 반환, O(logN)
kth() : 세그먼트 트리를 이용해 배열의 앞에서부터 k번째에 존재하는 원소의 인덱스 반환, O(logN)
'''

from array import array


def build(N, size):
    tree = array('i', [0]) * (2*size)

    for i in range(size+1, size+N+1):
        tree[i] = 1
    for i in range(size-1, 0, -1):
        tree[i] = tree[i<<1] + tree[i<<1 | 1]

    return tree


def update(N, tree, index, value):
    index += N
    tree[index] = value

    while index > 1:
        index >>= 1
        tree[index] = tree[index<<1] + tree[index<<1 | 1]


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


def kth(N, tree, k):
    index = 1

    while index < N:
        left = index<<1
        if tree[left] >= k:
            index = left
        else:
            k -= tree[left]
            index = left | 1

    return index - N
