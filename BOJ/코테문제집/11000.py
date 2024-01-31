# 강의실 배정
'''
빨리 시작 , 빨리 끝나는 거 쌓아두고
다음 거 시작이, 제일 빨리 끝나는 거 다음이면, 이어서 가능
'''
from sys import stdin
import heapq
input = stdin.readline
n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]

times.sort(key=lambda x:(x[0], x[1]))

que = []

for start, end in times:
    if que and start >= que[0]:
        heapq.heappop(que)
    heapq.heappush(que, end)
print(len(que))