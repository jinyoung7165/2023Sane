'''
외판원 순회
1~n 번호 도시 사이 길 존재. 
한 출발점 -> n 도시 모두 방문해 돌아오는 경로
길이 없을 수도 있음. 재방문 불가
w[i][j]는 도시 i->j 방문 비용. 단방향
0->1->2->3->0
0에서 출발한다고 하자
visit dfs 호출 전후 처리 -> 도시 많아질수록 배열 비용 높아짐
비트마스크 전달하며 단일 정수로 처리하자
비트마스크 사전으로 관리 dp[(?, 비트)] = ?
dp[(cur, visit)]: cur에서 시작하여 "아직 방문하지 않은  = visit에 없는 도시들을 모두 방문하고" 다시 "시작점 0"으로 돌아오는 최소 비용
0->1->3과 0->3->1 모두 같은 visit 값을 가집니다 0111
but dp값 다름 (cur: 가장 마지막으로 방문한 노드, visit에 의해 결정되기 때문)
'''
from sys import stdin
input = stdin.readline

M = float('inf')
answer = M
n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
dp = {}
# visit = [0]*n 대체해보자. 0 -> i까지의 최소 거리
# 각 dfs에 visit한 노드를 비트마스킹으로 전달
# 11111 n개만큼 1있으면 모두 방문한 것
# 1 << n: 1+  n만큼 0생김 100000 -> -1하면 1 * n개
def dfs(cur, visit):
    if visit == (1<<n) -1: # n 노드 모두 방문
        if w[cur][0] != 0: return w[cur][0] # cur -> 0 도달 가능
        return M
    if (cur, visit) in dp:
        return dp[(cur, visit)]
    
    min_cost = M
    for i in range(1, n): # 0빼고 다른 노드로 갈 수 있음
        if not(visit & (1 << i)) and w[cur][i]: # 방문하지 않았을 때
            cost = dfs(i, visit | (1 << i)) + w[cur][i]
            min_cost = min(cost, min_cost)
    dp[(cur, visit)] = min_cost
    return min_cost

print(dfs(0, 1))