'''
1~p산타
루돌프는 각 산타 공격. 산타는 루돌프 잡아야 함
n*n격자. (1,1)~(n,n)
m턴. 매턴마다 루돌프 1이동, 1~p산타 1번씩 움직임
기절 또는 격자 밖 나가면 탈락 산타
두 칸 사이의 거리는 (r1-r2)^2+(c1-c2)^2

루돌프는 '가장 가까운 산타를 향해' 1칸 돌진(인접 8방향)
가까운 산타 여러 명 -> 그 중 r좌표 큰 순 -> c 과표 큰 순 선택
인접 8방향 중

산타는 1~p 순서대로 (인접 4방향. 상우하좌) 움직이며
탈락x 산타는 루돌프에게 가까워지는 방향으로 1칸 이동
다른 산타 있는 칸이나 게임판 밖으로는 이동 불가
이동할 수 있는 칸 없거나 루돌프로 가까워질 수 있는 방법 없으면 가만히

충돌)
산타루돌프 같은 칸 -> 충돌 발생 + 기절 발생
루돌프가 움직여 발생한 경우, 산타는 c점수 얻음
-> 산타는 루돌프의 이동방향대로 c칸 밀려남
산타가 움직여 발생한 경우, 산타는 d점수 얻음
-> 산타는 산타의 반대 이동방향대로 d칸 밀려남
게임판 밖으로 밀려났다면 산타 탈락
밀려나는 도중에는 충돌x.
해당 위치로 텔레포트한 다음에, 거기에 다른 산타 있으면 상호작용 발생

상호작용)
원래 칸에 있던 다른 산타가 1칸 해당 방향으로 밀려남
밀려난 후에 또 산타 있으면 1칸씩 밀려남 반복.
게임판 밖으로 밀려나온 산타의 경우 탈락

기절)
k번째 턴이었다면 (k+1)번째 턴까지 기절해서 (k+2)턴부터 이동 가능
기절한 도중 충돌이나 상호작용으로 밀려나기 가능

게임 종료)
m턴. p산타가 모두 게임에서 탈락 시. 즉시 게임 종료
매 턴 이후, 아직 탈락하지 않은 산타들에게는 1점씩 추가 부여

각 산타의 최종 점수 배열
탈락 산타 위치를 (0,0), 기절 산타 구분해야 함

게임판 최대 50*50
턴 수 최대 1000

변수 unique하게 사용하자. (반대방향) 잘 읽고 기록...

방향? 8방향 모두 이동한 다음에 거리 구하지 말고, dx, dy를 각각 구하면 됨
    moveX = 0
    if closestX > rudolf[0]:
        moveX = 1
    elif closestX < rudolf[0]:
        moveX = -1

    moveY = 0
    if closestY > rudolf[1]:
        moveY = 1
    elif closestY < rudolf[1]:
        moveY = -1
'''
sdirs = [(0,-1),(1,0),(0,1),(-1,0)] # 상우하좌 거꾸로
rdirs = [(-1,0),(0,1),(1,0),(0,-1),(-1,-1),(1,-1),(-1,1),(1,1)]
n, rnd, p, c, d = map(int, input().split())
rr, rc = map(int, input().split()) # 루돌프 초기 위치
spos = [[x, y] for _, x, y in sorted(list(map(int, input().split())) for _ in range(p))] # p산타들의 초기 위치
scores = [0] * p # 산타들의 점수 배열
dead = [False] * (p)
faint = dict()

def move(x, y, d, cnt):
    # si 산타는 d방향으로 cnt 밀려남
    # 해당 위치로 텔레포트한 다음에,게임판 밖으로 밀려났다면 산타 탈락.
    # 거기에 다른 산타 있으면 상호작용 발생
    nx, ny = x+d[0]*cnt, y+d[1]*cnt
    si = spos.index([x, y]) # 현재 움직이려는 산타의 index
    if 0<nx<=n and 0<ny<=n: # 다음 칸으로 이동 가능
        if [nx, ny] in spos: move(nx, ny, d, 1) # 상호작용 발생
        spos[si] = [nx, ny]
    else:
        dead[si] = True
        spos[si] = [-1, -1]
    

# 기절 산타: 기절 시점. r == 기절시점 + 1이면 활동 불가능. del
for r in range(rnd):
    if False not in dead: break
    # 루돌프와 가장 가까운 산타의 pos, distance 찾기
    pos, distance, si = [], float('inf'), -1
    for i in range(p):
        if not dead[i]:
            tmp = (rr - spos[i][0])**2 + (rc - spos[i][1])**2
            if distance == tmp:
                if pos[0] < spos[i][0] or (pos[0] == spos[i][0] and pos[1] < spos[i][1]):
                    pos = spos[i]
                    si = i
                else: continue
            elif distance > tmp:
                pos = spos[i]
                si = i
                distance = tmp

    rd = 0 # 0~7
    distance = float('inf')
    # 방향 결정
    for i in range(8):
        dx, dy = rdirs[i]
        nx, ny = rr + dx, rc + dy
        tmp = (pos[0]-nx)**2 + (pos[1]-ny)**2
        if 0<nx<=n and 0<ny<=n and tmp < distance:
            distance = tmp
            rd = i
            if distance == 0: # 충돌 + 기절 발생
                # si 산타는 c점수 얻음
                # -> 산타는 rdirs의 rd방향대로 c칸 밀려남
                scores[si] += c
                faint[si] = r + 1 # 언제까지 기절할지 저장
                move(nx, ny, rdirs[rd], c)
                break
    # 루돌프 이동
    rr, rc = rr + rdirs[rd][0], rc + rdirs[rd][1]
    '''
    탈락x 산타는 루돌프에게 가까워지는 방향으로 1칸 이동
    다른 산타 있는 칸이나 게임판 밖으로는 이동 불가
    이동할 수 있는 칸 없거나 루돌프로 가까워질 수 있는 방법 없으면 가만히
    '''
    for i in range(p):
        if not dead[i]:
            if i in faint: # 루돌프와 충돌한 기록 있음
                if faint[i] == r: del faint[i]
                continue
            sx, sy = spos[i]
            distance = (rr-sx)**2 + (rc-sy)**2
            sd = -1
            # distance보다 가까워지는 방향 존재할 때만 이동
            for di in range(4):
                dx, dy = sdirs[di]
                nx, ny = sx+dx, sy+dy
                tmp = (rr-nx)**2 + (rc-ny)**2
                if 0<nx<=n and 0<ny<=n and tmp <= distance and [nx, ny] not in spos:
                    sd = di
                    distance = tmp
            if sd != -1: # 가까워지는 방향 존재 시, 이동
                spos[i][0] += sdirs[sd][0]
                spos[i][1] += sdirs[sd][1]
                if distance == 0: # 충돌 + 기절 발생
                    # i 산타는 d점수 얻음
                    # -> i산타는 sdirs의 sd방향의 반대로 d칸 밀려남
                    scores[i] += d
                    faint[i] = r + 1
                    revdirs = [-sdirs[sd][0], -sdirs[sd][1]]
                    move(spos[i][0], spos[i][1], revdirs, d)
    for i in range(p):
        if not dead[i]:
            scores[i] += 1
        
print(*scores)