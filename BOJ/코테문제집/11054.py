# 수열이 어떤 수(sk) 기준으로 s1<s2<...sk-1<sk>sk+1>...sn 만족
# {10,20,"30",25,20}, {10,20,30,40,"50",40,25,10}
# 수열 a가 주어졌을 때 그 부분 수열 중 가장 긴 바이토닉 수열 길이
# -> 증가하는 부분 수열 길이
# <- 증가하는 부분 수열 길이
# dp[i]: i번째까지 봤을 때 증가하는 부분 수열의 최대 길이. 해당 부분 수열에 자신이 낄 수도 있고, 안 낄 수도 있음
n = int(input())
seq = list(map(int, input().split()))
dp1 = [1]*n
dp2 = [1]*n
for i in range(n): # 0~n
    for j in range(0, i): # 0~i-1
        if seq[i] > seq[j]: # 이전보다 커지면 이전에 나온 증가하는 부분 수열에 끼거나. 말자
            dp1[i] = max(dp1[i], dp1[j]+1)
for i in range(n-1,-1,-1): # 거꾸로 순회
    for j in range(n-1, i, -1): # n-1~i+1
        if seq[i] > seq[j]: # 이전보다 커지면 이전에 나온 증가하는 부분 수열에 끼거나. 말자
            dp2[i] = max(dp2[i], dp2[j]+1)
m = 0
for a, b in zip(dp1, dp2):
    m = max(m, a+b)

print(m-1)