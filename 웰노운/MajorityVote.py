# Boyer-Moore Majority Vote - O(N)

'''
보이어-무어 다수결 투표 알고리즘은 어떤 수열에서 과반수를 차지하는 원소를 찾는 알고리즘이다.
예제 : #1270번
'''


def MajorityVote(nums):
    candidate = None
    count = 0
    for i in nums:
        # 후보가 실질적으로 0번 등장한 경우 -> 후보 교체
        if count == 0:
            candidate = i
            count = 1
        # 후보가 등장한 경우
        elif i == candidate:
            count += 1
        # 후보가 등장하지 않은 경우
        else:
            count -= 1
    
    if candidate != None and nums.count(candidate) > len(nums)//2:
        return candidate

    return None
