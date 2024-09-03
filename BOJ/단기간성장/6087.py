# 레이저 통신
# 사실상, 거울 설치와 같은 문제
# w*h 지도. 각 칸은 빈 칸/벽
# c로 표시된 칸 2개 존재
# 두 칸이 통신하기 위해 설치해야하는 '거울 개수 최솟값' 구하라
# 레이저는 c에서만 발사 가능. 빈 칸에 거울/\을 설치해서 방향을 90도 회전
# 빈칸., *벽, c레이저 연결해야 하는 칸
# 연결할 수 있는 입력만 주어짐
# 거울 개수 기준 탐색 필요
# c에서 레이저는 사방팔방으로 나올 수 있고 거울 설치해 대각선 이동 가능
# 이동수는 중요하지 않음. 도착까지 몇 번이나 방향 바꿔야 하는지
# 둘러와도, 방향만 적게 바꾸면 되는 것
# 이동 수, 시간이 아닌 거울 수 기준으로 확장 -> heapq
from sys import stdin
import heapq

input = stdin.readline
dirs = [(0,1),(0,-1),(1,0),(-1,0)]  # 오른쪽, 왼쪽, 아래, 위
n, m = map(int, input().split())
board = [input().rstrip() for _ in range(m)]

def bfs(start_x, start_y):
    # 큐 초기화: (거울 개수, x, y, 방향)
    que = []
    # 큐에 4방향 모두 추가
    for d in range(4):
        heapq.heappush(que, (0, start_x, start_y, d))
        visited[start_x][start_y][d] = 0
        
    # 방문 기록: (x, y, 방향)로 구분
    visited = [[[float('inf')] * 4 for _ in range(n)] for _ in range(m)]

    
    while que:
        cnt, cx, cy, d = heapq.heappop(que)
        
        # 이미 방문한 기록이 현재 cnt보다 크거나 같은 경우
        if cnt > visited[cx][cy][d]:
            continue
        
        # 도착점인 경우
        if board[cx][cy] == 'C' and (cx, cy) != (start_x, start_y):
            return cnt
        
        # 다음 위치 탐색
        for i in range(4):
            nx, ny = cx + dirs[i][0], cy + dirs[i][1]
            
            if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != '*':
                if i == d:
                    # 같은 방향으로 이동 (거울 필요 없음)
                    if visited[nx][ny][i] > cnt:
                        visited[nx][ny][i] = cnt
                        heapq.heappush(que, (cnt, nx, ny, i))
                else:
                    # 다른 방향으로 이동 (거울 필요)
                    if visited[nx][ny][i] > cnt + 1:
                        visited[nx][ny][i] = cnt + 1
                        heapq.heappush(que, (cnt + 1, nx, ny, i))

# 'C'를 찾기
for i in range(m):
    j = board[i].find('C')
    if j != -1:
        start_x, start_y = i, j
        break

# BFS 실행
result = bfs(start_x, start_y)
print(result)