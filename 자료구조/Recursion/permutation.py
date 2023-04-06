# 서로 다른 N개의 원소에서 R개를 중복없이 골라 순서대로 나열
from itertools import permutations

n, m = map(int, input().split())

result = list(map(list, permutations(range(1, n+1),m)))

for i in result:
    for j in i:
        print(j, end=' ')
    print()
    
'''
재귀(dfs) -> 1-m까지의 수 중 n개 뽑아라
'''
visited = [] # 방문한 수 기억

def dfs(): # 더 빠름
    if len(visited) == m: # 원하는 개수만큼 뽑았다
        print(' '.join(map(str, visited)))
        return
    
    for i in range(1, n+1):
        if i not in visited:
            visited.append(i)
            dfs()
            visited.pop()
dfs()

'''
재귀 visited -> 배열의 원소에 대한 순열 구해서 결과 배열
'''
# 배열의 원소에 대한 순열
def permutation(arr, r):
    arr = sorted(arr)
    visited = [0 for _ in range(len(arr))]

    def generate(chosen, visited):
        if len(chosen) == r:
            print(chosen)
            return
	
        for i in range(len(arr)):
            if not visited[i]:
                chosen.append(arr[i])
                visited[i] = 1 # 방문 처리
                generate(chosen, visited)
                visited[i] = 0
                chosen.pop()
    generate([], visited)