# A,E,I,O,U만을 사용한 길이 5 이하의 모든 단어 수록
# A, AA,.... UUUUU
# word가 주어졌을 때 사전에서 몇 번째 단어인지 return
# AAAAE = 6번째 단어
# AAAE = 10 (A,..., AAAAO, AAAAU, AAAE) 사전 순
# I = 1563
# EIO = 1189
# 5번째 자리는 문자가 바뀔 때마다 1 증가
# 4번째 자리는 6 증가
# 3번째 자리는 31 증가
'''
x 가 0이 아닐 때 : f(x) = f(x - 1) + 5^x
f(0) = 1
f(1) = 1 + 5^1 = 6
f(2) = 6 + 5^2 = 31
f(3) = 31 + 5^3 = 156
f(4) = 156 + 5^4 = 781
'''
from itertools import product
# 순열
def solution(word):
    words = []
    for i in range(1, 6):
        for c in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words.append(''.join(c))

    words.sort()
    return words.index(word) + 1


'''등비수열의 합'''
def solution(word):
    answer = 0
    for i, n in enumerate(word):
        answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
    return answer