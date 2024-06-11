'''
n*n
술래 처음에 중앙
m 도망자(좌우 이동하는 사람은 오른쪽 방향 시작 or 상하 이동하는 사람은 아래 방향 시작)
h개의 나무, 도망자와 초기에 겹쳐져 주어질 수 있음
(m명의 도망자 동시에 움직, 술래 움직) 총 k번 반복

1) m명의 도망자 중, 술래와 거리가 3이하인 도망자만 움직임
|x1 - x2| + |y1 - y2|
2-1) 현재 바라보고 있는 방향으로 1 움직일 때 격자 내부일 때
    2-1-1) 움직이려는 칸에 술래 없으면, 이동(나무 있어도 됨)
2-2) 격자 벗어남
    2-2-1) 방향 반대로 틀어줌, 이후 1움직일 때 술래 없다면 1 이동
3) 술래는 중심부터 시계 달팽이 경로로 1 움직임. 달팽이 끝 도착 시, 다시 거꾸로 중심으로 이동
    4) 이동 후의 위치가 이동방향 틀어지는 지점이면, 방향 바로 틀기.
    5) 이동 후의 위치가 양끝에 해당하는 위치 (0,0) 또는 정중앙에 도달하면, 방향 바로 틀어야 함
6) 턴을 넘기기 전에, 시야 내 도망자 잡음(현재 바라보는 방향 기준, 현재 칸 포함해 총 3칸)
6-1) 나무가 놓여 있는 칸이라면, !해당! 칸의 도망자 못 잡음. 뒷칸에는 영향 x
6-2) 잡힌 도망자 사라지고,
    술래는 t*x(t턴에서 잡힌 도망자 수x) 점수 얻음

k번 술래잡기 진행하는 동안, 술래가 얻게된 총점

틀린 이유: 2이면 d=0으로 바꿔줘야 함
'''
# board크기(홀수), 도망자, 나무, 라운드
# 이동 도중 도망자들의 위치는 겹칠 수 있음
n, m, h, k = map(int, input().split())
members = []
for _ in range(m):
    x, y, d = map(int, input().split())
    if d == 2: d = 0
    members.append([x-1, y-1, d])
trees = []
for _ in range(h):
    x, y = map(int, input().split())
    trees.append((x-1, y-1))
killed = [False] * m
dirs = [(1,0),(0,1),(-1,0),(0,-1)] # 하우상좌
# 1: 우좌우좌 1->3->1->3
# 2: 하상하상 2->0->2->0
answer = 0
pos = [n//2, n//2, 2, True] # x, y, 상, 시계방향
'''
1) m명의 도망자 중, 술래와 거리가 3이하인 도망자만 움직임
|x1 - x2| + |y1 - y2|
2-1) 현재 바라보고 있는 방향으로 1 움직일 때 격자 내부일 때
    2-1-1) 움직이려는 칸에 술래 없으면, 이동(나무 있어도 됨)
2-2) 격자 벗어남
    2-2-1) 방향 반대로 틀어줌!!!!, 이후 1움직일 때 술래 없다면 1 이동
'''
def move_members():
    for i in range(m):
        # 술래와 거리 3 이하
        if killed[i]: continue
        x, y, d = members[i]
        if abs(pos[0]-x)+abs(pos[1]-y) > 3: continue
        nx, ny = x+dirs[d][0], y+dirs[d][1]
        if not (0<=nx<n and 0<=ny<n):
            d = (d+2)%4
            nx, ny = x+dirs[d][0], y+dirs[d][1]
            members[i][2] = d
        if (pos[0], pos[1]) != (nx, ny):
            members[i][0], members[i][1]  = nx, ny

'''
3) 술래는 중심부터 시계 달팽이 경로로 1 움직임. 달팽이 끝 도착 시, 다시 거꾸로 중심으로 이동
4) 이동 후의 위치가 이동방향 틀어지는 지점이면, 방향 바로 틀기.
5) 이동 후의 위치가 양끝에 해당하는 위치 (0, 0) 또는 정중앙에 도달하면, 방향 바로 틀어야 함
시계 달팽이 상우하좌 2103 (-1)
반시계 달팽이 하우상좌 0123 (+1)

if flag == True and x==0 y==0일 때, flag=False, 다음 d=0
if flag == False and x==n//2 y==n//2일 때, flag=True, 다음 d=2
방향 바뀌는 지점 도착하면 flag=True일 때는 -1, False일 때 +1
'''
board = [[False]*n for _ in range(n)]
def chaser():
    x, y, d, _ = pos
    # 방향 바뀌는 지점 True로 표시
    dist, cnt = 1, 0
    # 2가 되면 dist+1, cnt=0. x,y (-1,0)이 되면 그만
    while True:
        for _ in range(dist):
            dx, dy = dirs[d]
            nx, ny = dx+x, dy+y
            if (nx, ny) == (-1, 0):
                return
            x, y = nx, ny
        cnt += 1
        board[x][y] = True
        d = (d-1)%4
        if cnt == 2:
            dist += 1
            cnt = 0

def move_snail():
    global pos
    x, y, d, flag = pos
    nx, ny = x+dirs[d][0], y+dirs[d][1]
    if board[nx][ny]: # 방향 바뀌는 지점
        if flag:
            d = (d-1)%4
        else:
            d = (d+1)%4
    elif nx == 0 and ny == 0:
        flag = False
        d = 0
    elif nx == n//2 and ny == n//2:
        flag = True
        d = 2
    pos = [nx, ny, d, flag]
'''
6) 턴을 넘기기 전에, 시야 내 도망자 잡음(현재 바라보는 방향 기준, 현재 칸 포함해 총 3칸)
6-1) 나무가 놓여 있는 칸이라면, !해당! 칸의 도망자 못 잡음. 뒷칸에는 영향 x
6-2) 잡힌 도망자 사라지고,
    술래는 t*x(t턴에서 잡힌 도망자 수x) 점수 얻음
'''
def catch_members(rnd):
    x, y, d, _ = pos
    area = [(x, y)]
    for _ in range(2):
        x, y = x+dirs[d][0], y+dirs[d][1]
        area.append((x, y))
    cnt = 0
    for i in range(m):
        if killed[i]: continue
        x, y = members[i][0], members[i][1]
        if (x, y) in area and (x, y) not in trees:
            killed[i] = True
            cnt += 1
    
    return rnd*cnt

chaser() # x, y, 순방향 -> 바꿔줌      
for rnd in range(1, k+1):
    move_members() # not killed, 도망자와 3거리 이하
    move_snail()
    answer += catch_members(rnd) # not killed, 나무 없으면 잡기
    if False not in killed: break
print(answer)