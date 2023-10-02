# 괄호의 값
'''
(()[[]])나 (())[][] 는 올바른 괄호열
([)] 나 (()()[] 은 모두 올바른 괄호열이 아니다
‘()’ 인 괄호열의 값은 2이다.
‘[]’ 인 괄호열의 값은 3이다.
‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
입력이 올바르지 못한 괄호열이면 반드시 0을 출력해야 한다.
열린 괄호 중첩될 때마다 곱하기 부분 누적값 증가
쌓인 열린 괄호 값 하나씩 없어질 때마다 부분 누적값에 곱할 값 줄어듦(나누기)
(('()'))'[]' 독립적인 괄호쌍 하나 찾을 때마다 answer에 그때까지의 값 누적
'''
parent = list(input())

pair = {'(':')', '[':']'}
val = {'(':2, '[':3}

r_val = {')':2, ']':3}

stack = []
answer = 0
tmp = 1

for i in range(len(parent)):
    cur = parent[i]
    if cur in pair: # 여는 괄호
        stack.append(pair[cur]) # 기다릴 애 넣음
        tmp *= val[cur]
    else:
        if stack and stack[-1] == cur:
            stack.pop() # 기다리던 짝 나옴
            if parent[i-1] in pair and pair[parent[i-1]] == cur:
                # 직전 원소가 내 짝일 때 -> 독립적 부분 괄호 값 누적
                answer += tmp
            tmp //= r_val[cur] # 중첩 괄호 끝났으니 누적곱도 해제
        else:
            answer = 0
            break
print(0 if stack else answer)
        
    