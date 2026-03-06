# SA 휴리스틱 (Simulated Annealing)

'''
최적해가 될 가능성이 없는 결과 탐색을 방지하여 탐색할 경우의 수를 줄이는 방법.
SA는 볼츠만 분포를 이용하며, 답이 될 가능성이 낮은 경우에 대해서도 낮은 확률로 탐색함.

감쇄율 = 0.9999, 임계 온도 = 0.0005일 경우 대략 76000번을 반복하게 된다.
'''

# Output-Only 문제인 경우 아래 옵션을 적용시켜서 하기
# from numba import njit        # OutPut-Only
# import numpy as np        # OutPut-Only

import random
from math import exp

DECREASE_RATE = 0.9999     # 감쇄율
BOLTZMANN_CONSTANT = 1     # 볼츠만 상수
MAX_EXPONENT = 100         # e^x를 계산하기 위한 값의 상한치
curT = 1                   # 시작 온도
limitT = 0.0005            # 임계 온도


# 에너지 체크 함수 : 현재 상태의 점수를 구하기
# @njit        # OutPut-Only
def scoring(status):
    pass


# 전이 함수 : nextV 값을 변경해 다음 상태로 전이
# @njit        # OutPut-Only
def move(nextV, status):
    pass


def SimulatedAnnealing(N, L, data):
    global curT

    # 배치 초기화 : 구간 [0, L-1] 내의 랜덤한 N개의 숫자를 뽑아 초기 상태 설정 
    status = [data[i] for i in random.sample(range(L), N)]
    curEnergy = scoring(status)
    count = 0

    # 임계 온도에 도달할 때까지 반복
    while curT > limitT:
        # print(f"반복 횟수 : {count:06d}, 현재 최적해 : {curEnergy}, 현재 온도 : {curT}")

        # 전이 : 변화를 줄 랜덤한 값을 구간 [0, L-1] 내에서 뽑기
        nextV = random.sample(range(L), 1)
        move(nextV, status)

        # 전이 후 에너지 계산
        nextEnergy = scoring(status)

        # 상태 전이 확률 : 상태가 개선되는 경우 무조건 전이, 상태가 나빠지는 경우 확률적으로 전이
        probability = exp(min(MAX_EXPONENT, (curEnergy - nextEnergy) / (BOLTZMANN_CONSTANT * curT)))

        # 전이하지 않을 경우 이전 상태로 롤백
        if (probability < random.random()):
            move(nextV, status)
        else:
            curEnergy = min(curEnergy, nextEnergy)

        # 온도 감률 적용
        curT *= DECREASE_RATE
        count += 1

    return status
