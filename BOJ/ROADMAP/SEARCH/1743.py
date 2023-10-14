'''
음식물 피하기
뭉친 것 중 가장 큰 거 크기 출력
k: 원소 개수. k줄에 거쳐 원소의 좌표 주어짐
'''
from sys import stdin
from collections import deque

answer = 0
input = stdin.readline
n, m, k = map(int, input().split())
board = [[0]*m for _ in range(n)]
for _ in range(k):
    i, j = map(int, input().split())
    board[i-1][j-1] = 1

dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs(x, y, path):
    que = deque([(x, y)])
    while que:
        cx, cy = que.popleft()
        for dx, dy in dirs:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == 1:
                board[nx][ny] = 0
                path.add((nx, ny))
                que.append((nx, ny))
            
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            path = set()
            board[i][j] = 0
            path.add((i, j))
            bfs(i, j, path)
            answer = max(answer, len(path))

print(answer)