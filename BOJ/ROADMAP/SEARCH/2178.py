'''
미로 탐색
n*m. 1이동가능.0불가
(0,0)->(n-1,m-1) 이동 시 최소 칸 수(시작도착 포함 계산)
'''
from sys import stdin
from collections import deque

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
input = stdin.readline

n, m = map(int, input().split())

board = [list(input()) for _ in range(n)]

answer = 0
que = deque([(0, 0, 1)])
board[0][0] = '0'
while que:
    x, y, cnt = que.popleft()
    if x == n-1 and y == m-1:
        answer = cnt
        break
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and board[nx][ny] == '1':
            board[nx][ny] = '0'
            que.append((nx, ny, cnt+1))
print(answer)