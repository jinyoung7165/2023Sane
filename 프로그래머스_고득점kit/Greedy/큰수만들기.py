# 어떤 숫자에서 k개 수 제거 시 만들 수 있는 가장 큰 수
# 1924 ->2개 제거. [19,12,14,92,94,24] -> 94
# 1231234 ->3개 제거. 3234
# 4177252841 -> 4개 제거. 775841
# k 엄청 커서 bruteforce 안됨
# 처음부터 순회하며 자기보다 작거나 같은 원소 오면 계속 쌓임
# 큰 거 옴 -> stack 뒤에서부터 pop 하고 현재 값 넣음
# # 한 방향으로 이동. 앞에 선택한 원소보다 크고, 
# 뒤에 뽑을 수 있는 원소 남아있어야 함
def solution(number, k):
    stack = []
    for n in number: 
        # 이전 선택이 현재보다 작고, 제거 가능한 기회 남아있으면 제거
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)
    if k > 0: 
        # 제거되지 못한 뒷부분(처음부터 내림차순이라 작은 애들이 맨 뒤로 감)
        stack = stack[:-k]
    return ''.join(stack)
        

# print(solution("1924", 2)) # 94
print(solution("1231234", 3)) # 3234