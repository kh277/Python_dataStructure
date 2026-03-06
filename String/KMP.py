# KMP - O(N+M)

'''
(1-base 인덱스)
문자열 text에서 pattern이 등장하는 시작 인덱스 전부 반환
'''


def getFail(pattern):
    fail = [0 for _ in range(len(pattern))]

    j = 0
    for i in range(1, len(pattern)):
        # pattern의 i번째와 pattern의 j번째가 일치하지 않는다면
        while j > 0 and pattern[i] != pattern[j]:
            j = fail[j-1]

        # pattern의 i번째와 pattern의 j번째가 일치한다면
        if pattern[i] == pattern[j]:
            j += 1
            fail[i] = j

    return fail


def KMP(text, pattern):
    # 반복 패턴 전처리
    fail = getFail(pattern)

    result = []
    j = 0
    for i in range(len(text)):
        # text의 i번째와 pattern의 j번째가 일치하지 않는다면
        while j > 0 and text[i] != pattern[j]:
            j = fail[j-1]

        # text의 i번째와 pattern의 j번째가 일치한다면
        if text[i] == pattern[j]:
            # pattern을 끝까지 탐색했다면
            if j == len(pattern)-1:
                result.append(i-len(pattern)+2)
                j = fail[j]
            else:
                j += 1
    
    return result