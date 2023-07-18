# 소문자 문자열 -> 같은 alpha 2개 연속 짝 제거 -> 앞뒤로 이어붙임
# 모두 제거 시(길이 0) 짝지어 제거 종료
# 모두 제거 가능 1, 아닐 시 0
# baab
# cbaabc adda (10 len -> set 크기 5이하여야 함)
def solution(s):
    size = len(s)
    s = list(s)
    if size % 2 != 0: return 0
    stack = [] # 괄호 닫기마냥 짝 기다림
    for i in s:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
        
    if not stack: return 1 # 모두 제거됨
    return 0