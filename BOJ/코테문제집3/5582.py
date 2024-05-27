# 공통 부분 문자열
'''
부분 수열 아닌, 연속된 문자열이어야 함
중간에 끊어지면, 누적이 아닌 새로 시작 -> 이전 값 재활용x
dp[i][j]
(i, j)까지 봤을 때, lcs의 누적 최장 길이.
a[i]==b[j]일 때, [i][j]에 [i-1][j-1]만 영향을 미침(이전 행의 정보들만 기억하면 됨)

i*j 크기로 tb 만들면 메모리 초과 -> 2*len(b) dp를 만들거나, 1차원 배열 2개 만들어 현재->이전 배열에 덮어씌우기
'''
from sys import stdin
input = stdin.readline
a = input().rstrip()
b = input().rstrip()

sa, sb = len(a), len(b)

def lcs():
    answer = 0
    dp = [0]*(sb+1) # 이전행의 결과
    for i in range(1, sa+1):
        temp = [0]*(sb+1) # 현재 행의 결과
        for j in range(1, sb+1):
            if a[i-1] == b[j-1]:
                temp[j] = dp[j-1] + 1
                if temp[j] > answer: answer = temp[j]
        dp[:] = temp # 덮어 씌움
    print(answer)
lcs()
'''

def lcs():
    answer = 0
    for i in range(sa):
        for j in range(sb):
            if a[i] == b[j]: 
                dp[(i+1)%2][j+1] = dp[i%2][j] + 1
                if dp[(i+1)%2][j+1] > answer: 
                    answer = dp[(i+1)%2][j+1]
            else: # 다를 때는, 다음 행에서의 사용을 위해 0으로 초기화 필요
                dp[(i+1)%2][j+1] = 0
    return answer
    
'''