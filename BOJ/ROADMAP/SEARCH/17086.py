'''
아기 상어2
n*m 크기 공간에 상어 여러 마리
안전거리: 해당 칸으로부터 가장 거리가 가까운 상어와 거리(칸의 수)
이동은 인접한 8방향(대각선 포함)
안전 거리가 가장 큰 칸!!(상어가 아니라 칸 기준)
0 0 1 0
0 0 0 0
1 0 0 0
0 0 0 0
0 0 0 1
-> 2
1의 위치부터 거리 누적

7 4
0 0 0 1
0 1 0 0
0 0 0 0
0 0 0 1
0 0 0 0
0 1 0 0
0 0 0 1
-> 2
'''
from sys import stdin
from collections import deque

input = stdin.readline

n, m = map(int, input().split())
que = deque([])
board = []
answer = 0
dirs = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1)]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1:
            que.append((i, j, 2)) # 다음 칸, 누적 거리 + 1
    board.append(row)
    
while que:
    x, y, cnt = que.popleft()
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and (board[nx][ny] == 0 or board[nx][ny] > cnt):
            board[nx][ny] = cnt
            que.append((nx, ny, cnt+1))
            
for i in range(n):
    for j in range(m):
        if board[i][j] > answer:
            answer = board[i][j]

print(answer-1)