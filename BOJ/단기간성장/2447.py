# 별 찍기 - 10
# 재귀적 패턴으로 별 출력
# N이 3의 거듭제곱(3,9,27,...)라고 할 때, 크기 n의 패턴은 n*n모양
# 크기 3 패턴은 가운데에 공백
'''
***
* *
***
'''
# 크기 9인 패턴 가운데에 3*3 공백
# (3, 3)부터 (5, 5) 크기 3*3 공백으로

# 크기 3인 패턴 가운데에 1*1 공백
# (1, 1) 크기 1의 정사각형을 공백으로 -> (1, 4)-> (1, 7)
# (4, 1) 크기 1의 정사각형을 공백으로 -> (4, 4)-> (4, 7)
# (7, 1) 크기 1의 정사각형을 공백으로 -> (7, 4)-> (7, 7)
'''
*********
* ** ** *
*********
***   ***
* *   * *
***   ***
*********
* ** ** *
*********
'''
# n이 3보다 큰 경우, 크기 n 패턴은 
# 가운데의 (n/3)*(n/3) 정사각형을 공백으로. 그리고 그것을 크기 n/3패턴으로 둘러싼 형태
n = int(input())
def divide(k):
    if k == 1: return ['*'] # 가장 작은 단위 1로 쪼갬
    stars = divide(k//3) # 길이 1이 나올 때까지 divide (*)
    return conquer(stars, k)  # 합친 결과를 return

def conquer(stars, k):
    rows = []
    for star in stars: # 위 칸
        rows.append(star*3) # ***
    for star in stars: # 중간 칸. 공백을 k//3만큼
        rows.append(star+' '*(k//3)+star)
    for star in stars: # 아래 칸
        rows.append(star*3)
    return rows
result = divide(n)
print('\n'.join(result))