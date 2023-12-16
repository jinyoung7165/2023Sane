# Is Graph Bipartite?
'''
무방향. 이분 그래프면 True return
인접 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두 가지 색으로만
정점을 방문할 때마다 두 가지 색 중 하나를 칠한다.
자신과 인접한 정점의 색이 자신과 동일하면 이분 그래프가 아니다.
모든 정점을 다 방문했는데 위와 같은 경우가 없다면 이분 그래프이다.
노드별 직접 연결된 노드 리스트 주어짐
graph = [[1,2,3],[0,2],[0,1,3],[0,2]] -> false
graph = [[1,3],[0,2],[1,3],[0,2]] -> true
'''
from collections import deque
def isBipartite(graph) -> bool:
    que = deque([])
    size = len(graph)
    colors = [-1] * size
    for i in range(size-1):
        if colors[i] == -1: # 미방문
            colors[i] = 1 # 임의 설정
            que.append(i)
            while que:
                cur = que.popleft()
                for node in graph[cur]:
                    if colors[node] == -1:
                        colors[node] = 1 - colors[cur]
                        que.append(node)
                    elif colors[node] == colors[cur]:
                        return False
    return True