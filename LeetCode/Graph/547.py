# Number of provinces
# 전형적 Union Find
# n*n isConnected 여부 1/0 주어짐
# 전체 덩어리 개수 return
'''
병합 후, 뭉텅이 개수 세는 방법 2가지
1. answer=0 초기화. 모든 병합 작업 종료 -> 한번더 find_parent
for i in range(size):
    find_parent(i)
answer = len(set(parent))

2. answer=모든 섬의 수. 병합할 때마다 덩어리 수-1
훨씬 효율적
'''
def findCircleNum(isConnected) -> int:
    size = len(isConnected)
    parent = [i for i in range(size)] # 자기 자신 부모
    answer = size # 모든 뭉텅이 수 = 모든 섬의 수 초기화!
    def find_parent(x):
        if parent[x] != x:
            parent[x] = find_parent(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find_parent(x), find_parent(y)
        if px == py: return False
        parent[py] = px
        return True # 병합

    for i in range(size-1):
        for j in range(i+1, size):
            if isConnected[i][j]:
                if union(i, j): answer -= 1 # 병합 시, 뭉텅이 수 감소
    return answer