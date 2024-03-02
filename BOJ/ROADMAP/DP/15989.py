# 123 더하기 4
'''
정수 4를 1,2,3의 합으로 나타낼 것(1개 이상 사용)
조합
1+1+1+1
1+1+2
2+2
1+3
dp[i]: ?번째 원소를 사용해 i를 만드는 경우의 수
'''
from sys import stdin
input = stdin.readline
n = int(input())
targets = [int(input()) for _ in range(n)]
dp = [1] * 10001 # 각 숫자 1로만 이뤄진 경우 오직 1개
for i in range(2, 10001):
    dp[i] += dp[i-2]
for i in range(3, 10001):
    dp[i] += dp[i-3]

for ta in targets:
    print(dp[ta])