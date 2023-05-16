# x, y축과 평행한 여러 직사각형 겹쳐진 상태 -> 뭉탱이의 가장 바깥 둘레를 따라 이동
# 꼭짓점에서 만나는 경우, 변이 겹치는 경우 없음
# 뭉탱이가 두 개 이상으로 분리된 경우도 없음(무조건 한 뭉탱이)
# 한 직사각형이 다른 직사각형 안에 완전 포함되는 경우도 없음
# 직사각형의 작은변 길이 1~4
# [왼밑x, 왼밑y, 우위x, 우위y] 좌표로 직사각형 표현
# 1<=x,y<=50
# 다른 직사각형의 x또는 y가 같은 경우 없음
# 캐릭터의 위치 좌표, 아이템의 위치 좌표 주어짐(처음부터 같은 경우 없음)
# 직사각형 총 1~4개 주어짐
# 둘레 길 어떻게 표현할 것인가? x, y축 평행 좌표 -> map 방식
# 직사각형의 내부를 0로 채우고 테두리는 1 -> 1따라 이동
# ㄷ 경로와 ㅁ 경로 헷갈리지 않기 위해 map 크기를 2배 -> 경로//2 return
from collections import deque

def solution(rectangle:list, characterX:int, characterY:int, itemX:int, itemY:int):
    answer = 0
    # 0-101
    maps = [[-1] * 102 for _ in range(102)] # 102*102 map (좌표 1~50. (0포함 51)50개 -> 2배로)
    for rec in rectangle: # 두 배가 된 map 내부 채우기
        x1, y1, x2, y2 = map(lambda x: x*2, rec) # 좌푯값 두 배
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if maps[x][y] == 0: continue # 이미 다른 직사각형의 내부
                if x in (x1, x2) or y in (y1, y2): # 테두리
                    maps[x][y] = 1 # 이동 가능
                else:
                    maps[x][y] = 0 # 이동 불가
                
    direction = [[0,1],[1,0],[0,-1],[-1,0]]
    que = deque([(characterX*2, characterY*2, 0)]) # itemX-1, itemY-1까지 도착해야 함
    maps[characterX*2][characterY*2] = -1 # 출발지 방문 처리
    # 큰 뭉탱이에서 출발->도착 이동하는 방법 2가지
    # BFS-> 사방으로 퍼지며 "같은 depth끼리 번갈아" FIFO 수행됨. root까지 온 첫번째 경로가 자연스럽게 최단 경로가 됨
    while que:
        x, y, move = que.popleft()
        if x == itemX*2 and y == itemY*2:
            answer = move # BFS->FIFO 최단거리 바로 찾을 수 있음
            break
        for i in range(4):
            nx, ny = x+direction[i][0], y+direction[i][1]
            if 1<=nx<102 and 1<=ny<102 and maps[nx][ny]==1:
                que.append((nx, ny, move+1))
                maps[nx][ny] = -1 # 방문 처리

    return answer // 2

solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8) # 17