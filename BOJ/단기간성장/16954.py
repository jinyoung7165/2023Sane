# 움직이는 미로 탈출
# 8*8 체스판
# 빈/벽. 가장 왼 아래 -> 오른 위 이동
# 1초에 빈 칸으로 인접/대각선 이동 또는 그냥 서있기 가능
# 이동->벽 이동. 벽이 캐릭터가 있는 칸으로 이동 시 stop
# 가장 오른 위로 이동가능한지 1/0
# 일단 유저 가능한 곳에 옮겨 놓고, 벽도 개수만큼 움직인 후에
# 남아 있는 유저 없으면 0
# 벽을 que에 넣지말고, 상대적으로 개수가 적은 유저를 넣는 게 낫다 -> 이걸로 다음에 풀어보자
from sys import stdin
from collections import deque
input = stdin.readline
dirs = {0:(0,1), 1:(0,-1), 2:(1,0), 3:(-1,0), 4:(1,1), 5:(-1,1), 6:(1,-1), 7:(-1,-1)}
board = []
que = deque([])
start = (7, 0)
wall_cnt = 0
board = [list(input()) for _ in range(8)]
for i in range(7, -1, -1): # board 아래->위로 보면서 que에 넣기
    row = board[i]
    for j in range(8):
        if row[j] == '#':
            wall_cnt += 1
            que.append((i, j))
END = False
if wall_cnt == 0: END = True

def move(s, x, y):
    global END
    s.add((x, y))
    if x == 0 and y == 7:
        END = True
        return
    for i in range(8):
        dx, dy = dirs[i]
        nx, ny = x+dx, y+dy
        if 0<=nx<8 and 0<=ny<8 and board[nx][ny] == '.':
            if nx == 0 and ny == 7:
                END = True
                return
            s.add((nx, ny))

pos = set()
move(pos, *start)

tmp_cnt = 0 # 해당 초동안 움직인 벽 수
while que: # 벽 이동
    x, y = que.popleft()
    board[x][y] = '.' # 벽 해제
    if x == 7:
        wall_cnt -= 1
        if wall_cnt == 0: # 벽 없음
            if pos: END = True
            break
    else:
        tmp_cnt += 1
        board[x+1][y] = '#' # 벽
        if (x+1, y) in pos: # 주인공 가능한 자리였음
            pos.remove((x+1, y))
            if not pos: break # 주인공 설 자리 없음
        que.append((x+1, y))

    if tmp_cnt == wall_cnt: # 모든 벽 이동 끝남
        tmp_cnt = 0
        tmp_pos = set()
        for _x, _y in pos:
            move(tmp_pos, _x, _y)
            if END: break
        pos = tmp_pos

print(1 if END else 0)