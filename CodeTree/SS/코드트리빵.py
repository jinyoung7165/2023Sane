'''
M명. 1번 사람은 1분에, M번 사람은 M번에 SOURCE에서 출발해 편의점으로 이동
출발 시간이 되기 전까지 격자 밖에. 각자의 목적지 다름
N*N 크기 격자

1분 동안 1)2)3 순서대로 진행
1) 격자에 있는 사람들 대상. 모두 각자의 DEST 방향으로 1칸 움직임
최단 거리로 움직이며, 방법 여러가지면, 위왼우하 순서
최단거리 = 인접하며 이동 가능한 칸들 경로

2) 격자에 있는 사람들 대상. DEST 도착 시, 거기에 멈추고
 다른 사람들은 해당 DEST 방문 불가.
격자 사람들 이동 끝난 후에 막힘(미리 예약 배열)

3) T분이 <=M 만족하면, T사람은 DEST와 가장 가까운 SOURCE에 들어감
가장 가까운 SOURCE 여러 개면, R작은 순, C 작은 순으로 선택
시간이 들지 않음. 다른 사람들은 해당 SOURCE 방문 불가.
격자 사람들 이동 끝난 후에 막힘(미리 예약 배열)

1분부터 시작
총 몇 분 후에 모두 편의점에 도착하는지?

이동 도중, 동일 칸에 여러 명이 위치 가능
'''
from collections import deque

N, M = map(int, input().split()) # map크기, 사람수
board = [list(map(int, input().split())) for _ in range(N)] # 0 빈 1 SOURCE
DESTS = [] # 각자 목적지
for _ in range(M):
    a, b = map(int, input().split())
    a-=1
    b-=1
    DESTS.append([a, b])

members = [] # 보드 위 멤버들
arrived = [False]*M # 각자 도착했는지
dirs = [(-1,0),(0,-1),(0,1),(1,0)] # 위왼우하
visited = [[False]*N for _ in range(N)]
'''
1) 격자에 있는 사람들 대상. 모두 각자의 DEST 방향으로 1칸 움직임
최단 거리로 움직이며, 방법 여러가지면, 위왼우하 순서
최단거리 = 인접하며 이동 가능한 칸들 경로
'''
def move_members():
    for i in range(len(members)):
        if arrived[i]: continue
        for X in range(N):
            for Y in range(N):
                visited[X][Y] = False
        DEST = DESTS[i]
        x, y = members[i][0], members[i][1]
        que = deque([])

        for d in range(4): # 가능한 방향 초기화
            dx, dy = dirs[d]
            nx, ny = x+dx, y+dy
            if nx == DEST[0] and ny == DEST[1]: # 바로 목적지 도착
                arrived[i] = True
                members[i] = DEST
                blocked.add((DEST[0], DEST[1]))
                break
            if 0<=nx<N and 0<=ny<N and board[nx][ny] != 2:
                que.append((nx, ny, d))
                visited[nx][ny] = True

        if arrived[i]: continue

        while que:
            x, y, d = que.popleft()
            if x == DEST[0] and y == DEST[1]: # 최단 경로로 도착 -> d방향 선택
                break
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 2 and not visited[nx][ny]: # 막힌 곳이 아니면 갈 수 있음
                    que.append((nx, ny, d))
                    visited[nx][ny] = True

        members[i][0] += dirs[d][0]
        members[i][1] += dirs[d][1]

'''
3) T사람은 DEST와 가장 가까운 SOURCE에 들어감
가장 가까운 SOURCE 여러 개면, R작은 순, C 작은 순으로 선택
시간이 들지 않음. 다른 사람들은 해당 SOURCE 방문 불가.
격자 사람들 이동 끝난 후에 막힘(미리 예약 배열)
'''
def put_member(t):
    que = deque([])
    DEST = DESTS[t]
    que.append((DEST[0], DEST[1], 0))
    for i in range(N):
        for j in range(N):
            visited[i][j] = False
    visited[DEST[0]][DEST[1]] = True
    m_distance = float('inf')
    candidates = []
    while que:
        x, y, distance = que.popleft()
        if distance > m_distance: break
        if board[x][y] == 1:
            m_distance = distance
            candidates.append([x, y])
            continue
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<N and board[nx][ny] != 2 and not visited[nx][ny]:
                que.append((nx, ny, distance+1))
                visited[nx][ny] = True
    candidates.sort(key=lambda x:(x[0], x[1]))
    members.append(candidates[0])
    blocked.add(tuple(candidates[0]))


def block_map():
    for x, y in blocked:
        board[x][y] = 2
    blocked.clear()
t = 1
blocked= set()
while True:
    move_members() # on_board에 있는 멤버들 1칸씩 움직임
    if blocked: block_map() # blocked에 있는 곳 block
    if t <= M: put_member(t-1) # t번 멤버를 dest와 가장 가까운 source에 둠
    if False not in arrived:
        print(t)
        break
    if blocked: block_map() # blocked에 있는 곳 block
    t += 1