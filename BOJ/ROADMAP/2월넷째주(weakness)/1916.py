'''
모든 단어 anta...tica 형식 -> a, n, t, i, c는 기본으로 알아야 함
k개 글자 가르칠 것. k개의 글자로만 이뤄진 단어 읽기 가능
읽을 수 있는 단어 개수 최대가 되도록.
단어의 개수 n(1~50), 각 단어 길이 8~15. 중복 없게 주어짐
각 알파벳 포함한 단어를 26자리 bit로 바꿈.
k - 5개만큼 새로 배울 수 있음
각 알파벳 기준으로 bruteforce하는 게 최선
그 비트에 내가 포함돼 있는지 -> 나랑 걔랑 &= 했는데 0이 아니면 됨
learn 11111 need 01111 공통 == need이면 배울 수 있음
'''
from sys import stdin
input = stdin.readline
n, k = map(int, input().split()) # 전체 단어의 개수, 가르칠 알파벳 수
words = list(input().strip() for _ in range(n))
alpha = {chr(i):i-97 for i in range(ord('a'), ord('z')+1)}
alp_bit = list(1<<alpha[key] for key in alpha if key not in 'antic') # 각 알파벳별 비트

def convert(string):
    bit = 0
    for st in string:
        bit |= 1 << alpha[st]
    return bit

answer = 0
basic = convert('antic') # 기본으로 알아야 함

def dfs(idx, k, learn): # 배울 알파벳의 idx, k개 배울 수 있음, 배운 알파벳 집합
    global answer
    if k == 0 or idx == 21: # 남은 수보다 배워야 할 단어 수가 많으면 그만
        result = 0 # 배울 수 있는 단어 수
        for need in needs:
            if need & learn == need: result += 1
        if result > answer: answer = result
        return
    # 필요한 알파벳일 때만 배움
    if alp_bit[idx] & total != 0: dfs(idx+1, k-1, learn|alp_bit[idx])   
    dfs(idx+1, k, learn) # 안배우기 선택
if k < 5: print(0)
elif k > 25: print(n)
else:
    total = 0
    needs = []
    for word in words:
        cvt = convert(word) ^ basic
        needs.append(cvt)
        total |= cvt # 전체 알파벳

    # 공통으로 배울 알파벳 배우고 시작
    dfs(0, k-5, 0)
    print(answer)