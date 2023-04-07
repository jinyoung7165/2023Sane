# 가장 최신 거랑 비교해야 함 LIFO
def solution(s):
    stack = []
    for c in s:
        if c == ')':
            if not stack:
                return False
            else:
                stack.pop()
        else:
            stack.append(1)
    return len(stack) == 0
    # if not stack: return True         
    # return False
'''
공간 효율을 높이자
'''
def solution(s):
    st = 0
    for c in s:
        if c == ')':
            st -= 1
        else:
            st += 1
        if st < 0:
            return False
    return st == 0