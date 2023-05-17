# n크기 입력. 1~n*n 숫자 시계방향
# n=3 -> [[123][894][765]]
# n=4 -> [[1234][12,13,14,5][11,16,15,6],[10,9,8,7]]
# ((0,0),(0,1),(0,2),(0,3),())
# 테스트 케이스 수 T. 그 아래로 각 테스트 케이스 -> n 입력
import sys
input = sys.stdin.readline
# SWEA에서는 위의 줄 주석 처리해야 함

# 오른쪽, 아래, 왼쪽, 위
d = [[0, 1], [-1, 0], [0, -1], [1, 0]]

tc = int(input())
            
for _ in range(tc):
    n = int(input())
    print("#{}".format(_+1))
    
    visit = [[0]*n for _ in range(n)]
    
    x, y, idx = 0, 0, 0 # 현재 위치, d 방향
    for i in range(1, n*n+1):
        visit[x][y] = i
        if i == n*n: break
        nx, ny = x+d[idx][0], y+d[idx][1]
        while not (0<=nx<n and 0<=ny<n and visit[nx][ny]==0):
            idx = (idx+1)%4
            nx, ny = x+d[idx][0], y+d[idx][1]
        x, y = nx, ny
    for i in range(n):
        print(*visit[i])
        
from collections import deque

def memory_exceed(): # 간단한 순회에 que 사용하지 말자
    for _ in range(tc):
        n = int(input())
        print("#{}".format(_+1))
        que = deque([(0, 0, 0)]) # x,y,d_idx
        visit = [[0]*n for _ in range(n)]
        
        num = 1
        while que:
            x, y, idx = que.popleft()
            visit[x][y] = num
            if num == n*n: break
            num += 1
            nx, ny = x+d[idx][0], y+d[idx][1]
            while not (0<=nx<n and 0<=ny<n and visit[nx][ny]==0):
                idx = (idx+1)%4
                nx, ny = x+d[idx][0], y+d[idx][1]
            que.append((nx, ny, idx))
            
        for i in range(n):
            print(*visit[i])