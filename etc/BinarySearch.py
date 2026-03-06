# BinarySearch - O(logN)

'''
정렬된 배열에서 target이 들어갈 위치를 logN의 시간에 탐색
'''

# arr에서 target 이상인 첫 번째 요소의 인덱스 반환
def LowerBound(arr, target):
    start = 0
    end = len(arr)

    while start < end:
        mid = (start+end)//2
        if arr[mid] < target:
            start = mid+1
        else:
            end = mid

    return start


# arr에서 target보다 큰 첫 번째 요소의 인덱스 반환
def UpperBound(arr, target):
    start = 0
    end = len(arr)

    while start < end:
        mid = (start+end)//2
        if arr[mid] <= target:
            start = mid+1
        else:
            end = mid

    return start