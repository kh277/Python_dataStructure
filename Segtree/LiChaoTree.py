# Li Chao Tree (비재귀 구현)

'''
직선 삭제 쿼리가 없는 Convex Hull Trick 문제를 Online으로 해결하기 위한 자료구조.
update : 직선 ax+b 추가
query : x가 주어질 때, 직선들 중 ax+b의 최대값 쿼리

직선의 기울기가 단조증가/단조감소할 경우 CHT를 사용하면 쿼리를 amortized O(1)에 처리가 가능하며,
단조증가/단조감소가 아닐 경우 리차오 트리를 이용해 쿼리를 O(logX)에 처리가 가능하다.
'''

MAX = 10**13
INF = 1<<63


class Line:
    __slots__ = ("a", "b")
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get(self, x):
        return self.a*x + self.b


def build():
    return [[-1, -1, -MAX, MAX, Line(0, -INF)]]


# index번 노드가 관리하는 구간 [s, e]에 직선 v를 추가하기
def update(tree, index, v):
    newLine = v
    curI = index

    while True:
        start = tree[curI][2]
        end = tree[curI][3]
        mid = (start + end) >> 1

        low = tree[curI][4]
        high = newLine

        # start에서 high가 위에 오도록 교환
        if low.get(start) > high.get(start):
            low, high = high, low

        # high가 start, end 모두 위에 있는 경우
        if low.get(end) <= high.get(end):
            tree[curI][4] = high
            return

        # 리프 노드에 도달한 경우
        if start == end:
            return

        # 오른쪽 부분에서 low와 high가 교차하는 경우
        if low.get(mid) < high.get(mid):
            tree[curI][4] = high
            newLine = low
            nextI = tree[curI][1]
            if nextI == -1:
                nextI = len(tree)
                tree[curI][1] = nextI
                tree.append([-1, -1, mid+1, end, Line(0, -INF)])
                tree[nextI][4] = newLine
                return
            curI = nextI
        # 왼쪽 부분에서 low와 high가 교차하는 경우
        else:
            tree[curI][4] = low
            newLine = high
            nextI = tree[curI][0]
            if nextI == -1:
                nextI = len(tree)
                tree[curI][0] = nextI
                tree.append([-1, -1, start, mid, Line(0, -INF)])
                tree[nextI][4] = newLine
                return
            curI = nextI


# index번 노드가 관리하는 구간에서 함수값 x 구하기
def query(tree, index, x):
    curI = index
    result = -INF

    while curI != -1:
        start = tree[curI][2]
        end = tree[curI][3]
        mid = (start + end) >> 1
        value = tree[curI][4].get(x)
        if value > result:
            result = value

        # 리프 노드에 도착한 경우
        if start == end:
            break

        # 왼쪽 부분으로 이동
        if x <= mid:
            curI = tree[curI][0]
        # 오른쪽 부분으로 이동
        else:
            curI = tree[curI][1]

    return result


def main():
    Q = int(input())
    tree = build()
    for _ in range(Q):
        q, *a = map(int, input().split())
        if q == 1:
            update(tree, 0, Line(a[0], a[1]))
        else:
            print(query(tree, 0, a[0]))


main()
