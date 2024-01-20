from collections import defaultdict
# dp[i-1]에 나온 결과에 사칙연산. 괄호(연산순서 바뀜) 사용
# -결과의 경우 -붙여서 한번더 기록(순서 55-5, 5-55 반전)
'''
(1) (5) ->
(2) 5 5, (55) ->
(3) 5 5 5, 55 5, (555) -> dp[1]dp[2]의 결과들 사칙연산. -만 부호바꿔서 추가하면 됨
(4) (5 5 5 5, 55 5 5, 555 5), (55 55), (5555) -> dp[1]dp[3], dp[2]dp[2]
(5) 5 5 5 5 5, 55 5 5 5, 555 5 5, 55 55 5, 5555 5, (555 55), (55555)
'''
def solution(N, number):
    dp = defaultdict(set) # dp[i]: i번 썼을 때 나온 결과들
    for i in range(1, 9): # 1~8회까지 N 사용 가능
        dp[i].add(int(str(N)*i)) # 이어붙이는 게 항상 최소
        for j in range(1, i): # N (1~i-1개) (i-j개) 조합  +-*/ 연산 (총 i개 사용)
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    if num1==0 or num2==0: continue
                    dp[i].add(num1-num2)
                    if i < 2*j: continue # j > i-j이면 중복 시작. -만 부호 바꿔서 넣어주면 됨
                    dp[i].add(num1+num2)
                    dp[i].add(num1*num2)
                    if num2>=num1: dp[i].add(num2//num1)
                    else: dp[i].add(num1//num2)
        if number in dp[i]: return i
    return -1