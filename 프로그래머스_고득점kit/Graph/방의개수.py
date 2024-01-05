# (0,0)에서 시작. 숫자가 적힌 방향으로 이동하며 선 그음. 방의 개수 return
# 방은 다른 방으로 둘러 싸일 수 있음(삼각형도 가능)
# 점 재방문 시 확인 필요
# maps 크기 주어지지 않음 -> 점 중심으로 dict[(x,y)]. 처음 map의 좌표를 2배 불가. 점 기준 이동을 2배씩
# 도착점 기준으로 처음 온 출발점일 때(겹치지 않는 선분) => 방 개수 +1
# (x,y->nx,ny) 겹치는 선분: (x,y->nx,ny) or (nx,ny->x,y)
from collections import defaultdict
dirs = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)] # 0~7
def solution(arrows:list):
    answer = 0
    maps = defaultdict(set)
    x, y = 0, 0
    for arr in arrows:
        for _ in range(2): # 대각선을 위해 2배
            nx, ny = x+dirs[arr][0], y+dirs[arr][1]
            # 이미 존재하는 점이고, 완전 같은 선분이 아니라면 방 생성
            if maps[(nx, ny)] and (x, y) not in maps[(nx, ny)]:
                answer += 1
            maps[(nx, ny)].add((x, y))
            maps[(x, y)].add((nx, ny))
            x, y = nx, ny
    return answer

print(solution([1,4,6,0,3]))
print(solution([1,4,6,0,3,6,1]))