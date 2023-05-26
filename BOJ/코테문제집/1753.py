# 최단 경로
# 방향 그래프 주어지면, 주어진 시작점=>다른 모든 정점 최단경로
# 시작점 자신은 0, 경로 존재x시 INF 출력
# deque로 돌면 시간 초과
import heapq
from sys import stdin
input = stdin.readline
v, e = map(int, input().split()) # 정점, 간선
start = int(input()) # 시작 정점
INF = float('inf')
distance = [INF] * (v+1)
distance[start] = 0

graph = [[] for _ in range(v+1)]
for _ in range(e):
    i, j, c = map(int, input().split())
    graph[i].append((j, c))

que = []
heapq.heappush(que, (0, start))

while que:
    cost, cur = heapq.heappop(que)
    if distance[cur] < cost: continue
    for node, c in graph[cur]:
        new_c = cost+c
        if distance[node] > new_c:
            distance[node] = new_c 
            # 같은 점 사이 가중치 다른 여러 간선 존재 가능
            # 여기서 지정해주는 게 제일 메모리 효율 좋음
            heapq.heappush(que, (new_c, node))
            
for i in distance[1:]:
    print("INF" if i == INF else i)