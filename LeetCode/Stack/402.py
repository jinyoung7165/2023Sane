# #Remove k digits
# k digit 삭제
# k개 수 제거했을 때, 가장 작은 정수 (중복돤 수 있을 때 하나만 제거)
# 1432219
# 4, 3, 2 제거 시
# 1219 제일 작음
# 현재 애보다 이전 애가 크면 이전 애 제거
# 현재 애가 0이면, stack에서 k개 제거
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        if k >= len(num): return '0'
        for i in list(num):
            while k > 0 and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)

        while k > 0 and stack:
            stack.pop()
            k -= 1
        
        while stack and stack[0] == '0': # 앞이 0으로 시작 -> 버려. str(int(''.join)) 보다 훨씬 빠름
            stack.pop(0)
        
        result = ''.join(stack) if stack else '0'
        return result