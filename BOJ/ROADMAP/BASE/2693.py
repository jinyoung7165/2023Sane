# n번째 큰 수
'''
배열 a가 주어졌을 때, 3번째 큰 값 출력
크기 항상 10, 자연수
'''
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
    stack = sorted(map(int, input().split()), reverse=True)
    print(stack[2])