# 퍼즐 조각을 이미 채워진 보드의 빈 공간에 놓으려 함
# 조각 1번에 1개 채워 넣음. 회전 가능. 뒤집기(반전) 불가
# 넣었을 때, 인접한 칸이 비면 안됨
# 최대로 퍼즐 채웠을 때, 총 몇 칸 채울 수 있는지 return
# gameboard, table 주어질 때, 
# gameboard의 연속된 0 부분에 table의 연속된 1 뭉탱이를 놓아야 함
# table보면서 블록 발견 시, 그것을 감싸고 있는 최소 직사각형 만들기+회전*3 결과 블록수 dict에 저장해 퍼즐과 비교
# 최소->간단하게 bfs로 구현해보자...
from collections import defaultdict, deque
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs_board(i, j, game_board): # board의 빈칸 탐색하며 최소 직사각형, 빈칸수 반환
    que = deque([(i, j)]) # 탐색 시작
    # 최소 직사각형의 좌표, 크기 구해야 하므로
    path = [] # bfs 탐색 경로
    size = len(game_board)
    while que:
        x, y = que.popleft()
        if game_board[x][y] != 0: continue # 이미 방문한 곳
        path.append((x, y))
        game_board[x][y] = 2 # 방문 처리
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0<=nx<size and 0<=ny<size and game_board[nx][ny]==0:
                que.append((nx, ny))
    # 이동 경로를 감싸는 최소 직사각형 map만들자
    x_all = set(pos[0] for pos in path) # 방문한 모든 x좌표
    y_all = set(pos[1] for pos in path) # 방문한 모든 y좌표
    x_min, x_max = min(x_all), max(x_all)
    y_min, y_max = min(y_all), max(y_all)
    
    n, m = x_max-x_min+1, y_max-y_min+1 # 행렬 크기이므로 +1
    maps = [[0]*m for _ in range(n)]
    # 원래의 보드 보며 부분 직사각형 채워넣기
    for i in range(n):
        for j in range(m): # 빈 공간 2 삽입, 채워진 곳은 1
            maps[i][j] = game_board[x_min+i][y_min+j]
    return maps, len(path) # 최소 직사각형, 퍼즐을 위한 빈 칸 개수

def bfs_puzzle(i, j, table, blocks):
    que = deque([(i, j)]) # 탐색 시작
    # 최소 직사각형의 좌표, 크기 구해야 하므로
    path = [] # bfs 탐색 경로
    count = 0 # 몇 조각짜리 퍼즐인지
    size = len(table)
    while que:
        x, y = que.popleft()
        if table[x][y] != 1: continue # 이미 방문한 곳
        path.append((x, y))
        count += 1
        table[x][y] = -1 # 방문 처리
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0<=nx<size and 0<=ny<size and table[nx][ny]==1:
                que.append((nx, ny))
        # table 채워진 곳 -1 빈 공간 0
    block_arr = blocks[count] # 해당 퍼즐과 비교할 빈공간 block들
    x_min = min([pos[0] for pos in path])
    y_min = min([pos[1] for pos in path])
    
    for i in range(len(block_arr)):
        _block = block_arr[i]
        for _ in range(4): # block 총 4번 회전 가능
            _block = rotate(_block) # 90도 회전
            n = len(_block) # 최소 직사각형의 세로 길이
            m = len(_block[0]) # 가로 길이

            flag = True # match 여부
            # 퍼즐판(table) 위에서 x_min부터 n행만큼, y_min부터 m열만큼 최소 직사각형 볼 것
            if 0<=x_min+n-1<size and 0<=y_min+m-1<size:
                for x in range(n):
                    for y in range(m):
                        if _block[x][y] + table[x_min+x][y_min+y] != 1:
                            
                            flag = False # 맞춰질 수 없음
                            break
                    if not flag: break

                if flag:# match 가능하면 
                    del blocks[count][i] # 사용한 block 제거
                    # 한 공간-한 퍼즐 match후 끝이므로 del 써도 됨
                    return count # match후, 칸의 수 반환
    return 0

def rotate(arr):
    return list(zip(*arr[::-1]))
    
def solution(game_board, table):
    answer = 0
    n = len(game_board)
    blocks = defaultdict(list)
    # 퍼즐이 들어갈 수 있는 보드의 최소직사각형
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                block, count = bfs_board(i, j, game_board) # 최소 직사각형, 몇 조각짜리인지
                blocks[count].append(block)
    # 퍼즐 보자. 개수 맞으면 block 회전*3해가며 확인
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                answer += bfs_puzzle(i, j, table, blocks)
                # 퍼즐 block에 맞출 수 있으면 +맞춘 칸의 수
    return answer