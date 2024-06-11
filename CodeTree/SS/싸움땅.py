'''
n*n board.
각 격자에 총들과 공격력
플레이어들 각각 초기 능력치 가짐.

아래 과정을 1~n플레이어가 순서대로 진행하며 round 진행
kround 동안 진행하며, 각 플레이어들이 얻은 포인트 출력하라.

1-1 플레이어 본인의 방향대로 1 이동
격자를 벗어나는 경우, 반대 방향으로 바꿔 1 이동
2-1 간 곳에 플레이어 없으면,
총 있는지 확인. 이미 다른 총 갖고 있는 경우, 총들 공격력 비교해서 획득하고 나머지 총은 내려놓음
2-2-1 플레이어 있으면, 싸움. 초기능력치+공격력 비교
그 합이 같은 경우, 초기 능력치 높은 애가 이김.
이긴 애는 초기능력치+공격력 합 차이만큼 포인트로 획득
2-2-2
진 애는 갖고 있던 총 그 자리에 내려놓고, 자기 방향대로 1 이동
다른 플레이어 있거나, 범위 밖인 경우, 오른쪽 90도씩 회전하며 빈 칸 보일 때 이동
이동한 칸에 총들 있으면, 공격력 비교해서 획득하고 나머지 총은 내려놓음
2-2-3 이긴 애는 그 칸에 떨어져 있는 총들과, 자기 총 비교해서 획득, 나머지 내려놓음

틀린 이유: 4방향 중 되는 거 찾을 때 x+dx, y+dy해야 하는데, nx+dx, ny+dy해버림
'''
from collections import defaultdict
n, m, k = map(int, input().split())
# 보드, 플레이어, 라운드
board = defaultdict(list) # (i,j): [총들의 공격력]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        board[(i, j)].append(row[j])

players = []
players_power = []
for _ in range(m):
    x, y, d, p = list(map(int, input().split()))
    players.append([x-1, y-1, d])
    players_power.append([p, 0]) # 초기, 소유한 총의 공격력

dirs = [(-1,0),(0,1),(1,0),(0,-1)]
# x, y, 방향(상우하좌), 초기능력
points = [0]*m

# 총 갖고 가면, pop하고, player에게 부여
# for _ in range(m) 돌면서 같은 위치에 있는 애 찾고
# 걔의 총+공격력 합

'''
플레이어 본인의 방향대로 1 이동
격자를 벗어나는 경우, 반대 방향으로 바꿔 1 이동
'''
def move(pi):
    x, y, d = players[pi]
    _, gun = players_power[pi]
    nx, ny = x+dirs[d][0], y+dirs[d][1]
    if not (0<=nx<n and 0<=ny<n):
        d = (d + 2)%4
        nx, ny = x+dirs[d][0], y+dirs[d][1]
    if gun: # 0 이상일 때 소유 -> 함께 이동
        board[(x, y)].remove(gun)
        board[(nx, ny)].append(gun)
    players[pi] = [nx, ny, d]
    
'''
플레이어 있으면, 초기능력치+공격력 비교
그 합이 같은 경우, 초기 능력치 높은 애가 이김.
이긴 애는 초기능력치+공격력 합 차이만큼 포인트로 획득
'''
def win_lose(i, pi):
    p, gun = players_power[i]
    pp, pgun = players_power[pi]
    win, lose = i, pi
    if (p+gun) < (pp+pgun) or ((p+gun) == (pp+pgun) and p<pp): # pi가 이김
        win, lose = pi, i
    points[win] += sum(players_power[win]) - sum(players_power[lose])
    return win, lose

'''
진 애는 갖고 있던 총 그 자리에 내려놓고,
자기 방향대로 1 이동
다른 플레이어 있거나, 범위 밖인 경우, 오른쪽 90도씩 회전하며 빈 칸 보일 때 이동
이동한 칸에 총들 있으면, 공격력 비교해서 획득하고 나머지 총은 내려놓음
'''
# 현재방향에서 시계방향 빈 칸 찾기
# -> for i in range(4) d+i로 내 방향부터 체크 가능
# 범위 안이면 break하고 이동하면 됨
def loser_move(pi):
    x, y, d = players[pi]
    nx, ny = x+dirs[d][0], y+dirs[d][1]
    players_power[pi][1] = 0 # 총 내려놓음
    while True: # 이동 가능할 때 stop
        if not (0<=nx<n and 0<=ny<n):
            d = (d + 1)%4
            nx, ny = x+dirs[d][0], y+dirs[d][1]
            continue
        for i in range(m):
            if i == pi: continue
            if nx == players[i][0] and ny == players[i][1]:
                d = (d + 1)%4
                nx, ny = x+dirs[d][0], y+dirs[d][1]
                break
        else: break # 걸리는 거 없을 때 nx, ny로 이동

    players[pi] = [nx, ny, d]
    if len(board[(nx, ny)])>0: players_power[pi][1] = max(board[(nx, ny)])
    
for _ in range(k):
    for i in range(m):
        move(i)
        # 가진 총과 함께 이동하며, 다음 위치에 gun추가
        # gun이 0이 아닐 때만 추가
        x, y = players[i][0], players[i][1]
        for pi in range(m):
            if i == pi: continue
            if x == players[pi][0] and y == players[pi][1]:
                win, lose = win_lose(i, pi)
                loser_move(lose)
                if len(board[(x, y)])>0: players_power[win][1] = max(board[(x, y)])
                break
        else: # 다른 플레이어 없었음
            if len(board[(x, y)])>0: players_power[i][1] = max(board[(x, y)])

print(points)