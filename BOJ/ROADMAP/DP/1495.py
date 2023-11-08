'''
기타리스트
n개 곡마다 볼륨 바꾸고 연주
각 곡마다 지정된 볼륨 변화 v[i]
p볼륨 -> i곡 연주할 때, p+-v[i] 로 연주 가능
0보다 작은 값, m보다 큰 값으로 볼륨 바꿀 수 없음
dfs의 0<=?<n 느낌
곡 개수N, 시작볼륨S, 최대볼륨M 주어짐
마지막 곡을 연주할 수 있는 볼륨 중 최댓값(여러 경우 중 최대)
모든 곡은 리스트에 적힌 순서대로 연주해야 함
마지막 곡 연주못하면 -1 출력
dfs... 생각했으나... 경우의 수 트리 그려보면 2**N(최대 50) -> 너무 큼
M 1000이하로 작은 수 주어짐 -> DP[i][j]: i node를 j 볼륨으로 만들 수 있는지 "여부". j 자체가 결과 볼륨이 됨
k는 i번째 원소의 주어진 차이. dp[i][j] = dp[i-1][j-k] 또는 dp[i-1][j+k]가 1이면 됨. 이때 0<=j-k, j+k<=M
'''
n, start, M = map(int, input().split())
sequence = list(map(int, input().split()))
dp = [[0] * (M+1) for _ in range(n+1)]
dp[0][start] = 1 # 0번째 곡을 start 볼륨으로 만들 수 있음
for i in range(1, n+1):
    k = sequence[i-1] # i번째 원소의 주어진 차이.(dp idx가 1부터 시작하기 때문에 input과 크기 차 -1)
    for j in range(M+1):
        if dp[i-1][j]: # i-1원소의 해당 볼륨 기준으로 i번째 원소의 j+k, j-k 볼륨 가능
            if 0 <= j-k:
                dp[i][j-k] = 1
            if j+k <= M:
                dp[i][j+k] = 1
answer = -1
for i in range(M, -1, -1):
    if dp[n][i]:
        answer = i
        break
print(answer)