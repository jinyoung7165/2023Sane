# Reconstruct Itinerary
'''
cycle 허용하며 모든 간선 다 써야 함 -> DFS
JFK에서 항상 시작. 답 여러 개면, 알파벳 더 작은 거 골라라(ticket 정렬해두자)
부분 경로: root출발지->다음 목적지 존재 시, pop하며 leaf 도착
=> leaf에서 root로 다시 올라가며(return), 다른 도착지(자식) 존재하면 확장하며 path 기록
주의1. 같은 코스의 간선 여러 번 주어질 수 있음 -> visited 단순 set 불가
    visited 처리를 graph[cur]에서 pop하는 걸로 대체
    -> 맨 뒤에서 pop()하기 때문에 처음의 ticket reverse 정렬 필요
주의2. dfs로 부분 경로 끝날 때까지(leaf도착) 탐색 시,
    leaf -> root 순으로 return하며 path 추가하기 때문에 result reverse 필요

Input1: tickets = [["JFK","KUL"],["JFK","NRT"],["KUL","JFK"]] -> JFK KUL JFK NRT
부분 경로: (root)JFK-KUL-JFK-NRT(leaf). root->leaf dfs 재귀 호출, leaf->root 위로 올라가며 각 dfs return
Input2: tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]] -> JFK NRT JFK KUL
부분 경로: (root)JFK-KUL(leaf) leaf부터 올라가며 dfs return하며,
이전 노드의 함수로 돌아와 다른 자식 확장 NRT-JFK(leaf), leaf->root 위로 올라가며 각 dfs return
'''
from collections import defaultdict

def findItinerary(tickets):
    graph = defaultdict(list) #출발지에 따른 목적지 여러 개일 수 있다
    for a,b in sorted(tickets, reverse=True): #사전 역순 정렬해 출발지에 대한 목적지 딕셔너리
        graph[a].append(b)
    route = []
    
    def dfs(a):
        while graph[a]: # a로부터 갈 수 있는 목적지가 있으면
            el = graph[a].pop()
            dfs(el) # pop했기 때문에 재방문하지 않는다
        route.append(a) # leaf 도착 시, append하며 이전 dfs로 return
    
    dfs("JFK")
    return route[::-1] # root부터 출력하도록 reverse


findItinerary([["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]])
findItinerary([["JFK","KUL"],["JFK","NRT"],["KUL","JFK"]])