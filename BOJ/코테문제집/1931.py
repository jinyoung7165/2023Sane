# 회의실 배정
# 1개의 회의실->n개의 회의에서 사용
# 회의: 시작,끝나는 시간 주어짐. 끝나는 동시에 다음 회의 시작 가능
# 각 회의가 겹치지 않는 회의의 최대 개수
# (0,6),(1,4),(2,13),(3,5),(3,8).(5,7),(5,9),(6,10),(8,11),(8,12),(12,14)
from sys import stdin
input = stdin.readline
n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]

meetings.sort(key = lambda x: (x[0],x[1]))
cnt = 0
last_end = -1
for start, end in meetings:
    if last_end <= start: # end이후 바로 start
        last_end =  end
        cnt += 1
    elif last_end > end: # 내가 더 빨리 끝남
        last_end = end
print(cnt)