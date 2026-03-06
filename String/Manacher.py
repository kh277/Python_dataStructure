# Manacher - O(N)

'''
문자열 string의 부분 문자열 중 팰린드롬인 구간의 개수와 길이를 O(N)에 찾는 알고리즘.
P[i] : 변형 문자열 text에서 i를 중심으로 했을 때 반지름 + 1
radius : i-1단계까지 모든 팰린드롬의 끝나는 인덱스 중 최대값
center : i-1단계까지 radius의 값이 최대가 되게 하는 중심 인덱스 값
'''

def Manacher(string):
    # 전처리 - 짝수 길이 팰린드롬을 처리하기 위한 구분자 추가
    text = '$#' + '#'.join(string) + '#@'

    # 매내처 알고리즘으로 보조 배열 P 계산하기
    P = [1] * len(text)
    radius = 0
    center = 0

    for i in range(1, len(text)-1):
        if i < radius:
            P[i] = min(P[2*center-i], radius-i)

        while text[i-P[i]] == text[i+P[i]]:
            P[i] += 1

        if i+P[i] > radius:
            radius = i + P[i]
            center = i

    return P


string = ""
P = Manacher(string)

# 최장 팰린드롬 부분 문자열
maxLen = max(P)-1

# 팰린드롬 부분 문자열의 수
total = sum([P[i]//2 for i in range(1, len(P)-1)])
