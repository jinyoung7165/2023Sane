# 가장 긴 감소하는 부분수열
# 수열 a가 주어졌을 때, 가장 긴 감소하는 부분 수열 구하라
# a={10,30,10,20,20,10}인 경우, {30,20,10}길이3
# 30 20 10 '1' '8' 1
# 이전 원소보다 감소하면, 이전 수열에 포함시키거나 지나쳐라
# dp[i] = dp[j] + 1
n = int(input())
a = list(map(int, input().split()))
dp = [1]*n
for i in range(1, n):
    for j in range(i):
        if a[i] < a[j]: # 감소
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))