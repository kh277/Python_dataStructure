# Trie - O(logN)

'''
문자열을 트리로 관리하여 문자열 존재 여부를 logN에 처리
'''

END_POINT = 0


class Trie:
    def __init__(self):
        self.root = dict()

    def add(self, value):
        curV = self.root
        for v in value:
            if v not in curV:
                curV[v] = dict()
            curV = curV[v]
        curV[END_POINT] = True