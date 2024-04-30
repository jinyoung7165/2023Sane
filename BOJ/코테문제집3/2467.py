# 용액
'''
산성:1~10**9
알칼리: -1~-10**9

두 용액 더한 값 -> 0에 가까운 용액 만들자
[-99, -2, -1, 4, 98] : -99랑 98 더하면 -1
정렬된 순서로 주어졌을 때, 두 용액을 찾아라
'''
from sys import stdin
input = stdin.readline
n = int(input())
liquids = list(map(int, input().split()))
left, right = 0, n-1
s = float('inf')
answer = []
while left < right:
    tmp = liquids[left] + liquids[right]
    if abs(tmp) < s:
       s = tmp
       answer = [liquids[left], liquids[right]]
    if tmp == 0: break
    elif tmp < 0: left += 1
    else: right -= 1
        
    
print(*answer)

