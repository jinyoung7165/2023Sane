'''
최소비용 구하기
N개의 도시. 한 도시->다른 도시 도착하는 M개 버스
a=>b도시 드는 버스 비용 최소화
간선 모두 양수 -> 다익스트라
누적 최소 비용으로 도착할 수 있는 노드 일단 꺼내기 -> 도착점이면 누적 비용이 정답
방문여부보다, distance dp로 비교해서 que에 넣는 게 메모리 훨씬 효율적
양방향이라는 말 없음
'''
import heapq
from sys import stdin
input = stdin.readline
n = int(input())
m = int(input())
distance = [[]*(n+1) for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    u, v, c = map(int, input().split())
    distance[u].append((v, c))
start, end = map(int, input().split())

que = []
heapq.heappush(que, (0, start)) # start->start 0
while que:
    cost, cur = heapq.heappop(que)
    if cur == end:
        print(cost)
        break
    if visited[cur]: continue
    visited[cur] = True
    for node, c in distance[cur]:
        if not visited[node]: # 어차피 최솟값만 뽑으므로, 방문여부만 저장함
            heapq.heappush(que, (cost+c, node))
    