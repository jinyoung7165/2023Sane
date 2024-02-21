# 줄세우기
'''
n명 줄세울 것, 두명씩 비교한 결과만 가짐
ingress == 0인 것부터 먼저 줄 세울 수 있음
'''
from sys import stdin
from collections import deque
input = stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
ingress = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    ingress[b] += 1
que = deque([a for a in range(1, n+1) if ingress[a] == 0])
path = []
while que:
    cur = que.popleft()
    path.append(cur)
    if len(path) == n: break
    while graph[cur]:
        node = graph[cur].pop()
        ingress[node] -= 1
        if ingress[node] == 0: que.append(node)

print(*path)