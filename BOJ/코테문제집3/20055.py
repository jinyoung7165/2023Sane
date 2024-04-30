# 컨베이어 벨트 위의 로봇
'''
길이가 n인벨트 두 줄 == 2n칸 (1~2n 번호)
1 2 3 ... n
2n 2n-1 2n-1 ... n+1

벨트 1 회전 시, 1~2n-1까지의 칸은 다음 번호 칸으로 이동 (+1)
2n 칸은 1번 칸 위치로 이동

i칸의 내구도 Ai
1번 칸의 위치에서 올림, n번 칸에서 내림

1번 위치에서만 로봇 올릴 수 있고, n번 칸에 도달하면 바로 내림
로봇은 벨트위에서 스스로 움직임
로봇 1번 칸에 올리거나, 로봇이 이동 시, 내구도 1 감소

1) 벨트가 각 칸 위의 로봇과 함께 1 회전
2) 가장 먼저 벨트에 올라간 로봇부터, 회전 방향으로 1 이동 가능 시, 이동
 - ) 다음 칸에 로봇 없고, 칸의 내구도가 1 이상 있어야 함
3) 올리는 위치에 있는 칸에 0이 아니면, 올리는 위치에 로봇 옮김
4) 내구도 0 칸의 개수가 k개 이상이면 종료, 아님 1) 반복

몇 단계에 종료인지 출력
'''
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
belts = list(map(int, input().split())) # 내구도
size = 2*n
t = 1
pos = dict() # robot의 위치(올라간 시간: 위치)
exists = [False]*size # 각 위치에 누가 있는지
while True:
    up, down = -t%size, (n-1-t)%size
    # 로봇들 위치 1씩 회전해야 함
    # 다음 방향으로 1 이동 가능 시, 이동
    delete = []
    for _t, _p in pos.items():
        cur = _p # 벨트 회전과 함께 로봇 돌아감 -> index 변하지 않음
        exists[_p] = False
        if cur == down: # 회전해서 도착 -> 즉시 제거
            delete.append(_t)
        else:
            if belts[(cur+1)%size] and not exists[(cur+1)%size]:
                cur = (cur+1)%size
                belts[cur] -= 1
                if cur == down: # 이동해서 도착 -> 즉시 제거
                    delete.append(_t)
                    continue
            exists[cur] = True
            pos[_t] = cur
    for _t in delete:
        del pos[_t]
    
    if belts[up]:
        pos[t] = up
        belts[up] -= 1 # 내구도 -1
        exists[up] = True
    if belts.count(0) >= k: break
    t += 1
print(t)

from collections import deque
from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
a = deque(map(int, input().split()))  # 내구도. A1, A2, ..., A2N
robot = deque([0] * n)  # 벨트위에 있는 로봇 (0~n-1에만 존재 가능)
result = 1
while True:
    a.rotate(1) # +1 회전
    robot.rotate(1) # +1 회전
    # n-1 -> n으로 땡겨지며, 즉시 삭제
    robot[-1] = 0
    
    # 먼저 올라간 순서대로 다음칸  +1 이동
    for i in range(n-2, -1, -1): # n-2~0 -> n-1~1 한 칸씩 땡긴
        if a[i+1] and robot[i] and not robot[i+1]:
            robot[i+1] = 1
            robot[i] = 0
            a[i+1] -= 1
    robot[-1] = 0 # 내리는 위치, 즉시 삭제    
        
    if a[0]: # 로봇 올림
        a[0] -= 1
        robot[0] = 1  
    if a.count(0) >= k: break
    result += 1
print(result)