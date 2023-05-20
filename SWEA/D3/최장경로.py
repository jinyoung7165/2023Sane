# m개 간선 무방향 그래프에서 최장 경로의 길이(정점 개수)
# 1-n 정점. 경로에 같은 정점 번호 2번 이상 등장 불가.
# 두 정점 사이 여러 간선 존재 가능. 최대 n

tc = int(input())
def dfs(cur, cnt):
    global answer
    answer = max(answer, cnt)
    visit[cur] = True
    for node in graph[cur]:
        if not visit[node]:
            dfs(node, cnt+1)
    visit[cur] = False
        
for T in range(1, tc+1):
    answer = 1
    n, m = map(int, input().split()) # 정점, 간선
    graph = [[]*(n+1) for _ in range(n+1)]
    visit = [False] * (n+1)
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1, n+1):
        dfs(i, 1)
        
    print("#"+str(T), answer)