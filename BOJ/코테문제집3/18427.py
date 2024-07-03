# 함께 블록 쌓기
'''
1~n명, 각자 최대 m개까지 블록 가짐
모든 블록들의 높이 서로 다를 수 있음
1~n이 하나씩 차례대로 블록 사용해 높이 h 만들 수 있는 경우의 수
어떤 학생 pass 가능, 한 학생당 최대 1 블록만 쌓음
'''
from sys import stdin
input = stdin.readline

n, m, h = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(h+1) for _ in range(n+1)]
# i번째 학생까지 만든 각 금액 경우의 수
for i in range(n+1):
    dp[i][0] = 1
# 1명일 때, dp를 n*h크기로 잡으면, i-1=자신이기 때문에 중복계산돼버림
for i in range(1, n+1):
    dp[i] = dp[i-1].copy()
    for k in blocks[i-1]:
        for val in range(k, h+1): # 조합해서 val값 만들 것
            dp[i][val] += dp[i-1][val-k]
print(dp[n][h] % 10007)