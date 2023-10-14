'''
바이러스
노드 수, 네트워크 연결 정보 주어짐
1번 노드 통해 연결되는 노드 수 출력
'''
from sys import stdin
from collections import deque

input = stdin.readline
n = int(input())
e = int(input())
visited = set()
edges = [[]*(n+1) for _ in range(n+1)]
for _ in range(e):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

visited.add(1)
que = deque([(1)])
while que:
    cur = que.popleft()
    for node in edges[cur]:
        if node not in visited:
            visited.add(node)
            que.append((node))
print(len(visited)-1)