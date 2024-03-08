# 거울 설치
'''
최소 거울 수 구함 -> 엄청 많이 돌아와도 거울 수만 최소면 됨 -> heapq
양면 거울 설치할 수 있는 위치들 정해져 있음. 설치 or not
# -> # 연결
* 벽
. 직진
! 직진 or 양면 거울 설치해 반사(방향 90 전환)
visited에 해당 위치를 d방향으로 도달하기 위한 최소 거울 수 저장

# # # # #
# S . . #
# . # . #
# . . E #
# # # # #

s에서 오른=>밑 방향으로 E에 도착하는 것과, 밑=>오른 방향으로 E에 도착할 때 
최소 거울 수 다름. 어떤 방향을 먼저 선택했는지 상관 있음 => 3차원 visited 배열 필요
'''
# 이동 중, 알고보니 방향 바꿔야 했음을 어떻게 아는가? -DFS 대신, 
# 일단 사방으로 움직이며 기록하고, 이전 방향과 달라지면 거울을 설치한 것이다
from sys import stdin
import heapq
input = stdin.readline
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
n = int(input())
board = [input().rstrip() for _ in range(n)]
M = float('inf')
def bfs(x, y):
    que = []
    visited = [[[M,M,M,M] for _ in range(n)] for _ in range(n)]
    for i in range(4):
        heapq.heappush(que, (0, x, y, i))
        visited[x][y][i] = 0
    
    while que:
        cnt, cx, cy, d = heapq.heappop(que) # 거울 수, i, j, dir
        if board[cx][cy] == '#' and (cx, cy) != (x, y):
            return cnt
        for nd in range(4):
            nx, ny = cx+dirs[nd][0], cy+dirs[nd][1]
            if 0<=nx<n and 0<=ny<n and board[nx][ny] != '*' and visited[nx][ny][nd] > cnt:
                if d == nd:
                    visited[nx][ny][d] = cnt
                    heapq.heappush(que, (cnt, nx, ny, d))
                elif board[cx][cy] == '!' and visited[nx][ny][nd] > cnt+1:
                    visited[nx][ny][nd] = cnt+1
                    heapq.heappush(que, (cnt+1, nx, ny, nd))

for i in range(n):
    j = board[i].find('#')
    if j != -1:
        print(bfs(i, j))
        break

# visited 배열의 크기를 바꾸어 방향도 고려할 수 있게 된 것입니다.
# 각 위치와 방향에 대해 최소 거울 수를 저장함으로써 정확한 결과를 얻을 수 있습니다.
'''
for i in (0,1,3): # 반대 방향으로 가는 거 굳이 코드로 거르고 싶다면. range(4) 대신
    nd = (d+i)%4
    nx, ny = cx+dirs[nd][0], cy+dirs[nd][1]
    if 0<=nx<n and 0<=ny<n and board[nx][ny] != '*' and visited[nx][ny][nd] > cnt:
        if i == 0:
            visited[nx][ny][d] = cnt
            heapq.heappush(que, (cnt, nx, ny, d))
        elif visited[nx][ny][nd] > cnt+1:
            visited[nx][ny][nd] = cnt+1
            heapq.heappush(que, (cnt+1, nx, ny, nd))
    if board[cx][cy] != '!': break

'''