# 행렬 곱셈 순서
# n*m행렬 a와 m*k행렬 b 주어짐
# 필요한 곱셈 연산의 수는 n*m*k번
# 행렬n개를 곱하는데 필요한 곱셈 연산의 수는 곱 순서에 따라 달라짐
# 5*3 a, 3*2 b, 2*6 c인 경우, 행렬의 곱 abc를 구할 때
# ab먼저 곱하고, c곱하는 경우 (ab)c 곱셈 연산의 수
# 5*3*2+ 5*2*6 = 30+60 = 90
# 'a[0]*a[1]' *b[1] + a[0]* 'c[0]*c[1]'
# 이전 s + 이전 뭉탱이[0]*현재[0]*현재[1]

# bc 먼저 곱하고 a 곱하는 경우 a(bc) 곱셈 연산의 수
# 3*2*6 + 5*3*6 = 36+90=126
# b[0]*'c[0]*c[1]' + 'a[0]*a[1]' *c[1]
# 이전 s + 직전 원소[0]*현재[0]*현재[1] + 이전 뭉탱이[0]*직전 원소[0]*현재[1]

# 행렬 n개 주어졌을 때, 모든 행렬을 곱하는데 필요한 곱셈 연산 횟수의 최솟값
# 입력으로 주어진 행렬의 순서 바꾸면 안됨. n-1가지 합치기(괄호)
# dp[i][j] : i~j 곱셈
'''
a b c d 행렬. 곱은 2 원소씩 가능
(a) (bc)d)
(ab) (cd)
(ab)c) d
-> 이 중 최소가 abcd 최솟값
-> 0~1, 1~2, 2~3 곱 먼저 계산 가능(두 원소의 곱. gap 1)
-> 0~2, 1~3  최소 비교해 계산 가능(gap2)
-> 0~3 (abcd) (0~1+1~3, 0~2+2~3)최소 비교해 계산 가능(gap3=n-1)
[0] [0] [1]
합, 1*3행렬
(ab)c)    d
(a(bc))   d
'''
from sys import stdin
input = stdin.readline
n = int(input())
# a[1]==b[0] -> a[0]*b[1]*공통
# n-1번 합
li = [list(map(int, input().split())) for _ in range(n)]
M = 2**32
dp = [[0]*n for _ in range(n)] # i~j까지 연산 결과
for gap in range(1, n): # n-1 종류의 묶기. gap:1~n-1로 넓혀갈 것
    for i in range(n-gap): # n-gap회 실행. n4, gap1일 때 3회 실행
        j = i+gap
        result = M
        for k in range(i, j): # k를 기준으로 조합. i~k이미 계산됨 -> [i~k] * [k+1~j]
            result = min(result, dp[i][k] + dp[k+1][j] + li[i][0]*li[k][1]*li[j][1])
        dp[i][j] = result
print(dp[0][n-1])