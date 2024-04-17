'''
M참가자
(1,1)~(N,N) 미로
빈칸: 이동 가능
벽: 1~9내구도. 회전 시 1씩 감소. 0 -> 빈 칸으로 변경
출구: 참가자가 도착하면 즉시 탈출

k초 동안 아래를 반복 -> k초 전, 모든 참가자 탈출 시 게임 종료
게임 종료 시, 모든 참가자들의 이동 거리 합과 출구 좌표 출력

1) 1초마다 모든 참가자 4방 빈칸으로 1씩 움직임
두 점 간 최단거리는 abs(x1-x2) + abs(y1-y2)
목적지는 현재 위치보다 출구까지의 최단 거리가 가까워야 함
목적지 여러 개 가능하면, 상하로 움직이는 것 우선시
움직일 수 없음 가만히
한 칸에 여러 참가자 가능

2) 미로 회전
1명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 선택
여러 개면, r 작은 것 우선, 여러 개면, c 작은 것 우선
선택된 정사각형은 시계 90도 회전 -> 회전된 벽은 내구도 -1

돌릴 때 멤버도 함께 돌아감 -> [좌표: 존재하는 멤버들 수] 기록 필요
'''
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# 0:빈칸, 1~9:벽 내구도
members = []
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    members.append([x, y])
x, y = map(int, input().split())
OUT = [x - 1, y - 1]
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
escaped = [False] * M
distance_all = 0


def check_escape():
    for i in range(M):
        if escaped[i]:
            continue
        x, y = members[i]
        if x == OUT[0] and y == OUT[1]:
            escaped[i] = True


'''
1) 1초마다 모든 참가자 4방 빈칸으로 1씩 움직임
두 점 간 최단거리는 abs(x1-x2) + abs(y1-y2)
목적지는 현재 위치보다 출구까지의 최단 거리가 가까워야 함
목적지 여러 개 가능하면, 상하로 움직이는 것 우선시
움직일 수 없음 가만히
한 칸에 여러 참가자 가능
'''
def move_members():
    global distance_all
    for i in range(M):
        if escaped[i]:
            continue
        x, y = members[i]
        cur_dis = abs(x - OUT[0]) + abs(y - OUT[1])
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                if abs(nx - OUT[0]) + abs(ny - OUT[1]) < cur_dis:
                    members[i] = [nx, ny]
                    distance_all += 1
                    break
    check_escape()


'''
2) 미로 회전
1명 이상의 참가자와 출구를 포함한 가장 작은 정사각형 선택
여러 개면, r 작은 것 우선, 여러 개면, c 작은 것 우선
선택된 정사각형은 시계 90도 회전 -> 회전된 벽은 내구도 -1
check_escape
'''


def rotate_out():
    global OUT
    # 크기, r, c
    size, r, c = 101, 0, 0
    ox, oy = OUT
    for sz in range(2, N+1): # 가장 작은 정사각형부터 만들기 시작
        for x1 in range(N-sz+1): # 좌상단 r
            for y1 in range(N-sz+1):
                x2, y2 = x1+sz-1, y1+sz-1
                if not (x1<=ox<=x2 and y1<=oy<=y2): continue # 출구 미포함
                # 한 명의 멤버라도 포함인지
                for i in range(M):
                    if escaped[i]: continue
                    mx, my = members[i]
                    if x1<=mx<=x2 and y1<=my<=y2:
                        size = sz
                        r, c = x1, y1
                        break
                    else: continue
                    break
                else: continue
                break
            else: continue
            break
        else: continue
        break
    #  break 이렇게 많을 거면 함수로 빼는 게 낫겠다

    # 정사각형 시계 90 회전
    # 회전 벽 내구도 -1
    # size+1 * size+1
    square = []
    for i in range(r, r+size):
        tmp = []
        for j in range(c, c+size):
            tmp.append(board[i][j] - 1 if board[i][j] else 0)
        square.append(tmp)

    # board 회전
    for i in range(size):
        for j in range(size):
            # Step2. 90도 회전 이후의 좌표가
            # (x, y) -> (y, size-x-1)
            ri, rj = j, size-i-1
            # Step3. 기준 원위치 (r, c)
            ri, rj = ri+r, rj+c
            board[ri][rj] = square[i][j]

    # 모든 참가자와 출구 회전
    for i in range(M):
        if escaped[i]: continue
        x, y = members[i]
        # 회전 범위 내일 때
        if r <= x < r + size and c <= y < c + size:
            # Step1. (r,c) -> (0,0) 기준
            ox, oy = x-r, y-c
            # Step2. (x, y) -> (y, size-x-1)
            rx, ry = oy, size-ox-1
            # Step3. 기준 원위치 (r,c)
            members[i] = [r + rx, c + ry]

    x, y = OUT
    if r <= x < r + size and c <= y < c + size:
        # Step1. (r,c) -> (0,0) 기준
        ox, oy = x - r, y - c
        # Step2. (x, y) -> (y, size-x-1)
        rx, ry = oy, size - ox - 1
        # Step3. 기준 원위치 (r,c)
        OUT = [r + rx, c + ry]
    check_escape()
# 0초에 이미 탈출구인 경우
check_escape()
for _ in range(K):
    if False not in escaped:
        break
    move_members()
    if False not in escaped:
        break
    rotate_out()

print(distance_all)
print(OUT[0] + 1, OUT[1] + 1)