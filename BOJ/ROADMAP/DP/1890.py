'''
점프
(0,0)->(n-1,n-1) 경로 개수 (최대 경로=경우의 수)
현재 칸에 적힌 수만큼 두 방향으로만 이동 가능((0,1*k), (1+k, 0))
오른쪽, 아래 == for i * j 그냥 반복문 돌리며 n-1,n-1 도달
(n-1,n-1)에는 항상 0 적혀 있음
4*4~100*100
해당 칸에 적힌 수만큼 이동하다가, 벽 만나면 이동 불가능한 거임
2 갈래로 이동하면서.
벽에 박으면 -1 return
아니면 쭉 가다가 0만나면 1 return
dfs 사용할 경우 시간 복잡도 매우 큼
'''
from sys import stdin

input = stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1 # 시작점 경우의 수 1
for x in range(n):
    for y in range(n):
        if x == n-1 and y == n-1:
            print(dp[x][y]) # 모인 경우의 수 더함
            break
        k = board[x][y]
        if 0<=x+k<n:
            dp[x+k][y] += dp[x][y] # 해당 칸으로 올 수 있는 경우의 수 증가
        if 0<=y+k<n:
            dp[x][y+k] += dp[x][y]
            
            
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