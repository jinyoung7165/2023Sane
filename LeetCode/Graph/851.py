# Loud and Rich
'''
0~N-1. m, q
richer [a, b]: a > b
quiet i : 크기 저장
answer[x]: x 본인 혹은 rich 큰 사람 중, quiet 가장 적음
방향성 비순환 그래프 -> 위상정렬. ingress 이용 : 작은 쪽으로 전파
혹은 dfs로 큰 애 찾아가서(leaf) return : 큰 쪽으로 전파
rich 큼: 먼저 실행 가능(ingress==0 작은 애한테 answer 전달 위함)
'''
# 위상 정렬 풀이
from collections import defaultdict, deque
class TopologicalSort:
    def loudAndRich(self, richer, quiet):
        size = len(quiet)
        ingress = [0]*size
        answer = [*range(size)]
        graph = defaultdict(list)
        for x, y in richer:
            graph[x].append(y) # 자기보다 작은 애 넣음. 작은 쪽으로 전파
            ingress[y] += 1 # 자기 이전에 실행돼야 하는 애 개수
        
        que = deque([x for x in range(size) if ingress[x] == 0])
        while que:
            x = que.popleft() # 큰 애
            for y in graph[x]:
                if quiet[answer[y]] > quiet[answer[x]]:
                    answer[y] = answer[x]
                ingress[y] -= 1
                if ingress[y] == 0: que.append(y) # 0인 것만 넣어야 시간 초과 해결
        return answer

# dfs 풀이(여행 일정 문제와 비슷함)
class DFS:
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for x, y in richer:
            graph[y].append(x) #y->x(더 rich한 쪽)
        
        result = [-1] * n
        def dfs(node):
            #least quiet person in this subtree
            if result[node] == -1: #아직 기록되지 않음
                result[node] = node #일단 자기자신. 현재 노드에 대한 min을 즉시 result[node]에 기록
                for child in graph[node]: # leaf가 될 때까지 계속 depth 확장
                    candidate = dfs(child)
                    if quiet[candidate] < quiet[result[node]]:
                        result[node] = candidate
            return result[node] #이미 기록된 노드는 탐색하지 않고 바로 리턴(여러 노드가 하나의 노드를 가리킬 수 있기 때문)

        for i in range(n):
            result[i] = dfs(i)
        return result