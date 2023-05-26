# 토마토
# n*m 상자 칸에 토마토 보관. 하루 지나면 익은 토마토 주위 안 익은 토마토 익음
# 며칠 지나면 다 익게 되는지 최소 일수
# 2*2~1000*1000 크기
# 1:익음. 0:안익음. -1:없음
# 처음부터 모두 익은 상태: 0 출력
# 익지 못하면 -1 출력
# 같은 시간대(depth)끼리 탐색하는 게 편함->bfs
# 어차피 방문 기록-> 다시 방문x 같고, 칸 별로 출발 로직 같기 때문에
# heapq보다 deque이 훨씬 시간 효율적
from collections import deque
from sys import stdin
que = deque([])
dir = [(0,1),(1,0),(-1,0),(0,-1)]
input = stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
day_m = 0
unripe = 0 # 안익은 애들
                
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            que.append((0, i, j))
            box[i][j] = -1 # 방문 처리
        elif box[i][j] == 0:
            unripe += 1
if unripe == 0:
    print(0)
    exit()
    
while que:
    day, x, y = que.popleft()
    day_m = max(day_m, day)
    for d in dir:
        nx, ny = x+d[0], y+d[1]
        if 0<=nx<n and 0<=ny<m and box[nx][ny] == 0:
            que.append((day+1, nx, ny))
            box[nx][ny] = -1 # 방문 처리. depth별 순회. 다시 겹칠 일 없음
            unripe -= 1
            
if unripe > 0: print(-1) # 모두 익히기 실패
else: print(day_m)