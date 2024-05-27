'''
게리맨더링 2
n*n. 최대 길이 20
구역을 다섯 선거구로 나눠야 함
구역A 인접 구역 -> 구역B 갈 수 있을 때, 연결됐다 표현
모두 같은 선거구에 포함된 구역이어야 함
기준 점(X,Y)와 경계길이 d1,d2(1이상. )

구역 (r, c)의 인구는 A[r][c]
선거구에 포함된 구역의 인구를 모두 합한 값
인구가 가장 많은 선거구-가장 적은 선거구의 인구 차이의 최솟값
'''
from sys import stdin
input = stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
result = float('inf')



def dfs(x, y, d1, d2):
    a = [0] * 5
    sections = list(set() for _ in range(5))
    for i in range(n):
        for j in range(n):
            if i<x+d1 and j<=y:
                sections[0].add((i, j))
            elif i<=x+d2 and y<j:
                sections[1].add((i, j))
            elif x+d1<=i and j<y-d1+d2:
                sections[2].add((i, j))
            elif x+d2<i and y-d1+d2<=j:
                sections[3].add((i, j))
            else:
                sections[4].add((i, j))
    for i in range(5):
        for r, c in sections[i]:
            a[i] += board[r][c]
    print(a)
    return max(a) - min(a)


for x in range(n):
    for y in range(n):
        for d1 in range(1, n-1):
            for d2 in range(1, n-1):
                if x+d1+d2<=n-1 and 0<=y-d1<y+d2<=n-1:
                    result = min(result, dfs(x, y, d1, d2))
                
print(result)