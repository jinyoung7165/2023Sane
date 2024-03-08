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
'''
# # # # #
# S . . #
# . # . #
# . . E #
# # # # #
s에서 오른=>밑 방향으로 E에 도착하는 것과, 밑=>오른 방향으로 E에 도착할 때 
최소 거울 수 동일. 어떤 방향을 먼저 선택했는지는 상관 없음 -> 2차원 배열만으로 충분
'''
from sys import stdin
import heapq
input = stdin.readline
dirs = [(0,1),(0,-1),(1,0),(-1,0)]
n, m = map(int, input().split())
board = [input().rstrip() for _ in range(m)]
def bfs(x, y):
    que = []
    visited = [[float('inf')]*n for _ in range(m)]
    heapq.heappush(que, (0, x, y, 0))
    heapq.heappush(que, (0, x, y, 1))
    heapq.heappush(que, (0, x, y, 2))
    heapq.heappush(que, (0, x, y, 3))
    visited[x][y] = 0
    while que:
        cnt, cx, cy, d = heapq.heappop(que) # 거울 수, i, j, dir
        if board[cx][cy] == 'C' and (cx, cy) != (x, y):
            return cnt
        # 출발지에서 사방으로 출발 -> 비록 현재 방향의 반대 방향으로는 바로 이동 불가지만, heapq가 걸러줄 것
        for i in range(4):
            nx, ny = cx+dirs[i][0], cy+dirs[i][1]
            if 0<=nx<m and 0<=ny<n and board[nx][ny] != '*':
                if d == i:
                    # 특정 지점 수직 방향으로 재방문, cnt가 같아도 이후 경로에 대한 최단 거울 수 다르기 때문에 방문해야 함
                    # 비용이 어차피 추가로 발생하지 않음
                    if visited[nx][ny] >= cnt:
                        visited[nx][ny] = cnt
                        heapq.heappush(que, (cnt, nx, ny, i))
                else:
                    # 최소 비용(거울 설치 cnt)를 구해야 하기 때문에, 비용을 줄일 수 있는 경우에만 재방문(=붙여도 되지만 시간 더 걸림)
                    if visited[nx][ny] > cnt+1:
                        visited[nx][ny] = cnt+1
                        heapq.heappush(que, (cnt+1, nx, ny, i))

for i in range(m):
    j = board[i].find('C')
    if j != -1:
        print(bfs(i, j))
        break