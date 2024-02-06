#  좋은 수열
'''
1,2,3으로만 이뤄진 수열 만들어라.
인접한 두 부분 수열(연속 부분 수열)이 동일하면 나쁜 수열
그렇지 않음 좋은 수열
길이 n(1~80)인 좋은 수열 list -> int화 -> 그 중 가장 작은 수 return
ex) 나쁜 수열
33
3(2121)323
(123123)213

ex) 좋은 수열
1213121 if, n==7일 때, 가장 작은 좋은 수열
if, n=8일 때, 12131213 불가능 -> n=7 재활용 불가. 백트래킹해서 더 큰 수 대상으로 찾아야함
최소 중복순열 만들면서, 반복되는 구간있는지 계속 확인
크기-1 누적 + 1개만 맨 뒤에 추가되므로,
마지막 원소를 포함하는 수열과, 그것의 인접 수열만 check하면 됨 (for문 하나임!!)
'''
from sys import stdin

input = stdin.readline
n = int(input()) # 1~80
result = ''
# 중복되는 인접 수열 있는지 check
def check(string, size):
    for gap in range(1, size//2+1): # 각 인접수열 사이즈
        if string[-gap:] == string[-2*gap:-gap]: return False
    return True 

# size n인 중복 순열 만들기
def product(string, size):
    if size == n:
        print(string)
        return True

    for num in '123':
        if check(string + num, size+1) and product(string+num, size+1): return True
    return False

product('1', 1)