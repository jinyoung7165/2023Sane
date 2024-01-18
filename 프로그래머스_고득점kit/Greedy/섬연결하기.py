# n개 섬 사이 다리 건설 비용
# 최소 비용으로 모든 섬 -> 도달 가능해야 함 (A->B->C일 때, A->C 통행 가능)
# MST. 간선 n-1개 선택해야 함. 노드는 n개 선택
# 1. Prim 알고리즘(node기준)
# 특정 node 중심에서 거리 짧은 간선 선택해서
# 다음 node 방문하지 않았으면 포함
# 전체 node 포함할 때까지만 실행
import heapq
from collections import defaultdict
def solution(n, costs):
    graph = defaultdict(list)
    for u, v, c in costs:
        graph[u].append((v, c))
        graph[v].append((u, c))

    answer = 0
    que = []
    visited = [False] * n
    heapq.heappush(que, (0, 0))
    while False in visited: # 모든 노드 방문 시 즉시 종료
        cost, cur = heapq.heappop(que)
        if not visited[cur]: # 방문하지 않았으면 간선 선택
            visited[cur] = True
            answer += cost
            for node, c in graph[cur]:
                if not visited[node]: # 방문하지 않았으면 (최적화)
                    heapq.heappush(que, (c, node))
    return answer

# 2. Kruskal 알고리즘(간선 기준)
# 최소 간선부터 선택하며, cycle 생성 시 제거 (Union Find)
# => cycle 생성하지 않는 최소 간선만 모이게 됨.
def solution(n, costs):
    answer = 0
    parent = [*range(n)] 
    def find_parent(x):
        if parent[x] != x: # 루트 찾을 때까지
            parent[x] = find_parent(parent[x])
        return parent[x]

    def union(x, y):
        x = find_parent(x)
        y = find_parent(y)
        if x == y: return False # 원래 같은 집합. cycle 발생
        elif x > y: x, y = y, x
        parent[y] = x
        return True # 병합 성공
    
    costs.sort(key=lambda x: (x[2]))
    for i in range(len(costs)): # 간선 작은 순으로 모든 노드 방문
        u, v, c = costs[i]
        if union(u, v): # cycle 발생하지 않으면 해당 간선 선택
            answer += c
    return answer