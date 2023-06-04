# 소가 길을 건넌 이유6
# 작은 정사각형 목초지(2*2-100*100)
# 인접 목초지 간 자유롭게 건널 수 있지만, 일부는 길 건너야 함
# 길은 상하좌우 인접 목초지 이음
# k마리 소가 있고, 각 소는 다른 목초지에 있음
# 길 건너지 않음 만나지 못하는 소의 쌍 개수
# 길(장애물) 없는 곳으로만 이동 가능
# 각 소가 못 만난 경우, 길을 이용해야만 만날 수 있는 걸
from sys import stdin
from collections import defaultdict, deque

dirs = [(1,0),(0,1),(-1,0),(0,-1)]
input = stdin.readline
n, k, r = map(int, input().split()) # map크기, 소, 길 개수
board = [[-1]*(n) for _ in range(n)]
cows = [] # 소 위치
roads = defaultdict(list)
for _ in range(r): # 길. r, c - r, c
    r1, c1, r2, c2 = map(int, input().split())
    roads[(r1-1, c1-1)].append((r2-1, c2-1))
    roads[(r2-1, c2-1)].append((r1-1, c1-1))
for i in range(k): # 0~k-1소 번호 부여
    r, c = map(int, input().split())
    board[r-1][c-1] = i
    cows.append((r-1, c-1))

def bfs(idx, start_x, start_y): # 소idx, 위치
    que = deque([(start_x, start_y)])
    meets = k-idx-1 # 만나야할 소(idx+1~k-1)
    visited = [[False]*(n) for _ in range(n)]
    visited[start_x][start_y] = True
    while que:
        x, y = que.popleft()
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if (nx, ny) in roads[(x, y)]: continue
                que.append((nx, ny))
                visited[nx][ny] = True
                if board[nx][ny] > idx:
                    meets -= 1
    return meets # 만나지 못하고 남은 소
    

cnt = 0
for i in range(k-1):
    # i소는 i+1~k-1번 소까지 만날 수 있는지 check
    cnt += bfs(i, *cows[i]) # 못 만난 소 count
print(cnt)
'''
0 - 1,2,3
1 - 2,3
2 - 3
3
'''