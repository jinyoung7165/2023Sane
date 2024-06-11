# 수영장 만들기
'''
n*m board를 이루는
각 칸의 땅 높이 주어짐
낮은 곳을 높은 곳들이 에워싸고 있을 때,
물이 채워질 수 있음
n,m<=50, 각 칸의 높이 1~9
어차피 테두리에 물 못 채움
-> x=1~n-2, y=1~m-2의 주변 탐색
물은 높은 곳에서 낮은 곳으로 흐름
사방의 높이 중, 가장 작은 벽의 높이가 나에게 영향을 줌
_9_
929
9529
929
_9_
의 경우, 5기준 사방이 2라도,
더 큰 영역인 9때문에 9 높이의 물이 채워짐

제일 큰 영역이 중요-> 테두리부터 탐색하며 사방에 영향 주기?
테두리 원소부터, 테두리가 아닌 인접 칸들 탐색하며
나보다 작은 칸 나오면 걔한테 power(나-걔 크기) 줌
이미 기록 된 칸이면, min power로 갱신
범위 좁혀 가며, 각 칸의 사방 보면서, 나보다 작은 칸한테 기록된 power+(나-걔 크기)줌

1~8 높이의 물 채우겠다(min벽으로 둘러싸인 경우부터 채워야 하므로)
-> 자기보다 낮거나 같은 벽 따라 이동(자기보다 높은 거는 벽)
-> board 밖으로 나가면, 성립 안되는 것
1의 경우, 자기보다 낮거나 같은 개수만큼 채울 수 있고
(1 주위를 최소 2이상이 둘러싸고 있음 성립-> 최소 높이 차 1씩 더해짐)
2의 경우, 이전 누적합(1 결과)+자기보다 높은 벽 개수
(1~2 주위를 최소 3이상이 둘러싸고 있음 성립-> 최소 높이 차 1씩 더해짐)
'''
from sys import stdin
from collections import deque
input = stdin.readline
n, m = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(n)]
answer = 0
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
def bfs(x, y, water):
    global answer
    que = deque([(x, y)])
    visited[x][y] = True
    cnt = 1
    flag = True # 수영장 성립
    while que:
        x, y = que.popleft()
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m:
                if not visited[nx][ny]:
                    if board[nx][ny] <= water:
                        que.append((nx, ny))
                        cnt += 1
                    visited[nx][ny] = True
            else: # 수영장 성립 안됨. 그래도 연결된 나머지 다 찾아서 방문하자
                flag = False
    if flag: answer += cnt
    
for water in range(1, 9):
    visited = [[False]*m for _ in range(n)]
    for i in range(1, n-1):
        for j in range(1, m-1):
            if not visited[i][j] and board[i][j] <= water:
                bfs(i, j, water)
print(answer)