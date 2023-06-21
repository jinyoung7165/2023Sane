# 레이저 통신
# w*h 지도. 각 칸은 빈 칸/벽
# c로 표시된 칸 2개 존재
# 두 칸이 통신하기 위해 설치해야하는 '거울 개수 최솟값' 구하라
# 레이저는 c에서만 발사 가능. 빈 칸에 거울/\을 설치해서 방향을 90도 회전
# 빈칸., *벽, c레이저 연결해야 하는 칸
# 연결할 수 있는 입력만 주어짐
# 거울 개수 기준 탐색 필요
# c에서 레이저는 사방팔방으로 나올 수 있고 거울 설치해 대각선 이동 가능
# 이동수는 중요하지 않음. 도착까지 몇 번이나 방향 바꿔야 하는지
# 둘러와도, 방향만 적게 바꾸면 되는 것
import heapq
from sys import stdin
dirs = {0:(0,1), 1:(1,0), 2:(0,-1), 3:(-1,0)}
input = stdin.readline

que, graph = [], []
w, h = map(int, input().split())
M = float('inf')        
visited = [[M]*w for _ in range(h)]
start = (0, 0)
for i in range(h):
    row = input()
    graph.append(row)
    idx = row.find('C')
    if idx != -1 and not que:
        heapq.heappush(que, (0, i, idx, 0)) # 거울 수, i, j, dir
        heapq.heappush(que, (0, i, idx, 1))
        heapq.heappush(que, (0, i, idx, 2))
        heapq.heappush(que, (0, i, idx, 3))
        visited[i][idx] = 0
        start = (i, idx)
 
while que:
    cnt, x, y, d = heapq.heappop(que)
    if graph[x][y] == 'C' and (x,y) != start: # 도착
        print(cnt)
        break

    for i, dir in dirs.items():
        dx, dy = dir
        nx, ny = x+dx, y+dy # 다음칸 이동

        if 0<=nx<h and 0<=ny<w and graph[nx][ny] != '*': # 이동 가능
            if i == d: # 애초에 시작점에서 선택지가 4방향-> 같은 회전수로 같은 점 다른 경로로 재방문 가능함, 이후 벽 피하기 위해, 출발지에서의 초기방향에 따라 회전 필요 유무가 달라짐
                if visited[nx][ny] >= cnt:
                    visited[nx][ny] = cnt
                    heapq.heappush(que, (cnt, nx, ny, i))
            else:
                if visited[nx][ny] >= cnt+1:
                    visited[nx][ny] = cnt+1
                    heapq.heappush(que, (cnt+1, nx, ny, i))