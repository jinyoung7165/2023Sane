# 팰린드롬?
from sys import stdin

input = stdin.readline

n = int(input())
li = list(map(int, input().split()))
m = int(input())
dp = [[0]*(n+1)for _ in range(n+1)]
for i in range(1, n+1):
  dp[i][i] = 1
  if i < n and li[i-1] == li[i]:
    dp[i][i+1] = 1
# 1 2 3 gap=2
# dp[2][2] 1+2//2
# 1 2 3 4 gap=2
# dp[2][3] 1+1    
for gap in range(2, n):
  for i in range(1, n-gap+1):
    j = i+gap
    if li[i-1] == li[j-1]: # 양 끝 수가 같음
        #  (i+1~i+1+(gap-2))
        if dp[i+1][j-1] == 1:
            dp[i][j] = 1
for _ in range(m):
  s, e = map(int, input().split())
  print(dp[s][e])