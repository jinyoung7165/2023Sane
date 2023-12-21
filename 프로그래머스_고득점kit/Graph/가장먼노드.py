# 1-n 번호 노드
# 1노드에서 가장 멀리 떨어진 노드의 개수 구하려 함
# 가장 멀리 떨어진 노드: 최단 경로로 이동 시 간선 개수 가장 많은 노드
# 가중치 없는 그래프 -> heapq 쓰지 않고 bfs로 해결
from collections import defaultdict, deque
def solution(n:int, edge:list):
    M = 0
    answer = 0
    visited = set()
    que = deque([(1, 0)])
    graph = defaultdict(list)
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)

    visited.add(1)
    while que:
        flag = False
        cur, depth = que.popleft()
        for node in graph[cur]:
            if node not in visited:
                visited.add(node)
                flag = True
                que.append((node, depth + 1))
        if not flag: # leaf면 depth, answer 갱신
            if depth > M:
                M = depth
                answer = 1
            else:
                answer += 1
    
    return answer