# 한자리 숫자 조각들 붙여 몇 개의 소수 만들 수 있나
# 17 -> 3 [7, 17, 71]
# 011 -> 2 [11, 101] 11==011 
# int(str) 적용 시 자동 맨 앞 0 제거 -> set으로 중복 제거
from itertools import permutations
def solution(numbers: str):
    numarr = list(numbers)
    result = set()
    for i in range(1, len(numarr)+1): # 총 자릿수
        for j in list(permutations(numarr, i)): # [(1,), (7,)]
            new = int(''.join(j))

            if prime(new):
                result.add(new)
                
    return len(result)

def prime(number: int): # 제곱근보다 작은 수까지만 나눠보면 됨
    if number < 2:
        return False
    for k in range(2, int(number**0.5) + 1):
        if number % k == 0:
            return False
    return True
print(solution("011"))

'''
재귀로 combination 생성
'''
primeSet = set()

# 빈 문자열에 str2의 원소 하나씩 갖다 붙임
def makeCombinations(str1, str2):
    if str1 != "":
        if prime(int(str1)):
            primeSet.add(int(str1))

    for i in range(len(str2)):
        makeCombinations(str1 + str2[i], str2[:i] + str2[i + 1:])


def solution(numbers):
    makeCombinations("", numbers)
    answer = len(primeSet)
    return answer
