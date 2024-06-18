# 성곽
'''
벽/통로
1) 방의 개수(bfs 방문하지 않았을 때 방문)
2) 가장 넓은 방의 넓이(1번 구할 때 넓이도 구함)
3) 하나의 벽을 제거해 얻을 수 있는 가장 넒은 방의 크기
(인접 두 방 더하기. bfs하면서 자기랑 인접한 방 번호 기억)

visited > 방번호 저장.
sizes > 방의 크기 저장
adjacent > 인접 방 나오면 일단 임시 방번호들 저장
각 칸의 벽 정보는 비트 합으로 나타냄 (0~15)
좌 벽이 있을 때1
상 벽있을 때2
우 벽 있을 때4
하 벽 있을 때8
'''
from sys import stdin
from collections import deque

input = stdin.readline
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
dirs = [(0,-1),(-1,0),(0,1),(1,0)] # 좌상우하
sizes = []
answer = [0] * 3

def bfs(x, y, tidx):
    adjacent = set() # 현재 팀이랑 인접한 팀넘버
    size = 1
    visited[x][y] = tidx
    que = deque([(x, y)])
    while que:
        x, y = que.popleft()
        for k in range(4):
            dx, dy = dirs[k]
            nx, ny = x+dx, y+dy # 다음 볼 곳
            if 0<=nx<n and 0<=ny<m: # 가능한 범위
                if board[x][y] & 2**k: # 벽 막혀 있고, 다른 팀이면 인접 팀
                    if -1 < visited[nx][ny] < tidx: # 다른 팀
                        adjacent.add(visited[nx][ny])
                elif visited[nx][ny] == -1: # 해당 방향 빈 칸
                    size += 1
                    que.append((nx, ny))
                    visited[nx][ny] = tidx
    
    for ad in adjacent:
        if answer[2] < size + sizes[ad]:
            answer[2] = size + sizes[ad]

    sizes.append(size)
    
tidx = 0
for i in range(n):
    for j in range(m):
        if visited[i][j] == -1: # 미방문
            bfs(i, j, tidx)
            tidx += 1

answer[0] = tidx
answer[1] = max(sizes)
for i in range(3): print(answer[i])