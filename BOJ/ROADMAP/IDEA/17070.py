# 파이프 옮기기 1
'''
n*n 격자판. 1*1 정사각형 칸(r,c)
빈 칸0/벽1
2개 연속 칸 차지. 회전 가능 파이프
-- | \ 모양 가능
빈 칸 위에서 밀어서 이동
(오른쪽, 아래, 오른쪽 아래)방향으로 밀면서 회전 45도 가능
가로. 이동 방법 2개(오른쪽(1&2번째 col+1), 오른쪽 아래(1))
세로. 이동 방법 2개(아래, 오른쪽 아래)
대각선. 이동 방법 3개(오른쪽 아래, 아래)
(1,1),(1,2) 가로 파이프 존재 -> 한쪽 끝을 (n,n)로 이동시키는 방법 수
'''
'''
시간 초과 -> dp로 해결하려면?
dp[i][j][0]: 현재 칸을 꼭짓점으로 하는 가로 pipe 수
dp[i][j][1]: 현재 칸을 꼭짓점으로 하는 세로 pipe 수
dp[i][j][2]: 현재 칸을 꼭짓점으로 하는 대각선 pipe 수
따라서, 초기 상태를 dp[0][1][0]= 1 로 표현((0,1)에 가로 꼭짓점이 놓인 상태)
i, j 기준으로 먼저 채움
첫 번째 행에는 모두 가로 상태의 pipe 꼭짓점만 올 수 있음 dp[0][1,..n-1][0] = 1
첫 번째 열에는 꼭짓점이 오는 경우 없음 -> (1,1)~(n-1,n-1) 순회
빈 칸이면 (0,1,2)를 놓기 전, 이전 pipe 상태 고려해서 설치
'''
from sys import stdin
input = stdin.readline
n = int(input())
board = [list(input().split()) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]

dp[0][1][0] = 1 # (0,1)칸에 가로 꼭짓점 1경우
for i in range(2, n): # 첫 번째 행의 가로 꼭짓점 경우 채우기
    if board[0][i] == '1': break # 벽 나오면 stop
    dp[0][i][0] = 1 # 오른쪽으로 계속 밀기

for i in range(1, n):
    for j in range(1, n):
        # 대각선의 경우, 3방향 벽 먼저 고려 후, 대각선에서 오는 경우의 수 더함
        if board[i][j] == board[i][j-1] == board[i-1][j] == '0':
            dp[i][j][2] = sum(dp[i-1][j-1])
        if board[i][j] == '0': # 가로 세로를 고려하는 경우, 다음 꼭짓점 위치의 벽만 보면 됨
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2] # 가로의 경우, 가로 또는 대각선에서 올 수 있음
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2] 

print(sum(dp[n-1][n-1]))

'''
시간 초과 남 -> dfs로 여러 번 방문했던 곳 재방문 막기 위해 dp 필요
'''
from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**6)
n = int(input())
board = [list(input().split()) for _ in range(n)]

# 이동방향, 다음 상태 저장
status = [[[0,1,0],[1,1,2]],[[1,0,1],[1,1,2]],[[0,1,0],[1,0,1],[1,1,2]]] # 수평, 수직, 대각선
answer = 0

def dfs(x, y, st):
    global answer
    if x == n-1 and y == n-1:
        answer += 1
        return
    for nx, ny, ns in status[st]: # status별로 이동 방법 두 개
        if 0<=x+nx<n and 0<=y+ny<n:
            if nx == ny == 1: # 4칸을 차지함
                if board[x][y+1] == board[x+1][y] == board[x+1][y+1] == '0':
                    dfs(x+nx, y+ny, ns)
            else: # 두 칸을 차지함
                if board[x+nx][y+ny] == '0': # 이동 가능
                    dfs(x+nx, y+ny, ns)

dfs(0, 1, 0)
print(answer)