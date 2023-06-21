# 계단 오르기
# 아래 시작점부터 꼭대기의 도착점까지
# 각 계산에는 일정 점수->밟으면 획득
# 한번에 한 계단/두 계단 오를 수 있음
# 연속된 3개의 계단을 모두 밟을 수 없음
# 시작점은 계단에 포함x
# 도착점은 반드시 밟아야 함
# 총 점수의 최댓값
from sys import stdin
input = stdin.readline
n = int(input())
stairs = []
for i in range(n):
    stairs.append(int(input()))
# 제일 아래 계단부터 점수 주어짐(300개 이하의 계단)
# 10 20 15 25 10 "20"
# 마지막 계단 반드시 밟아야 함
# 직전 거 밟으면 그 이전 거 못 밟음
# 2개 전 거 밟으면 가능
# dp[i]: i번째 계단(마지막 계단) 밟았을 때, 그 이전 최대까지 비교해 누적

dp = [0]*(n+1)
dp[0] = stairs[0] # 0번 밟음
if n > 1: # 2개 이상일 때
    dp[1] = stairs[0]+stairs[1] # 1번 밟고, 그 앞도 밟아야 최대
if n > 2: # 3개 이상일 때
    dp[2] = max(stairs[1]+stairs[2], dp[0]+stairs[2]) # 2번 밟고, 1번 밟거나, 0번 밟아야 함

for i in range(3, n): # 4개 이상일 때
    # i번째 계단+2개 전 거 밟거나, i번째 계단+직전 거 밟음
    dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])
    
print(dp[n-1])