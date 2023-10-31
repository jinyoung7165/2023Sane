'''
백조의 호수
호수는 차례로 녹는데, 매일 물과 접촉한 모든 빙판 녹음
두 공간 접촉하려면, 가로-세로 닿은 것만 생각
오직 물에서만 이동 가능함. 며칠 지나야 둘이 만날 수 있을까
. 물. x 빙판. L 백조
백조가 속한 . 영역끼리 닿아야 함 -> 2parent가 같으면 그만
.을 만나기 위해 기다려야 하는 day 수
.이 움직여야 함. 백조가 X로 둘러싸인 경우. 아무튼. 백조도 물위에 있음 -> 전파 가능
물이 이동하는 것을 BFS로 처리
'''
from sys import stdin
from collections import deque

def find_swan(swan_q, board):
    nxt_swan = deque() # 다음으로 swan이 탐색할 곳 저장(물과 인접한 빙판)
    while swan_q: # 현재 swan의 area 전달
        x,y = swan_q.popleft()
        if x == ex and y == ey: # 현재 swan area에 다음 swan존재 시
            return True, None
        # 다른 swan 찾았으면 그만둬라
        # found flag True 전달
        
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if board[nx][ny] == 'X':
                    # 물과 인접한 빙판이면. 나중에 녹이고 swan의 area에 포함할 것
                    nxt_swan.append((nx,ny))
                else: # 현재 swan의 영역 확장
                    swan_q.append((nx,ny))
                visited[nx][ny] = True
    # 현재 swan이 지금area에서 다른 swan 못찾았음
    # 현재area와 닿은 빙판 녹이고 거기서 탐색 시작. 다음 area 전달
    return False, nxt_swan    

def melt(water_q, board): # 현재 물 모든 위치 가지고 있음 -> 확장할 필요 없음
    # 다음 날 녹일 인접 빙하 찾기
    nxt_water = deque()
    while water_q:
        x,y = water_q.popleft()
        for dx,dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == 'X':
                nxt_water.append((nx,ny)) # 물과 인접한 빙판 다음에 녹일 것
                board[nx][ny] = '.'
                
    return nxt_water

input = stdin.readline
dirs = [(-1,0),(1,0),(0,-1),(0,1)]

n,m = map(int,input().split())
board = []
swan = [] # 두 개 위치 파악
swan_q = deque()
water_q = deque()

for i in range(n):
    row = list(input().rstrip())
    for j, info in enumerate(row):
        if info == '.' or info == 'L':
            water_q.append((i, j)) # 현재 모든 물 위치
        if info == 'L': # swan의 위치 박아두기
            swan.append((i, j))
    board.append(row)

day = 0
visited = [[False] * m for _ in range(n)]

sx, sy = swan[0]
ex, ey = swan[1]
swan_q.append((sx,sy)) # swan이 탐색 시작할 곳 -> area 확장해나감
visited[sx][sy] = True

while True: # 물이 얼음 녹임. swan이 영역 확장하며 다른 swan 찾아감은 별개
    found, nxt_swan = find_swan(swan_q, board)
    # swan이 존재 가능한 area에서 탐색 시작 -> 다음 날 탐색 시작할 area 확장해 전달받기
    if found: break # endswan 찾았으면 그만둬라
    swan_q = nxt_swan
    
    day += 1 # 현재 water와 인접한 빙하 녹일 것
    water_q = melt(water_q, board)
    # 현재 물 근처 얼음 위치 녹이기 -> 다음날 물이 될 위치 전달 받기

print(day)