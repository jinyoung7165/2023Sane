# 이분 그래프
# 정점 집합을 둘로 분할, 각 집합에 속한 정점끼리 인접하지 않도록
# 이분그래프인지 아닌지 판별해라
# 인접 정점끼리 서로 다른 색으로 칠해. 모든 정점을 두 가지 색으로만 칠해야 함
# BFS-> 같은 레벨 정점끼리 같은 색
#  1
# 2 3
#  4
# 이것 또한 이분 그래프
# 그래프의 모든 노드가 연결되었단 가정x-> tree 여러 개일 수도 있음
from sys import stdin
from collections import defaultdict, deque
input = stdin.readline
tc = int(input())
for _ in range(tc):
    flag = True
    graph = defaultdict(list)
    v, e = map(int, input().split())
    for i in range(e):
        _u, _v = map(int, input().split())
        graph[_u].append(_v)
        graph[_v].append(_u)
    
    colors = [0]*(v+1) # -1 or 1
    # start를 1부터
    for i in range(1, v+1):
        if colors[i] == 0:
            que = deque([(i)])
            colors[i] = 1
            while que:
                u = que.popleft()
                while graph[u]:
                    node = graph[u].pop()
                    if colors[node] == 0: # 미방문
                        que.append((node))
                        colors[node] = -colors[u]
                    elif colors[node] == colors[u]: # 인접 노드가 현재 색과 같음
                        flag = False
                        break
                if not flag: break
    print("YES" if flag else "NO")