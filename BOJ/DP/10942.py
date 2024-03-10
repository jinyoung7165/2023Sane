# 팰린드롬?
'''
n개 숫자 적고, 질문 총 m번
s~e번째 수(1~n)까지가 팰린드롬인지 -> 1/0
1213121
범위 계속 바꿔가며 질문 -> 미리 다 구해놓자
gap=0~n-1 * n만큼
'''
from sys import stdin
input = stdin.readline
n = int(input())
nums = list(map(int, input().split()))

dp = [[0]*n for _ in range(n)] # (i,j) i번째에서 시작할 때, j까지 팰린드롬인지

for i in range(n):
    dp[i][i] = 1
    if i == n-1: break
    if nums[i] == nums[i+1]: dp[i][i+1] = 1

for gap in range(2, n):
    for i in range(n-gap):
        if nums[i] == nums[i+gap] and dp[i+1][i+gap-1]:
            dp[i][i+gap] = 1

for _ in range(int(input())): # 질문 수 엄청 많음 -> 따로 저장x
    s, e = map(int, input().split())
    print(dp[s-1][e-1])