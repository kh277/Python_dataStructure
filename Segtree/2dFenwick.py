# 2D Fenwick Tree

'''
펜윅 트리는 구간 합, 점 업데이트 쿼리를 O((logN)^2)에 처리할 수 있는 자료구조임.

build - O(YX)
update - O(logY * logX)
query - O(logY * logX)
'''

from array import array


# Y*X 크기의 arr을 기반으로 2D Fenwick Tree 생성
def build(Y, X, arr):
    tree = [array('i', [0]) * (X+1) for _ in range(Y+1)]

    for y in range(1, Y+1):
        for x in range(1, X+1):
            tree[y][x] = arr[y-1][x-1]
    for y in range(1, Y+1):
        for x in range(1, X+1):
            nextX = x + (x & -x)
            if nextX <= X:
                tree[y][nextX] += tree[y][x]
    for y in range(1, Y+1):
        nextY = y + (y & -y)
        if nextY <= Y:
            for x in range(1, X+1):
                tree[nextY][x] += tree[y][x]

    return tree


# Y*X 크기의 tree에서 [tY][tX] 위치의 값에 diff 더하기
def update(Y, X, tree, tY, tX, diff):
    y = tY
    while y <= Y:
        x = tX
        while x <= X:
            tree[y][x] += diff
            x += (x & -x)
        y += (y & -y)


# y범위 [0, tY], x범위 [0, tX]에 대해 구간 합 쿼리
def basicQuery(tree, tY, tX):
    result = 0
    y = tY
    while y > 0:
        x = tX
        while x > 0:
            result += tree[y][x]
            x -= (x & -x)
        y -= (y & -y)

    return result


# y범위 [sY, eY], x범위 [sX, eX]에 대해 구간 합 쿼리
def query(tree, sY, sX, eY, eX):
    return (basicQuery(tree, eY, eX)
        - basicQuery(tree, eY, sX-1)
        - basicQuery(tree, sY-1, eX)
        + basicQuery(tree, sY-1, sX-1))
