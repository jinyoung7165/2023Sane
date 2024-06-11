# 새로운 게임
'''
N*N 보드. 흰/빨/파 각 칸

원판 모양 K개의 말(1~k. 이동방향 정해져 있음)
말끼리 업을 수 있음(같이 움직임. 가장 아래의 말만 이동지시 가능)
각 턴에 1~k 순서대로 이동 (10이하)

a번 말이 이동하려는 칸이
1) 흰 -> 이동, 이미 말이 있는 경우, 가장 위에 a 쌓음
1.1) a가 이미 누굴 업은 상황이면, 그 위 모두 함께 이동
2) 빨 -> 이동, 이미 말이 있는 경우, 가장 위에 a 쌓음
2.1) a가 누굴 업은 상황이면, 그 위 순서 반대로
3) 파/체스판 벗어남 -> a 말의 이동 방향 반대로. 1칸 이동
3.1) 이동하려는 칸 또 파/체스판 벗어남 -> 이동x. 방향만 반대로

4개의 말 쌓이면 게임 종료
게임 종료 턴 번호 구하라(값이 1000이상이거나, 종료되지 않을 때, -1 출력)

말의 위치, 이동 방향
누가 누굴 무슨 순서로 업었는지 parents
0 또는 바로 위의 애, 맨 위는 0 가리킴
'''
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
colors = [list(map(int, input().split())) for _ in range(n)]
# 0흰 1빨 2파
board = [[-1]*n for _ in range(n)] # 가장 밑 말의 번호만 저장
horse = []
for i in range(k):
    r, c, d = map(int, input().split())
    horse.append([r-1,c-1,d-1])
    board[r-1][c-1] = i
# r, c, 이동방향(우좌상하)
dirs =  [(0,1),(0,-1),(-1,0),(1,0)]
re_dirs = {0:1,1:0,2:3,3:2}
parents = [-1]*k
def re_parents(h_i):
    cur, parent = h_i, -1
    while cur!=-1:
        next = parents[cur] # 다음 이동 루트
        parents[cur] = parent
        parent = cur # 전달할 부모의 값 저장
        cur = next
    return parent

def find_parent(h_i):
    cur = h_i
    while parents[cur]!=-1:
        cur = parents[cur]
    return cur

def check_size(h_i):
    cur = h_i
    size = 1
    while parents[cur]!=-1:
        cur = parents[cur]
        size += 1
        if size >= 4: return True
    return False

for rnd in range(1, 1001): # 1~1000
    flag = False
    for i in range(k):
        x, y, d = horse[i]
        if board[x][y] != i:
            continue # 자기가 맨 밑 말이 아닐 때
        nx, ny = x+dirs[d][0], y+dirs[d][1]
        if not (0<=nx<n and 0<=ny<n) or colors[nx][ny] == 2:
            d = re_dirs[d]
            nx, ny = x+dirs[d][0], y+dirs[d][1]
            horse[i][2] = d
        # 또 파랑 or 범위 벗어나면 이동 없이 방향만 반대로 해줌
        if (0<=nx<n and 0<=ny<n):
            exist, exist_p = board[nx][ny], find_parent(board[nx][ny])
            if colors[nx][ny] == 0:
                # horse 단체 이동. 기존 위에 업기
                board[x][y] = -1 # 이동
                horse[i][0], horse[i][1] = nx, ny
                if exist == -1: # 존재하지 않음
                    board[nx][ny] = i
                else:
                    parents[exist_p] = i
                    if check_size(exist):
                        flag = True
                        break # -> 4이상이면 stop    
            elif colors[nx][ny] == 1:
                # horse 단체 이동, REVERSE후, 기존 위에 업기
                board[x][y] = -1 # 이동
                p_i = re_parents(i)
                if exist == -1: # 존재하지 않음
                    board[nx][ny] = p_i
                    horse[p_i][0], horse[p_i][1] = nx, ny
                else:
                    parents[exist_p] = p_i
                    if check_size(exist):
                        flag = True
                        break # -> 4이상이면 stop    
    if flag:
        print(rnd)
        break
    
else: print(-1)        
        