# 이항 계수1
# 자연수n, 정수k 주어졌을 때 이항 계수 C(n,k)=nCk 구하라
# 0<=k<=n -> 이항 계수: n! / (k!(n-k)!)
# nCk = nC(n-k)
# n+1Ck+1 = nCk + nCk+1
# nCk = n-1Ck-1 + n-1Ck
n, k = map(int, input().split())
dp = [0] * (n+1)
dp[0] = 1
for i in range(1, n+1):
    dp[i] = dp[i-1] * i

print(dp[n]// (dp[k] * dp[n-k]))