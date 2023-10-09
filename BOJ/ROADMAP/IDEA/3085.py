# 사탕게임
# n*n 크기. 색 다른 인접 두 칸 고르고 swap
# 모두 같은 색으로 이뤄진 가장 긴 행/열 크기
# 색 c,p,z,y
# n 3~50
# 출발지에서 아래, 오른쪽으로 이동했는데, 같으면 쭉 이동.
# (visited 표시)
# 다르면, 걔의 사방 확인해 swap 하거나 stop
'''
3
CCP
CCP
PPC
-> 3

4
PPPP
CYZY
CCPY
PPCC
-> 4

5
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ
-> 4(4번 행의 Y C 바꿈)
'''
from sys import stdin

input = stdin.readline

answer = 1
dirs = [(0,1),(1,0)] # 오른쪽, 아래
n = int(input())
board = [list(input()) for _ in range(n)]
# 기본 checkRow n번, checkCol n번
# j 바꾸면, checkRow 한번, checkCol 두번
# i 바꾸면, checkRow 두번, checkCol 한번
def checkCol(col): # 위아래
    global answer
    tmp = 1
    color = ''
    for i in range(n):
        if color != board[i][col]:
            color = board[i][col]
            tmp = 1
        else:
            tmp += 1
            if tmp > answer:
                answer = tmp
            
def checkRow(row): # 양옆
    global answer
    tmp = 1
    color = ''
    for i in range(n):
        if color != board[row][i]:
            color = board[row][i]
            tmp = 1
        else:
            tmp += 1
            if tmp > answer:
                answer = tmp

for i in range(n):
    checkRow(i)
    checkCol(i)
    for j in range(n):
        for k in range(2):
            dx, dy =  dirs[k]
            nx, ny = i+dx, j+dy
            if 0<=nx<n and 0<=ny<n and board[i][j]!=board[nx][ny]:
                board[i][j], board[nx][ny] = board[nx][ny], board[i][j]
                if k == 0: # 오른쪽
                    checkRow(i)
                    checkCol(j)
                    checkCol(ny)
                else: # 아래
                    checkCol(j)
                    checkRow(i)
                    checkRow(nx)
                board[i][j], board[nx][ny] = board[nx][ny], board[i][j] 
        if answer == n: break                    

print(answer)