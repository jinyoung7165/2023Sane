# 타임머신
# 벨만 포드: 유향 가중치 그래프에서 최단 거리 찾기
# 가중치가 음수도 가능할 때 한 노드->다른 노드 최단 거리
# 단순 음수 간선->그대로 가중치 계산
# 사이클 존재, but, 양수값 더 클 때 -> 그대로 진행
# 사이클 존재, 음수값 더 클 때 -> 사이클 순환할 수록 가중치 감소 -> 비용은 감소하지만, 동일 노드 방문x 제약 조건 필요
# 시작 노드->다른 노드 값 무한 대로 설정
# 현재 노드의 모든 인접 노드 탐색 후. 거리 갱신
# (v-1개) 노드의 인접 노드에 대해 거리 갱신 후, 또 거리 갱신된다면 -무한대를 발생시키는 음수 사이클이 존재한다는 것
# n개 도시. 다른 도시로 도착하는 버스 m개
# 버스 a도시->c(시간)->b도시
# c=0인 경우 순간 이동, c<0인 경우 타임머신으로 시간 되돌아가는 경우
# 1번 도시에서 출발해 나머지 도시로 가는 가장 빠른 시간 구하라
# 만약 어떤 도시로 가는 과정에서 시간을 무한히 옛날로 돌릴 수 있다면 -1 출력
# 그렇지 않으면 n-1 줄에 걸쳐 1->각 도시로 가능 가장 빠른 시간 출력
# 만약 해당 도시로 가는 경로 없으면 -1 출력
# edge 기준 저장, 순회해야 함(defaultdict나 이중 리스트로 저장하면, 모든 노드*모든 edge를 n회 탐색하는 3중 포문->비효율)
from sys import stdin
M = float('inf')
input = stdin.readline
edges = []

n, m = map(int, input().split()) # 도시, 버스 노선 수

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
  
result = [M]*(n+1) # 1~n개의 도시로 도착하는 최소 비용
result[1] = 0 # 자신에게 도착

def bellman_ford():
    global result
    for i in range(n):
        for a, b, c in edges:
            # start->a로 갈 수 있다고 기록
            # a거쳐서 b로 도착하면 비용 감소할 때 갱신
            if result[a] != M and result[a] + c < result[b]:
                if i == n-1: # 음수 사이클
                    return True
                result[b] = result[a] + c # 경유 후 갱신
    return False

flag = bellman_ford() # 음수 사이클  

if flag: # 음수 사이클
    print(-1)
else:
    for i in range(2, n+1):
        print(result[i] if result[i]!=M else -1)