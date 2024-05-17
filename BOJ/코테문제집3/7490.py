# 0 만들기
'''
1부터 N까지의 수를 오름차순으로 쓴 수열 123,,,N
+, -, 공백(숫자 이어붙임)을 숫자 사이에 삽입
수식의 값 계산하고, 그 결과가 0이 될 수 있는지 살피자
N이 주어졌을 때, 수식의 결과가 0이 되는 모든 수식 찾자
ascii 순서(공백,+,- 순)에 따라 결과가 0이 되는 모든 수식 출력
'''
from sys import stdin
input = stdin.readline
def convert(string):
    answer = 0
    ch = ''
    mid = 0
    # 연산자 만나면 현재까지의 수 이전 연산
    for st in string:
        if st == '+':
            if mid == 0: answer += int(ch)
            else: answer -= int(ch)
            mid = 0
            ch = ''
        elif st == '-':
            if mid == 0: answer += int(ch)
            else: answer -= int(ch)
            mid = 1
            ch = ''
        elif st != ' ':
            ch += st
            
    if mid == 0: answer += int(ch)
    else: answer -= int(ch)
    
    if not answer: return True
    return False

def dfs(idx, path):
    # 숫자 idx, 현재 수 문자열, sum, 경로 문자열, 현재 수 문자열이 어떤 연산인지
    if idx == num:
        if convert(path): print(path)
        return
    
    dfs(idx+1, path + ' ' + nums[idx])
    dfs(idx+1, path + '+' + nums[idx])
    dfs(idx+1, path + '-' + nums[idx])
       
tc = int(input())
for _ in range(tc):
    num = int(input())
    nums = list(map(str, range(1, num+1)))

    dfs(1, nums[0])
    if _ != tc-1: print()