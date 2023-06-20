# 서로 다른 n개 자연수 주어짐
# 길이 m인 수열
n, m = map(int, input().split())
nums = sorted(map(int, input().split()))
path = []
visited = [False]*n
def dfs(idx):
    if idx == m:
        print(*path)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            path.append(nums[i])
            dfs(idx+1)
            path.pop()
            visited[i] = False
dfs(0)