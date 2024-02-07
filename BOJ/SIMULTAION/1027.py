# 고층 건물
'''
50개 이하 N개 빌딩 중, 가장 많은 빌딩을 볼 수 있는 빌딩 찾자
A가 B에서 보이려면, 
두 지붕을 잇는 선분이 다른 고층 빌딩을 지나거나 접하면 안됨
가장 많은 고층 빌딩이 보이는 빌딩에서 보이는 빌딩의 수 출력
왼쪽 <- (높이차/idx차 점점 커져야 함) 기준 빌딩 (높이차/idx차 점점 커져야 함) ->  오른쪽
'''
from sys import stdin

input = stdin.readline
n = int(input())
buildings = list(map(int, input().split()))
answer = 0
for idx in range(n): # idx번째를 기준으로 측정
    height = buildings[idx]
    tmp, cnt = float('inf'), 0
    for left in range(idx-1, -1, -1):
        cur = (height - buildings[left]) / (idx - left)
        if cur < tmp:
            tmp = cur
            cnt += 1
    tmp = float('inf')
    for right in range(idx+1, n):
        cur = (height - buildings[right]) / (right - idx)
        if cur < tmp:
            tmp = cur
            cnt += 1
    if answer < cnt: answer = cnt
print(answer)