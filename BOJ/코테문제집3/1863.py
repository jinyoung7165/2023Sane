# 스카이라인 쉬움
'''
윤곽을 보고 건물이 최소 몇 개인지
고도가 바뀌는 지점의 x, y 주어짐
(1~10**6, 0~5*10**5)
높이y 바뀌지 않는 동안(x) 해당 높이의 건물 존재
x 1부터 주어짐
stack보다 내가 크면, 일단 넣기
같으면, 넣지 않음
stack보다 내가 작으면, stack애들 분리 가능
'''
from sys import stdin
input = stdin.readline
n = int(input())
stack = []
answer = 0
for i in range(n):
    x, y = map(int, input().split())
    while stack and stack[-1] > y:
        stack.pop()
        answer += 1
    if y and (not stack or stack[-1] < y):
        stack.append(y) # 높이 1이상 건물만 넣음
print(answer+len(stack)) # 오름차순 남아있을 수 있음