# Cheapest Flights Within K Stops
'''
src->dst 최대 k경유만 가능. 최단 비용 return
heapq: 최소 비용 기준 탐색
비용 최소 경로로 갔는데, 너무 많은 노드 경유하는 경우
-> 해당 노드를 더 큰 비용으로, "더 작은 경유 수로 재방문"해야 할 수 있음
=> distance가 작아지거나(heapq보장, 따로 안봐도 됨),
=> 경유 수count가 더 작아질 때 재방문!!!

최소 경유 수 기준이 아니기 때문에 count 바로 갱신 불가!!!
heapq에서 최소 비용 꺼냈을 때, 경유 수가 줄어든 경우, 그제서야 count 갱신
'''
import heapq
from collections import defaultdict
def findCheapestPrice(n, flights, src, dst, k) -> int:
    que = []
    M = float('inf')
    count = [M]*n # 특정 경유 수로 노드에 도착
    graph = defaultdict(list)
    for u, v, c in flights:
        graph[u].append((v, c))

    heapq.heappush(que, (0, 0, src)) # 비용, 경유 수, 노드
    while que:
        cost, path, cur = heapq.heappop(que) # 최소 비용(간선 가중치) 기준 이동
        if cur == dst: return cost
        if path >= k+1 or count[cur] <= path: continue # 경유수=k인데, 다음 v가 dst면 여전히 이동 가능, 경유 수 작아지는 경우에만 더 큰 비용으로 재방문 허용
        count[cur] = path # 경유 수 업데이트
        for v, c in graph[cur]:
            heapq.heappush(que, (c+cost, path+1, v))
    return -1