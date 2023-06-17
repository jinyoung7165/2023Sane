# 평범한 배낭
# n개 물건-> w무게, v가치
# 해당 물건을 배낭에 넣어 가면 v만큼 즐길 수 있음
# "최대 k만큼" 무게만 넣을 수 있음
# 가치 최댓값
# 넣어서 가치를 올리거나, 안 넣고 무게를 보존
# dp[i][j]: i원소까지 봤을 때 jcapa 가방의 최대 가치
# dp[i-1][j](i번째 챙김x), dp[i-1][j-w]+v(i번째 챙기기 위해 j-wcapa 가방의 최대 value+i번째 value)
# 한번 사용한 물건은 쓰지 않음
'''
7capa
3 6
4 8
5 12
6 13
'''
from sys import stdin
input = stdin.readline
n, k = map(int, input().split())
# 무게, 가치
elements = [list(map(int, input().split())) for _ in range(n)]
bag = [[0]*(k+1) for _ in range(n+1)] # i원소까지 봤을 때, jcapa 가방의 최대 가치
for i in range(1, n+1):
    for j in range(1, k+1):
        if elements[i-1][0]<=j: # capa 충족 시
            bag[i][j] = max(bag[i-1][j], bag[i-1][j-elements[i-1][0]]+elements[i-1][1])
        else:
            bag[i][j] = bag[i-1][j] # 챙기지 말고, jcapa 남은 상태
        
print(bag[n][k]) # n물건까지 봤을 때, kcapa 가방의 최대 가치