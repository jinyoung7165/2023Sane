# 소형기관차
'''
dp[i][j]: i개의 차 사용. j객실까지 고려했을 때 누적 최댓값 -> dp[3][n-1] 구하면 됨
dp[i][j] = max(
    dp[i][j-1], 현재 원소 포함x 묶음 유지
    (el[j]+el[j-1]+...el[j-k+1]) + dp[i-1][j-k])
    현재 원소까지 포함하는 묶음1 + 현재 이전묶음의 최대
'''
from sys import stdin
input = stdin.readline
n = int(input())
members = list(map(int, input().split()))
k = int(input())
s = [0]*n # [i]까지 k개 포함했을 때의 합
for i in range(n):
    if i < k: s[i] += s[i-1]+members[i]
    else: s[i] = s[i-1]-members[i-k]+members[i]
dp = [[0]*n for _ in range(4)] # i개 차 사용할 때, j객실까지 고려
for i in range(1, 4):
    for j in range(k*i-1, n):
        dp[i][j] = max(dp[i][j-1], s[j]+dp[i-1][j-k])
print(dp[3][n-1])

'''
dp[i][j]: i원소부터 끝까지 j묶음 만들었을 때 최댓값 -> dp[0][3]
dp[i][j] = max(
    dfs(i+1, cnt), # 나 포함x
    (el[i]+el[i+1]...el[i+k-1]) + dfs(i+k, cnt-1) # 나부터 k개 선택 + 다음 묶음
'''
from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
input = stdin.readline
n = int(input())
members = list(map(int, input().split()))
k = int(input())
s = [0]*n # [i]부터 k개 포함했을 때의 합
s[n-1] = members[n-1]
for i in range(n-2,-1,-1):
    if i >= n-k: s[i] += s[i+1]+members[i]
    else: s[i] = s[i+1]-members[i+k]+members[i]
dp = [[-1]*4 for _ in range(n)] # i차까지 보며 j묶음 만들 때, 최댓값
def dfs(i, cnt):
    if cnt == 0 or i >= n: return 0
    if dp[i][cnt] >= 0: return dp[i][cnt]
    dp[i][cnt] = max(dfs(i+1, cnt), s[i] + dfs(i+k, cnt-1))
    return dp[i][cnt]
    
print(dfs(0, 3)) # [0]부터 끝까지 3묶음 생성