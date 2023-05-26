# RGB 거리
# 1~N 집
# 빨, 초, 파 중 하나의 색으로 칠. 최소 비용
# 인접한 집 색 같으면 안됨
from sys import stdin
input = stdin.readline
n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    _dr, _dg, _db = dp[i-1]
    dp[i][0] += min(_dg, _db)
    dp[i][1] += min(_dr, _db)
    dp[i][2] += min(_dr, _dg)
print(min(dp[n-1])) # maps[-1]보다 n-1로 접근하는 게 훨 빠름