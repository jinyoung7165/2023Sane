# # 0-9 번호 문자열. 같은 번호 붙어있는 쌍 소거. 남은 번호를 반환
# # 소거 후 좌우 쌍이 또 같으면 소거 가능
# # 009900 -> 0000 -> 00 -> _
for _ in range(1, 11):
    size, nums = input().split()
    size = int(size)
    i = 0
    while 0<= i < len(nums)-1:
        if nums[i] == nums[i+1]: # 같은 걸 찾은 후 부터 <->
            j = 1 # 짝수 palindrome. i로부터 1씩 떨어진 window
            while 0<=i-j and i+j+1<len(nums):
                if nums[i-j] == nums[i+1+j]:
                    j += 1
                else: break
            nums = nums.replace(nums[i-j+1:i+j+1], "")
            i = i-j+1
            # j==1이면 i~i+1
            # j==2이면 i-1~i+2
        else:
            i += 1
    answer = nums
    print("#"+str(_), answer)
    
# 쌍 찾는 거 괄호 맞추기 문제랑 비슷    
def solution(password):
    stack = []
    for p in password:
        if stack and stack[-1] == p:
            stack.pop()
        else:
            stack.append(p)
    result = "".join(stack)