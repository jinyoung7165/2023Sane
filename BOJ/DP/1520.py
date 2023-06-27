# 내리막길
# 직사각형 지도
# 지점의 높이. 인접 지점 이동 가능
# 제일 위쪽 칸(0,0) -> 제일 오른쪽 아래(n-1,m-1)
# 항상 더 낮은 지점으로만 이동
# (0, 0) -> (i, j) 까지 올 수 있는 내리막 경로의 수
# 이동 가능한 경로의 수 출력(dfs 저장)
# 각 지점을 출발지점으로 잡고 도착지점까지 경로의 수 갱신
from sys import stdin
input = stdin.readline

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1]*m for _ in range(n)]
# dp[i][j]: (i,j)->(n-1,m-1) 갈 수 있는 수 
dp[n-1][m-1] = 1
def dfs(x, y):
    if x == n-1 and y == m-1: # 도착
        return 1
    if dp[x][y] != -1: # 이미 방문한 적이 있을 때, 여기서 출발해서 종점으로 가는 수 return
        return dp[x][y]
    
    cnt = 0 # 종점으로 가는 수(4방향에 대해 누적)
    h = board[x][y]
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and h>board[nx][ny]:
            # dp[nx][ny]를 return시 dp[x][y]에 더해야 함
            # dfs(nx, ny)를 더하되
            # dfs의 최종 return값은 dp[x][y]
            cnt += dfs(nx, ny)
    dp[x][y] = cnt # 종점 도달 불가 시 0 또는 누적cnt
    return dp[x][y]
dfs(0, 0)
print(dp[0][0])

'''
나의 코드, 조금 더 효율 좋음
dp[n-1][m-1] = 1
def dfs(x, y):
    if x == n-1 and y == m-1: # 도착
        return True
        
    cnt = 0 # 종점으로 가는 수(4방향에 대해 누적)
    h = board[x][y]
    if dp[x][y] == -1: # 방문한 적 없으면 dp 구하라
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and h>board[nx][ny]: # 사방 살피며
                if dfs(nx, ny): # 끝까지 갈 수 있으면
                    cnt += dp[nx][ny] # (nx,ny)->(n-1,m-1) 경우의 수
        dp[x][y] = cnt # 0 또는 현재->사방->(n-1,m-1) 경우의 수
    if dp[x][y] > 0: return True # 현재->끝까지 갈 수 있으면 true 리턴
    return False # 그렇지 않으면 0리턴
'''