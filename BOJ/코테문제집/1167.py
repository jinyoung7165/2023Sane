# 트리의 지름
# 임의의 두 점 사이 거리 중 가장 긴 것
# 시작점 중요x. 1번 노드->다른 모든 노드로 갈 때 길이 저장
# 1번 노드에서 가장 긴 노드까지의 거리 + 그 노드로부터 가장 긴 노드까지의 거리 = 트리의 지름
from sys import stdin
from collections import defaultdict, deque
graph = defaultdict(list)
input = stdin.readline
v = int(input())
for _ in range(v):
    edge = list(map(int, input().split()))
    node = edge[0]
    for i in range(1, len(edge)-1, 2):
        graph[node].append((edge[i], edge[i+1]))

def bfs(start): # 시작노드로부터 가장 먼 노드 구하기 * 2번
    answer = [0, 0] # 가장 큰 비용, 노드
    que = deque([(start, 0)]) # 현재 노드, 지금까지 비용
    distance =  [-1] * (v+1)
    distance[start] = 0
    while que:
        cur, c = que.popleft() # 노드, 가격
        if c > answer[0]:
            answer = [c, cur]
        for node, cost in graph[cur]:
            if distance[node] == -1: # 미방문
                n_cost = cost + c
                que.append((node, n_cost))
                distance[node] = n_cost
    return answer

dis, node = bfs(1) # 아무 노드 기준 가장 먼 노드 구하기
dis, node = bfs(node) # 해당 노드 기준 가장 먼 노드, 길이 구하기
print(dis)
