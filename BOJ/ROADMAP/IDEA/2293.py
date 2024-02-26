# 동전1
# 동전 n 종류. 합 k원 만들고 싶음
# 경우의 수?
'''
n, k가 주어진다. (1 ≤ n ≤ 100, 1 ≤ k ≤ 10,000)
3 10
1
2
5
-> 10

dp[i][j]: j동전까지 고려했을 때, i원 만드는 경우의 수
dp[i-coin] 존재하면, dp[i]에 더함(거기에 coin 하나만 더하면 됨)
dp[coin] 무조건 1개 추가해야 함(coin*1) => dp[0]=1로 두면 됨
'''
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)] # 동전 종류

dp = [0] * (k+1) # 특정 coin무조건 쓸 때, k원 만들기 위한 경우의 수.
dp[0] = 1

for coin in coins:
    for i in range(coin, k+1): # i원 만들기 위한 경우의 수
        dp[i] += dp[i-coin] # i-coin원에 coin 하나만 더하면 됨
print(dp)