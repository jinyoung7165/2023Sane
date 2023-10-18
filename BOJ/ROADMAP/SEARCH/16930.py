'''
달리기
N×M 크기. 빈 칸. / 벽#
1초마다 4방 중 1 선택. 최소 1개, 최대 K개의 빈 칸 이동
시작점 (x1, y1)과 도착점 (x2, y2)가 주어졌을 때, 최소 시간
이동할 수 없는 경우에는 -1을 출력
1000,000 최대 크기
한 칸씩 이동하는 게 아니라, 최대 k칸만큼 이동하기 때문에
이전에 방문했던 곳을 현재 시점에 더 일찍 갈 방법이 있을 수도 있음 => 누적 값 비교
'''
from sys import stdin
from collections import deque

input = stdin.readline
n, m, k = map(int, input().split())
board = [list(input()) for _ in range(n)]
sx, sy, ex, ey = map(int, input().split())
sx, sy, ex, ey = sx-1, sy-1, ex-1, ey-1
M = float('inf')
answer = M
que = deque([(sx, sy, 1)])
visited = [[M]*m for _ in range(n)]
visited[sx][sy] = 0
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
while que:
    x, y, cnt = que.popleft()
    if x == ex and y == ey:
        answer = cnt
        break
    
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        for _ in range(k):
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == '.':
                if visited[nx][ny] >= cnt:
                    if visited[nx][ny] == M: # 첫 방문
                        que.append((nx, ny, cnt+1)) # 여기서부터 또 탐색
                    visited[nx][ny] = cnt
                    nx += dx 
                    ny += dy
                # 다른 쪽에서 와서 이미 방문했는데, 
                # 현재 방법이 더 최소일 땐, 거기서부터 또 시작할 필요는 없지만
                # 그래도 일단 이 방향으로 쭉 가며 아직 기록 안 된 원소 찾기
                else: break
            else: break # 벽이거나 범위 벗어남. k까지 증가할 필요 없음
        
print(answer-1 if answer != M else -1)