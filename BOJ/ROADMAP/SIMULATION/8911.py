'''
거북이
LR 명령 시 방향만 90도 바꿈
F: 1 앞. B: 1 뒤
이동한 길을 모두 포함하는 가장 작은 직사각형 넒이?
선분의 경우 0
(0,0)출발. 위 방향
mx,Mx,my,My
'''
from sys import stdin

input = stdin.readline

dirs = [(0,1),(1,0),(0,-1),(-1,0)] 
# 우밑왼위 0: My, 1: Mx, 2: my, 3: mx 만 달라질 거라 생각하면 안됨
# 이전과 방향 달라지면, x, y 모두 변할 수 있기 때문에 그 때마다 모두 갱신
# +1로 오른 90회전
# -1로 왼 90회전
tc = int(input())
for _ in range(tc):
    command = input().rstrip()
    Mx, My, mx, my = 0, 0, 0, 0
    x, y, d = 0, 0, 3 # 초기 상태
    for com in command:
        if com == 'F':
            dx, dy = dirs[d]
            x, y = x+dx, y+dy
            My = max(My, y)
            Mx = max(Mx, x)
            my = min(my, y)
            mx = min(mx, x)
        elif com == 'B':
            dx, dy = dirs[d]
            x, y = x-dx, y-dy
            My = max(My, y)
            Mx = max(Mx, x)
            my = min(my, y)
            mx = min(mx, x)
        elif com == 'L':
            d = (d-1) % 4
        else:
            d = (d+1) % 4
    print((Mx-mx) * (My-my))