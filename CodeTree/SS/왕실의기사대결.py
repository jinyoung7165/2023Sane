# (1,1)~(l,l)체스판. 빈칸.함정.벽(체스판 밖도 벽)
# 기사
# (r,c)를 좌측 상단으로 하며 h*w크기의 직사각형 형태
# 체력 k
'''
1 기사이동 ) 명령 받은 기사 상하좌우 1이동
이미 다른 기사 있으면 기존 기사 연쇄적으로 한 칸 밀려남
밀려나며 이동하려는 방향의 끝에 벽이 있으면 모든 기사는 이동 불가(밀려남 없던 일)
죽은 기사에게 명령 내리면 아무 반응x

2 대결대미지 ) 명령 받은 기사가 다른 기사 밀치면, 밀려난 기사는 대미지 입음
밀려난 기사는 밀려난 결과위치에서 w*h 직사각형 내에 놓여 있는 "함정의 수"만큼 대미지
"현재 체력 이상의 대미지 받은 경우, 체스판에서 사라지며 죽음"
명령 받아서 민 기사는 피해 입지 않음
각 기사들은 모든 밀림이 끝난 후에 대미지 얻음
밀렸더라도, 밀쳐진 위치에 함정이 없으면 대미지 전혀 입지 않음

생존한 기사들이 총 받은 대미지의 합 출력

dead 배열
각 기사들의 대미지 배열

L: 체스판의 크기 (3≤L≤40)
N: 기사의 수 (1≤N≤30)
Q: 명령의 수 (1≤Q≤100)
k: 기사의 체력 (1≤k≤100)


0번 depth 근처 모두 밀기 가능 -> 1번 depth 근처 모두 밀기 가능 -> 3번 depth 근처 모두 밀기 가능
0번 depth 근처 모두 밀기 가능
'''
from collections import deque
L,N,Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(L)]
# 0:빈칸, 1:함정, 2:벽
knights = []
for _ in range(N):
    r,c,h,w,k = map(int, input().split())
    r -= 1
    c -= 1
    knights.append([r,c,h,w,k])
# 기사의 처음 위치는 (r,c)를 좌측 상단 꼭지점으로 하며
# 세로 길이가 h, 가로 길이가 w인 직사각형 형태를
# for i in range(r-1, r-1+h): for j in range(c-1, c-1+w)
# 초기 체력이 k
commands = [list(map(int, input().split())) for _ in range(Q)]
# (i,d) i번(1~n) 기사에게 방향d로 1이동 -> i-1로 해석해야 함
# 사라진 기사번호 주어지면 무시해야 함
# d:0123 = 상우하좌
dead = [False] * N
damage = [0] * N
dirs = [(-1,0),(0,1),(1,0),(0,-1)]

def check_area(k_i, d_i):
    # 벽이면 이동 불가
    # 벽이 아니어서 가능할 때, 다음 knight영역을 return
    r, c, h, w, k = knights[k_i]
    dx, dy = dirs[d_i]
    k_area = set() # 현재 기사의 영역 좌표들
    for x in range(r, r+h):
        for y in range(c, c+w):
            nx, ny = x+dx, y+dy
            if 0<=nx<L and 0<=ny<L and board[nx][ny] != 2:
                k_area.add((nx, ny))
                continue
            else: return None # 벽이라서 못 움직임
    return k_area

def move_knight(k_i, d_i): # 벽이면 이동 불가
    k_area = check_area(k_i, d_i) # 기사의 다음 영역 좌표들
    if k_area == None: return False # 벽에 부딪혀서 이동 불가
    # 이미 다른 기사 있음 -> 밀치고 이동(못 밀고 이동 못 할 수도 있음)
    # 그렇지 않으면 이동 가능
    # 다른 기사의 영역과 겹치는지 확인(여러 기사와 겹칠 수 있음)
    # 겹치면서 밀 수 있는 기사들 -> 전부 가능할 때만 나중에 실제 이동
    que = deque([(k_i, k_area)])
    candidates = [] # 실제 밀린 기사들 모두 저장
    while que:
        cur, cur_area = que.popleft() # cur과 겹치는 기사들 모두 넣을 것
        for i in range(N):
            if i == cur or dead[i]: continue
            r, c, h, w, k = knights[i]
            for x in range(r, r+h):
                for y in range(c, c+w):
                    if (x, y) in cur_area: # 겹침 -> 얘 밀치고 이동해야 함
                        # 후보 기사 중 하나라도 밀기 불가능하면, 아까 실행했던 결과 되돌려야 함
                        # depth 엄청 큰데 모두 되돌리려면 힘듦 -> bfs로 가는 게 낫다
                        cand_area = check_area(i, d_i)
                        if cand_area == None: return False
                        # 기사를 밀 수 있으면 후보군에 넣음
                        que.append((i, cand_area))
                        candidates.append(i)
                        break
                else: continue
                break # 이미 겹침 판정함
    
    # candidates 실제 push진행 + 장애물 확인
    for i in candidates:
        if dead[i]: continue
        knights[i][0] += dirs[d_i][0]
        knights[i][1] += dirs[d_i][1]
        r, c, h, w, k = knights[i]
        for x in range(r, r+h):
            for y in range(c, c+w):
                if board[x][y] == 1:
                    damage[i] += 1
                    k -= 1
                    if k <= 0:
                        dead[i] = True
                        break
            else: continue
            break
        knights[i][4] = k
    # 나 이동
    knights[k_i][0] += dirs[d_i][0]
    knights[k_i][1] += dirs[d_i][1]
    return True
        
    
def solution():
    for q in range(Q):
        i, d = commands[q]
        if not dead[i-1]: move_knight(i-1, d)
            
    print(sum(damage[i] for i in range(N) if not dead[i]))
    
solution()