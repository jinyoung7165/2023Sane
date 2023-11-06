'''
최소 스패닝 트리
모든 정점 연결하는 부분 그래프 중, 가중치 합이 최소인 tree
MST 구하는 2방법
1. Kruskal 크루스칼 - 정렬 -> 간선 기준 선택. cycle 발생하면 안됨(Union-Find)
2. Prim 프림 - 노드 기준 최소 간선 선택(PQ) -> 모든 노드 선택될 때까지
u-v 사이 간선 여러 개이므로 매번 입력할 때마다 min?? 그러지말고.. 그냥 append하자
메모리 제한 있으므로 que에 간선 10**6개 넣는 것 보다 한 번 정렬하자
'''
from sys import stdin

input = stdin.readline
M = float('inf')
v, e = map(int, input().split())

answer, cnt = 0, 0
parent = [range(v+1)]

def find_parent(x):
    if parent[x] != x: # 루트 찾을 때까지
        parent[x] = find_parent(parent[x])
    return parent[x]
    
def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x > y: x, y = y, x
    parent[y] = x
    return True

graph = [list(map(int, input().split())) for _ in range(e)]
graph.sort(key=lambda x: x[2]) # cost 작은 순으로 정렬

for u, n, c in graph:
    if find_parent(u) != find_parent(n):
        union(u, n)
        answer += c
        cnt += 1
        if cnt == v-1: break

print(answer)