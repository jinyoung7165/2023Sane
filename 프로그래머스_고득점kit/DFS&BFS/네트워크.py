# A-B, B-C 연결 시 A-C 간접 연결 가능 -> A,B,C 같은 네트워크
# 컴터 개수, 연결 정보 주어질 때 -> 네트워크 집합 개수 반환
# 무방향 연결집합 찾기-> UNION FIND
# 간선 탐색하면서
# # 부모가 같으면 -> 같은 집합의 원소
# # 부모가 다르면 -> 합집합
from collections import defaultdict   

def find_parent(x):
    global parent
    if x != parent[x]: # 스스로를 부모로 가지지 않을 때, 부모의 부모(루트) 찾아나감
        parent[x] = find_parent(parent[x])
    return parent[x]
        
def union_parent(x, y):
    global parent
    x = find_parent(x) # 루트 찾아나감
    y = find_parent(y)
    if x == y: return # 이미 같은 집합
    if x > y: # x에 더 작은 숫자 두기 위함
        x, y = y, x
    parent[y] = x # y->x 연결
 
def solution(n, computers):
    graph = defaultdict(list)
    
    global parent
    parent = [i for i in range(n)]
    
    for i in range(n): # n개의 컴터에 대한 연결 정보
        # 연결할 때마다 union하는 게 오류 안 남 -> 작은 원소부터 삽입하기 때문에
        for j in range(n):
            if computers[i][j]:
                graph[i].append(j)
                union_parent(i, j)
    dic = defaultdict(int)            
    for i in parent:
        dic[find_parent(i)] += 1 # 특정 루트와 연결된 노드 개수
        
    
    return len(dic) # 루트 개수 == 집합 개수