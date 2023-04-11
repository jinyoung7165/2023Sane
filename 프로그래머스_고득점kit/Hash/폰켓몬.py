# n/2개를 가져도 됨
# [3,1,2,3] 종류가 있다면, 이 중 2개를 고를 때
# 최대한 많은 종류 선택 : 2종류(1,3), (1,2), (2,3)
def solution(nums):
    return min(len(nums)//2, len(set(nums)))