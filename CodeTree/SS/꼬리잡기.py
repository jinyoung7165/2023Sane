'''
n*n board. 3명 이상이 한 팀
머리사람-중간...-꼬리사람
각 팀은 주어진 이동 경로만 따라 이동(반복되는 원형)
각 팀의 이동 경로 겹치지 않음

각 팀이 획득한 점수의 총합 출력

1. 각 팀은 머리사람을 따라 1 이동
2. 각 rnd마다 정해진 선 따라 ball 던짐
    0 rnd에 0row의 (0->n-1) col 따라서 쭉 이동
    ...
    n-1 rnd에 n-1row의 (0->n-1) col 따라서 쭉 이동
    n rnd에 0col의 (n-1->0) row 따라서 쭉 이동
    ...
    2n-1 rnd에 n-1col의 (n-1->0) row 따라서 쭉 이동
    2n rnd에 n-1row의 (n-1->0) col 따라서 쭉 이동
    ...
    3n-1 rnd에 0row의 (n-1->0) col 따라서 쭉 이동
    3n rnd에 n-1col의 (0->n-1) row 따라서 쭉 이동
    ...
    4n-1 rnd에 0col의 (0->n-1) row 따라서 쭉 이동
    이후 다시 0rnd 방향으로 돌아감
3. 공이 던져지는 선에 최초로 만나는 사람만 점수 얻음
    해당 사람이 팀에서 k번째(idx 1부터 시작)사람인 경우, k**2만큼 점수 얻음
    누군가 점수를 얻었다면, 머리사람과 꼬리사람 바뀜(이동방향 반대로)

틀린 이유
1. range(-1, -size-1, -1), range(n-1, -1, -1) 혼동
2. trace 배열 구성 bfs로 안 함
3. 1-3 순환구조 시, 각 멤버 이동 후, 맨마지막에 board 덮어씌워야 함
'''
from collections import deque
n, m, k = map(int, input().split())
# board 크기, 팀 수, 라운드 수
board = [list(map(int, input().split())) for _ in range(n)]
# 0빈칸, 1머리사람, 2중간사람, 3꼬리사람, 4이동선
# 1,2,3이 있는 곳도 이동선의 일부이다.

teams = [[] for _ in range(m)] # 각 팀의 멤버들의 위치
heads = [0]*m # 각 팀의 머리사람의 위치(0또는 팀크기)
tails = [0]*m # 빠른 head tail 전환 위해(0또는 팀크기)
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
'''
1부터 시작해서 2따라서 3나올 때까지 member 기록
'''
def insert_members(ti, x, y):
    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True
    teams[ti].append([x, y])
    que = deque([(x, y)])
    last = [] # 3의 위치 기억
    while que:
        x, y = que.popleft()
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board[nx][ny]!=0:
                visited[nx][ny] = True
                if board[nx][ny] == 2:
                    teams[ti].append([nx, ny])
                    que.append((nx, ny))
                elif board[nx][ny] == 3:
                    last.append((nx, ny))
    teams[ti].append(last[0])
    tails[ti] = len(teams[ti])-1
    
'''
해당 팀이, 머리 사람 따라 1씩 이동
머리 인접한 곳에 멤버 없는 4칸으로 이동하거나, 이것 없으면 꼬리칸으로 이동
board에 기록하며 이동해야 함(teams 멤버들의 좌표 이동)
(+머리사람의 경우, 꼬리 위치로 가는 게 아니라면, 다음 board 칸에 1 기록)
(+꼬리사람의 경우, 원래 자리에 머리사람이 온 게 아니라면, board 칸 4로)
'''
def move_members(ti):
    members = teams[ti]
    head, tail = heads[ti], tails[ti]
    x, y = members[head]
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<n and board[nx][ny] == 4:
            break
    else: # 머리가 갈 경로가 없다 == 경로가 머리~꼬리 크기여서 꽉 차 있다
        nx, ny = members[tail]
        
    members[head] = nx, ny # head 이동
    size = len(members) # members 크기
    if head == 0: rng = range(1, size)
    else: rng = range(-2, -size-1, -1)
    
    for ni in rng:
        nx, ny = members[ni] # 원래 위치
        members[ni] = x, y
        x, y = nx, ny
    board[x][y] = 4 # 3이 지나간 자리 4가 됨
    board[members[head][0]][members[head][1]] = 1 # 순환 구조 때문에 이때 덮어씌움
    board[members[tail][0]][members[tail][1]] = 3
        
'''
공이 던져지는 선에 최초로 만나는 사람만 점수 얻음
해당 사람이 팀에서 k번째(idx 1부터 시작)사람인 경우, k**2만큼 점수 얻음
누군가 점수를 얻었다면, 머리사람과 꼬리사람 바뀜(이동방향 반대로)
'''
def throw_ball(div1, div2):
    global answer
    flag = False # 누군가 맞췄는지
    if div1 in (0, 2):
        if div1 == 0:
            row = div2
            col = range(n)
        else:
            row = n-1-div2
            col = range(n-1, -1, -1)
        for c in col:
            if 0 < board[row][c] < 4: # 누군가 존재
                flag = True
                x, y = row, c
                break
    else:
        if div1 == 1:
            row = range(n-1, -1, -1)
            col = div2
        else:
            row = range(n)
            col = n-1-div2
        for r in row:
            if 0 < board[r][col] < 4: # 누군가 존재
                flag = True
                x, y = r, col
                break
    if flag:
        '''
        해당 사람이 팀에서 k번째(idx 1부터 시작)사람인 경우, k**2만큼 점수 얻음
        누군가 점수를 얻었다면, 머리사람과 꼬리사람 바뀜(이동방향 반대로)
        '''
        ti = 0
        for i in range(m):
            members = teams[i]
            if (x, y) in members:
                ti = i
                break
        else: return
        head = heads[ti]
        size = len(members) # members 크기
        if head == 0: rng = range(size)
        else: rng = range(-1, -size-1, -1)
        
        for mi in rng:
            mx, my = members[mi]
            if x==mx and y==my:
                if mi >= 0:
                    answer += (mi+1)**2
                else:
                    answer += mi**2
                break
        heads[ti], tails[ti] = tails[ti], heads[ti]
ti = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            # 새로운 팀 멤버들 쭉 훑으며 teams에 위치 추가
            insert_members(ti, i, j)
            ti += 1
answer = 0
div1, div2 = 0, 0
for rnd in range(k):
    for i in range(m): # 각 팀이 머리 따라서 1 이동
        move_members(i)
    throw_ball(div1, div2)
    if div2 == n-1:
        div1 = (div1+1)%4
        div2 = 0
    else:
        div2 += 1
print(answer)