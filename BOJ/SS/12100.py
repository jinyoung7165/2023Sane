# 2048(Easy)
'''
1이동: 보드 위 전체 블록들을 같은 방향으로 최대한 이동(벽이면 stop)
"같은 값을 갖는" 두 블록 인접 시, 합체
이미 한번 합체된 블록은 다른 블록과 합체 불가
-> 다른 블록이 옆에 오면 그냥 위치 인접한 블록됨
여러 개 인접 경우, 이동하려는 방향의 칸부터 합쳐짐

n*n 보드에서 최대 5번 이동해서 만들 수 있는 가장 큰 블록의 값?
0은 빈칸, 나머지는 블록을 나타냄. 블록에 쓰여 있는 수는 2이상, 1024보다 작은 2의 제곱꼴

합합x
합합합 의 경우, 더 이상 합체 없음
(합체되지 않은 거 2개 이상이어야 계속)
'''
from sys import stdin

input = stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def dfs(depth, board):
    global answer
    if depth == 5:
        answer = max(answer, max(max(board[i]) for i in range(n)))
        return
    for d in range(4):
        nboard = [bo[:] for bo in board]
        if d == 0: # 아래로 이동(아래부터 이동)
            # x == n-1위치부터 보며, +dx하며 x-1~0 위치에 있는 블록 존재 시, 끌어내릴 것
            for j in range(n):
                for i in range(n-1, -1, -1): # (i, j)로 밀어낼 블록 찾기
                    flag = False
                    for ni in range(i-1, -1, -1):
                        if nboard[ni][j]: # 값 존재
                            if nboard[i][j] == 0: # 끌어당기기
                                nboard[i][j] = nboard[ni][j]
                            elif nboard[ni][j] == nboard[i][j]: # 합체
                                nboard[i][j] += nboard[ni][j]
                                flag = True # (i, j) 자리 확정
                            else: break # 값이 다름 무시 
                            nboard[ni][j] = 0
                            if flag: break # 합체 후, break
        elif d == 1:
            # x == 0위치부터 보며 -dx하며 x+1~n-1 위치에 있는 블록 위로 올릴 것
            for j in range(n):
                for i in range(n):
                    flag = False
                    for ni in range(i+1, n):
                        if nboard[ni][j]:
                            if nboard[i][j] == 0: # 끌어당기기
                                nboard[i][j] = nboard[ni][j]
                            elif nboard[ni][j] == nboard[i][j]:
                                nboard[i][j] += nboard[ni][j]
                                flag = True
                            else: break 
                            nboard[ni][j] = 0
                            if flag: break # 끌어내린 후, break                
        elif d == 2:
            for i in range(n):
                for j in range(n-1, -1, -1): # (i, j)로 밀어낼 블록 찾기
                    flag = False
                    for nj in range(j-1, -1, -1):
                        if nboard[i][nj]:
                            if nboard[i][j] == 0:
                                nboard[i][j] = nboard[i][nj]
                            elif nboard[i][nj] == nboard[i][j]:
                                nboard[i][j] += nboard[i][nj]
                                flag = True
                            else: break 
                            nboard[i][nj] = 0
                            if flag: break
        else:
            for i in range(n):
                for j in range(n):
                    flag = False
                    for nj in range(j+1, n):
                        if nboard[i][nj]:
                            if nboard[i][j] == 0:
                                nboard[i][j] = nboard[i][nj]
                            elif nboard[i][nj] == nboard[i][j]:
                                nboard[i][j] += nboard[i][nj]
                                flag = True
                            else: break 
                            nboard[i][nj] = 0
                            if flag: break

        dfs(depth+1, nboard)
        
dfs(0, board)

print(answer)