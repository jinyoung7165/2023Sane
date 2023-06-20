# 외판원 순회
# 1~N 도시. 사이 길 존재
# 어느 한 도시 -> N개 모두 거쳐 다시 원래대로 돌아오는 순회
# 한번 갔던 도시로는 다시 갈 수 없음.
# 가장 적은 비용 출력하라
from sys import stdin
input = stdin.readline

n = int(input())
weights = [list(map(int, input().split())) for _ in range(n)]
res = float('inf')
path = [False]*n
path[0] = True

def dfs(cur, cost, visit):
    global path, res
    if visit == n:
        if cur == 0:
            res = min(res, cost)
        return
    for v, c in enumerate(weights[cur]):
        if c == 0 or cost+c >= res: continue
        if not path[v]: # 방문x곳만 가자
            path[v] = True
            dfs(v, cost+c, visit+1)
            path[v] = False
        elif visit+1 == n and v == 0:
            dfs(v, cost+c, visit+1)
            
dfs(0, 0, 0)

print(res)