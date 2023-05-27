# 플로이드
# n(2~100)개의 도시. 한 도시=>다른 도시에 도착하는 m(1~100,000)개 버스
# 각 버스는 한 번 사용할 때 필요한 비용 존재
# 모든 도시 쌍(a,b)에 대해 a->b 비용의 최솟값 구하라
# 버스 a->b c 주어짐. 같은 지점 간 c여러 개일 수 있음
# 출발지 여러 개=> distance 저장하는 여러 개의 dp 필요
from sys import stdin
input = stdin.readline
n = int(input()) # 도시 수
m = int(input()) # 버스 수

distance = [[float('inf')]*(n+1) for _ in range(n+1)] # i->i도시로 가는 비용
for _ in range(m):
    u, v, c = map(int, input().split())
    distance[u][v] = min(c, distance[u][v]) # 같은 지점 간 간선 여러 개 가능

for k in range(1, n+1): # 경유지가 맨 위에 있어야 모든 경유지 거쳐 감
    for i in range(1, n+1): # 출발지
        for j in range(1, n+1): # 도착지
            if i == j: # 출발지=도착지
                continue
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j]) 

for dis in distance[1:]:
    for i in dis[1:]:
        print(i if i!=float('inf') else 0, end =" ")
    print()