# 미네랄
'''
한칸만 제거 가능하고, 떨어질 때 모양 유지하며
다른 클러스터나 땅 만날 때까지 떨어짐
제거할 때, 연결된 클러스터가 땅에 닿지 않으면 떨어뜨림
한쪽에서 공격했을 때, 클러스터 최대 3개 나올 수도 있고, 1개 나올 수도 있음
'''
from sys import stdin
from collections import deque

input = stdin.readline
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
rnd = int(input())
heights = list(map(int, input().split()))

def bfs(x, y, visited, path): # 사방 중 땅에 닿지 않으면 return 경로
    que = deque([(x, y)])
    visited[x][y] = True
    path.append((x, y))
    flag = True
    while que:
        x, y = que.popleft()
        if x == n-1: flag = False # 땅에 닿는 클러스터다
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == 'x' and not visited[nx][ny]:
                que.append((nx, ny))
                visited[nx][ny] = True
                path.append((nx, ny))
    return flag

def down(path): # 경로
    # 계속 swap하는 것말고, 일단 비운 상태에서
    # 다른 클러스터나, 땅 만날 때까지 칸 수 계산한 다음에, 1번만 이동하는 것으로 9배 시간 개선
    flag = True
    path.sort(reverse = True) # 아래 row에 있는 애들부터 하강
    for x, y in path:
        board[x][y] = '.' # 같은 cluster이 자기 아래에 있는 거 무시하기 위해 일단 비우기
    cnt = 1 # 몇 칸 움직일지
    while flag:
        for x, y in path:
            # 다음 칸에서 부딪히면 그만. cnt-1까지 이동해야 함
            if x + cnt == n or board[x+cnt][y] == 'x':
                flag = False
                break
        if flag: # 부딪히지 않았을 때만 한 칸 더 이동
            cnt += 1
    for x, y in path:
        board[x+cnt-1][y] = 'x'
    
       
for r in range(rnd):
    s, e, k = 0, m, 1
    if r % 2 != 0: # 오른쪽에서 왼쪽으로 던질 때
        s, e, k = m-1, -1, -1
    h = n - heights[r]
    visited = [[False] * m for _ in range(n)]
    for j in range(s, e, k):
        # 만나면 걔 기준 사방 노드가 땅에 닿는지 확인
        if board[h][j] == 'x': # 파괴할 거 하나 발견
            board[h][j] = '.'
            for dx, dy in dirs:
                nx, ny = h + dx, j + dy
                if 0<=nx<n and 0<=ny<m and board[nx][ny] =='x' and not visited[nx][ny]:
                    path = []
                    if bfs(nx, ny, visited, path): # 허공에 떠있음
                        down(path)
            break

for row in board:
    print(''.join(row))