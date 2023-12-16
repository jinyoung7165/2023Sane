# longest substring without repeating characters
# longest substring부분문자열 without 반복 문자의 길이
'''
d가 이전에 나온 idx이후~현재 idx까지
acccca
acbcb -> acb
abcabd -> abc bca cab cabd start_idx바꿔서 누적
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = dict()
        answer = 0
        left = 0 # 시작 idx
        for right, a in enumerate(s):
            if a in dic and dic[a] >= left: # 아까 나온 애 -> 부분 substring 길이 계산
                left = dic[a] + 1 # 중복으로 나온 원소 다음부터 start로 둠
            dic[a] = right
            answer = max(answer, right-left+1)
        return answer