# Remove Duplicate Letters
# s -> remove 중복 알파벳. 가능한 문자열 중 정렬 시 가장 첫번째 경우
# (b)ca(b) => bca
# (bc)a(bc) => abc
# abacb
# a  cb
# ab c
# 주어진 문자 순회하며
# 현재애가 이전에 처리된 애면 다시 append x
# 현재 애가 여러번 나오는 앞의 수보다 앞설 때, 앞에 거를 지우고 나중에 붙이면 됨
from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = Counter(s)
        stack = []
        for char in s:
            cnt[char] -= 1
            if char in stack: continue
            while stack and char < stack[-1] and cnt[stack[-1]] > 0:
                stack.pop()
            stack.append(char)
        return ''.join(stack)