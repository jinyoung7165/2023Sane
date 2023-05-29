# 스도쿠
# 9*9칸. 시작 전 일부 칸에 1-9숫자 쓰여짐
# 나머지 빈 칸을 규칙으로 채워라
# 각 가로줄, 세로줄에는 1-9 숫자 한번씩 나와야 함
# 9개의 각 3*3 정사각형 안에도 1-9 숫자 한번씩 나와야 함
# 여러 방법인 경우 하나만 출력. 규칙에 따라 모두 채울 수 있는 경우만 주어짐
# nqueen과 비슷한 모양-> dfs
from sys import stdin
input = stdin.readline
require = set(range(1,10))
board = [list(map(int, input().split())) for _ in range(9)]
blank = [] # 빈 칸 위치 기억
for i in range(9):
    for j in range(9):
        if board[i][j] == 0: blank.append((i, j))
def dfs(idx):
    if idx == len(blank): # 다 채웠음
        for row in board:
            print(*row)
        exit()
    for i in range(1, 10): # 1~9를 blank[idx] 자리에 넣을지 고려
        x, y = blank[idx] # 빈 칸 죄표
        if checkRow(x, i) and checkCol(y, i) and checkRect(x, y, i):
            board[x][y] = i # (x,y)에 i 지정
            dfs(idx+1) # 다음 blank 채우자
            board[x][y] = 0 # 했는데 아니어서 return 됐으면 복구
def checkRow(x, num): # 해당 row에 있는 숫자면 False 리턴
    if num in board[x]: return False
    return True

def checkCol(y, num): # 해당 col에 있는 숫자면 False
    for i in range(9):
        if num == board[i][y]: return False
    return True

def checkRect(x, y, num): # 해당 3*3 사각형에 있는 숫자면 False
    start_x, start_y = x//3*3, y//3*3
    for i in range(3):
        for j in range(3):
            if num == board[start_x+i][start_y+j]:
                return False
    return True
       
dfs(0) # blank[0]부터 채워라