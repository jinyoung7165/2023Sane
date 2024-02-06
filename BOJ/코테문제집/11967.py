# 불 켜기
'''
n*n개의 방번호 (1,1)~(n,n)존재
(1,1): 유일하게 불 켜져 있음. 출발지
불 켜진 방으로만 이동 가능. 상하좌우 인접 방
불을 켤 수 있는 방의 최대 개수
(x,y) 방에서 (a,b) 방 켜고 끌 수 있음
방을 위한 스위치 여러 개 존재 가능

스위치 켜놓은 방들 일단 미리 저장
인접한 방이 켜져 있으면 이동 가능

1. 나의 구현 (느림)
불 켜기 -> 인접 이동하면서 불 있으면 큐에 넣기 -> que 비면, light랑 visited 모두 뒤져서 큐에 넣기
visited[i][j] 1: (i, j) 인접 노드 방문함, 2: (i, j) 방문까지 끝남


2. 답지 참고
불켜면서 방문 기록 있으면(이동은 가능한데 불 나중에 켠 것), 큐에 추가
인접 이동하면서 불 켜져 있으면, 큐에 추가. 켜져 있지 않으면 방문 기록만
'''
from sys import stdin
from collections import defaultdict, deque

input = stdin.readline
graph, ingress = defaultdict(list), defaultdict(int)
dirs = [(0,1),(1,0),(0,-1),(-1,0)]
answer = 0

n, m = map(int, input().split())
for _ in range(m):
    a, b, c, d = map(int, input().split()) # (c,d) 도달 위해 (a,b) 방문 필요
    graph[(a, b)].append((c, d))

def bfs():
    visited = [[0]*(n+1) for _ in range(n+1)] # (i,j) 인접 좌표에 방문한 기록 존재
    visited[1][1] = 2 # 1: 해당 좌표의 인접 방문했다. 2: 해당 좌표까지 방문했다

    que = deque([(1,1)])
    lights = set() # 새롭게 불 켠 곳들
    lights.add((1,1)) # (1,1) 처음부터 켜짐
    while que:
        x, y = que.popleft()
        
        for a, b in graph[(x, y)]:
            lights.add((a, b)) # 불 켠 곳 추가
            
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0<nx<=n and 0<ny<=n and visited[nx][ny] != 2:
                if (nx, ny) in lights:
                    que.append((nx, ny))
                    visited[nx][ny] = 2
                else:
                    visited[nx][ny] = 1
        
        if not que:
            for a, b in lights:
                if visited[a][b] == 1:
                    que.append((a, b))
                    visited[a][b] = 2
                    
    print(len(lights))

bfs()


import sys
from collections import deque,defaultdict
input=sys.stdin.readline

n,m=map(int,input().split())
graph=defaultdict(list)

for i in range(m):
    x,y,a,b=map(int,input().split())
    graph[(x,y)].append((a,b))
    

def bfs():
    queue=deque()
    queue.append((1,1))
    visited=[[0]*(n+1) for _ in range(n+1)]
    visited[1][1]=1
    lighted=[[0]*(n+1) for _ in range(n+1)]
    lighted[1][1]=1
    ans=1
    while queue:
        x,y=queue.popleft()
        for x1,y1 in graph[(x,y)]:
            if not lighted[x1][y1]:
                lighted[x1][y1]=1
                ans+=1
                if visited[x1][y1]:
                    queue.append((x1,y1))

        for dx,dy in [(-1,0),(0,1),(0,-1),(1,0)]:
            x1=x+dx
            y1=y+dy
            if 1<=x1<=n and 1<=y1<=n and not visited[x1][y1]:
                visited[x1][y1]=1
                if lighted[x1][y1]:
                    queue.append((x1,y1))
            
                
    return ans
 

print(bfs())   