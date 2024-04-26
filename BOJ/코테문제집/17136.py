# 색종이 붙이기
'''
정사각형 다섯 종류의 종이
1*1, 2*2,... 5*5
각 종류 5개씩
이를 10*10 위에 붙일 때, 각 칸에는 0/1 적힘
1이 적힌 칸 모두 덮어야 함. 0에는 붙이면 안됨
종이의 경계 밖으로 나가선 안됨. 겹쳐서도 안됨
1이 적힌 모든 칸을 붙이는데 필요한 색종이 최소 개수? 불가능 -1

일단 여기에 큰 것부터 붙이고, 걔 떨어지면, 다음 작은 거 조합해 붙임
정사각형 -> n
직사각형 2*3의 경우, 2*2, 1*1*2개
'''
from sys import stdin
input = stdin.readline
board = list(input().split() for _ in range(10))

papers = [0]*6
answer = float('inf')
def dfs(x, y, cnt): # 모든 (x, y) 탐색 for i in range(10)* for j in range(10)
    global answer
    if x >= 10: # 행 다 쓰면, cnt 기록
        answer = min(answer, cnt)
        return
    if y >= 10: # 열 다 쓰면, 다음 행부터 다시 시작
        dfs(x+1, 0, cnt)
        return
    
    if board[x][y] == '1': # 현재 좌표 기준 종이 붙이기 시작
        for size in range(5, 0, -1):
            if papers[size] == 5: continue # 해당 크기 종이 다 씀
            if x+size>10 or y+size>10: continue # 전체 10*10 벗어남
            for nx in range(x, x+size):
                for ny in range(y, y+size):
                    if board[nx][ny] == '0': break
                else: continue
                break
            else: # (x, y) 시작점부터 size*size 크기의 종이 붙이기 가능
                papers[size] += 1 # size 종이 사용
                # 종이 board에 방문 표시하지 않으면, 행 이동하면서 겹칠 수 있음
                # 종이 방문 표시
                for i in range(x, x+size):
                    for j in range(y, y+size):
                        board[i][j] = '0'
                dfs(x, y+size, cnt+1)
                papers[size] -= 1 # size 종이 사용 취소
                # 종이 방문 표시 취소
                for i in range(x, x+size):
                    for j in range(y, y+size):
                        board[i][j] = '1'
    else: # 다음 시작 좌표 탐색
        dfs(x, y+1, cnt)
 
        
dfs(0, 0, 0) # x, y, 종이 개수

print(answer if answer!=float('inf') else -1)