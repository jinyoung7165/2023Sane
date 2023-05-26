# 스택
# push x : 정수 x를 스택에 넣기
# pop : top 빼고, 츨력. 스택 빈 경우 -1 출력
# size : 개수 출력
# empty: 비어있으면 1, 아님 0
# top: 가장 위 출력. 스택 빈 경우 -1 출력
from sys import stdin
input = stdin.readline

class Stack:
    def __init__(self) -> None:
        self.val = []
    def push(self, x):
        self.val.append(x)
    def size(self):
        print(len(self.val))
    def empty(self):
        if not self.val:
            return 1
        return 0
    def pop(self):
        if self.empty():
            print("-1")
        else:
            print(self.val.pop())
    def top(self):
        if self.empty():
            print("-1")
        else:
            print(self.val[-1])
stack = Stack()
n = int(input())
for _ in range(n):
    line = input().split()
    ins = line[0]
    if ins == "push":
        stack.push(line[1])
    elif ins == "pop":
        stack.pop()
    elif ins == "top":
        stack.top()
    elif ins == "empty":
        print(stack.empty())
    elif ins == "size":
        stack.size()