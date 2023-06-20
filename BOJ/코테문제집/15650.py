# n과 m(2)
# n, m 주어졌을 때 1~n 자연수 중 중복 없이 m개 고른 수열
# 오름차순 수열
# 1<=m<=n<=8
# 한 줄에 하나씩 문제의 조건 만족하는 수열 오름차순 출력
# nPm
n, m = map(int, input().split())
visit = [False] * n
def dfs(idx, path):
    global visit
    if idx == m:
        print(*path[1:])
        return
    for i in range(path[-1], n): # 방문한 원소보다 오름차순
        if not visit[i]: # 방문x일 때만
            visit[i] = True
            path.append(i+1)
            dfs(idx+1, path)
            visit[i] = False
            path.pop()
    
dfs(0, [0])