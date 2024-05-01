# 틱택토
'''
두 명이 번갈아가며 말 놓음
3*3 보드. x/o말 놓는데, 반드시 x->o 순서
가로, 세로, 대각선 방향으로 3칸 이으면 즉시 종료
보드 가득 차도 즉시 종료
보드 상태 주어지면, 가능한 최종 상태인지 판별
1) x >= o 개수 같거나, +1이어야 함
2) 꽉 차거나, 한 줄 이상 이어져 있어야 함
    가능한 승리 상태면 valid
    승리자 없는 상태인데, 꽉 차 있으면 valid
    그 외 invalid
3) x, o 둘 중 하나만 1번/2번 승리한 상태여야 함
    4) x의 경우, 대각선 2개 승리 가능, 가로 세로 1개씩 가능, 대각선 1개+가/세 가능
    4) o의 경우, 1개만 가능
'''
from sys import stdin
input = stdin.readline
name = {'X':1, 'O':2}
def win(board, xcnt, ocnt):
    winner = 0 # x:1, o:2
    rcnt, ccnt, cross = 0, 0, 0 # 승리 수
    for i in range(0, 7, 3):
        if board[i]!='.' and board[i] == board[i+1] == board[i+2]:
            if not winner:
                winner = name[board[i]]
            elif winner != name[board[i]]: return 0 # 잘못된 승리
            rcnt += 1
    if rcnt > 1: return 0
    for i in range(3):
        if board[i]!='.' and board[i] == board[i+3] == board[i+6]:
            if not winner:
                winner = name[board[i]]
            elif winner != name[board[i]]: return 0 # 잘못된 승리
            ccnt += 1
    if ccnt > 1: return 0
    
    if board[4]!='.' and board[4] == board[0] == board[8]:
        if not winner:
            winner = name[board[4]]
        elif winner != name[board[4]]: return 0
        cross += 1
    if board[4]!='.' and board[4] == board[2] == board[6]:
        if not winner:
            winner = name[board[4]]
        elif winner != name[board[4]]: return 0
        cross += 1
    if cross == 2 and not winner == 1: return 0

    if rcnt + ccnt + cross > 2 or (winner == 2 and rcnt + ccnt + cross == 2): return 0
    
    if winner: # 승리자 생기면, 즉시 종료 조건
        if (winner == 1 and xcnt == ocnt+1): return 1
        elif winner == 2 and xcnt == ocnt: return 1
        return 0
    return 2

while True:
    board = input().strip()
    if board == 'end': break
    
    xcnt, ocnt = board.count('X'), board.count('O')
    if xcnt == ocnt or xcnt == ocnt+1:
        # 가능한 승리 상태 / 가능한 무승부 상태
        flag = win(board, xcnt, ocnt)
        if flag == 1 or (flag == 2 and xcnt == 5): print('valid')
        else: print('invalid')            
    else: print('invalid')