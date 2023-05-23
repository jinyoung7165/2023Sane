# 폭우로 일부 지역 물에 잠김
# 잠기지 않은 지역 통해 학교 가자
# 집->학교 가는 길 m*n 크기의 격자 모양
# m=4, n=3 집(1,1)->(m,n)학교
# 물웅덩이 피해. 오른쪽. 아래쪽으로만 움직여 학교까지 갈 수 있는 최단경로 개수
# ->1,000,000,007로 나눈 나머지 return
# 메모리 줄이기 위해 이런 문제의 경우 bfs대신
# 방법1. dfs+백트래킹+dp로 풀어야 함: dp: 종점~해당좌표까지의 최단 경로 경우의 수(종점에서부터 더하는 dfs)
# 방법2. dp: (1,1)->해당 위치까지 최단 경로의 경우의 수: 바로 위의 원소 + 바로 왼쪽의 원소(출발지에서부터 더하는 dp)
def solution(m,n,puddles): # 훨씬 효율적인 dp
    # (1,1)->(x,y) 최단경로로 가는 경우의 수
    grid = [[0]*(m+1) for _ in range(n+1)]
    if puddles != [[]]: #물이 잠긴 지역이 0일 수 있음
        for a, b in puddles:
            grid[b][a] = -1  #미리 -1로 체크 -> i, j 커지면 set in연산보다 나음
            
    grid[1][1] = 1 # (1,1)->(1,1) 경우의 수 1
    
    for x in range(1,n+1): # 아래로 이동
        for y in range(1,m+1): # 오른쪽으로 이동하며 dp채우자
            if x == y == 1: #(1,1)은 1로 만들어두고, 0이 되지 않도록
                continue
            if grid[x][y] == -1: #웅덩이는 0으로 만들어 다음 덧셈 때 영향끼치지 않게
                grid[x][y] = 0
                continue
            # 현재 위치로 최단 거리로 올 수 있는 경우의 수
            # (내 "이전" 경로의 경우의 수 합): 내 왼쪽에서부터 + 내 윗쪽에서부터
            # 이전 경로이므로, 이동 가능 경로와 반대!!!!!!!
            grid[x][y] = (grid[x][y-1] + grid[x-1][y])%1000000007   #[a,b] = [a-1,b] + [a,b-1] 공식

    return grid[n][m]

print(solution(4,3,[[2,2]]))

dp = []
dir = [[0,1],[1,0]] # 오른쪽/아래쪽으로만 이동 가능
def dfs(x, y, n, m, puddles):
    global dp
    if x == n and y == m: return 1 # 종점 도착 가능 시 경로 수 추가
    if dp[x][y] != 0: return dp[x][y] # 이미 방문한 기록이 있으면 그거 쓰자
    for d in dir:
        nx, ny = x+d[0], y+d[1]
        if 0<nx<=n and 0<ny<=m and [ny, nx] not in puddles: # 이동 가능할 때
            dp[x][y] += dfs(nx, ny, n, m, puddles) # 다음으로 이동해서 종점 만나면 +1
    return dp[x][y] # 자신->종점 갈 수 있는 경우의 수 합 return
# dfs를 통해 맨마지막에 (1,1)->(n,m) 경우의 수 return
def solutionDFS(m:int, n:int, puddles:list):
    global dp
    dp = [[0]*(m+1) for _ in range(n+1)] # (x,y)->(m,n)
    # 해당 좌표로부터 종점까지의 경우의 수 
    answer = dfs(1,1,n,m,puddles)
    return answer % 1000000007