'''
라이언 2*2 배치된 7개 블록과 콘이 2*2
한꺼번에 찾고, 지워진 후, 블록이 아래로 떨어져 빈 공간 채움
지워지는 블록의 수 return
아래로 내려가기: col별 위로 쭉 순회하며 사라질 block 만나면,
걔 위부터 천장까지 보면서 not 사라질 애랑 swap 후 break
'''
from collections import defaultdict

def solution(m, n, board):
    board = [list(x) for x in board] # 2차원 배열로 만듦
    destroy = defaultdict(set) # col별 사라질 row 저장
    def swap():
        tmp = 0
        for j in range(n): # col별로
            for i in range(m-1, -1, -1): # row 순회
                if i in destroy[j]:
                    tmp += 1
                    board[i][j] = ''
                if board[i][j] == '': # 공백이면, 그 위에 채워진 애랑 swap
                    for k in range(i-1, -1, -1): # 사라질 block의 위부터 천장까지 싹 다 내림
                        if k not in destroy[j] and board[k][j]:
                            board[i][j], board[k][j] = board[k][j], board[i][j]
                            break
            del destroy[j]
        return tmp
    def check():
        answer = 0
        while True:
            flag = False
            for i in range(m-1):
                for j in range(n-1):
                    if board[i][j] and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                        destroy[j].add(i)
                        destroy[j].add(i+1)
                        destroy[j+1].add(i)
                        destroy[j+1].add(i+1)
                        flag = True
            if flag:
                answer += swap()
                continue
            return answer
    return check()