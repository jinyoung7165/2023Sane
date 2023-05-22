# 1-n 번호 노드
# 1노드에서 가장 멀리 떨어진 노드의 개수 구하려 함
# 가장 멀리 떨어진 노드: 최단 경로로 이동 시 간선 개수 가장 많은 노드
# import heapq
from collections import defaultdict, deque

def solution(n:int, edge:list):
    visit = set()
    graph = defaultdict(list)
    m = 0 # 최대 거리
    answer = 0 # 최대 거리를 갖는 노드 개수
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
        
    que = deque([(0, 1)])# 1->1 0의 비용
    while que:
        c, u = que.popleft()
        if u in visit: continue
        visit.add(u)
        
        if c > m: # 최댓값 갱신
            m = c
            answer = 1
        else:
            answer += 1
            
        if len(visit) == n:
            break
        
        for node in graph[u]:
            if node not in visit:
                que.append((c+1, node))

    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))