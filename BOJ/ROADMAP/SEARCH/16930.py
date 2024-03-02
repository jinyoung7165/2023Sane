# 달리기
'''
4방향 선택. 1초 동안 1~k개의 빈 칸 이동
시작 -> 도착 이동하는 최소 시간
.빈 #벽

일단 벽 만날 때까지 최대로 k칸 이동표시(1칸이든 k칸이든 1초)
하지만, k 최대 1000, map크기 10**6이기 때문에, que에 다 넣지는 않음
해당 칸을 더 작은 시간으로 재방문할 일 없음(작은 시간 순으로 넣으므로)

시간 초과 줄이기 위해, que에 중복 노드 넣는 걸 제한하자.
-> que 삽입(실제 최단 경로 방문) 1번
-> 이미 방문한 노드 지나칠 때도 존재. 최단 경로가 아니면 k칸 쭉 이동하는 거 그만 둠
    -> 현재 시간+1보다 다음 노드에 기록된 시간이 더 작으면, 지금 탐색하던 거 break, 다음 노드로부터 4방향으로 출발하는 게 낫지만
    그렇지 않으면 현재의 출발지에서 현재 시간+1동안 최대 k칸 남은 경로 이동하는 게 나음. break x
    1   2   
    1->(2)->?
    현재 1에서 옆으로 출발했는데, (2)를 세로 방향에서 이미 방문함, 
    but, 쭉 오른쪽으로 이동 시, 2의 오른쪽에 방문하지 않은 노드들도 2로 방문할 수 있기 때문에 쭉 탐색하며 기록((2)에서 출발시 3전파)
    
    1   1   2
    1->(1)->?
    
    현재 1에서 옆으로 출발했는데, (1)를 세로 방향에서 이미 방문함 -> 1->(1) 이동하는 거 2초 걸리기 때문에 이미 최단 경로 아님. break
'''
from sys import stdin
from collections import deque
input = stdin.readline
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
n, m, k = map(int, input().split())
board = [input().rstrip() for _ in range(n)]
a, b, c, d = map(int, input().split()) # 시작, 도착점
a -= 1
b -= 1
c -= 1
d -= 1

def bfs(a, b):
    que = deque([(a, b)])
    visited = [[float('inf')]*m for _ in range(n)]
    visited[a][b] = 0
    while que:
        x, y = que.popleft()
        if x == c and y == d:
            print(visited[c][d])
            break
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            for _ in range(k): # 현재 위치에서 출발해 k칸 이동하며 거리 갱신할 것
                if 0<=nx<n and 0<=ny<m and board[nx][ny] == '.' and visited[nx][ny] > visited[x][y]: # 이동 가능한 칸
                    # visited[nx][ny] == visted[x][y]+1 같은 시간대 내에 이미 방문한 칸도 포함(쭉 가다보면, 방문하지 않은 칸 존재 가능)
                    if visited[nx][ny] == float('inf'): # 첫 방문 시, 최단 시간 que에 넣음
                        que.append((nx, ny))
                        visited[nx][ny] = visited[x][y]+1
                    nx += dx
                    ny += dy
                else: break # 막혀서 같은 방향으로는 더 못 감      
    else: print(-1)
    
bfs(a, b)