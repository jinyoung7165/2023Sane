# 퇴사
# n+1일째 되는 날 퇴사.
# n일 동안 최대한 많은 상담
# 하루에 하나씩 상담 잡아둠
# 각 상담 완료하는데 t기간, p금액
# i일에 t기간의 상담 시, (i+t)일부터 다시 상담 가능
# n+1일째부터는 상담 불가-> 그 전에 시작해도 안 끝나는 거 불가
# 최대 수익 구하라
# dp[i][0] = i번째 상담 시 다음 날짜, 최대 가격
# 5,50
# 4,40
# 3,30
# 2,20
# 1,10
# 1,10 (0, 50) -> 50+10 = 60
# 2,20 (0, 50)(5, 60) -> 60+20
# 3,30 -> 60+30
# 4,40 (6, 80)
# 5,50 (7, 90)
# dp[1] = (4,10) ->dp[4]=10
# dp[2] = (7,20) ->dp[7]=20(dp[1]아직 안 끝남)
# dp[3] = (4,10) ->dp[4]=10(dp[2]아직 안 끝남)
# dp[4] = (5,20) ->dp[5]=20
# dp[5] = (15,7)
from sys import stdin
input = stdin.readline

n = int(input())
dur_cost = list(map(int, input().split()) for _ in range(n))

dp = [0]*(n+1) # i번째 상담하거나, 안 하거나
for i in range(n):
    dur, cost = dur_cost[i]
    # dp[i+dur] : i번째 연산하지 않고 넘어갈 때랑, 누적 최대랑 비교
    dp[i+1] = max(dp[i+1], dp[i]) # i번째 연산하지 않고 넘어갈 때
    if i+dur <= n: # i번째 연산 수행
        dp[i+dur] = max(dp[i+dur], dp[i]+cost)
print(max(dp))

# 메모리 효율, 시간 효율 배열 2개 쪼개는 것이 나음
'''
from sys import stdin

input = stdin.readline
n = int(input())

t, p = [], []
dp = [0 for _ in range(n+1)] #n+1일까지의 최대 수익

for _ in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

m = 0 #현재까지의 최대 수익
for i in range(n):
    m = max(m, dp[i]) #이미 누적돼 있을 경우 비교
    if i + t[i] > n: continue #n일 넘기면 누적x
    #현재 강의 선택 시 다음 강의에 영향을 줌 다음 강의가 이미 큰 경우 현재 선택x
    dp[i+t[i]] = max(m+p[i], dp[i+t[i]])

print(max(dp))

'''