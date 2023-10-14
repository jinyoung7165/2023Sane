'''
DFS와 BFS
방문할 수 있는 정점이 여러 개인 경우, 작은 것 먼저 방문. 1~N번
'''
from sys import stdin
from collections import defaultdict, deque

input = stdin.readline

n, m, start = map(int, input().split()) # 정점, 간선 수, 시작 노드
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for key in graph:
    graph[key].sort()

visited = [start]

def dfs(cur):
    for node in graph[cur]:
        if node not in visited:
            visited.append(node)
            dfs(node)
        
dfs(start)
print(*visited)

visited = [start]
que = deque([(start)])
while que:
    cur = que.popleft()
    for node in graph[cur]:
        if node not in visited:
            visited.append(node)
            que.append((node))
        
print(*visited)