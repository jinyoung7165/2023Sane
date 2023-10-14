# 전쟁 - 전투
'''
n명 뭉치면 제곱 위력. 상하좌우만 뭉쳤다고 봄
누가 승리할지(B:남 /W: 나)
w팀 위력의 합 b팀 위력의 합 출력
'''
from sys import stdin
from collections import deque

input = stdin.readline

m, n = map(int, input().split())
board = [list(input()) for _ in range(n)]
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

WB = {'W':0, 'B':0}

def bfs(x, y, team):
    que = deque([(x, y)])
    TMP = 1
    board[x][y] = '-'
    while que:
        c_x, c_y = que.popleft()
        for dx, dy in dirs:
            nx, ny = c_x+dx, c_y+dy
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == team:
                TMP += 1
                board[nx][ny] = '-'
                que.append((nx, ny))
    WB[team] += TMP**2    
    
for i in range(n):
    for j in range(m):
        if board[i][j] in ('W','B'):
            bfs(i, j, board[i][j])

print(WB['W'], WB['B'])