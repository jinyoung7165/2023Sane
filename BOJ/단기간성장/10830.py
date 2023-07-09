# 행렬 제곱
# 크기가 n*n인 행렬 a 주어짐
# a의 b제곱 구하는 프로그램
# a^b의 각 원소를 1000으로 나눈 나머지를 출력하라
# b 크기 어마어마하게 큼 -> (같은 일)을 연속적으로 재귀
# 곱하는 일 순서가 상관 없음 -> 2분할해가며 거듭제곱 -> 합치자
# 행렬 크기 n과 b 주어짐
# 행렬 각 원소는 0~1000
from sys import stdin
input = stdin.readline

n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

def divide(matrix, n, b): # (두 행렬 곱)제곱이 될 때까지 나누자
    if b == 1: return matrix # 1 제곱 자기 자신
    elif b == 2: return conquer(matrix, matrix, n) # 거듭 제곱
    else:
        result = divide(matrix, n, b//2) # 2개씩 끝까지 나눠 갔을 때 결과, 자기자신 or 거듭제곱
        # b=4였을 때, 거듭제곱 결과인 result끼리 곱해 return
        # b=3였을 때, divide결과인 자기자신=result*(거듭제곱=result*result) 곱해 return
        if b%2 == 0: # 총 제곱을 2의 배수만큼 해야 하는 경우, 깔끔하게 거듭제곱끼리 합침
            return conquer(result, result, n)
        else: # 제곱을 홀수 번 해야 하는 거였음 -> ex:?번 -> 자기자신*(거듭제곱 ?-1번 결과)
            return conquer(matrix, conquer(result, result, n), n)
            # 자기자신!=result -> matrix 곱해야 함!!!!!!!!!!!!!!!!!!
def conquer(m1, m2, n): # 두 행렬 곱
    result = [[0]*n for _ in range(n)]
    for i in range(n): # 앞의 행렬->행 뽑기
        for j in range(n): # 뒤의 행렬->열 뽑기
            for k in range(n): # 뽑은 행, 열에 있는 n개의 원소만큼 계산 
                result[i][j] += m1[i][k]*m2[k][j]
            result[i][j] %= 1000
    return result
    
result = divide(matrix, n, b)
for row in result:
    for col in row:
        print(col%1000, end=' ')
    print()