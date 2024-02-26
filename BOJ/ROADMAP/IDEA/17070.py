# 파이프 옮기기 1
'''
n*n크기 격자판. 1부터 시작. 빈칸0/벽1
파이프는 2개의 2칸 크기. 밀면서 회전 가능
--(1*2) |(2*1) \(2*2) 빈칸만 차지 가능
처음에 가로 모양으로 (1,1),(1,2) 차지함 -> 한쪽 끝을 (n,n)로 이동시키는 방법의 개수
가로. (1,2)-> 가로(1,3) (c+1)/ 대각선(2,3) c+1, r+1, (r+1,c+1)확인
세로. (2,2)-> 세로(3,2) (r+1)/ 대각선(3,3) c+1, r+1, (r+1,c+1)확인
대각선. (2,3)-> 가로(2,4) (c+1)/ 세로(3,3) (r+1)확인 / 대각선 c+1, r+1, (r+1,c+1)확인
같은 위치라도 다른 모양일 수 있음.
모든 경우의 수 -> 재활용 위해 dp + dfs
각 위치에 특정 모양으로 도착했을 때, 이후 가능한 경우 최대 2개
가로세로대각선012
'''
from sys import stdin
input = stdin.readline
n = int(input())
board = [list(input().split()) for _ in range(n)]
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1
for i in range(n):
    for j in range(n):
        if i==n-1 and j==n-1: break
        for k in range(3): # 가로, 세로, 대각선
            if dp[i][j][k]:
                if k!=0 and i < n-1 and board[i+1][j] == '0':
                    dp[i+1][j][1] += dp[i][j][k]
                if k!=1 and j < n-1 and board[i][j+1] == '0':
                    dp[i][j+1][0] += dp[i][j][k]
                if i < n-1 and j < n-1 and board[i+1][j] == '0' and board[i][j+1] == '0' and board[i+1][j+1] == '0': # 대각선 이동 가능
                    dp[i+1][j+1][2] += dp[i][j][k]
print(sum(dp[n-1][n-1]))