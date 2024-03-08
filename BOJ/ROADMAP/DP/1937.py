# 욕심쟁이 판다
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
def dfs(x, y):
    if dp[x][y]: return dp[x][y]
    
    dp[x][y] = 1 # 현재 노드 방문 처리
    tmp = 0 # 다음 경로 중 최장 저장
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and board[nx][ny] > board[x][y]:
            tmp = max(tmp,  dfs(nx, ny))
    dp[x][y] += tmp
    return dp[x][y]

answer = 1
for i in range(n):
    for j in range(n):
        if not dp[i][j]: answer = max(answer, dfs(i, j))
print(answer)