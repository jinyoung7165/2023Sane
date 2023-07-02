# 가스관
# 가스 파이프라인 설계
# r행 c열
# 7가지 기본 블록
# 양방향 가능. 각 칸 비어있거나, 기본 블록
# +는 특별 블록으로, 두방향(수직/수평)으로 흘러야 함
# 가스의 흐름이 유일한 경우만 입력으로 주어짐. 불필요한 블록 존재x
# 없어진 블록을 추가하면, 모든 관에 가스가 흐름
# m->z로 향하는 설계 완성 후,
# 블록 하나를 지움->지워진 위치, 원래 어떤 블록이었는지 구하라
# 빈 파이프 상하좌우 연결돼야 하면 십자
# 블록 1234는 들어가는 방향과 나오는 방향 다름
# 빈 칸일 때, 사방에 파이프 존재->십자가 두기
# 빈 칸일 때, 사방 중 두 방향의 파이프 존재& 
# 각 파이프별 나가는 방향 다르므로 미리 선택지 저장
# 들어가고, 나가는 방향 저장해버리면 파이프별 구분 못함
'''
Mㄱ
.ㄴ
M  Tㄱ
ㄴ(+)-|   + 지우면, MZ에서 도달하지 못하는 파이프들 생김 -> 걔네를 시작점으로 두고 한번더 탐색해야 함
Z-|.
-> MZ에서 냅다 탐색 시작 + 방문 못한 파이프에서 한번더 탐색해 가스 구멍 뚫린 위치 찾기

어느 방향으로 연결해야 하는지 check_list에 저장
check_list에 4방향이면, +가스관 필요
다른 경우에는 하나씩 대입하며 check_list에 저장된 방향과 일치하는지 검사 후 출력
'''
from sys import stdin
from collections import deque
input = stdin.readline
dirs = [(-1,0),(0,1),(1,0),(0,-1)] # 위,우,아래,왼
pipes = {'|':[0,2] ,'-':[1,3],
    '+':[0,1,2,3], 'M':[0,1,2,3], 'Z':[0,1,2,3],
    '1':[1,2], '2':[0,1], '3':[0,3], '4':[2,3]}
r, c = map(int, input().split())
board = []
start, check_list = [], []
fx, fy = None, None # 최종적으로 지워진 칸
visited = [[False]*c for _ in range(r)]
for i in range(r):
    tmp = input()
    if tmp.find('M') != -1:
        j = tmp.find('M')
        start.append((i, j))
    if tmp.find('Z') != -1:
        j = tmp.find('Z')
        start.append((i, j))
    board.append(tmp)
    
def bfs(x, y, dir_list):
    global fx, fy
    que = deque([(x, y, dir_list)]) # x,y, 나갈 수 있는 방향들
    visited[x][y] = True
    while que:
        x, y, dir_list = que.popleft()
        for dir in dir_list: # 현재 파이프에서 나갈 수 있는 방향 -> 나갔을 때 파이프가 존재해야 함
            dx, dy = dirs[dir]
            nx, ny = x+dx, y+dy
            if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:
                if board[nx][ny]!='.': # pipe
                    visited[nx][ny] = True
                    ndirs = pipes[board[nx][ny]] # 나갈 수 있는 방향들
                    que.append((nx, ny, ndirs))
                else: # 나갈 수 있는 방향으로 갔는데 다음 칸이 .일 때
                    # MZ의 경우 +방향과 동일하게 뒀기 때문에 다음칸이 .일수도 있음
                    if board[x][y] in 'MZ': continue
                    if not fx and not fy: # 빈칸/지워진 칸 등록돼 있지 않으면
                        fx, fy = nx, ny
                    ndir = (dir+2)%4 # 현재 나갈 수 있는 방향과 반대=지워진 파이프가 나갈 수 있는 방향
                    if ndir not in check_list:
                        check_list.append(ndir)

# 출발~도착지 이어지기만 하면 돼서, 둘 중 아무데서나 출발 가능
# 출발지나 도착지 옆이 지워졌을 수도 있음
# 가스관이 총 하난데 지워져버림->출발지/도착지에서 탐색 불가
for x, y in start: # M/Z에서 각각 출발(MZ의 경우 4방향)
    bfs(x, y, pipes[board[x][y]])
    
# for i in range(r):
#     for j in range(c): # MZ에서 출발했을 때 도달하지 못한 파이프에서 출발
#         if board[i][j] != '.' and not visited[i][j]:
#             bfs(i, j, pipes[board[i][j]])
check_list.sort() # 방향 dict를 오름차순으로 저장했기 때문
result = None
if len(check_list)==4: # 4방향으로 나갈 수 있어야 하면, +모양
    result = '+'
else:
    pipe_list = ['|','-','1','2','3','4']
    for pipe in pipe_list: # 각 pipe 끼워보며 나갈 수 있는 방향이 동일하면 정답
        if check_list == pipes[pipe]:
            result = pipe
            break
print(fx+1, fy+1, result)

# dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# pipes = {'|': '010 010 010', '-': '000 111 000',
#          '+': '010 111 010', 'M': '010 111 010', 'Z': '010 111 010',
#          '1': '000 011 010', '2': '010 011 000',
#          '3': '010 110 000', '4': '000 110 010'}

# def pipe_board(pipe):
#     return [list(row) for row in pipes[pipe].split()]

# r, c = map(int, input().split())
# board = [input().strip() for _ in range(r)]

# end = ([i for i, row in enumerate(board) if 'Z' in row][0], board[[i for i, row in enumerate(board) if 'Z' in row][0]].index('Z'))
# new_board = [['.' for _ in range(3 * c)] for _ in range(3 * r)]

# for i in range(r):
#     for j in range(c):
#         pipe = board[i][j]
#         if pipe != '.':
#             new_pipe = pipe_board(pipe)
#             for k in range(3):
#                 for l in range(3):
#                     new_board[3 * i + k][3 * j + l] = new_pipe[k][l]
