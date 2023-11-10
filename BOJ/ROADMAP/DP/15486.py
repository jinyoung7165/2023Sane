'''
퇴사 2
n일 동안 최대한 많은 수익을 얻게끔 참여
[[소요 시간, 수익]] 주어짐
i번째 원소 사용한다고 하면, i+소요시간 부터 다음 이용 가능
i 순회하며 dp[i+day] = max(dp[i+day], dp[i]+cost)
이전에 수행한 일끼리 비교
만약 [[2, 100], [2, 300]...] 주어지면
idx 5에 100기록, 3에 20 기록 가능하지만, 두 일 모두를 누적해서 사용해야 함
dp[i+day] = "i일 이전까지 나온 누적 최대" + i일에 주어진 cost
오늘 일 하되, 이전에 나온 누적 최대를 저장해놔야 함(dp[오늘]아님)
'''

from sys import stdin

input = stdin.readline

n = int(input())
day_cost = [list(map(int, input().split())) for _ in range(n)]
# 정렬 필요한 것도 아니고 그냥 day, cost 배열 나눠서 받는 게 훨씬 빠름
lastmax = 0 # 이전에 나온 누적일 중 최대
dp = [0] * (n+1) # n-1(마지막)일에 1일치 일 하면 n에 기록해야 함
for i in range(n):
    lastmax = max(dp[i], lastmax) # 현재까지의 누적 최댓값
    day, cost = day_cost[i]
    if day + i > n: continue
    dp[i+day] = max(dp[i+day], lastmax + cost)

print(max(dp[n], lastmax))