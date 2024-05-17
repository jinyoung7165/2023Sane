'''
mn개 단위 정사각형으로 나뉜 m*n 보드
검/흰. 이 보드 잘라서 8*8 체스판으로 만들려함
맨 왼쪽 위가 흰/검 두 경우밖에 없음
8*8 잘라낸 후, 다시 칠해야겠다. 칠해야하는 최소 개수
BWBWBWBW
WBWBWBWB
check[i][j]: i행 j열을 맨 왼쪽 위로 삼았을 때,
'''
from sys import stdin

input = stdin.readline
answer = float('inf')
n, m = map(int, input().split())
board = [input() for _ in range(n)]
result = []
for i in range(n-7):
    for j in range(m-7): # 시작점 (i,j)
        l = 0 # 첫번째 거가 B
        r = 0 # 첫번째 거가 W
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0: # 짝수일 때(홀수 조합. ex 둘째줄 두 번째 열(1,1) -> B(왼쪽 위와 동일)여야 함)
                    if board[a][b] != 'B':
                        l += 1
                    else:
                        r += 1
                else:
                    if board[a][b] != 'W':
                        l += 1
                    else:
                        r += 1
        result.append(l)
        result.append(r)           

print(min(result))