# 빵집
'''
각 열의 행에 대해서 맨 끝열 만날 때까지 DFS 한 칸씩 늘려나감
각 열의 행 순회하며, (012) 방향 중 갈 수 있는 거 위에서부터 선점.
해당 점으로부터 출발했는데, 맨 마지막 열에 도달 못햇으면 막힌 거임 -> visited 표시하기
'''
from sys import stdin

input = stdin.readline
dirs = [(-1,1),(0,1),(1,1)]
n, m = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
visited = [[False]*m for _ in range(n)]

def dfs(i, j):
    if j == m-1: return True
    
    # 다음 열의 행 선택
    for dx, dy in dirs:
        nx, ny = i+dx, j+dy
        if 0<=nx<n and 0<=ny<m and board[nx][ny] == '.' and not visited[nx][ny]:
            visited[nx][ny] = True
            if dfs(nx, ny): return True # 이미 끝에 도착하는 경로 찾았으면 그만둬라

    return False

answer = 0
for i in range(n):
    if dfs(i, 0): answer += 1
    
print(answer)