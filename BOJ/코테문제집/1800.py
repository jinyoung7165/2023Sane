# 1-n 컴터. p쌍만 서로 이어질 수 있음
# 1번은 인터넷 서버와 바로 연결. 1-n연결 목표. 나머지 컴터 연결은 상관x.
# k개 인터넷 선에대해 공짜 연결. 나머지 선은 남은 것 중 가격이 제일 비싼 것
# 1번과 n컴터 연결 불가능 시 -1 출력
# 가격 범위 큼. 경로 상 k개 최대 비용 제거, 결과로는 경로상 최대 비용 return(이게 최소가 돼야 함)
# 지금 당장 최소 비용으로 가는 게 중요한 게 아님. 
# 예산을 정하고, n까지 최대 예산 지켜 최단 거리로 감. 이 때 예산을 초과한 케이블 수가 k개 이하여야 함
# 예산, 케이블 수 지켜 1-n 연결 할 수 있는지 핵심
# 예산->bs로 결정. n도착 가능할 때 예산 줄여나감
# 케이블수->해당 예산만큼 쓰며 이동. 예산 넘으면 free 케이블 씀.
# free cable 최대한 적게 쓰며 이동해야(예산 최대한 적게 넘겨 이동해야)
# 마지막에 남은 free cable만큼 공짜 처리 받을 수 있음
# 최소 heap으로 이동하며, 해당 노드까지 쓴 free cable수가 줄어들면 재방문
# distance값: 해당 노드 도달하기까지 쓴 free cable 수
# distance[n]: k보다 크면, 공짜 k개로는 1-n 연결할 수 없다는 의미
import heapq
from sys import stdin
from collections import defaultdict
INF = float('INF')
input = stdin.readline
n, p, k = map(int, input().split()) # 컴터 수, 연결된 컴터 수, 공짜 cable수
graph = defaultdict(list)
m_c = 0
for _ in range(p): # 연결 가능 p쌍
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    m_c = max(m_c, c) # 최대 비용

start, end =  0,  m_c # 최소 비용, 최대 비용

def check(budget): 
    que = []
    visited = [INF] * n
    visited[0] = 0 # 1번 CABLE까지 도착하기 위해 사용된 free cable수
    heapq.heappush(que, (0, 1))
    
    while que:
        used, cur = heapq.heappop(que) # 사용된 free케이블 수, 현재 노드
        if cur == n:
            return True
        # 노드까지 도달하기 위한 free케이블 수가 줄어들 때만 재방문
        if visited[cur-1] < used: continue
        for v, cost in graph[cur]:
            tmp = used # free cable 더 쓸지 고민하자
            if cost > budget: # 예산 초과
                if tmp < k: # cable 남았을 때
                    tmp += 1 # 사용해야 하는 free cable 수 증가 
                else: continue
            
            if tmp < visited[v-1]: # free cable 수 줄어들 때만 재방문
                visited[v-1] = tmp
                heapq.heappush(que, (tmp, v))
    return False 

def bs(left, right):
    answer = -1
    while left <= right:
        mid = (left+right) // 2 # 최대 간선 비용
        if check(mid): # 해당 비용으로 n도달 가능, 예산 더 줄여보자 
            right = mid - 1
            answer = mid
        else:
            left = mid + 1
    return answer

answer = bs(start, end) # 무료 k개 제외한 최대 간선 비용
print(answer)
