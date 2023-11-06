'''
피아의 아틀리에
5*5모양에 서로 다른 재료 3개. 순서대로 넣어
재료 후보 10개 이하.
주어진 재료 중 3개 고른 뒤, 순서 정해 가마에 넣어야 함
각 칸 초기 0. 흰색.
재료는 4*4. (i,j)에 숫자, 색(R, B, G, Y, W) 쓰여 있음
회전 가능
1. 재료 없는 가마엔 아무 변화x
2. 재료 있는 
    가마의 숫자 더해짐(음수인 경우 0, 9초과인 경우 9)
    가마의 색 -> 재료 흰색인 경우 그대로, 아닌 경우 덮어 쓰기
3. 최종 상태에서 R,G,B,Y 색상 부분의 숫자 더하면 폭탄 품질 나옴
    (폭탄의 품질) = 7R + 5B + 3G + 2Y
permutation
(0,1,2) 번째 재료를 골랐다고 할 때,
순서 0 -> 1 -> 2 라고 칠 때
0을 4가지 위치에. 각 4가지 방향으로 놓을 수 있음.
2차원 배열 회전 list(zip(*arr[::-1]))
'''
from sys import stdin
from itertools import permutations
input = stdin.readline
n = int(input()) # 재료 개수
quality, color = [], []
answer = 0

def rotate(board): # 90도 회전 결과 반환
    return list(zip(*board[::-1]))
    
for i in range(n):
    quality.append([[list(map(int, input().split())) for _ in range(4)]])
    color.append([[list(input().rstrip().split()) for _ in range(4)]])
    for j in range(3): # 0 1 2
        quality[i].append(rotate(quality[i][j])) # 90도씩 회전한 결과 넣어놓기
        color[i].append(rotate(color[i][j])) # color도 회전해야 함!!!
        
sc = {'R':7, 'B':5, 'G':3, 'Y': 2, 'W': 0}

def score(board):
    global answer
    TMP = 0
    SC = dict()
    for i in range(5):
        for j in range(5):
            s, c = board[i][j] # 점수, 색상
            if c in SC:
                SC[c] += s
            else:
                SC[c] = s
    for c in SC: TMP += sc[c] * SC[c]
    if TMP > answer:
        answer = TMP

def put(cur, cur_color, start, board): # 현재 조각을, 해당 start범위부터 board에 두기
    sx, sy = start
    for i in range(4):
        for j in range(4):
            bn, bc = board[sx+i][sy+j] # 칸의 숫자, 색상
            cnum = cur[i][j]
            cc = cur_color[i][j]
            if bn + cnum < 0:
                bn = 0
            elif bn + cnum > 9:
                bn = 9
            else:
                bn += cnum
            if cc != 'W':
                bc = cc
            board[sx+i][sy+j][0] = bn
            board[sx+i][sy+j][1] = bc

   
def dfs(perm, el, board): # 순서조합, 몇 번째 재료 순서인지, 전체 board 결과
    if el == 3: # 3번째 재료까지 봤을 때
        # 점수 계산 과정
        score(board)
        return
    ingredient = quality[perm[el]] # 해당 순서의 재료(4가지 모양)
    ing_color = color[perm[el]]
    for rot in range(4): # 회전 모양새
        cur = ingredient[rot] # 현재 조각의 모양
        cur_color = ing_color[rot]
        for start in [(0,0),(0,1),(1,0),(1,1)]: # 출발지
            BOARD = [[r[:] for r in row] for row in board] # 3차원 배열 복사해두기
            put(cur, cur_color, start, BOARD)
            dfs(perm, el+1, BOARD)

for perm in permutations(range(n), 3):
    # n 재료 중 3개만 선택한 각 순서 (0,1,2)일 때
    # 각 재료 당 (quality[perm[012]][0123])-> 4pos에 배치
    # 4방향 회전 결과 * (0,0)시작, (0,1)시작, (1,0)시작, (1,1)시작
    board = [[[0, 'W'] for _ in range(5)] for _ in range(5)]
    dfs(perm, 0, board)
print(answer)