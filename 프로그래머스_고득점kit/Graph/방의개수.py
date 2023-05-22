# (0,0)에서 시작. 숫자가 적힌 방향으로 이동하며 선 그음
# 그림 그릴 때, 사방 막히면 방 하나로 셈
# 이동하는 방향이 담긴 배열 주어질 때, 방의 개수 return
# 방은 다른 방으로 둘러 싸일 수 있음
from collections import defaultdict

def solution(arrows:list):
    answer = 0
    move = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
    # arrows=선택할 move의 idx로 이뤄진 배열
    maps = defaultdict(list)
    x, y = 0, 0
    # 2배 map... 아마 그 문제
    for arr in arrows:
        dx, dy = move[arr]
        for _ in range(2): # 대각선을 위해 map두 배 칠함
            nx, ny = x+dx, y+dy
            # 다른 선분의 점끼리 만났을 때
            # 다른 선분: 평행하지 않으면 됨(틀림. 꼭짓점 말고 같은 선분 안의 점이 만나 도형이 완성될 수 있음)
            # 다른 선분: 갔다가 되돌아오는 한 직선만 아니면 됨
            # 한 선분: (nx,ny)<-(x,y)경로로 방문했다는 뜻
            if maps[(nx,ny)] and (x, y) not in maps[(nx,ny)]: # 완전 같은 경로로 선분 지날 때 무시
                # 한 점에서 만나는데 다른 방향의 선인 경우 도형 생성
                answer += 1
            maps[(nx,ny)].append((x,y))
            maps[(x,y)].append((nx, ny))
            # 방향성 없는 선분이므로 양방향 연결
            x, y = nx, ny # 이동
                
    return answer