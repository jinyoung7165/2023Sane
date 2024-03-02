# 평범한 배낭
'''
n개의 물건 필요. w무게. v가치 가짐
최대 k만큼의 무게만 넣을 수 있음. 최대 가치를 구하라

방법1. dp[i][j]: item i까지 고려해서 무게 j를 만들었을 때의 최대 가치
= max(dp[i-1][j], item[i][1] + dp[i-1][j-item[i][0]])
현재 item 포함x 혹은, 포함 + 그만큼 무게를 줄인 누적최댓값

방법2. dp[i] : ?번째 원소까지 고려해서 무게 i를 만들었을 때의 최대 가치
for j in range(k-item[?]+1)
-> 이렇게 하면 ?번째 원소로 j무게를 만들었을 때의 결과가 j+?의 무게를 만들 때의 결과에 영향을 미침
=> ?번째 원소 이용해 만들 수 있는 가장 큰 무게부터 만들며 거꾸로 순회
'''
# 방법 2
from sys import stdin
input = stdin.readline
n, k = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(n)]
dp = [0] * (k+1)

for i in range(n): # i번째 원소 사용할 것
    for j in range(k, items[i][0]-1, -1): # item 무게 사용해 item 무게~k무게 만들 것(거꾸로 순회)
        dp[j] = max(dp[j], items[i][1] + dp[j-items[i][0]])

print(max(dp))

# 방법 1
elements = [list(map(int, input().split())) for _ in range(n)]
bag = [[0]*(k+1) for _ in range(n+1)] # i원소까지 봤을 때, jcapa 가방의 최대 가치
for i in range(1, n+1):
    for j in range(1, k+1):
        if elements[i-1][0]<=j: # capa 충족 시
            bag[i][j] = max(bag[i-1][j], bag[i-1][j-elements[i-1][0]]+elements[i-1][1])
        else:
            bag[i][j] = bag[i-1][j] # 챙기지 말고, jcapa 남은 상태
        
print(bag[n][k]) # n물건까지 봤을 때, kcapa 가방의 최대 가치