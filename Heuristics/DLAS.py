# DLAS 휴리스틱 (Diversified Late Acceptance Search)

import random

MEMORY_SIZE = 5     # 기억할 이전 상태의 개수
MAX_ITER = 1000     # 지역 최적해를 찾지 못했을 경우 탐색을 종료하는 기준점
END_SCORE = 0       # 탐색을 종료할 목표 점수


# 점수 체크 함수
# TODO : 점수 체크 함수 작성 필요
def scoring(status):
    pass


# 상태 변이 함수
# TODO : 상태 변이 함수 작성 필요
def move(N, status):
    # 구간 [0, 100] 내에서 랜덤하게 상태 변화
    revCol = int(random.randint(0, 101)) % N
    pass


def DLAS(N, status):
    curScore = scoring(status)
    bestStatus = status.copy()
    bestScore = curScore

    memory = [curScore] * MEMORY_SIZE
    k = 0
    iterCount = 0

    while curScore > END_SCORE and iterCount < MAX_ITER:
        prevScore = curScore
        curStatus = status.copy()
        
        # 상태 변이
        move(N, status)
        nextScore = scoring(status)

        # 상태가 개선된 경우 최적해 갱신
        if nextScore < bestScore:
            iterCount = 0
            bestStatus = status.copy()
            bestScore = nextScore

        # 수용 전략
        if nextScore == curScore or nextScore < max(memory):
            curScore = nextScore
        else:
            status = curStatus

				# 대체 전략
        if curScore > memory[k] or (curScore < memory[k] and curScore < prevScore):
            memory[k] = curScore

        k = (k+1) % MEMORY_SIZE
        iterCount += 1

    return bestScore, bestStatus
