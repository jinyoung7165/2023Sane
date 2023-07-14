# 오큰수
'''
5
1 8 5 7 9
[8, 9, 7, 9, -1]
8 9 7 9 -1
'''
from sys import stdin
input = stdin.readline

n = int(input())
aArr = list(map(int, input().split()))

stack = [] # 나보다 큰 애 나올 때까지 기다림
result = [-1]*n
for idx, num in enumerate(aArr):  # 현재 수 뽑기 -> 이전 수랑 비교할 것
    # 현재 수가 이전 수보다 크면, 오름차순
    while stack and num > stack[-1][1]:
        _idx, _num = stack.pop()
        result[_idx] = num
    stack.append((idx, num)) # 이전수가 될 애 내림차순 append
print(*result)