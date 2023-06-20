# n과 m(4)
# 같은 수 여러 번 골라도 됨(중복 수열)
# 1<=m<=n<=7
# 중복되는 수열 출력x. 비내림차순 출력(path의 top보다 크거나 같아야 함)
#
n, m = map(int, input().split())
path = [0] # 매개변수로 전달하는 것보다 global 변수 쓰는 게 훨 빠름
def dfs(idx):
    if idx == m:
        print(*path[1:])
        return
    for i in range(path[-1], n+1):
        if i==0: continue
        path.append(i)
        dfs(idx+1)
        path.pop()
dfs(0)