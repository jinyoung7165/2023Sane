# 최소 스패닝 트리
# 그래프 주어졌을 때, 최소 스패닝 트리 구하라
# 모든 정점을 연결하는 부분 그래프 중 가중치 합 최소인 트리
# kruskal. tree->cycle없어야 함
# 최소 간선 구하고, cycle 생기면 버리기. 정점만 set에 넣어서는 cycle 일으키는 간선이 들어갔는지 파악 못함
# union find (disjoint set)
from sys import stdin
input = stdin.readline
v, e = map(int, input().split())

total = 0
graph = []
parent = [i for i in range(v+1)] # 정점은 1~v
for _ in range(e):
    graph.append(list(map(int, input().split())))
graph.sort(key=lambda x: int(x[2]))

def find_parent(x):
    if parent[x]!=x:
        parent[x] = find_parent(parent[x]) # 루트까지 찾아라
    return parent[x]

def union_parent(a, b):
    p1, p2 = find_parent(a), find_parent(b)
    if p1 != p2:
        if p1 > p2: p1, p2 = p2, p1
        parent[p2] = p1
        return True # 연결 성공
    return False # 이미 같은 집합
        
for u, v, c in graph:
    if union_parent(u, v):
        total += c
print(total)