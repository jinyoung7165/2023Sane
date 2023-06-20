# IOIOI
# N+1개의 I와 N개의 O로 이뤄짐. 교대로 나오는 문자열
# P1 IOI
# P2 IOI OI
# P3 IOI OI OI
# PN IO...OI(O가 N개)
# I와 O로 이뤄진 문자열 S와 정수 N주어짐
# S안에 PN 몇 군데 포함됐는지 구하라
# n=1이고, S: OOIOIOIOIIOII
# P1: IOI를 S에서 찾아라 -> 4번
# I로 시작하고, OI반복되는 홀수 길이
'''
1 ≤ N ≤ 1,000,000
2N+1 ≤ M ≤ 1,000,000
'''
n = int(input())
m = int(input()) # s의 길이
s = input()

i, left = 0, n # ioi시작 idx, Pn이 되기 위해 남은 oi 수
answer = 0
while i < m:
    if s[i:i+3] == 'IOI': # 시작
        left -= 1 # OI 하나 감소
        if left == 0: # OI 총 N개 나왔다. PN 생성
            answer += 1
            left += 1 # 다음부터 다시 PN 만들기 위해 남은 oi 수
        i += 2 # IO'I'로 이동해 IOI 검색 연결
    else: # IOI 끊어짐
        i += 1
        left = n
        
print(answer)