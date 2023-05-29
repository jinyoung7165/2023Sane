# 말이 되고픈 원숭이
# 말의 움직임 따라하고 싶음. 말은 장애물 뛰어넘을 수 있음
# 원숭이는 총 k번만 말처럼 움직일 수 있고, 그 외에는 인접한 칸으로만 이동 가능
# 대각선은 인접 칸 아님. (0,0)->(n-1,m-1)
# 최소 동작으로 말의 움직임(최대 k번)+인접칸움직임 갈 수 있는 방법
# 도착지에 갈 수 없는 경우 -1
# 0:평지, -1:장애물. 시작점과 도착점은 항상 평지
# deque로 이동수(depth)같은 애들끼리 확장하면. 늘 최소 이동 수. 방문한 곳 다시 갈 필요x
# 말처럼 이동 가능한 경우, 원숭이처럼 이동하는 경우 각각 경로를 처리해야 최소가 나옴
# visited[i][j][k]: (i,j)까지 horse만큼 k번 움직였을 때 최소 이동 거리
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
horse = [(1,2),(2,1),(1,-2),(-2,1),(-1,2),(2,-1),(-1,-2),(-2,-1)]

from sys import stdin
from collections import deque
input = stdin.readline

k = int(input()) # 말처럼 움직일 수 있는 횟수
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[[-1]*(k+1) for _ in range(m)] for _ in range(n)]
# 인접이동, 말처럼 이동 섞어서 방문한 곳에 기록
que = deque([(0, 0, 0)]) #x, y, horse움직임 count
visited[0][0][0] = 0 # start. horse 0번 썼을 때 방문 처리
while que:
    x, y, h = que.popleft()
    if x==n-1 and y==m-1:
        print(visited[n-1][m-1][h])
        break
    for dx, dy in dirs: # 인접 이동
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and board[nx][ny]==0 and visited[nx][ny][h]==-1:
            que.append((nx, ny, h))
            visited[nx][ny][h] = visited[x][y][h]+1 # 이전에 h만큼 horse썼을 때. 최소 이동수. 방문 처리
    if h < k: # 말처럼 이동 가능
        for dx, dy in horse:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and board[nx][ny]==0 and visited[nx][ny][h+1]==-1:
                que.append((nx, ny, h+1))
                visited[nx][ny][h+1] = visited[x][y][h]+1 # h만큼 horse썼을 때 방문 처리
else: # while문이 정상적으로 끝나는 경우에만 출력. 도착지 못 간 경우. break로 빠져나온 경우 else 실행x
    print(-1)