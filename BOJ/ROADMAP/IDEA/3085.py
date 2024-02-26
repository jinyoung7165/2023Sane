# 사탕게임
'''
n*n 크기에 사탕 채워넣고, (종류4개)색이 다른 인접 두 칸 한번만 고름
서로 교환. 모두 같은 색으로 이뤄진 가장 긴 행/열 크기
i 행 내 교환(j<->j+1일 때, check col[j],col[j+1],row[i])
j 행 내 교환(i<->i+1일 때, check row[i],row[i+1],col[j])
'''
from sys import stdin
input = stdin.readline
n = int(input())
board = [list(input().strip()) for _ in range(n)]

answer = 1

def checkRow(x): # 행 내에서 열끼리 검사
    global answer
    tmp = 1
    for y in range(n-1):
        if board[x][y] == board[x][y+1]:
            tmp += 1
            if answer < tmp: answer = tmp
        else: tmp = 1

def checkCol(y):
    global answer
    tmp = 1
    for x in range(n-1):
        if board[x][y] == board[x+1][y]:
            tmp += 1
            if answer < tmp: answer = tmp
        else: tmp = 1
        
for i in range(n):
    checkRow(i)
    checkCol(i)
    for j in range(n):
        if i < n-1 and board[i][j] != board[i+1][j]:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            checkRow(i)
            checkRow(i+1)
            checkCol(j)
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
        if j < n-1 and board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            checkRow(i)
            checkCol(j)
            checkCol(j+1)
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
print(answer)