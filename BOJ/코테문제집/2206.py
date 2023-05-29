# 벽 부수고 이동하기
# 0: 이동 가능. 1: 벽
# (0,0)->(n-1,m-1) 최단경로 이동(시작, 끝 칸도 셈)
# 벽 최대 1개 부술 수 있음. 출발도착은 빈칸
# 도달 불가 시 -1 출력
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
# visited[i][j]: 벽을 부쉈을 때 (i,j)까지 최단 거리 or 안 해도 되면 걍 이동
from collections import deque # 이동 수(depth)같은 애들끼리 같이 확장

n, m = map(int, input().split())
board = []
for _ in range(n):
    row = input()
    tmp = []
    for i in row:
        tmp.append(int(i))
    board.append(tmp)
visited = [[[-1,-1] for _ in range(m)] for _ in range(n)] # (i,j)까지 올 때 벽 0개 부쉈을 때, 1개 부쉈을 때
visited[0][0][0] = 1 # 출발지 도착지도 포함해서 방문 수 셈
que = deque([(0, 0, 0)]) # x,y, 부순 벽 수

while que:
    x, y, cnt = que.popleft()
    if x==n-1 and y==m-1:
        print(visited[x][y][cnt])
        break
    
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny]==1: # 벽일 때
                if cnt==0: # 벽 부술 수 있음
                    que.append((nx, ny, 1))
                    visited[nx][ny][1] = visited[x][y][0] + 1 
            elif visited[nx][ny][cnt]==-1: # 방문 안한 빈칸일 때
                    que.append((nx, ny, cnt))
                    visited[nx][ny][cnt] = visited[x][y][cnt] + 1   
else:
    print(-1)