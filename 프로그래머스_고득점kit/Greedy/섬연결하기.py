# n개 섬 사이 다리 건설 비용
# 최소 비용으로 모든 섬 -> 도달 가능해야 함 (A->B->C일 때, A->C 통행 가능)
# Kruskal 알고리즘 -> 최소 간선부터 선택하며, cycle 생성 시 제거
# => cycle 생성하지 않는 최소 간선만 모이게 됨. 간선 n-1개 선택해야 함. 노드는 n개 선택
def solution(n, costs):
    # cost 작은 순으로 정렬
    costs.sort(key=lambda x: (x[2]))
    visited = set([costs[0][0]]) # cycle 판별. 출발점 하나 넣음
    answer = 0
    while len(visited) != n:
        print(costs)
        for u, v, c in costs:
            if u in visited and v in visited: # cycle이라 선택x
                continue
            if u in visited or v in visited: # 이미 방문한 노드 하나에 연결
                visited.add(u)
                visited.add(v)
                answer += c   
                break
            # 두 노드 모두 없으면 간선 cost 작더라도 다음 순회 기다려야 함
    return answer

import heapq
from collections import defaultdict
def solution(n, costs):
    answer = 0
    graph = defaultdict(list)
    visited = [False] * n
    que = []
    
    for u, v, c in costs:
        graph[u].append((v, c))
        graph[v].append((u, c))
    
    heapq.heappush(que, (0, 0)) # 비용, 현위치 0
    # 0 -> n-1 노드 모두 방문 가능해야 함
    # que로 어차피 가는 데에 최소 비용만 뽑음
    while False in visited: # 모두 방문 시 즉시 종료
        cost, node = heapq.heappop(que)
        if visited[node]: continue
        
        visited[node] = True
        answer += cost
        for ne, co in graph[node]:
            if visited[ne]: continue
            else:
                heapq.heappush(que, (co, ne))
    return answer
    
    