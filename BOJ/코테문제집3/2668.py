# 숫자고르기
'''
2*n 표
첫째 줄에는 1~n 차례대로
둘째 줄에는 1~n 범위 수 랜덤하게 있음
첫째 줄에서 숫자 최대한 많이 뽑음
뽑힌 수들 바로 밑 칸 수들이 이루는 집합 일치
1234567
3115546
(1,3,5) 뽑으면 됨 : 집합 크기 3
특정 숫자에서 출발해서, 자기 자신에게 돌아오면 됨
재방문 가능 -> dfs
'''
from sys import stdin

input = stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n):
    graph[i+1].append(int(input()))

selected = set()

def dfs(start, cur):
    for node in graph[cur]:
        if not visited[node]:
            visited[node] = True
            dfs(start, node)
        elif node == start: # 루트 재방문 발생
            for i in range(1, n+1):
                if visited[i]: selected.add(i)
            
for i in range(1, n+1):
    visited = [False] * (n+1)
    visited[i] = True
    dfs(i, i)

result = sorted(selected)
print(len(result))
for s in result: print(s)