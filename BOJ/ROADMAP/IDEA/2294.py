# 최소 개수
'''
12
1 2 5

1 5 12

12 + 1*3
5 * 3
'''
from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
answer = -1
M = float('inf')

dp = [M] * (k+1)
dp[0] = 0
for coin in coins:
    for i in range(coin, k+1):
        dp[i] = min(dp[i], dp[i-coin] + 1)
print(dp[k] if dp[k] != M else -1)