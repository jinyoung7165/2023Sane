# 항상 ICN에서 시작
# 방문하는 공항 경로를 배열에 담아 return
# 모든 티켓을 다 써야 함. 가능 경로가 여러 개면 알파벳 오름차순
# 모든 공항은 대문자. 3글자
# tickets의 [a,b]는 a->b로 갈 수 있음 의미
# tickets=[["ICN","JFK"],["HND","IAD"],["JFK","HND"]]
# => [ICN,JFK,HND,IAD]
# tickets=[["ICN","SFO"],["ICN","ATL"],["SFO","ATL"],["ATL","ICN"],["ATL","SFO"]]
# => [ICN,ATL,ICN,SFO,ATL,SFO]>[ICN,SFO,ATL,ICN,ATL,SFO]

# 무조건 알파벳 순서가 앞서는 거 선택하면 안됨(모든 티켓 순회 가능해야 함) -> 단순heapq.pop 아님
# 최단 거리보다는. 모두 순회하는 문제

# CYCLE이 존재할 수도 있는 구조-> 위상정렬(INGRESS)로 풀면 안됨
# 출발지 정해져 있는데, 그 경로가 여러 가지임

# BFS while Que: FIFO로 [ICN,ATL], [ICN,SFO] 부터 탐색 시 모두 순회 안되는 경우에 다시 출발지로 돌아오기 어려움
# 따라서 DFS로 푸는 게 효율적이다.
# 보통 DFS는 STACK 사용->pop쓰기 위해 역순으로 넣자 

# 모든 간선 탐색해야 하는데(완전탐색), 순환 가능-> bfs보다 dfs 쓰자
# stack에 간선 넣으면, visited 볼 필요도 없음
from collections import defaultdict

# 따봉 지피티의 도움
def solution(tickets: list):
    graph = defaultdict(list)
    # stack 사용을 위해 내림차순 정렬
    for start, end in sorted(tickets, reverse=True):
        graph[start].append(end)
        
    def dfs(cur, path):
        if len(path) == len(tickets) + 1: # 모든 간선 순회
            return path # 이동 경로 반환
        if cur not in graph: # 간선 다 돌지 못했는데, 더 이동 불가
            return None # 잘못된 경로 선택이었음 -> dfs로 돌아가기
        
        # for문 돌릴 때마다 reversed iterator 반환
        for end in reversed(graph[cur]):  # 오름차순으로 end 선택
            graph[cur].remove(end) # 일단 작은 알파벳부터 선택
            ret = dfs(end, path + [end]) # 임시 경로에 추가
            if ret: # 모든 간선 순회할 수 있다면 바로 path를 리턴할 것
                return ret
            # 잘못된 선택->다음 오름차순 원소를 선택하기 위해 재정비
            # 다음에 다시 선택하기 위함
            graph[cur].append(end)

    return dfs("ICN", ["ICN"])

def findItinerary(tickets):
    graph = defaultdict(list) #출발지에 따른 목적지 여러 개일 수 있다
    for a,b in sorted(tickets, reverse=True): #사전 역순 정렬해 출발지에 대한 목적지 딕셔너리
        graph[a].append(b)
    route = []
    
    def dfs(a):
        while graph[a]: #a로부터 갈 수 있는 목적지가 있으면
            el = graph[a].pop()
            print(el)
            dfs(el) #첫번째 목적지를 넘기며 pop했기 때문에 재방문하지 않는다
        route.append(a)
        print(route)
        # 목적지로 모두 이동 후 현재 위치 append ->
        # DFS이기 때문에 맨 끝 Leaf Node들부터 append됨
        # 간선 중 알파벳 제일 작은 원소 먼저 선택하는데, 
        # 빠르게 Leaf만나면 route에 추가, 이후 더 큰 원소 선택 후 많이 이동하고 Leaf만나면 route에 추가
        # <-> 둘의 상황 반대가 될 수 있음. 아무튼 가장 depth가 짧은 leaf부터~다시 위로 올라가며 root까지 경로에 추가하기 때문에 reverse시 바른 순서 반환
        #(오름차순. 먼저 선택) 6 root 1(기록 순서)
        #                   5 /   ^ 2
        #                   4 v -> 3 
        # dfs 재귀-> 맨마지막 방문 노드가 route에 먼저 기록됨
        # 이동 순서 알려면 뒤집어야 함
    dfs("ICN")
    return route[::-1]

print(findItinerary([["ICN","A"],["ICN","B"],["B","ICN"]]))
# ICN->B->ICN->A
# graph {'ICN': ['B', 'A'], 'B': ['ICN']}
# A가 Leaf->route에 추가. B->ICN Leaf->route에 ICN,B 추가->루트였던 ICN추가
# route:[A,ICN,B,ICN] => reverse[ICN,B,ICN,A]
print(findItinerary([["ICN","A"],["ICN","B"],["A","ICN"]]))
# ICN->A->ICN->B
# graph {'ICN': ['B', 'A'], 'A': ['ICN']}
# A->ICN Leaf->route에 ICN,A추가 -> B가 Leaf->route에 추가->루트였던 ICN추가
# route:[B,ICN,A,ICN] => reverse[ICN,A,ICN,B]