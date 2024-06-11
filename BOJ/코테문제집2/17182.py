# 우주 탐사선
'''
모든 노드 방문하는 거리 중 최소, 즉
모든 노드 간 최단 거리. n->n 플로이드 워셜
시작 행성 위치, 행성 간 시간 주어짐
0~n-1 행성
[i][j]: i->j 도달 시간

재방문 가능 -> 아래와 같을 때 0>1>0>2>0>3으로 방문하며, 답이 5
4 0
0 1 1 1
1 0 100 100
1 100 0 100
1 100 100 0

미리, 플로이드 워셜 dp[i][j]로 최종 최단 거리 구해놓음
-> visited 처리 하면서 모두 순회만 하면 됨
'''
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline
n, start = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited_all = int('1'*(n), 2)
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j: continue
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

answer = float('inf')
def dfs(cur, total, visited):
    global answer
    if visited == visited_all:
        answer = min(answer, total)
        return
    for i in range(n):
        if cur == i: continue
        if not (1<<i)&visited:
            dfs(i, total+graph[cur][i], visited|(1<<(i)))

dfs(start, 0, 1<<(start))
print(answer)