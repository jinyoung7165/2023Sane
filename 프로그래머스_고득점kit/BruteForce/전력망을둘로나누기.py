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
루트 노드인 경우. uf배열에 -|집합 크기|(음수) 저장(find()시 자신=노드 번호 반환)
자식 노드인 경우. 루트 노드 번호(양수) 저장(find()시 루트노드 찾아 반환)
find 함수 -> 루트 노드 번호를 반환하는 것은 동일
uf배열에는 다른 거 저장
'''
uf = []

def find(a):
    global uf
    if uf[a] < 0: return a # 본인이 parent
    uf[a] = find(uf[a]) # 루트 노드 찾음
    return uf[a] # 루트 반환(양수 a 혹은, 음수로 합집합 개수)

def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb: return # 부모가 같음. 같은 집합.
    uf[pa] += uf[pb] # 부모 다르면 합집합 (-)개수만큼 커짐(음수)
    uf[pb] = pa # pa를 부모로 가리킴(양수). 루트 가리킴. merge

def solution(n, wires):
    global uf
    answer = int(1e9)
    k = len(wires)
    for i in range(k): # 간선 모두 순회하며 i간선 끊음
        uf = [-1 for _ in range(n+1)] # 부모 테이블 초기화. 모두 루트로서, -|집합크기1| 가짐
        tmp = [wires[x] for x in range(k) if x != i]
        for a, b in tmp: merge(a, b) # 간선 하나 제외하고 union find
        v = [x for x in uf[1:] if x < 0] # 0노드 제외하고, 루트 노드만 모음. 최대 2개
        # 루트 노드의 parent tb 값의 차 = 집합 노드 개수 차
        # 음수만 넣음(: -해당 집합 내 원소 개수)
        answer = min(answer, abs(v[0]-v[1])) # wires 트리 형식이라고 주어짐 -> 간선 하나 제거하면 반드시 루트 2개 나옴

    return answer