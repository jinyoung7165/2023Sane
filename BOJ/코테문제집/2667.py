# 정사각형 지도. 1:집, 0:빈 곳
# 연결된(상하좌우) 집 모임:단지-> 번호를 붙이자
# 총단지수, 각 단지에 속하는 집의 수를 오름차순 정렬해 출력
# 지도 크기 5*5 ~25*25
from sys import stdin
input = stdin.readline
n = int(input())
graph = [[0]*n for _ in range(n)]
dir = [(0,1),(1,0),(0,-1),(-1,0)]
cnt = []

def dfs(x, y, path):
    if graph[x][y] == 1:
        graph[x][y] = -1 # 방문 처리
        path.add((x,y))
        for d in dir:
            nx, ny = x+d[0], y+d[1]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 1:
                dfs(nx, ny, path)
            
for i in range(n): # 행
    tmp = input()
    for j in range(n): # 열
        if tmp[j] == '1':
            graph[i][j] = 1
            
for i in range(n): # 행
    for j in range(n): # 열
        if graph[i][j] == 1:
            path = set()
            dfs(i, j, path)
            cnt.append(len(path))
print(len(cnt))
for c in sorted(cnt):
    print(c)