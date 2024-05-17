# List of Unique Numbers
'''
길이 n 수열
수열에서 연속한 1개 이상의 수를 뽑았을 때
같은 수가 여러 번 등장하지 않는 경우의 수
1~n개씩 뽑음
'''
from sys import stdin
input = stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
answer = 0
left = 0
include = set()

for right in range(n):
    while numbers[right] in include:
        include.remove(numbers[left])
        left += 1
    include.add(numbers[right])
    answer += right - left + 1
    # left~right 범위에서,
    # [right] 수로 끝나는 수열 cnt
print(answer)