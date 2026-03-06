# 좌표 압축 - O(NlogN)

'''
N개의 좌표를 axis 좌표축에 대해 좌표 압축.
'''

def compress(N, points, axis):
    points.sort(key= lambda x: x[axis])
    before = points[0][axis]
    end = 0
    for i in range(N):
        if points[i][axis] == before:
            points[i][axis] = end
        else:
            before = points[i][axis]
            end += 1
            points[i][axis] = end

    return end, points
