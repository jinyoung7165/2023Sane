# 마라톤 2
'''
n개 지점. 1번에서 시작해 모든 지점 순서대로 방문
중간 총 k개 지점 방문하지 않으려 함(연속 아니어도 됨)
단, 1번과 n번은 방문해야 함
최대 k개 건너뛰며 다닐 때, 최소 거리는?
|x1-x2|+|y1-y2|
여러 지점의 좌표 겹칠 수 있음. 위치 같아도, 다른 체크포인트로 셈
[1-B](a) + [B-N](b). a+b k이하
1~k개 건뛰했을 때, 구간(1~p, p~n)끼리의 최솟값 더해야 함
1~N + N~N일 수 있으니, 각자 자신에게 가는 거리는 0
'''
n, k = map(int, input().split()) # n = 3~500
pos = [list(map(int, input().split())) for _ in range(n)]
distance = [[0]*n for _ in range(n)]  # 두 점간 거리(누적합 아님)
for i in range(n-1):
    for j in range(i+1, n):
        distance[i][j] = abs(pos[i][0]-pos[j][0]) + abs(pos[i][1]-pos[j][1])
        distance[j][i] = distance[i][j]
        
dp = [[float('inf')]*(k+1) for _ in range(n)]
# 0~k개 스킵 수 남아있을 때, 각 노드까지의 최솟값
# 0까지 스킵수 k개 남아있을 때, 최소거리 0
for i in range(k+1): dp[0][i] = 0

# i번째 노드에서 남은 스킵이 j개일 때, 실제 스킵할 수 k
# 스킵 후, 도달한 칸은, i+k+1 (즉, i->i+k+1 직행), 남은 스킵의 수 j-k

# i+k+1까지 방문했을 때, j-k개의 skip이 남았을 때 최단 거리는,
# i번째 노드에서 j번의 스킵이 남을 때까지 방문한 누적거리합+직행거리
# i도달 시, j이상이 남아있을 수도 있지 않나? 그러면 어차피 최단거리가 아님(거리의 합이기 때문에, skip 쓸수록 최소)
# dp[i+k+1][j-k] = min(기존, dp[i][j] + distance[i][i+k+1])
for i in range(n-1): # i에서 출발할 때,
    for j in range(k+1): # j번의 skip 남아있을 때
        if dp[i][j] == float('inf'): continue # 최솟값으로 줄일 수 없음
        for c in range(j+1): # 실제로 건너뛸 칸 수
            if i+c+1 >= n: break # 건너뛰고 거리 초과시
            dp[i+c+1][j-c] = min(dp[i+c+1][j-c], dp[i][j] + distance[i][i+c+1])
            # 건너뛴 후, 스킵수 j-c. 현재 상태에(dp[i][j]) 직행 거리(i->i+c+1) 더함
print(dp[n-1][0]) # 마지막 노드까지, 모든 skip 다 써서 도달했을 때의 최단 거리