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
dirs = [(0,1),(1,0),(0,-1),(-1,0),
        (1,1),(1,-1),(-1,1),(-1,-1)]

n, m = map(int, input().split())
board = [list(input().split()) for _ in range(n)]
que = deque([])
for i in range(n):
    for j in range(m):
        if board[i][j] == '1':
            que.append((i, j))
            board[i][j] = 0

answer = 0
while que:
    x, y = que.popleft()
    if board[x][y] > answer: answer = board[x][y]
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and board[nx][ny] == '0':
            board[nx][ny] = board[x][y] + 1
            que.append((nx, ny))
print(answer)