# 케빈 베이컨 6단계 법칙
# 모든 사람들 최대 6단계 이내에 서로 지인으로 연결 가능
# 두 사람이 최소 몇 단계만에 이어질 수 있는지 계산
# 모든 사람과 계산했을 때, 단계의 총 합이 가장 적은 사람
# 1-3, 1-4, 2-3, 3-4, 4-5인 경우
# 1: 1-2-3, 1-4-5 로 모두 연결 가능. 모든 사람에 대한 단계합 1+1+2+2=6
# 3: 3-1, 3-2, 3-4-5. 1+1+1+2=5로 최소(4도 마찬가지).
# 최소합을 가지는 사람 중 가장 번호 작은 사람 출력
# 모든 사람 간의 거리 구해야 하므로 플로이드 워셜 floyd
from sys import stdin
INF = float('inf')
input = stdin.readline
cnt, answer = INF, 0 # sum, 사람
n, m = map(int, input().split()) # 사람, 관계수
distance = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split()) 
    distance[u][v] = 1
    distance[v][u] = 1
    
for k in range(1, n+1): # 경유지
    for i in range(1, n+1): # 출발
        for j in range(1, n+1): # 도착
            if i == j: # 자기자신
                distance[i][j] = 0
                continue
            distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
for i in range(1, n+1):
    s = sum(distance[i][1:])
    if s < cnt:
        cnt = s
        answer = i
print(answer)