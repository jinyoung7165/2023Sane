# 2019 상반기 LINE 인턴
'''
A가 B를 잡는 데까지 걸리는 최소시간. 잡지 못하면 -1 출력
1. B는 처음위치X에서 1초 후 1만큼 움직임. 이후 가속이 붙어 매초마다 이동거리+1만큼 움직임
    X X+1 X+3 X+6
2. A는 현재위치Y에서 Y-1, Y+1, 2*Y 중 하나로 이동
    반드시 이동해야 함, 1초후 위치가 같을 수는 없지만 얼마든지 재방문 허용한다는 뜻
3. 좌표 0~200,000
4. A는 좌표 위에서 움직이고, B가 좌표를 벗어나면 게임끝남
T초 후 A의 위치: A + T(T-1)/2 + T
+1, -1 섞은 경우엔 2초 뒤에 위치 재방문함(2,4,6,8.. 재재재방문...)
0초에 방문한 거 2초에 재방문
1초에 방문한 거 3초에 재방문
홀/짝수별 각 위치 방문 여부 체크해서 재사용
'''
from collections import deque

x, y = map(int, input().split())
visited = [[False, False] for _ in range(200_001)]
que = deque([(y, 0)]) # 짝수 초에 y에 도착 
for i in range(1000):
    x += i
    if x > 200_000:
        print(-1)
        break
    if visited[x][i%2]:
        print(x, i)
        break
    for _ in range(len(que)):
        pos, t = que.popleft()
        t = (t+1)%2
        if 0<=pos*2<200001 and not visited[pos*2][t]: # 방문했으면, 어차피 계속 true 상태 -> 2초 뒤에 재방문 가능
            visited[pos*2][t] = True
            que.append((2*pos, t))
        if pos<200001 and not visited[pos-1][t]:
            visited[pos-1][t] = True
            que.append((1+pos, t))
        if 0<=pos and not visited[pos+1][t]:
            visited[pos+1][t] = True
            que.append((1-pos, t))
else: print(-1)