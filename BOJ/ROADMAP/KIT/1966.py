# 프린터 큐
'''
중요도 높은 게 뒤에 나오면, 현재값 다시 맨 뒤로 보냄
'''
from sys import stdin

input = stdin.readline
tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split()) # 전체 길이, 궁금한 idx
    priority = list(map(int, input().split()))
    sor = sorted(priority)
    answer = 1
    idx = 0
    while sor:
        pri = sor.pop()
        while priority[idx] != pri:
            idx = (idx+1) % n
        if idx == m: break
        answer += 1
        idx = (idx+1) % n
    print(answer)
        
            