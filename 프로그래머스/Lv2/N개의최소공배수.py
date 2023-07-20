# 수의 최소공배수(LCM): 공통 배수 중 최소
# N개 숫자를 담은 배열의 LCM 구하라
# 168 -> 84 -> 42 -> 21 -> 7, 3 * 2^3
def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b): # 최소공배수: a*b/최대공약수
    return a * b / gcd(a, b)

def solution(arr):
    arr.sort(reverse=True)
    answer = 1 # 최대 공배수
    for i in range(len(arr)):
        answer = lcm(answer, arr[i])
    return answer