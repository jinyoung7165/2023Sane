'''
R*C 격자 (1,1)~(R,C)통 모양
맨 윗 ROW를 통해서만 통 안에 들어올 수 있음
십자가 모양의 탐사선(총 5칸). 중앙 제외한 부분 중 하나는 EXIT
정령은 어떤 방향에서든 탑승 가능하지만, 나갈 때는 EXIT으로만

I번째로 내려온 탐사선은 가장 윗 줄부터 시작해 센터가 CI열까지 내려옴
초기 출구는 DI 방향에 위치

1. 각 탐사선 하강: 정지할 때까지 무한 반복
1->2->3 순서대로 시도 후, 3도 안되면 종료
CHECK 다음 센터+센터의 사방 후 실제 이동 1번
1) 가능할 때만 남쪽으로 1칸 내려옴
2) 왼쪽으로 1칸 이동 -> 남쪽으로 1칸 이동 가능할 때만 회전하며 내려옴(EXIT 반시계 회전)
3) 오른쪽으로 1칸 이동 -> 남쪽으로 1칸 이동 가능할 때만 회전하며 내려옴(EXIT 시계 회전)
정지 후, 탐사선의 가장 윗 날개가 MAP 위에 존재 시, MAP 초기화 후 다음 탐사선 하강
(센터ROW-1 < 0 이라면, MAP위의 모든 탐사선 제거, 정령도 탐사 불가
MAP이 텅 비어도, 정령 최종 위치의 합 누적은 유지됨)

2. 각 탐사선 정지 후, 해당 탐사선의 정령이 바로 탐사 시작
각 탐사선 방문 여부 check
각 탐사선의 exit 상하좌우 인접한 곳에 다른 탐사선의 index 존재하는지
갈 수 있는 모든 칸 중, 가장 남쪽으로 이동 후 종료
정령의 최종 위치: 갈 수 있는 가장 아래 탐사선의 센터 ROW+1
정령들의 최종 위치의 합을 구해야 함

틀린 이유: 냅다 돌리는 게 아니라, 1칸 왼쪽으로 이동 가능한지 check + 그 자리에서 1칸 아래로 이동 가능한지 check 해줘야 함
좌우하만 확인하면 안됨, 상도 확인해야 함(옆으로 이동하는 경우 때문에)
Down할 때, exits[r_i]의 x좌표에만 +1 해주면 안 됨
구현할 때, 최대한 코드를 생략하지 말아라

# elif i == 2: return False # 하인데 행 조건 충족 x
# center 아래 날개 x는 최소 0, 최대 r-1까지 가능
해당 조건 먼저 넣어버리면
맨 위에서 좌회전 할 때도 걸려버려서 아예 하강 못 함
-> 일단 row가 0 미만일 때 상관없이 하강 한다고 치고
-> 최대한 내렸을 때 row확인해서 0 미만 1번만 체크해야 함
'''
from collections import deque

dirs = [(-1,0),(0,1),(1,0),(0,-1)] # 북동남서. +1 시계. -1반시계
R, C, K = map(int, input().split()) # 숲의 크기, 탐사선 수

rockets = [] # 각 탐사선의 센터
exits, ex_dirs = [[] for _ in range(K)], [] # 출구 위치, 방향
for i in range(K): # 출발 row, exit 방향(북동남서)
    a, b = map(int, input().split())
    rockets.append([-2, a-1]) # (r, c)
    ex_dirs.append(b)

scores = [0]*K
board = [[K]*C for _ in range(R)] # 탐사선은 INDEX로 표현할 것

def init_board():
    for i in range(R):
        for j in range(C):
            board[i][j] = K

def check(x, y): # 센터 기준 상좌우하 확인
    # row는 x<R, col은 0<=y<C 지켜야 함
    # center x는 최대 r-2까지 가능
    # center 아래 날개 x는 최소 0, 최대 r-1까지 가능
    if x>=R-1 or y<0 or y>=C: return False
    elif 0<=x and board[x][y] != K: return False

    for i in range(4): # 센터의 상하좌우 날개 확인
        nx, ny = x+dirs[i][0], y+dirs[i][1]
        if 0<=ny<C: # col 조건은 항상 만족해야 함
            if 0<=nx<R:
                if board[nx][ny] != K: return False
            # elif i == 2: return False # 하인데 행 조건 충족 x
        else: return False
    return True

def put_on_board(r_i):
    x, y = rockets[r_i]
    board[x][y] = r_i # 센터 색칠
    for dx, dy in dirs: board[x+dx][y+dy] = r_i # 날개 색칠

def down(r_i):
    center = rockets[r_i]
    e_d = ex_dirs[r_i]
    
    x, y = center[0]+1, center[1] # 새로운 센터
    if not check(x, y): return False

    rockets[r_i] = [x, y]
    exits[r_i] = [x+dirs[e_d][0], y+dirs[e_d][1]]
    return True
    
def leftdown(r_i):
    center = rockets[r_i]
    e_d = ex_dirs[r_i]
    
    # 좌측 이동 새로운 센터
    x, y = center[0], center[1]-1
    if not check(x, y): return False

    # 아래 이동 새로운 센터
    x, y = x+1, y
    if not check(x, y): return False

    rockets[r_i] = [x, y]
    # check true시, exit dir 반시계 회전
    e_d = (e_d - 1) % 4
    ex_dirs[r_i] = e_d
    exits[r_i] = [x+dirs[e_d][0], y+dirs[e_d][1]]
    return True

    
def rightdown(r_i):
    center = rockets[r_i]
    e_d = ex_dirs[r_i]
    
    # 우측 이동 새로운 센터
    x, y = center[0], center[1]+1 # 새로운 센터
    if not check(x, y): return False
    
    # 아래 이동 새로운 센터
    x, y = x+1, y
    if not check(x, y): return False
    
    rockets[r_i] = [x, y]
    # check true시, exit dir 시계 회전
    e_d = (e_d + 1) % 4
    ex_dirs[r_i] = e_d
    exits[r_i] = [x+dirs[e_d][0], y+dirs[e_d][1]]
    return True
    
def put_rocket(r_i):
    while True:
        if not down(r_i):
            if not leftdown(r_i):
                if not rightdown(r_i): break
    
    # 최대한 하강 후, center row-1이 0보다 작으면 false
    if rockets[r_i][0]-1 < 0: return False
    return True

def explore(r_i):
    que = deque([r_i])
    visited = [False] * K
    visited[r_i] = True
    row = 0
    while que:
        cur = que.popleft()
        center = rockets[cur]
        if center[0]+1 > row: row = center[0]+1 # 센터의 아래날개
        
        ex, ey = exits[cur]
        for dx, dy in dirs:
            nx, ny = ex+dx, ey+dy
            if 0<=nx<R and 0<=ny<C and board[nx][ny]!=K:
                if not visited[board[nx][ny]]:
                    que.append(board[nx][ny])
                    visited[board[nx][ny]] = True
    
    scores[r_i] = row+1 # 격자 row는 1~R로 간주

def solution():
    for i in range(K):
        # 탐사선 하강 성공 시, 탐사 시작
        # 그렇지 않으면, map 초기화
        if put_rocket(i):
            put_on_board(i) # board 색칠
            explore(i)
        else:
            init_board()

    print(sum(scores))
    
solution()