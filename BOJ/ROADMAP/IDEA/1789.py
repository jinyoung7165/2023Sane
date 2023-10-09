'''
수들의 합
서로 다른 n개 자연수 합 S
S 알 때, 자연수 n의 최댓값?
'''
s = int(input())
total = 0
i = 1
while total <= s:
    total += i
    i += 1

print(i - 2)