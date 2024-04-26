# 문자열 폭발
'''
폭발 부분은 같은 문자 중복 없음
폭발 부분만 사라지고, 나머지 문자열은 다시 합쳐짐
1) 폭발 부분 존재할 때, 모든 폭발 부분 사라짐
2) 새로 생긴 문자열에 폭발 부분 포함 가능
3) 폭발 부분 없을 때까지 반복
모든 과정 끝나고, 빈 문자열일 때, FRULA 출력
stack[start:end] start -> end 방향 순회 (start 생략 시 0 들어감. end 생략 시 -1 들어감)
stack[start:end:-1] end <- start 방향 순회 (start 생략 시 -1 들어감. end 생략 시 0 들어감)
'''
from sys import stdin

input = stdin.readline

origin = input().strip()
explode = list(input().strip())
L = len(origin)
ep_size = len(explode)
stack = [] # 쭉 넣다가 bomb 발견되면 그만큼 제거할 것
# stack[-ep_size:]: 끝자리부터 ep_size 원소~ 끝까지. 정방향 출력
for i in range(L):
    stack.append(origin[i])
    if stack[-ep_size:] == explode:
        for j in range(ep_size):
            stack.pop()
    
print(''.join(stack) if stack else 'FRULA')