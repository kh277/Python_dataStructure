# Convex Hull (Monotone Chain)

'''
2차원 평면 위의 점 집합을 모두 포함하는 가장 작은 볼록 다각형을 구하는 알고리즘.

ConvexHull() : 2차원 좌표 집합 points에 대해 볼록 껍질 도출, O(NlogN)
'''

def CCW(A, B, C):
    return (B[0]-A[0]) * (C[1]-A[1]) - (B[1]-A[1]) * (C[0]-A[0])


def ConvexHull(points):
    # x좌표 오름차순으로 정렬
    points = sorted(set(points))

    # 아래쪽 Hull 구하기
    lower = []
    for point in points:
        # 반시계 방향이 아닐 경우 마지막 점 제거
        while len(lower) >= 2 and CCW(lower[-2], lower[-1], point) <= 0:
            lower.pop()
        lower.append(point)

    # 위쪽 Hull 구하기
    upper = []
    for point in reversed(points):
        # 반시계 방향이 아닐 경우 마지막 점 제거
        while len(upper) >= 2 and CCW(upper[-2], upper[-1], point) <= 0:
            upper.pop()
        upper.append(point)

    # 아래쪽 Hull과 위쪽 Hull을 중복제거하여 합치기
    return lower[:-1] + upper[:-1]
