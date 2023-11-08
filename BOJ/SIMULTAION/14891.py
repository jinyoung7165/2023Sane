'''
톱니바퀴
8개 톱니 가진 바퀴 4개. 각 톱니마다 n/s극
바퀴 여러 개. 가장 왼쪽부터 1 idx가지고 증가: 1,2,3,4 바퀴

바퀴를 총 k번 (톱니기준 k번) 회전 시키려 함.
회전시킬 바퀴와. (시계/반시계)방향 결정해야 함
맞닿은 극 다르면 옆 바퀴는 현재 바퀴와 반대로 회전
ns-ns-ns-sn 맞닿은 상태에서 하나 회전 시키면 마지막 빼고 모두 회전

초기 상태와 회전방법 주어질 때, 최종 바퀴의 상태 구하라
1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
점수 합 출력
10101111
01111101
11001110
00000010
2
3 -1
1 1
-> 7

k 회전 동안
    1. 현재 상태에서 연결 여부 판단
    2. 회전
점수 계산

que 안 쓰고 현재 for 문 돌리며, 연결돼 있으면 반대 방향으로 돌리기 가능
'''

'''
from sys import stdin
from collections import deque
input = stdin.readline

answer = 0

wheels = [input().rstrip() for _ in range(4)] # wheels[0][0~7]: 0/1극

for r in range(int(input())):
    idx, dir = map(int, input().split()) # 바퀴 선택, 1시계 -1 반시계
    if dir == -1: dir = 0 # -1 대신 0 쓰겠다
    visited = [False] * 4
    connection = [[] for _ in range(4)]
    for i in range(3):
        if wheels[i][2] != wheels[i+1][6]: # i-i+1 연결
            connection[i].append(i+1)
            connection[i+1].append(i)
    for i in range(1, 4):
        if wheels[i][6] != wheels[i-1][2]: # i-i-1 연결
            connection[i].append(i-1)
            connection[i-1].append(i)
    
    # 바퀴 선택, 회전
    que = deque([(idx-1, dir)]) # 회전 시킬 노드, 방향
    visited[idx-1] = True
    
    while que:
        cur, d = que.popleft()
        for node in connection[cur]:
            if not visited[node]:
                visited[node] = True
                que.append((node, 1 - d)) # 현재와 반대 방향
        # 회전 str
        s = wheels[cur] # 원래 바퀴
        if d == 1: # 시계 >> 1. 맨 뒤 -> 맨 앞위치에 붙이기
            s = s[7] + s[:-1]
            wheels[cur] = s
        
        else: # 반시계 << 1. 맨 앞 -> 맨 뒤위치에 붙이기
            s = s[1:] + s[0]
            wheels[cur] = s
for i in range(4):
    if wheels[i][0] == '1':
        answer += 2 ** i

print(answer)
'''
# que 안 쓰고. 자신 왼쪽으로 쭉 탐색. 자신 오른쪽으로 쭉 탐색
from sys import stdin
input = stdin.readline

answer = 0
wheels = [input().rstrip() for _ in range(4)] # wheels[0][0~7]: 0/1극

def rotate(cur, d):
    s = wheels[cur] # 원래 바퀴
    if d == 1: # 시계 >> 1. 맨 뒤 -> 맨 앞위치에 붙이기
        s = s[7] + s[:-1]
        wheels[cur] = s
    else: # 반시계 << 1. 맨 앞 -> 맨 뒤위치에 붙이기
        s = s[1:] + s[0]
        wheels[cur] = s

for r in range(int(input())):
    idx, dir = map(int, input().split()) # 바퀴 선택, 1시계 -1 반시계
    connection = [[False, False] for _ in range(4)]
    for i in range(3):
        if wheels[i][2] != wheels[i+1][6]: # i-i+1 연결
            connection[i][1] = True
            connection[i+1][0] = True
    for i in range(1, 4):
        if wheels[i][6] != wheels[i-1][2]: # i-i-1 연결
            connection[i][0] = True
            connection[i-1][1] = True
    
    # 바퀴 선택, 회전
    cur = idx-1
    rotate(cur, dir)
   
    for i in range(cur-1, -1, -1): # 자기 왼쪽
        if not connection[i][1]: break
        rotate(i, dir*((-1)**(cur-i)))
        
    for i in range(cur+1, 4): # 자기 오른쪽
        if not connection[i][0]: break
        rotate(i, dir*((-1)**(i-cur)))

for i in range(4):
    if wheels[i][0] == '1':
        answer += 2 ** i
print(answer)