# Point in Polygon

'''
2차원 좌표 point가 다각형 hull 내부에 존재하는지 판정하는 알고리즘.
여기서 hull은 반드시 볼록 다각형이어야 하며, 시계/반시계 방향으로 정렬되어 있어야 함.

checkInner() : 다각형 hull 내부에 point가 존재하는지 여부 판정, O(logN)
주석처리된 부분은 다각형 변 위에 존재하는 점을 제외시켜야 하는 경우의 코드임.
'''

def CCW(A, B, C):
    return (B[0]-A[0]) * (C[1]-A[1]) - (B[1]-A[1]) * (C[0]-A[0])


def onLine(A, B, point):
    return min(A[0], B[0]) <= point[0] <= max(A[0], B[0]) and min(A[1], B[1]) <= point[1] <= max(A[1], B[1])


def checkInner(hull, point):
    # 초기 선분 체크
    # if CCW(hull[0], hull[1], point) <= 0:
    if CCW(hull[0], hull[1], point) < 0:
        return False
    # if CCW(hull[0], hull[-1], point) >= 0:
    if CCW(hull[0], hull[-1], point) > 0:
        return False

    # 이분 탐색으로 점이 속한 삼각형 찾기
    left = 1
    right = len(hull) - 1
    while left < right:
        mid = (left + right + 1) >> 1
        if CCW(hull[0], hull[mid], point) >= 0:
            left = mid
        else:
            right = mid - 1

    # 볼록 껍질이 선분인 경우 예외 처리
    if left == len(hull) - 1:
        return CCW(hull[0], hull[-1], point) == 0 and onLine(hull[0], hull[-1], point)

    # 최종 삼각형 판정
    # return CCW(hull[0], hull[left], point) > 0 and CCW(hull[left], hull[left+1], point) > 0 and CCW(hull[left+1], hull[0], point) > 0
    return CCW(hull[0], hull[left], point) >= 0 and CCW(hull[left], hull[left+1], point) >= 0 and CCW(hull[left+1], hull[0], point) >= 0
