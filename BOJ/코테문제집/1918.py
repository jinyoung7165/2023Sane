# 후위 표기법
# 연산자가 피연산자 뒤에 위치
# 괄호 필요 없음
# a+b*c -> (a+(b*c)) -> (a+bc*) -> abc*+
# A+B*C-D/E -> ABC*+DE/-
# 이전 연산자보다 현재 연산자 순위가 높으면 일단 쌓기
# 현재 연산자 순위가 낮거나 같으면 쌓인 nums popleft,이전 연산자 pop
# 연산자 우선순위에 따라 괄호로 묶음
# 괄호 안 연산자를 괄호 오른쪽으로 옮김
# 괄호 > */ > +-
origin = input()
priority = {'(':0, '*': 2, '/':2, '+':1, '-':1}
stack = []
result = ''
for i in range(len(origin)):
    el = origin[i]
    if el.isalpha():
        result += el
    else:
        if el == ')':
            while stack and stack[-1] != '(': # 여는 괄호 나올 때까지
                result += stack.pop()
            stack.pop() # 여는 괄호 pop
        elif el == '(': # 여는 괄호는 계속 stack에 append
            stack.append('(')
        else: # 지금 게 더 낮거나 같은 경우는 pop해 result에 추가. 혹은 그냥 append
            while stack and priority[stack[-1]] >= priority[el]:
                result += stack.pop() # ( 여는 괄호의 순위가 낮아야 여기서 pop당하지 않고 )일 때 pop당함
            stack.append(el)
while stack:
    result += stack.pop()
print(result)