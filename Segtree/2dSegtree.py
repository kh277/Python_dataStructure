# 2D Segment Tree (비재귀 구현)

'''
점 업데이트, 구간 쿼리를 O((logN)^2)에 처리할 수 있는 자료구조
2D 펜윅 트리보단 느리지만 펜윅 트리가 처리할 수 없는 최대값, 최소값 등의 중간 구간에 대한 처리를 할 때 유용함.

build() : 배열 A를 기반으로 2차원 세그먼트 트리 생성, O(NM)
update() : A의 i번째 원소값 수정 및 전파, O(logNlogM)
query() : x구간 [sX, eX], y구간 [sY, eY]의 총합 도출, O(logNlogM)
'''

from array import array


# Y*X 크기의 A을 기반으로 2D Segment Tree 생성
def build(Y, X, A):
    tree = [array('i', [0]) * (X<<1) for _ in range(Y<<1)]

    for y in range(len(A)):
        for x in range(len(A[0])):
            tree[y+Y][x+X] = A[y][x]
    for y in range(Y, Y<<1):
        for x in range(X-1, 0, -1):
            tree[y][x] = max(tree[y][x<<1], tree[y][x<<1 | 1])
    for y in range(Y-1, 0, -1):
        for x in range(1, X<<1):
            tree[y][x] = max(tree[y<<1][x], tree[y<<1 | 1][x])

    return tree


# Y*X 크기의 tree에서 [tY][tX] 위치의 값에 diff 더하기
def update(Y, X, tree, tY, tX, diff):
    tY += Y
    tX += X
    tree[tY][tX] += diff

    curX = tX
    while curX > 1:
        curX >>= 1
        tree[tY][curX] = tree[tY][curX<<1] + tree[tY][curX<<1 | 1]

    curY = tY
    while curY > 1:
        curY >>= 1
        tree[curY][tX] = tree[curY<<1][tX] + tree[curY<<1 | 1][tX]
        curX = tX
        while curX > 1:
            curX >>= 1
            tree[curY][curX] = tree[curY<<1][curX] + tree[curY<<1 | 1][curX]


# tree[curY] 에서 x범위 [sX, eX]에 대해 구간 합 쿼리
def queryX(X, tree, curY, sX, eX):
    result = 0
    x1 = sX + X
    x2 = eX + X

    while x1 <= x2:
        if x1 & 1:
            result += tree[curY][x1]
            x1 += 1
        if ~x2 & 1:
            result += tree[curY][x2]
            x2 -= 1
        x1 >>= 1
        x2 >>= 1
    
    return result


# y범위 [sY, eY], x범위 [sX, eX]에 대해 구간 합 쿼리
def query(Y, X, tree, sY, sX, eY, eX):
    result = 0
    y1 = sY + Y
    y2 = eY + Y

    while y1 <= y2:
        if y1 & 1:
            result += queryX(X, tree, y1, sX, eX)
            y1 += 1
        if ~y2 & 1:
            result += queryX(X, tree, y2, sX, eX)
            y2 -= 1
        y1 >>= 1
        y2 >>= 1

    return result