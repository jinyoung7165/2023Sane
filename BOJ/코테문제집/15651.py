# n과 m(3)
# 같은 수 여러 번 골라도 됨(중복 수열)
# 1<=m<=n<=7
# 중복되는 수열 출력x
n, m = map(int, input().split())
path = [] # 매개변수로 전달하는 것보다 global 변수 쓰는 게 훨 빠름
def dfs(idx):
    if idx == m:
        print(*path)
        return
    for i in range(1, n+1):
        path.append(i)
        dfs(idx+1)
        path.pop()
dfs(0)