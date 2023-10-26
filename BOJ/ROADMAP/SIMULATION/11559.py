'''
puyo puyo
바닥이나 다른 노드 나올 때까지 하강
같은 색 4개 상하좌우 -> 모두 없어짐 1연쇄
그 위에 쌓여 있는 애들 아래로 떨어짐
없어짐 반복할 때마다 연쇄 +1
여러 그룹 동시에 터지면 1연쇄만 추가
12행 6열 주어짐
이때 .은 빈공간이고
R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑이다.
1   1
'   '
1   '
'   1
1   1
계속 끌어내리는 1기준. 밑에 .있으면 끌어내려라
Y...YR
B.RGGY
R.GGYY
G.RYGR
YGYGRR
YBRYGY
RRYYGY
YYRBRB
YRBGBB
GBRBGR
GBRBGR
GBRBGR
-> 14
'''
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우밑왼위
from sys import stdin
from collections import deque

input = stdin.readline

board = [list(input().rstrip()) for _ in range(12)]
answer = 0

def bfs(x, y, visited):
    color = board[x][y]
    tmpset = set()
    que = deque([(x, y)])
    tmpset.add((x, y))
    visited[x][y] = True
    while que:
        x, y = que.popleft()
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<12 and 0<=ny<6 and board[nx][ny] == color and not visited[nx][ny]:
                tmpset.add((nx, ny))
                visited[nx][ny] = True
                que.append((nx, ny))
                
    if len(tmpset) > 3:
        for i, j in tmpset:
            board[i][j] = '.'
        return True # 1 연쇄
    return False

flag = True
while flag: # 각 turn마다 flag true여야 함
    flag = False
    visited = [[False] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.' and not visited[i][j]:
                if bfs(i, j, visited): flag = True

    if flag:
        answer += 1
        for j in range(6): # 열마다
            for i in range(10, -1, -1): # 맨 밑에서 두 번째부터
                # 밑에서부터 순회. 자기(알파벳) 밑의 공백 발견하면 끌어내려야 함(swap 1번만, break)
                if board[i][j] == '.': continue
                for k in range(11, i, -1): # 맨 밑에서부터 자기 위치 사이에 공백 있는지 체크
                    if board[k][j] == '.':
                        board[i][j], board[k][j] = board[k][j], board[i][j]  # swap 후 break 필수(기준 자리의 알파벳 이미 공백으로 대체)
                        break

print(answer)
