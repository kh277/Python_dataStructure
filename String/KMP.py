# KMP - O(N+M)

'''
(1-base 인덱스)
문자열 S(string), P(pattern)이 주어지면 P와 동일한 S의 부분 문자열을 O(|S|+|P|)에 찾는 알고리즘
정확히는 S의 부분 문자열 중 P와 일치하는 곳 시작 인덱스를 전부 1-base로 반환함
'''


def getFail(P):
    fail = [0 for _ in range(len(P))]

    j = 0
    for i in range(1, len(P)):
        # P의 i번째와 P의 j번째가 일치하지 않는다면
        while j > 0 and P[i] != P[j]:
            j = fail[j-1]

        # P의 i번째와 P의 j번째가 일치한다면
        if P[i] == P[j]:
            j += 1
            fail[i] = j

    return fail


def KMP(S, P):
    # 반복 패턴 전처리
    fail = getFail(P)

    result = []
    j = 0
    for i in range(len(S)):
        # S의 i번째와 P의 j번째가 일치하지 않는다면
        while j > 0 and S[i] != P[j]:
            j = fail[j-1]

        # S의 i번째와 P의 j번째가 일치한다면
        if S[i] == P[j]:
            # P을 끝까지 탐색했다면
            if j == len(P)-1:
                result.append(i-len(P)+2)
                j = fail[j]
            else:
                j += 1

    return result
