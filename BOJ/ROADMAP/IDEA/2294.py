# 동전2
from sys import stdin
input = stdin.readline
n, k = map(int, input().split())
dp = [float('inf')]*(k+1) # dp[i]를 만드는 최소 동전의 수
dp[0] = 0
coins = [int(input()) for _ in range(n)]
coins.sort()

for c in coins:
    if c > k: break
    for i in range(c, k+1):
        if 1 + dp[i-c] < dp[i]: dp[i] = 1 + dp[i-c]
print(dp[k] if dp[k] != float('inf') else -1)