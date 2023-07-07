# 운동
# v개 노드 e개 간선
# 일방통행 간선
# 1~v 노드
# 운동하고 난 후 시작점으로 돌아오는 것이 좋음
# cycle 찾기를 원함
# cycle 이루는 도로 길이 합이 최소가 되도록
# 두 마을 왕복하는 경우도 cycle에 포함됨
# 2번 풀이 다익스트라(최단 거리이므로)
# 모든 출발점에 대해서. 경유할말 고민하는 건 똑같음
import heapq
from sys import stdin
from collections import defaultdict
input = stdin.readline

v, e = map(int, input().split())
M = float('inf')
que = []
graph = defaultdict(list)
dp = [[M]*(v+1) for _ in range(v+1)] # i->j 최단거리 배열
for _ in range(e):
    a, b, c = map(int, input().split())
    dp[a][b] = c # 경유 없이 거리
    graph[a].append((b, c))
    heapq.heappush(que, (c, a, b)) # 모든 출발 노드에 대해서 어차피 계산해야 하므로

answer = M
while que:
    c, start, cur = heapq.heappop(que) # 누적값, 시작점, 현재위치
    if start == cur: # 출발지와 현재 노드가 같음
        answer = c # heapq이므로 최소 가격이 나옴
        break
    if c > dp[start][cur]: continue
    for node, cost in graph[cur]: # 현재 위치에서 갈 수 있는 노드
        n_cost = cost + c
        # dp [start->node]일 때!!!!(경유 할지말지 고르는 거임)
        # dp [cur->node]가 아님!!!!!!
        if dp[start][node] > n_cost: # 더 최소의 경우에만 node 경유
            dp[start][node] = n_cost
            heapq.heappush(que, (n_cost, start, node))
            
print(answer if answer!=M else -1)
   
# 1번 풀이. 각 노드를 시작점으로 해서-> 자기까지 오는 최단 거리 모두 봐야 함
# 이를 위해 dp[i][j], 즉. 플로이드-와샬
# 시간 초과
# for _ in range(e):
#     a, b, c = map(int, input().split())
#     dp[a][b] = c
        
# answer = M
# for k in range(1, v+1): # 경유지 거치며 i->j 최소 갱신
#     for i in range(1, v+1): # 출발지
#         for j in range(1, v+1):
#             dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
            
# for i in range(1, v+1):
#     if dp[i][i]<M: answer = min(M, dp[i][i])
# print(answer if answer!=M else -1)