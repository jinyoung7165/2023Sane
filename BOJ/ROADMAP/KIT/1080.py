from sys import stdin
# 행렬
'''
3*3 window에서 row 또는 col이 동일하면, 이동 혹은, XOR
'''
input = stdin.readline
n, m = map(int, input().split())
a = [list(map(int, input().strip())) for _ in range(n)]
b = [list(map(int, input().strip())) for _ in range(n)]

def convert(row, col):
    for i in range(3):
        a[row+i][col] ^= 1
        a[row+i][col+1] ^= 1
        a[row+i][col+2] ^= 1
    
answer = 0
for row in range(n-2):
    for col in range(m-2):
        if a[row][col] != b[row][col]:
            answer += 1
            convert(row, col)
if a != b: answer = -1
print(answer)