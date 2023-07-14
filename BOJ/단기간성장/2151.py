# 거울 설치
# 설치 가능한 곳 여러 개
# 문 2개-> 한쪽에서 다른 문 비추도록 거울 설치
# 설치해야 하는 거울의 최소 개수
# 45도 기울어진 대각 방향으로 설치
# 모든 거울 양면 -> 모두 반사
# #: 문, .: 빈칸, !: 거울 설치 가능한 곳, *: 벽
# 거울 개수 기준 탐색 필요
# 문에서 빛 사방팔방으로 나올 수 있고 거울 설치해 방향 전환 가능
# 이동수는 중요하지 않음. 도착까지 몇 번이나 방향 바꿔야 하는지
# 둘러와도, 방향만 적게 바꾸면 되는 것
# 이동 중, 알고보니 방향 바꿔야 했음을 어떻게 아는가? -DFS 대신, 
# 일단 사방으로 움직이며 기록하고, 이전 방향과 달라지면 거울을 설치한 것이다
import heapq
from sys import stdin

dirs = {0: (0, 1), 1: (0, -1), 2: (1, 0), 3: (-1, 0)}
input = stdin.readline
n = int(input())
answer = 0
M = float('inf')
board, que = [], []
start = (0, 0)
visited = [[[M for _ in range(4)] for _ in range(n)] for _ in range(n)]

for i in range(n):
    row = input()
    board.append(row)
    idx = row.find('#')
    if idx != -1 and not que:
        for d in range(4):
            heapq.heappush(que, (0, i, idx, d))
            visited[i][idx][d] = 0
        start = (i, idx)

while que:
    cnt, x, y, d = heapq.heappop(que)
    if board[x][y] == '#' and (x, y) != start:
        answer = cnt
        break
    for i, dir in dirs.items():
        dx, dy = dir
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != '*':
            if i == d:
                if visited[nx][ny][d] > cnt:
                    visited[nx][ny][d] = cnt
                    heapq.heappush(que, (cnt, nx, ny, i))
            elif board[x][y] == '!':
                if visited[nx][ny][i] > cnt + 1:
                    visited[nx][ny][i] = cnt + 1
                    heapq.heappush(que, (cnt + 1, nx, ny, i))
print(answer)

# visited 배열의 크기를 바꾸어 방향도 고려할 수 있게 된 것입니다.
# 각 위치와 방향에 대해 최소 거울 수를 저장함으로써 정확한 결과를 얻을 수 있습니다.
''' 4가 정답인데, 7이 나오는 문제
20
#.....!.!...........
******.*.***********
*!....!*.***********
*.****.*.***********
*.**!.!*.***********
*.**.***.***********
*.**!.!*.***********
*.****.*.***********
*.**!.!*.***********
*.**.***.***********
*!..!.......#*******
********.***.*******
********.***.*******
********.***.*******
********.***.*******
********.*!.!*******
********.*.*********
********.*!.!*******
********.***.*******
********!...!*******

'''