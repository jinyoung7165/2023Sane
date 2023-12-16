# Surrounded Regions
'''
x로 둘러싸인 o 뭉탱이 -> x로
만약 x로 완전히 싸여있지 않다면
즉, o 한 면이라도 끄트머리에 위치한다면
그 덩어리는 빼고 모두 x로 바꿔야 함 -> 끄트머리의 덩어리를 찾는 것이 포인트!!!!
'''
from collections import deque
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
def solve(self, board) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    n, m = len(board), len(board[0])
    # 끄트머리에 위치한 O 중심으로 확장
    def bfs(x, y):
        que = deque([(x, y)])
        while que:
            cx, cy = que.popleft()
            for dx, dy in dirs:
                nx, ny = cx+dx, cy+dy
                if 0<=nx<n and 0<=ny<m and board[nx][ny] == 'O':
                    que.append((nx, ny))
                    board[nx][ny] = '.'
    for i in [0, n-1]:
        for j in range(m):
            if board[i][j] == 'O':
                bfs(i, j)
                board[i][j] = '.'
    for i in range(n):
        for j in [0, m-1]:
            if board[i][j] == 'O':
                bfs(i, j)
                board[i][j] = '.'
    for i in range(n):
        for j in range(m):
            if board[i][j] == '.':
                board[i][j] = 'O'
            elif board[i][j] == 'O':
                board[i][j] = 'X'