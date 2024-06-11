# 피자 판매
'''
각 조각 크기 존재
피자 두 판 존재 -> 크기 조각들 다름
피자 조각 크기 합이 주문한 크기가 돼야 함

같은 종류 피자 -> 2조각부터는 연속 조각들 판매
손님이 원하는 피자 판매하는 모든 경우의 수 계산

while left < n and right < n+left
order 1~2,000,000 너무 큼
a, b 크기 3~1000
원형으로 도는데,
7만들기 위해 (1,2,4) 전체가 쓰였다고 할 때
(2,4,1) 중복 안됨 -> 전체합의 경우 따로 빼줌
'''
from sys import stdin
from collections import defaultdict
input = stdin.readline
order = int(input()) # 원하는 전체 조각
n, m = map(int, input().split()) # 각 피자 조각의 개수
a = list(int(input()) for _ in range(n)) # 시계방향으로 조각 크기들 주어짐
b = list(int(input()) for _ in range(m))
answer = 0 # 경우의 수
a_case, b_case = defaultdict(int), defaultdict(int)
a_case[0], b_case[0] = 1, 1
for left in range(n):
    right = left
    total = 0 
    for right in range(left, n+left-1):
        total += a[right%n]
        if total > order: break
        a_case[total] += 1
        
if sum(a) <= order: a_case[sum(a)] += 1

for left in range(m):
    total = 0 
    for right in range(left, m+left-1):
        total += b[right%m]
        if total > order: break
        b_case[total] += 1
        
if sum(b) <= order: b_case[sum(b)] += 1

for a_k, a_v in a_case.items():
    answer += b_case[order-a_k]*a_v

print(answer)