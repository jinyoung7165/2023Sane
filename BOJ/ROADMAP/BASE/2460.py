# 지능형 기차 2
'''
내릴사람이 모두 내린 후 기차에 탐
32 -> -3(29) +13(42)
출발역에서 내린 사람 수와 종착역에서 탄 사람 수는 0
정원 10000명
기차에서 사람이 가장 많을 때의 사람 수

'''
from sys import stdin

input = stdin.readline
status = 0
answer = 0
for _ in range(10):
    a, b = map(int, input().split())
    status -= a - b
    answer = max(answer, status) 

print(answer)