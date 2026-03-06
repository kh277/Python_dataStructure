# Point in Polygon - O(logN)

'''
2차원 좌표 point가 볼록 다각형 hull 내부에 존재하는지 체크
'''

def CCW(A, B, C):
    return (B[0]-A[0]) * (C[1]-A[1]) - (B[1]-A[1]) * (C[0]-A[0])


def PointInPolygon(point, hull):
    # 1번과 n-1번 반직선 사이에 점이 존재하지 않는 경우
    if CCW(hull[0], hull[-1], point) > 0:
        return False
    if CCW(hull[0], hull[1], point) < 0:
        return False

    # 이분 탐색으로 두 직선 구하기
    left = 1
    right = len(hull) - 1
    while left < right:
        mid = (left + right) // 2
        if CCW(hull[0], hull[mid], point) > 0:
            left = mid + 1
        else:
            right = mid

    # 최종적으로 남은 left와 left-1 사이에 점이 있는지 확인
    return CCW(hull[left-1], hull[left], point) > 0