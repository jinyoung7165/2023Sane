# Maaaaaaaaaze
'''
5개의 5*5 board 주어짐
임의로 시계/반시계 회전 가능
board 순서 임의로 겹쳐 5*5*5육면체 만듦
(0,0,0) ->. (4,4,4)
현재 칸에서 면으로 인접한 칸 중, 장애물이 없는 칸으로 이동 가능
최소 몇 번 이동??
각 경우에서 각 판 3번씩 돌려가며 출발->도착
'''
from sys import stdin
from collections import deque
from itertools import permutations
input = stdin.readline
boards = [[list(map(int, input().split(' '))) for _ in range(5)] for _ in range(5)]
rotates = []
dirs = [(0,0,1),(0,1,0),(1,0,0),(0,0,-1),(0,-1,0),(-1,0,0)]

for board in boards:
    tmp = []
    tmp.append(board)
    _board = board
    for _ in range(3):
        _board = list(map(list, zip(*_board[::-1])))
        tmp.append(_board)
    rotates.append(tmp)

M = float('inf')
answer = M
seq = dict() # 쌓인 순서 (0,1,2,3,4)
cube = [[] for _ in range(5)] # 최종적으로 쌓인 큐브
def bfs(): # cube 탐색. 각 지점까지 최단 거리일 때만 방문(재방문하지 않음)
    global answer
    que = deque([(0, 0, 0)])
    visited = [[[0,0,0,0,0] for _ in range(5)] for _ in range(5)]
    while que:
        x, y, z = que.popleft()
        if 4 == x == y == z:
            answer = min(answer, visited[4][4][4])
            if answer == 12: # 가능한 최솟값일 때, 바로 종료
                print(12)
                exit()
            break
        for dx, dy, dz in dirs:
            nx, ny, nz = x+dx, y+dy, z+dz
            if 0<=nx<5 and 0<=ny<5 and 0<=nz<5 and cube[nx][ny][nz] and not visited[nx][ny][nz]:
                visited[nx][ny][nz] = visited[x][y][z] + 1
                que.append((nx, ny, nz))

    
def stacks(level): # 5층까지 쌓아서 cube에 지정 dfs
    for rotate in rotates[seq[level]]:
        cube[level] = rotate
        if level == 0 and not rotate[0][0]: continue  
        elif level == 4:
            if rotate[4][4]: bfs()
        else: stacks(level+1)

for perm in permutations(range(5)): # 쌓이는 순서
    for i in range(5):
        seq[i] = perm[i]
    stacks(0)

print(-1 if answer == M else answer)