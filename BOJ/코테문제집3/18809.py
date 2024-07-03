# Gaarden
'''
초록/빨강 배양액 각각 개수 주어짐
뿌릴 수 있는 땅 중에서 골라 각 배양액 뿌린 후,
매초마다 어느 배양액도 도달하지 않은 인접 땅으로 퍼짐
초록, 빨강 동시 도달 시 꽃 생성. 생성 후 인접 이동x
퍼지면서 사방 중, 어느 배양액도 도달하지 않은, 호수가 아닌 땅으로 이동
0은 호수, 1은 일반땅, 2는 배양액 처음에 뿌리기 가능한 땅

피울 수 있는 꽃의 최대 수
# rnd_color = [[[0,0] for _ in range(m)] for _ in range(n)]
하면 시간 초과남. 3차원배열하지 말고 2차원 배열 두 개로 떼자
'''
from sys import stdin
from collections import deque
input = stdin.readline
n, m, g, r = map(int, input().split()) # 보드, 초록수, 빨강수
# g,r 모두 소진해야 함
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0
# 2땅을 초록으로 할지, 빨강으로 할지. r+g이상이고, 10개 이하로 주어짐
avail, comb = [], [] # 2땅 좌표, 각 좌표를 r/g/x로 했는지
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            avail.append((i, j))

size = len(avail)
def combinations(idx, arr, lg, lr): # avail원소의 순서, 경로, 남은g, 남은r
    if size-idx < lg+lr: return
    if idx == size:
        if lg == 0 and lr == 0: comb.append(arr)
        return
    if lg: combinations(idx+1, arr + '0',  lg-1, lr)
    if lr: combinations(idx+1, arr + '1', lg, lr-1)
    combinations(idx+1, arr + '2', lg, lr)
    
combinations(0, '', g, r)
csize = len(comb) # 각 경우 돌면서, 꽃의 수 셈
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def bfs():
    global answer
    for idx in range(csize):
        avail_comb = comb[idx] # 각 땅에 g/r/x 배치해야 함
        que = deque([]) # 특정 배치일 때, 각 배양액의 위치
        # 일단 넣어둔 위치 한 칸씩 이동해놓고, 같은 라운드에 다른 색깔 만난 경우 꽃을 피워야 함
        # 해당 위치에 꽃 피어있으면 이동x
        # 같은 라운드인지를 -라운드 번호로 알 수 있음
        # 원본 board에서 1, 2 이동 가능
        # 라운드, 색깔 기억하는 board -> [0,0]이거나, 같은 라운든데 다른 색깔이면 이동 가능
        # 꽃 피우고 색깔 2으로 변경.
        rnd = [[0]*m for _ in range(n)]
        colors = [[0]*m for _ in range(n)]
        for i in range(len(avail_comb)):
            status = avail_comb[i]
            x, y = avail[i]
            if status == '0': # g
                que.append((x, y, 0, 1)) # green, 1라운드
                rnd[x][y] = 1
            elif status == '1': # r
                que.append((x, y, 1, 1)) # red, 1라운드
                rnd[x][y] = 1
                colors[x][y] = 1
        
        result = 0
        while que:
            x, y, color, round = que.popleft()
            if colors[x][y] == 2: continue # 꽃 피운 자리
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m and board[nx][ny] != 0:
                    if rnd[nx][ny] == 0: # 안 가본 곳
                        rnd[nx][ny] = round+1
                        colors[nx][ny] = color
                        que.append((nx, ny, color, round+1))
                    elif rnd[nx][ny] == round+1 and colors[nx][ny]^color == 1: # 같은 라운드에서 방문한 다른 색
                        colors[nx][ny] = 2
                        result += 1
        if result > answer: answer = result
bfs()
print(answer)