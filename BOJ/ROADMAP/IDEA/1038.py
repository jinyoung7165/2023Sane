# 감소하는 수
'''
0~양수 x의 가장 큰 자리부터 작은 자릿수까지 감소한다면, 감소하는 수
321, 950 감소하는 수
322, 958 x
n번째 감소하는 수를 출력하라. 없으면 -1
감소하는 수 마지막: 9876543210
'''
from itertools import combinations
n = int(input())
answer = ''
M = 9876543210
for size in range(1, 11):
    tmp = 0
    li = []
    for num in combinations(range(10), size):
        tmp += 1
        li.append(''.join(map(str, num))[::-1])
    if n < tmp:
        answer = sorted(li)[n]
        break
    else: n -= tmp
print(answer if answer else -1)