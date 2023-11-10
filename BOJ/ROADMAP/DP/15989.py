'''
123 더하기 4
정수n 주어졌을 때, 1,2,3 합으로 나타내는 방법의 수
정수 4를 1,2,3의 합으로 나타내는 방법 총 4가지
'''
dp = [1] * 10001 # 각 숫자가 되는 경우의 수 1개씩(1로만 이뤄짐)
for i in range(2, 10001):
    dp[i] += dp[i-2] # 2 더하는 경우

for i in range(3, 10001):
    dp[i] += dp[i-3] # 3 더하는 경우

for _ in range(int(input())):
    n = int(input())
    print(dp[n])