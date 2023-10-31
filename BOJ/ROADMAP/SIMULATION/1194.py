'''
달이 차오른다, 가자
미로 탈출
.빈칸 #벽 a~f열쇠 -> A~F문 열 수 있음
현재 위치 0 -> 출구 1(여러 개 존재)
이동 횟수의 최솟값. 0->1 탈출 불가능하면 -1 출력
문에 대응하는 열쇠 없을 수도 있고, 같은 열쇠-문 여러 개 존재 가능
재방문 가능한 경우. 다른 종류의 키 가지고 돌아왔을 때
키 종류를 최대 방문 수...
abcdef
000001 (1 << 0. a)
000010 (1 << 1. b)
111111 (key 6개 모두 가졌을 때. | 연산)
matches 랑 & 연산해서 matches 나오면 열기 가능한 것
visited: 특정 key 조합 가지고 방문했는지
100000 갖고 방문한 거랑, 100001 갖고 방문한 거랑 다른 case
둘 다 허용해야 함 -> n*m*(1<<6. 111111)만큼 칸 필요
'''
from collections import deque
n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def filter(key, door):
    haveKey = key & (1 << (ord(door) - ord('A')))
    return True if haveKey else False

que = deque([])
answer = -1
visited = [[[False]*(1 << 6) for _ in range(m)] for _ in range(n)]
# 특정 key 조합 갖고 방문했는지 여부
for i in range(n):
    flag = False
    for j in range(m):
        if board[i][j] == '0':
            que.append((i, j, 0, 0)) # keys, cnt 전달
            board[i][j] = '.'
            visited[i][j][0] = True
            flag = True
            break
    if flag: break

while que:
    x, y, keys, cnt = que.popleft()
    if board[x][y] == '1':
        answer = cnt
        break
    
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0<=nx<n and 0<=ny<m and board[nx][ny] != '#' and not visited[nx][ny][keys]:
            if board[nx][ny] == '.' or board[nx][ny] == '1':
                que.append((nx, ny, keys, cnt+1))
                visited[nx][ny][keys] = True
            elif 'a' <= board[nx][ny] <= 'f':
                # 반복문 돌아야 하므로 keys 냅다 더하면 안됨
                tmp_key = keys | (1 << (ord(board[nx][ny]) - ord('a')))
                que.append((nx, ny, tmp_key, cnt+1))
                visited[nx][ny][tmp_key] = True
            else:
                if filter(keys, board[nx][ny]): # 문에 해당하는 열쇠 가졌는지 확인
                    que.append((nx, ny, keys, cnt+1))
                    visited[nx][ny][keys] = True
    
print(-1 if answer == float('inf') else answer)