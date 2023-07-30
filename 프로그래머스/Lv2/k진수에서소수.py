# 양수 n -> k진수 변환(K: 3-9)
'''
0P0 처럼 소수 양쪽에 0이 있는 경우
P0 처럼 소수 오른쪽에만 0 존재. 왼쪽에는 나띵
0P
P
'''
# 단, P는 각 자릿수에 0을 포함하지 않는 소수(10진법상)
# 예를 들어, 101은 P가 될 수 없음
'''
437674 -> 3진수 => (211)0(2)01010(11)
211: p0, 2:0p0, 11:0p
3개
'''
'''
110011 -> 10진수 => (11)00(11)
2개
'''
def is_prime(num:int):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def convert(num:int, base:int):
    tmp = ''
    while num:
        tmp = str(num % base) + tmp
        num //= base
    return tmp
    
def solution(n, k):
    answer = 0
    nums = convert(n, k).split('0')
    for num in nums: # 빈 문자열 나올 수 있음 -> if num 처리
        if num and is_prime(int(num)):
            answer += 1
    return answer

print(solution(1, 3))
print(solution(3, 3))
print(solution(437674, 3))
print(solution(110011, 10))