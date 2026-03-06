# 비트마스킹 처리

'''
전체 크기가 N일 때 비트마스킹 처리
'''


# 시작 상태 (방문=1, 미방문=0, 전부 미방문 표시)
START = 0
N = 10

# 종료 상태 (전부 방문 표시)
MAX = (1<<N) - 1


# 상태 status에서 curV가 포함되어 있는지 확인
def hasMask(status, curV):
    return bool(status & (1<<curV))


# 상태 status에서 curV를 포함시킨 상태 반환
def addMask(status, curV):
    return status | (1<<curV)


# 상태 status에서 curV를 제거시킨 상태 반환
def delMask(status, curV):
    return status & ~(1<<curV)