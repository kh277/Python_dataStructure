# Tenary Search

'''
아래로 볼록인 함수 f(x)가 존재할 때,
구간 [minX, maxX]에 대해 함수 f(x)의 최소값 반환.
'''

INF = 10**6
def f(x):
    return


def TernarySearch(minX, maxX):
    start = minX
    end = maxX

    # 삼분 탐색
    while end - start >= 3:
        first = (2*start+end)//3
        second = (start+2*end)//3

		# 함수값 체크
        if f(first) > f(second):
            start = first+1
        else:
            end = second

    # 최종 범위에 대해 결과 도출
    result = INF
    for i in range(start, end+1):
        result = min(f(i), result)

    return result