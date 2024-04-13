# 사회망 서비스
'''
내가 활성노드가 아니라면, 모든 인접노드가 활성 노드여야 함
연결 형식 주어졌을 때 필요한 활성 노드의 최소 수?

각 서브트리의 루트 활성화 -> 자식은 활성일 수도 있고, 아닐 수도 있음
각 서브트리의 루트 비활성화 -> 자식은 무조건 활성이어야 함
선택 or not -> dp + dfs
dp[i][0]: i번(루트) 활성화 x, 그 밑 전체 포함해서 활성화 노드 수
dp[i][1]: i번(루트) 활성화 시, 그 밑 전체 포함해서 활성화 노드 수. 나 자신 활성화 -> 전체 활성화 개수 +1 됨
'''
from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)
input = stdin.readline

n = int(input())
edges = [[] for _ in range(n+1)]
visited = [False] * (n+1)
dp = [[0, 1] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

def dfs(cur): # cur을 루트로 보고, 그 아래 서브트리로 이동해나감
    visited[cur] = True
    for node in edges[cur]:
        if not visited[node]:
            dfs(node)
            dp[cur][0] += dp[node][1] # 자식 무조건 활성화해야 함
            dp[cur][1] += min(dp[node]) # 자식 활성화할 수도 있고, 아닐 수도 있음
            
dfs(1) # 아무노드에서 시작해도 됨
print(min(dp[1]))