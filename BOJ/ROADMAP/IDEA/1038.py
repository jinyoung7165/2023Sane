# 감소하는 수
'''
N번째 감소하는 수.
0=0번째 감소하는 수
1=1번째
1~9:9
10: 1
21 20 : 2
32 31 30 : 3
...
100번대 없음
210 : 1
321 310 : 2
432 431 430 421 410 : 5
543 542 541 540 532 531 530 521 520 510 : 10
654 653 652 651 650 643 642 641 640 632 
'''
from itertools import combinations

N = int(input())

num = -1

nums = [*range(10)]

tmp = []
for i in range(1, 10): # len
    for comb in combinations(nums, i):
        tmp.append(int(''.join(map(str, comb))[::-1]))
print(sorted(tmp)[N] if len(tmp) >= N else -1)