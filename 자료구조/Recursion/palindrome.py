from sys import stdin
from collections import deque
import re

def palindrome():
    str = deque()
    input = stdin.readline()

    for i in input:
        if i.isalnum():
            str.append(i.lower())

    while len(str) > 1: # 반복문으로 양 끝 계속 확인
        if str.pop() != str.popleft(): #리스트의 [-i-1]보다 시간복잡도 좋음
            return False

    return True
    
print(palindrome())

#더 빠른 정규식 필터 -> 슬라이싱
def palindrome():
    input = stdin.readline().lower()

    input = re.sub('[^a-z0-9]','',input) #불필요한 문자 제거
    
    return input == input[::-1] #문자열 거꾸로 뒤집은 거랑 비교


'''
재귀
'''
def recursive(pStr):
    if len(pStr) <= 1:
        return True

    if pStr[0] != pStr[-1]: # 양 끝 한 번 확인
        return False

    return recursive(pStr[1:len(pStr)-1]) # 내부의 양 끝 봐라