# 퇴사 2
'''
n일 동안 조합해 "최대의 금액"
t동안 p얻을 수 있음
i일에 t기간-> i+t 부턴 가능. i+t-1까지는 선택 불가
i+t > n이면 불가능
dp[i]: i시간까지의 최대 수익
원소 1순회하며, dp[i+t-1]에 dp[i-1] + p를 전달
'''
from sys import stdin
input = stdin.readline
n = int(input())
time, pay = [], []
for _ in range(n):
    t, p = map(int, input().split())
    time.append(t) # n범위 몹시 크고, 정렬이 필요 없기 때문에 다른 배열로 입력받는 게 낫다
    pay.append(p)
dp = [0] * (n+1) # 각 숫자 1로만 이뤄진 경우 오직 1개

for i in range(n):
    t, p = time[i], pay[i]
    if i + t <= n: dp[i+t-1] = max(dp[i+t-1], dp[i-1]+p)
    dp[i+1] = max(dp[i+1], dp[i]) # 특정 기간 동안 원소를 선택하지 않는대도, 최대 누적값은 계속 유지돼야 함
print(dp[n])