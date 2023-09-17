'''
구슬 탈출 2
10번 이내. MAP 크기 작음
직사각형 보드.빨/파 하나씩. 빨간 구슬을 빼내는 게임
파랑 구슬보다 빨강 먼저 나와야 함
10번 이하로 움직여서 빼낼 수 없으면 -1
벽/정지상태구슬 마주치면 stop
##########
#.O....RB# => 같은 rnd에 rb 둘 다 구멍 들어가므로 -1
########## 
dfs 하나 재귀 끝날 때까지 너무 오래 기다려야 함
같은 깊이별로 움직여야함 -> BFS
##########
#.....RB## => 좌우로만 움직여서 계속 시간 낭비 -> VISIT체크
###O######
##########
벽. 구멍만 신경 쓰며 이동 -> 같은 좌표에 도착
: 둘 중 하나가 공 뚫었음. 더 많이 이동한 애가 뚫은 거. 한 칸 뒤로 가기
'''
from sys import stdin
from collections import deque
input = stdin.readline
dirs = [(1,0),(0,1), (-1,0), (0,-1)] # 0101
n, m = map(int, input().split())

RED, BLUE, HOLE = None, None, None
board = [list(input()) for _ in range(n)]

for i in range(1, n-1):
    for j in range(1, m-1):
        if board[i][j] == 'R':
            RED = (i, j)
            board[i][j] = '.'
        elif board[i][j] == 'B':
            BLUE = (i, j)
            board[i][j] = '.'
        elif board[i][j] == 'O':
            HOLE = (i, j)
    if RED and BLUE and HOLE: break
    
result = -1
visit = set()
que = deque([]) # rnd번호, red, blue 위치
que.append((1, RED[0], RED[1], BLUE[0], BLUE[1]))
visit.add((RED[0], RED[1], BLUE[0], BLUE[1]))

while que:
    rnd, rx, ry, bx, by = que.popleft()
    if rnd > 10: continue # 10이
    
    for dx, dy in dirs:
        # 이동 후 결과 좌표
        r_rx, r_ry, r_bx, r_by = rx, ry, bx, by
        r_cnt, b_cnt = 0, 0 # 공끼리 막지 못하고 지나쳤을 때, 되돌려야 함
        # 같은 좌표에 도착했을 때, 더 많이 이동한 애가 한 칸 뒤로 물리면 됨 
        blue_hole = False
        while board[r_rx + dx][r_ry + dy] != '#':
            r_cnt += 1
            r_rx += dx
            r_ry += dy
            if (r_rx, r_ry) == HOLE: break
        while board[r_bx + dx][r_by + dy] != '#':
            b_cnt += 1
            r_bx += dx
            r_by += dy
            if (r_bx, r_by) == HOLE:
                blue_hole = True
                break
        if blue_hole: continue # blue가 구멍에 빠지면 안됨
        
        if (r_rx, r_ry) == HOLE:
            result = rnd
            break
        if (r_rx, r_ry) == (r_bx, r_by): # 둘 중 하나가 지나쳐버림
            # 통과한 애가 한 칸만 뒤로 가면, 서로 겹치지 않음
            if r_cnt > b_cnt:
                r_rx -= dx
                r_ry -= dy
            else:
                r_bx -= dx
                r_by -= dy
            
        if ((r_rx, r_ry, r_bx, r_by)) not in visit:
            visit.add((r_rx, r_ry, r_bx, r_by))
            que.append((rnd+1, r_rx, r_ry, r_bx, r_by))
    if result != -1: break
print(result)


''' 시간 초과
que = deque([]) # rnd번호, 방향, red, blue 위치
for i in range(4):
    que.append((1, i, RED, BLUE))

while que:
    rnd, dir, red, blue = que.popleft()
    r_pos = [red, blue] # 최종 이동 후 pos
    seq = [0, 1] # red부터 이동
    # r, b 중 해당 방향쪽으로 치우친 애 먼저 이동
    mod = dir % 2
    if dirs[dir][mod] * red[mod] < dirs[dir][mod] * blue[mod]:
        seq = [1, 0] # blue부터 이동
    success = [False, False]
    dx, dy = dirs[dir]
    for flag in seq:
        x, y = r_pos[flag]
        while True:
            nx, ny = x+dx, y+dy
            if 1<=nx<n-1 and 1<=ny<m-1 and board[nx][ny] != '#':
                if (nx, ny) == HOLE:
                    success[flag] = True
                    x, y = nx, ny
                    break
                if (nx, ny) != r_pos[1-flag]:
                    x, y = nx, ny
                else:  break
            else: break
        r_pos[flag] = (x, y)
    if success[1]: continue # blue가 성공해버림
    if success[0]: # red 성공
        result = rnd
        break
    if rnd == 10: continue # 다른 방향에서 10rnd에 답 찾을 수 있기 때문에 break하면 안됨
    for i in range(4):
        que.append((rnd+1, i, r_pos[0], r_pos[1]))

print(result)
'''