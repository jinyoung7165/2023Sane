# A-B, B-C 연결 시 A-C 간접 연결 가능 -> A,B,C 같은 네트워크
# 컴터 개수, 연결 정보 주어질 때 -> 네트워크 집합 개수 반환
# 무방향 연결집합 찾기-> UNION FIND
# 간선 탐색하면서
# # 부모가 같으면 -> 같은 집합의 원소
# # 부모가 다르면 -> 합집합 
# 네트워크 개수 return
# 뭉칠 때마다 1개씩 감소

def solution(n, computers):
    answer = n
    parent = [*range(n)]
    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]
    
    def union(x, y):
        px, py = find_parent(x), find_parent(y)
        if px != py:
            parent[py] = px
            return True
        return False
    
    for i in range(n-1):
        for j in range(i+1, n): # 자신 다음 원소랑 비교
            if computers[i][j] and union(i, j):
                answer -= 1
    return answer