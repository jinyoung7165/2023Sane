# 거스름돈
# 2, 5원짜리 거스름돈
# 무한정 많이 가지고 있음
# 동전 개수가 최소가 되도록 거슬러 줘야 함
# 거스름돈이 n인 경우. 최소 동전의 개수
# 15원 -> 5원 3개
# 14원 -> 5원 2개(10), 2원 2개(4)
# 13원 -> 5원 1개(5), 2원 4개(8)
# 7원 -> 5원 1개(5), 2원 1개(2)
n = int(input()) # 거스름돈 액수
ans = 0
f, t = n//5, n//2
MAX = float('inf')
dp = [MAX] * (n+1) # k원을 만들기 위한 개수

for i in range(1, t+1): # 2원 반드시 쓸 것
    dp[2*i] = min(i, dp[2*i])
    for j in range(1, f+1): # 5원 반드시 쓸 것
        dp[5*j] = min(j, dp[5*j])
        s = 2*i+5*j
        if s > n: break
        dp[s] = min(dp[s], dp[i*2]+dp[j*5])
        if dp[n] != MAX: break
        
if dp[n] == MAX: print(-1) # 거슬러 줄 수 없음
else: print(dp[n])