# Search a 2D Matrix II
'''
왼->오 오름차순
위->아래 오름차순
있으면 true return
'''
from bisect import bisect_left
def searchMatrix(matrix, target) -> bool:
    n, m = len(matrix), len(matrix[0])
    row = 0
    while row < n:
        idx = bisect_left(matrix[row], target)
        if idx < m and matrix[row][idx] == target:
            return True
        row += 1
    return False