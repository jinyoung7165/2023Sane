# 행렬의 곱셈
# n*m행렬 a와 m*k행렬 b 주어짐
# 두 행렬 곱해라 (n*k)
'''
1,2   -1 -2 0  -> -1 -2 6
3,4    0  0 3  -> -3 -6 12
5,6            -> -5 -10 18
'''
from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]
c= [[0]*k for _ in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            c[i][j] += a[i][l] * b[l][j]
    print(*c[i])
