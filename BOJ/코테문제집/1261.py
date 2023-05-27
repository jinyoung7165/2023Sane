# 알고스팟
# n*m 미로에 갇힘
# 0: 빈방/1: 벽. 부수면 이동 가능
# 상하좌우 이동 가능.(1,1)->(n,m) 이동하려면 벽 최소 몇 개 부숴야 하나
# (1,1),(n,m) 항상 빈 방
# 재방문 가능.
# 벽 부술 때와 아닐 때 따로 돌리지 말고 한 번에 돌려서 
# 최소 부순 횟수 찾고 싶음 -> heapq. 다익스트라
# 부술 수 있는 최대 벽 개수 한정된 게 아니기 때문에 DFS로 모두 탐색하면 시간 초과
# 벽 안 부수고 이미 visit한 곳-> 굳이 벽 부수고 다시 갈 필요 없음-> 재방문x
# deque의 경우. depth(이동 수)가 같은 애들끼리 움직임.
# 이동 수가 작은 애가 움직일 때, 벽을 쓸 데 없이 많이 부수면서 이동 시 최소 벽 부숨 수 못 구함
# depth(이동 수)말고, 최소 부숨 수 순으로 움직여야 함
# 0일 때 도착 불가->이제 벽 안 부수고는 "방문 못한 곳만 가면됨" -> 이미 넣어놓은 1 que에서 pop하고 부수며 다녀라
import heapq
from sys import stdin

input = stdin.readline
que = []
graph = []
walls, answer = 0, 0 # 벽 수, 몇 개 부술지
dir = [(0,1),(1,0),(0,-1),(-1,0)]

m, n = map(int, input().split()) # 세로, 가로
visited  = [[-1]*m for _ in range(n)] # 해당 위치까지 오기 위한 최소 벽 부숨 수. 몇 칸 이동했는지는 중요치 않음. 최소 부수기에 초점
for i in range(n):
    row = input().rstrip()
    graph.append(row)
    if '1' in row:
        for j in range(m):
            if row[j] == '1':
                walls += 1
visited[0][0] = 0 # 벽 없음
if walls > 0:
    heapq.heappush(que, (0, 0, 0)) # 부순 벽수, 현재 위치
while que:
    cnt, x, y = heapq.heappop(que)
    if x == n-1 and y == m-1: # 도착
        answer = cnt
        break
    for dx, dy in dir:
        nx, ny = x+dx, y+dy
        if 0<=nx<n and 0<=ny<m and visited[nx][ny] == -1: # 방문 x
            if graph[nx][ny]=='0': # 원래 빈 방
                visited[nx][ny] = cnt
                heapq.heappush(que, (cnt, nx, ny))
            else: # 벽
                visited[nx][ny] = cnt + 1
                heapq.heappush(que, (cnt+1, nx, ny))
print(answer)    

def solutionDFS(): # 시간 초과
    def dfs(x, y, path, cnt):
        if x == n-1 and y == m-1:
            return True
        for dx, dy in dir:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and (nx, ny) not in path:
                if graph[nx][ny]=='0': # 원래 빈 방
                    path.add((nx, ny))
                    if dfs(nx, ny, path, cnt):
                        return True
                    path.remove((nx, ny))
                elif cnt > 0: # 부술 수 있음
                    path.add((nx, ny))
                    if dfs(nx, ny, path, cnt-1): # 벽 하나 부숨
                        return True
                    path.remove((nx, ny))
                    
        return False  

    if len(walls) == 0 or dfs(0, 0, set((0, 0)), 0): # 그냥 이동 가능
        print(0)
    else:
        for i in range(1, len(walls)): # 벽 반드시 부숴야 함
            if dfs(0, 0, set((0, 0)), i):
                answer = i
                print(answer)
                break