# 치즈
'''
정사각형 격자들로 치즈 이뤄짐
치즈 없는 격자 - 해당 격자에서 출발했을 때, 
n*m 가장자리에 닿으면 치즈 외부
n*m 가장자리에 못 가면 치즈 내부

치즈 있는 격자 - 해당 격자에서 사방 바로 살폈을 때, 치즈 외부0가 2군데 이상이면 치즈 없어짐

모든 치즈가 없어지는데 걸리는 시간?

1) 치즈 외부 따라 쭉 공백 이동. 치즈 만나면 +1씩 해줌
2) 치즈 삭제 (3이상인 애들. 아니면 1로 다시 만들어줌)

해당 초에 방문했는지 기록
'''
from sys import stdin
from collections import deque

input = stdin.readline
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
   
for t in range(10000):
    que = deque([(0, 0)]) # 가장자리 다 0임
    visited = [[False]*m for _ in range(n)] # 해당 초에 방문했는지
    visited[0][0] = True
    # 치즈 외부에서부터 쭉 녹임
    while que:
        x, y = que.popleft()
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                if board[nx][ny] == 0:
                    visited[nx][ny] = True
                    que.append((nx, ny))
                else: board[nx][ny] += 1 # 인접 공백이 해당 칸 녹임

    flag = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] < 2: continue
            elif board[i][j] == 2: board[i][j] = 1
            else: board[i][j] = 0 # 사방에서 2개 이상의 공백 만남
            flag = 1
    
    if not flag:
        print(t)
        break