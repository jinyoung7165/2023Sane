# n개의 송전탑이 전선을 통해 하나의 트리 형태
# 전선 중 하나 끊어 전력망 네트워크를 2개로 분할
# 두 전력망이 갖게 되는 송전탑의 개수를 비슷하게 맞추자
# 두 망의 송전탑 개수 차를 return
# n=9, wires=[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
# -> 3 (6-3) : 3-4 또는 4-7 끊음
# n=4, wires=[[1,2],[2,3],[3,4]]
# -> 0 (2-2) : 2-3 끊음
# 간선을 두 개 이상 가진 노드의 간선을 끊어야 함
from collections import defaultdict

graph = defaultdict(list)

def dfs(v: int, visited: set):
    visited.add(v)
    for u in graph[v]:
        if u not in visited:
            dfs(u, visited)
        
def solution(n: int, wires: list):
    answer = n
    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)
        
    graph_sorted = sorted(graph.items(), key=lambda x: len(x[1]), reverse=True)
    length = len(graph_sorted[0])
    for v, edges in graph_sorted:
        if len(graph[v]) < length: break # 더 적은 간선 가지는 노드에 대해선 볼 필요 없음
        for e in edges:
            visited1 = set()
            visited2 = set()
            visited1.add(e)
            visited2.add(v)
            dfs(v, visited1)
            dfs(e, visited2)
            print(visited1, visited2)
            answer = min(answer, abs(len(visited1)-len(visited2)))
    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
#print(solution(4, [[1,2],[2,3],[3,4]]))
#print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))

'''
union find
'''
uf = []

def find(a):
    global uf
    if uf[a] < 0: return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb: return
    uf[pa] += uf[pb]
    uf[pb] = pa

def solution(n, wires):
    global uf
    answer = int(1e9)
    k = len(wires)
    for i in range(k):
        uf = [-1 for _ in range(n+1)]
        tmp = [wires[x] for x in range(k) if x != i]
        for a, b in tmp: merge(a, b)
        v = [x for x in uf[1:] if x < 0]
        answer = min(answer, abs(v[0]-v[1]))

    return answer