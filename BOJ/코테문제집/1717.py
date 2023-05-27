# 집합의 표현
# n+1개의 집합 {0},{1},...{n} 존재
# 합집합 연산과, 두 원소가 같은 집합에 포함되어 있는지 확인 연산
# 0 a b: 합집합 연산(a가 포함된 집합과 b가 포함된 집합 합치자)
# 1 a b: 두 원소가 같은 집합에 포함돼 있는지 확인 =>"YES", "NO"출력
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline

def find_parent(x):
    p = x
    if parent[x] != x: # 스스로가 루트가 아니면 루트 찾아나감
        p = find_parent(parent[x])
        parent[x] = p # 부모 테이블 갱신
    return p

def union_parent(a, b):
    p1, p2 = find_parent(a), find_parent(b)
    if p1 != p2:
        if p1 > p2: p1, p2 = p2, p1
        parent[p2] = p1 # 큰 숫자가 작은 숫자 가리키게 함
    
n, m = map(int, input().split()) # n:0~n 숫자 집합. m: 연산 수
parent = [range(n+1)] # 자신을 부모로 가지는 parent tb
for _ in range(m):
    op, a, b = map(int, input().split())
    if op == 0: union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
    