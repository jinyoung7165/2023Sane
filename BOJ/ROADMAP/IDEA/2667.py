# 동전2
from sys import stdin

# 1:집, 0:없는 곳
# 연결된 곳 단지에 번호 붙일 것.
# 단지 수 출력, 각 단지에 속하는 집 수 오름차순
# path set 전달하는 게 더 낫다 => 탐색 후 len(path)를 cnts에 append
from sys import setrecursionlimit

setrecursionlimit(10**6)
n = int(input())
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
board = [list(input()) for _ in range(n)]

cnts = []

def dfs(x, y, idx):
    global cnts
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and board[nx][ny] == '1':
            board[nx][ny] = '0'
            cnts[idx] += 1
            dfs(nx, ny, idx)

idx = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == '1':
            board[i][j] = '0'
            cnts.append(1)
            dfs(i, j, idx)
            idx += 1

cnts.sort()        
print(len(cnts))
for cnt in cnts:
    print(cnt)