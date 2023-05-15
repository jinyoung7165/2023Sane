# 두 팀 -> 상대 팀 먼저 파괴하면 이김
# 최대한 상대 팀 땅에 빨리 도착 시 유리
# 0: 벽, 1: 길
# (1,1)에서 출발 -> (n,m) 도착해야 함
# 도달 불가 시 -1리턴. 칸 개수 최솟값 리턴
# 최단 경로 (heapq + bfs)
import heapq

def solution(maps: list):
    answer = -1 # 도달 불가
    que = [] # n-1, m-1 도착해야 함
    n = len(maps)
    m = len(maps[0])
    d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    heapq.heappush(que, (1, 0, 0)) # 이동 칸수, x, y
    while que:
        c, x, y = heapq.heappop(que)
        if maps[x][y] != 1: continue # 이미 방문했는지 체크->효율 측에서 매우 중요
        if x == n-1 and y == m-1:
            answer = c
            break
        maps[x][y] = -1 # 방문처리
        for i in range(4):
            dx = x + d[i][0]
            dy = y + d[i][1]
            if 0<=dx<n and 0<=dy<m and maps[dx][dy]==1:
                heapq.heappush(que, (c+1, dx, dy))
    
    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))