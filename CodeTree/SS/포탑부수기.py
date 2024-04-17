# n*m 격자. 모든 칸에 포탑(nm개의 포탑)
# 공격력 0이하 -> 포탑 죽음
'''
k round
한 round당 4 action순서대로 수행
살아 있는 포탑 1개 되면 즉시 중지

1) 공격자 선정 -> n+m만큼 공격력 증가
살아있는 포탑 중, 
가장 공격력 작은 포탑
여러 개면, 가장 최근에 공격한 포탑(시점 0 true로 간주. 숫자 크면 최근)
여러 개면, row+col 가장 큰 포탑
여러 개면, col 가장 큰 포탑

2) 공격자가 레이저 공격 시도 -> 안되면 포탄 공격
살아있는 포탑 중,(위와 기준 반대)
가장 공격력 크고, 공격한지 가장 오래된, row+col 가장 작은, col가장 작은

3) 레이저 공격(최단경로 -> 공격자의 공격력만큼의 대상의 공격력 감소
공격 대상을 제외한, 최단경로에 있는 포탑은 공격자의 공격력//2만큼 공격력 감소)
상하좌우 이동. "죽은 포탑의 위치 지날 수 없음"
맵의 경계 방향으로 나갈 때 -> 반대편으로 나옴
공격자의 위치에서 대상 포탑까지 "최단 경로"로 공격
최단 경로 없으면 포탄 공격
최단 경로 여러 개일 때, 우하좌상 중 먼저 움직인 경로 선택

4) 포탄 공격
공격자 공격력만큼 대상의 공격력 감소
대상의 주위 8방향 포탑은 공격력//2만큼 공격력 감소
공격자는 해당 공격에 영향 받지 않음
맵의 경계에 포탄 떨어지면 -> 맵의 반대편에 영향 미침


5) 죽었는지 확인. 죽지 않음(0초과) 포탑 중, 공격자가 아닌 포탑 중 피해 없는 포탑의 공격력 1 증가

전체 과정 종료 후, 남아있는 포탑 중 가장 강한 포탑의 공격력 출력

nx = (x + dx + N) % N
ny = (y + dy + M) % M
으로 격자 넘어감 표현 가능
'''
from collections import deque

l_dirs = [(0,1),(1,0),(0,-1),(-1,0)]
b_dirs = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
N,M,K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
alive = set() # 살아있는 위치 (i, j) 저장
last_time = [[0]*M for _ in range(N)] # 가장 마지막 공격 시점
for i in range(N):
    for j in range(M):
        if board[i][j]: alive.add((i, j))
        
def selection(): # 살아있는 애들 중, 공격자, 대상 선정
    vals = []
    # 작은 공격력, 큰 시점, 큰 row+col, 큰 col 기준
    for i, j in alive: vals.append((board[i][j], last_time[i][j], i, j))
    
    vals.sort(key=lambda x: (x[0], -x[1], -x[2]-x[3], -x[3]))
    killer = (vals[0][2], vals[0][3])
    
    vals.sort(key=lambda x:(-x[0], x[1], x[2]+x[3], x[3]))
    victim = (vals[0][2], vals[0][3])
    return killer, victim

def lazer(damage): # 최단경로 -> 대상 + 경로의 포탑들 피해
    '''
    "죽은 포탑의 위치 지날 수 없음"
    맵의 경계 방향으로 나갈 때 -> 반대편으로 나옴
    '''
    path = dict()
    que = deque([killer])
    path[killer] = killer
    while que:
        x, y = que.popleft()
        if x == victim[0] and y == victim[1]:
            break
        for dx, dy in l_dirs:
            nx, ny = (x+dx+N)%N, (y+dy+M)%M
            
            # if nx == -1: nx = N-1
            # elif nx == N: nx = 0
            # elif ny == -1: ny = M-1
            # elif ny == M: ny = 0
            
            if (nx, ny) in alive and (nx, ny) not in path:
                que.append((nx, ny))
                path[(nx, ny)] = (x, y) # 이전 노드 저장
    else: return False # 도착 불가능
    
    board[victim[0]][victim[1]] -= damage
    if board[victim[0]][victim[1]] <= 0: alive.remove(victim)
    
    # 경로에 있는 포탑들에게도 1/2 피해 -> related 추가
    damage //= 2
    cur = path[victim]
    while cur != killer:
        board[cur[0]][cur[1]] -= damage
        if board[cur[0]][cur[1]] <= 0: alive.remove(cur)
        related.add(cur)
        cur = path[cur]

    return True # 최단 경로 존재

def bomb(damage): # 대상 + 8방향 피해
    '''
    공격자 공격력만큼 대상의 공격력 감소
    대상의 주위 8방향(공격자 제외) 포탑은 공격력//2만큼 공격력 감소
    맵의 경계에 포탄 떨어지면 -> 맵의 반대편에 영향 미침
    '''
    x, y = victim
    board[x][y] -= damage
    if board[x][y] <= 0: alive.remove(victim)
    
    # 주위 포탑들에게도 1/2 피해 -> related 추가
    damage //= 2
    for dx, dy in b_dirs:
        nx, ny = (x+dx+N)%N, (y+dy+M)%M
            
        # if nx == -1: nx = N-1
        # elif nx == N: nx = 0
        # if ny == -1: ny = M-1
        # elif ny == M: ny = 0
        
        if (nx, ny) != killer and (nx, ny) in alive:
            board[nx][ny] -= damage
            if board[nx][ny] <= 0: alive.remove((nx, ny))
            related.add((nx, ny))
           
for t in range(1, K+1):
    related = set() # 해당 round에서 공격자이거나, 피해 입었음
    if len(alive) == 1: break
    
    # 공격자, 대상 선정
    killer, victim = selection()
    last_time[killer[0]][killer[1]] = t
    related.add(killer)
    related.add(victim)
    # 최단 경로로 레이저 공격
    # 최단 경로 없으면 포탄 공격
    board[killer[0]][killer[1]] += N + M
    damage = board[killer[0]][killer[1]]
    if not lazer(damage): bomb(damage)
    
    # alive 중, not related +1씩
    for i, j in alive:
        if (i, j) not in related:
            board[i][j] += 1

result = 0
for i, j in alive:
    if board[i][j] > result: result = board[i][j]
print(result)