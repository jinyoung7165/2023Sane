from collections import deque
# 서로 다른 직사각형의 변이 겹치는 경우 없음
# 만나서 새로운 테두리 형성
# 캐릭터의 위치 -> 아이템의 위치 주어질 때, 최단 거리 return
# ㄷ 경로, ㅁ 경로 다르게 취급돼야 함 -> map 2배
# 좌표만 2배로 변경, 초기map 2배씩 채움, 캐릭터 이동은 1번씩 -> answer = distance//2
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
def solution(rectangle:list, characterX:int, characterY:int, itemX:int, itemY:int):
    board = [[-1]*102 for _ in range(102)]
    for a, b, c, d in rectangle:
        for i in range(2*a, 2*c+1):
            for j in range(2*b, 2*d+1):
                if 2*a<i<2*c and 2*b<j<2*d: # 현재 직사각형의 내부
                    board[i][j] = 0
                elif board[i][j] != 0: # 다른 직사각형의 내부도 아닐 때, 테두리가 됨
                    board[i][j] = 1
        
    que = deque([(characterX*2, characterY*2, 0)])
    board[characterX*2][characterY*2] = -1 # 이동 불가 처리
    while que:
        x, y, cur = que.popleft()
        if x == itemX*2 and y == itemY*2: return cur//2
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 1<=nx<102 and 1<=ny<102 and board[nx][ny] == 1:
                board[nx][ny] = -1
                que.append((nx, ny, cur+1))
    return 0

solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8) # 17