# 나이트의 이동
# 체스판 위 1나이트 놓임. 출발지, 도착지 주어질 때 최소 이동 수
from sys import stdin
from collections import deque

input = stdin.readline

dir = [[1,2],[2,1],[-1,2],[-2,1],[1,-2],[2,-1],[-1,-2],[-2,-1]]

tc = int(input())
for _ in range(tc):
    n = int(input()) # 판 크기
    start_x, start_y = map(int, input().split()) # 출발지
    end_x, end_y = map(int, input().split()) # 도착지
    board = [[-1]*n for _ in range(n)]
    que = deque([(start_x, start_y)]) # 위치, move수
    answer = 0
    board[start_x][start_y] = 0
    while que:
        x, y = que.popleft()
        if x==end_x and y==end_y:
            answer = board[x][y]
            break
        
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and board[nx][ny]==-1:
                que.append((nx, ny))
                board[nx][ny] = board[x][y] + 1
    print(answer)