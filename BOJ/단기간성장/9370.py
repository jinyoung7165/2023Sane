# 미확인 도착지
# S지점에서 출발. 목적지 후보 주어짐
# G-H 교차로 사이의 도로를 지나갔음(최단 거리의 일부)
# 교차로 사이 도로 최대 1개
# 도착지로 가는 최단 거리 중, "G-H를 포함하는 경우 도착지" 구하라
# 목적지 후보 중 불가능한 경우를 제외한 목적지들을 오름차순으로 출력
# start->모든 정점으로 가며, dest비교+flag로 g-h 비교 시 시간 초과 문제
'''
s-> (g-h/h-g) 지나 목적지 t에 최단 거리로 도착하는 법
s->t 거리가 아래와 같으면 됨
s→g/h 까지의 최단거리 + →t 까지의 최단거리가 s→t 까지의 최단거리
'''
# 주의! s->t 이동불가(inf), 부분거리도 이동불가(inf)시 true -> 틀림
import heapq
from sys import stdin
from collections import defaultdict

M = float('inf')
input = stdin.readline

def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    visited = [M for _ in range(n + 1)] # start에서 출발 시 최단거리
    visited[start] = 0
    while que:  # flag: g-h 지나갔는지 여부
        cost, cur = heapq.heappop(que)
        if cost > visited[cur]: continue
        for node, dist in graph[cur]:
            cur_cost = cost + dist
            if visited[node] > cur_cost:
                visited[node] = cur_cost
                heapq.heappush(que, (cur_cost, node))
    return visited

for _ in range(int(input())):
    mid = M
    graph = defaultdict(list)
    candidates, result = set(), []
    
    n, m, t = map(int, input().split())  # 교차로vertex, 도로, 목적지 후보 수
    s, g, h = map(int, input().split())  # 출발지, g-h 사이의 도로 지나감
    for _ in range(m):  # 양방향 도로
        a, b, d = map(int, input().split())
        if a in {g, h} and b in {g, h}:
            mid = d
        graph[a].append((b, d))
        graph[b].append((a, d))
    for _ in range(t):  # 목적지 후보
        candidates.add(int(input()))

    # 각 출발지에서의 최단거리
    s_dist = dijkstra(s)
    mid_start = 0
    if s_dist[g] >= s_dist[h]: # s->h가 더 짧으면 s->h->g->dest (g가 다음start)
        mid_start = g
    else:
        mid_start = h
        
    mid_dist = dijkstra(mid_start)
    for candidate in candidates:
        if s_dist[candidate]<M:
            if s_dist[candidate] == (s_dist[mid_start] + mid_dist[candidate]):
                result.append(candidate)
    result.sort()
    print(*result)

'''
   while que:  # flag: g-h 지나갔는지 여부
        cost, cur, flag = heapq.heappop(que)
        if cost > visited[cur][0] or (visited[cur][0] == cost and not visited[cur][1]):
            continue
        visited[cur][0], visited[cur][1] = cost, flag
        if cur in candidates and flag:
            result.append(cur)

        for node, dist in graph[cur]:
            cur_cost = cost + dist
            new_flag = flag or ((cur in {g, h}) and (node in {g, h}))
            if visited[node][0] > cur_cost or (visited[node][0] == cur_cost and not visited[node][1]):
                heapq.heappush(que, (cur_cost, node, new_flag))
'''