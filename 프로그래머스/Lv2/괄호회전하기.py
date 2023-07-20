# (),[],{}, ([]), {}([]) 올바른 괄호 문자열
# 괄호 문자열 s주어짐 -> 왼쪽으로 x칸만큼(0이상 s길이보단 작음) 
# 회전 시 올바른 괄호 문자열이 되게 하는 x 개수 return
# s의 길이는 1 이상 1,000 이하
'''
"[](){}"	3
"}]()[{"	2
"[)(]"	0
"}}}"	0
()}][{ 맞는 괄호 1
연 다음에 닫는 괄호 나오면 안됨
''' 
# 여는 괄호로 시작해 자기 짝으로 끝나야함 (...)[...]
# 제일 큰 여는 괄호의 위치들를 list에 저장
def solution(s):
    answer = 0
    stack = [] # 짝을 기다림
    op = {'(':')', '{':'}', '[':']'} # 여는 괄호
    if len(s) > 1:
        for _ in range(len(s)): # 0~len(s)만큼 회전
            flag = True
            stack = []
            for p in s:
                if p in op: # 여는 괄호면
                    stack.append(op[p])
                else: # 닫는 괄호
                    if stack and stack[-1] == p:
                        stack.pop()
                    else:
                        flag = False
                        break
            s = s[1:] + s[0]
            if not stack and flag: answer += 1
    return answer

print(solution("[](){}")) # 맞는 괄호 3
print(solution("}]()[{")) # 맞는 괄호 2
print(solution("[)(]")) # 틀린 괄호 0
print(solution("}}}")) # 틀린 괄호 0
print(solution("()}][{")) # 맞는 괄호 1
# ())(