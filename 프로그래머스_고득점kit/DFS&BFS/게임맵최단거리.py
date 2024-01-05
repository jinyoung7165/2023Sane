# 두 팀 -> 상대 팀 먼저 파괴하면 이김
# 최대한 상대 팀 땅에 빨리 도착 시 유리
# 0: 벽, 1: 길
# (1,1)에서 출발 -> (n,m) 도착해야 함
# 도달 불가 시 -1리턴. 칸 개수 최솟값 리턴
from collections import deque
def solution(maps):
    que = deque([(0, 0, 1)]) # x,y,cnt
    n, m = len(maps)-1, len(maps[0])-1
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]
    while que:
        x, y, cnt = que.popleft()
        if x==n and y==m: return cnt
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<=n and 0<=ny<=m and maps[nx][ny]:
                maps[nx][ny] = 0
                que.append((nx, ny, cnt+1))
    return -1
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))