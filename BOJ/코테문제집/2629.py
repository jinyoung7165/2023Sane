# 양팔저울
# 추 주어졌을 때, 1, 4g 두 개의 추
# 추의 개수는 30이하
# 추의 무게는 500g이하
# 추의 개수별로 만들 수 있는 무게 리스트를 만들어주자.
# 무게를 확인하려하는 구슬 개수 주어짐
# 주어진 각 구슬 무게 확인가능하면 y, 아니면 n 출력
# 구슬+추 조합 = 추 조합이면 무게 확인 가능
# 1g 추, 4g 추
from sys import stdin
input = stdin.readline

n = int(input()) # 추 개수
weights = list(map(int, input().split())) # 가벼운 애들부터 주어짐(중복 가능)
k = int(input()) # 구슬 개수
balls = list(map(int, input().split())) # 예상 무게
result = ['N'] * k
dp = [[0] * ((i+1)*500 + 1) for i in range(n+1)]

# 3번째 추 볼 때->최대 1500(추 최대 무게 500)
# dp[i][j] = i 번째까지의 추를 놓았을 때, j 무게를 만들 수 있는지
# 추를 구슬과 같이 왼쪽에 놓았을 때, 추를 오른쪽에 놓았을 때, 추를 놓지 않았을 때
def dfs(idx, target): # idx추까지 봤을 때, target만큼 무게 만들 수 있는지
    if idx > n: return
    if dp[idx][target]: return # 이미 앞에서 만들어 본 무게
    dp[idx][target] = 1
    dfs(idx+1, target) # 이미 idx추로도 target무게 만들 수 있음->idx+1추까지 볼 때도 만들 수 있음
    dfs(idx+1, target+weights[idx-1]) # idx번째 추 더한 무게 만들 수 있음
    dfs(idx+1, abs(target-weights[idx-1])) # idx번째 추 뺀 무게 만들 수 있음

dfs(0, 0) # idx0 추부터 보며 0무게 만듦    
for idx, ball in enumerate(balls):
    if ball > n*500: continue
    if dp[n][ball] == 1:
        result[idx] = 'Y'
print(*result)