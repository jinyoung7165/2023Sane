# 출근 기록
# 
'''
dp[날짜][남은a][남은b][남은c]: dp[마지막날][0][0][0]일 뗴 1 가능한지 여부
조합. a를 쓰거나, b를 쓰거나, c를 쓰거나
dp[a][b][c][pprev][prev]: 조합뿐만 아니라, 이전 원소 순서에 영향 받음 -> prev, pprev 기억해야 함
'''
from sys import stdin

input = stdin.readline

records = input().rstrip()
a = records.count('A')
b = records.count('B')
c = records.count('C')
size = len(records)
dp = [[[[[-1]*3 for _ in range(3)] for _ in range(c+1)] for _ in range(b+1)] for _ in range(a+1)]

result = []
def dfs(idx, a, b, c, pprev, prev):
    if idx == size:
        if a == 0 and b == 0 and c == 0: return 1
        return 0
    
    if dp[a][b][c][pprev][prev] != -1: return dp[a][b][c][pprev][prev]
    
    if c and pprev!=2 and prev!=2:
        dp[a][b][c-1][prev][2] = dfs(idx+1, a, b, c-1, prev, 2)
        if dp[a][b][c-1][prev][2]:
            result.append('C')
            return 1
    if b and prev!=1:
        dp[a][b-1][c][prev][1] = dfs(idx+1, a, b-1, c, prev, 1)
        if dp[a][b-1][c][prev][1]:
            result.append('B')
            return 1
    if a: 
        dp[a-1][b][c][prev][0] = dfs(idx+1, a-1, b, c, prev, 0)
        if dp[a-1][b][c][prev][0]:
            result.append('A')
            return 1
    return 0
dfs(0, a, b, c, 0, 0) # 전전날, 전날
print(''.join(result) if result else -1)