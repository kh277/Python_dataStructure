# Rotating Calipers - O(N)

'''
2차원 좌표 N개가 points로 주어질 때, 가장 먼 두 점 사이의 거리 반환.
볼록 껍질 도출에 O(NlogN), 회전하는 캘리퍼스 처리에 O(N) 소모.
'''


def CCW(A, B, C):
    return (B[0]-A[0]) * (C[1]-A[1]) - (B[1]-A[1]) * (C[0]-A[0])


def distance(A, B):
    return (A[0]-B[0])**2 + (A[1]-B[1])**2


def ConvexHull(points):
    points = sorted(set(points))

    lower = []
    for point in points:
        while len(lower) >= 2 and CCW(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)

    upper = []
    for point in reversed(points):
        while len(upper) >= 2 and CCW(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)

    return lower[:-1] + upper[:-1]


def RotatingCalipers(points):
    # 볼록 껍질 구하기
    hull = ConvexHull(points)
    length = len(hull)

    # 특수 케이스 처리
    if length < 2:
        return 0
    elif length == 2:
        return distance(hull[0], hull[1])**0.5
    
    result = 0
    curFarestP = 1
    for curP in range(length):
        nextP = (curP+1) % length

        # i와 다음 점 next_i을 잇는 직선과 가장 멀리 떨어진 점 도출
        while True:
            nextFarestP = (curFarestP+1) % length

            # 두 점 curP, nextP에서 curFarestP, nextFarestP까지 거리 비교
            d1 = CCW(hull[curP], hull[nextP], hull[curFarestP])
            d2 = CCW(hull[curP], hull[nextP], hull[nextFarestP])

            # nextFarestP까지의 거리가 더 클 경우 갱신
            if d1 < d2:
                curFarestP = nextFarestP
            else:
                break

        # 갱신
        result = max(result, distance(hull[curP], hull[nextFarestP]), distance(hull[nextP], hull[nextFarestP]))

    return result**0.5
