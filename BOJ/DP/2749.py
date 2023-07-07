# 피보나치 수는 0과 1로 시작
# 0 1 1 2 3 5 8 13 21 ...
# n이 주어졌을 때, n번째 피보나치 수(n 0부터 시작)
# 10**6으로 나눈 나머지 출력하라
# dp = [0]*(n+1) 저장 시 O(N)이지만, 주어진 N 매우 커서 메모리 초과 문제
# dp 2칸짜리 만들거나 3칸짜리 만드는 것 고민
# 피보나치 수를 k로 나눈 나머지는 항상 주기를 가짐
# 주기 길이가 p일 때->n번째 피보나치 수를 m으로 나눈 나머지는
# n%p번째 피보나치 수를 m으로 나눈 나머지와 같음
# m=10**k일 때, k>2라면(여기선 6), 주기p는 항상 15*10**(k-1)
n = int(input())
dp = [0,1]
mod = 10**6
period = 15*(mod//10)
for i in range(2, period):
    dp.append(dp[i-1]+dp[i-2])
    dp[i] %= mod
print(dp[n%period])

# 메모리 초과
# from sys import setrecursionlimit
# setrecursionlimit(10**6)
# n = int(input())
# dp = [0]*(n+1)
# if n>0: dp[1] = 1
# def fibonacci(x):
#     if x < 2 or dp[x] > 0: return dp[x]
#     l, r = None, None
#     if dp[x-1]: # 계산 결과 존재 시 사용
#         r = dp[x-1]
#         l = dp[x-2]
#     else:
#         if dp[x-2]: l = dp[x-2]
#         else: l = fibonacci(x-1)
#         r = fibonacci(x-2)
#     dp[x] = l + r
#     return dp[x]
# print(fibonacci(n))