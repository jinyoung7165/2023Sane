# 점프
'''
n*n 판에서 (0,0)->(n-1,n-1)
각 칸에는 갈 수 있는 거리 존재(오른쪽/아래쪽. 한 방향으로만)
0은 진행 막는 종척점. "경로의 개수" 구하라
dfs+dp? 이미 dp(종점까지 도달한 경우) 존재 시 재활용. 시간 복잡도 큼
방향 단순하기 때문에 dp로만? dp(해당 칸까지 도달하는 경우)
x+=1 또는 y+=1 ?번씩
'''
from sys import stdin
input = stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        cnt = board[i][j]
        if cnt == 0: continue
        if i + cnt < n: dp[i+cnt][j] += dp[i][j]
        if j + cnt < n: dp[i][j+cnt] += dp[i][j]
print(dp[n-1][n-1])
            
''' dfs-> 정답이지만 어려움ㅠ
direction = [(1, 0), (0, 1)]    # 하 우
dp = [[-1]*N for _ in range(N)]

def dfs(x, y):
    if x == N-1 and y == N-1: # 도착지인 경우
        return 1 # 1경우 추가
    if dp[x][y] != -1: # 이미 방문한 흔적 있을 때 그거 쓰자
        return dp[x][y]
    else: # 처음 방문
        dp[x][y] = 0 # 경우 누적을 위한 초기화
        for d in direction:
            nx = x + d[0] * graph[x][y]
            ny = y + d[1] * graph[x][y]
            if 0 <= nx < N and 0 <= ny < N:
                dp[x][y] += dfs(nx, ny) # 재귀로 현재경로 출발 시 누적 경우의 수 구함
        return dp[x][y] # 재귀함수이기 때문에 return 값 필요!!!!!
'''