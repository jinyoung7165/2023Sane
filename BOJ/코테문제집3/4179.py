# 불
'''
불에 타기 전에 탈출 여부, 얼마나 빨리
나, 불은 매분마다 1칸. 수평/수직 이동
불은 각 지점에서 4방으로 확산
나는 미로의 가장자리에 접한 공간에서 탈출 가능
벽이 있으면 통과 불가
# 벽, . 통과, J 나, F 불

나 -> 불 순서 지켜서 que에 넣은 다음에
불이 지나가면, 나의 자리에 F 덮어 쓰기 가능 -> BOARD에 바로 J, F 기록 가능
QUE 하나로 처리 가능함
내 자리가 J면서, 가장자리면 STOP
'''
from sys import stdin
from collections import deque

input = stdin.readline

answer = 0

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
me, fire = deque([]), deque([])
visited = [[False]*m for _ in range(n)] # 내가 지나간 곳
for i in range(n):
    for j in range(m):
        if board[i][j] == 'J':
            me.append((i, j))
            visited[i][j] = True
            board[i][j] = '.'
        elif board[i][j] == 'F':
            fire.append((i, j))

dirs = [(0,1),(1,0),(0,-1),(-1,0)]
answer = float('inf')
t = 0

while True:
    me_next, fire_next = deque([]), deque([])
    # 내가 .이고, 다음 공간에 불, 벽이 아니면 이동 가능
    # 다음 공간 x==n-1 또는 y==m-1이면 탈출 가능
    while me:
        x, y = me.popleft()
        if board[x][y] != '.': continue
        if x in (0, n-1) or y in (0, m-1):
            answer = t+1
            break
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == '.' and not visited[nx][ny]:
                me_next.append((nx, ny))
                visited[nx][ny] = True
    # 이미 답 나옴
    if not me_next or answer != float('inf'): break
    
    # 불의 경우, 다음 공간이 .이면 이동 가능(board에 바로 기록)
    while fire:
        x, y = fire.popleft()
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == '.':
                board[nx][ny] = 'F'
                fire_next.append((nx, ny))
                
    me, fire = me_next, fire_next
    t += 1
print(answer if answer != float('inf') else "IMPOSSIBLE")