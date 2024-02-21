# Minimun Window Substring
from collections import Counter
# s에 t의 원소 모두 포함된 가장 짧은 구간 return
# 최솟값/최댓값 찾는 게 아니라, 정확한 substring 찾는 거라 bs 불가
# missing 원소가 0일 때, right-left로 substring 길이 구할 수 있고
# 특정 원소 넘치게 찾았으면, 걔 이후, 넘치지 않게끔 찾은 원소를 시작점으로 둘 수 있음.
# 다음 윈도우와 현재 윈도우 절대 겹치지 않아야 함 -> left +1 한번 더 해줘야 함
def minWindow(s: str, t: str) -> str:
    if len(t) == 1:
        if t in s: return t
        return ''
    needs = Counter(t)
    missing = len(t)
    left, right = 0, 0
    result = ''
    while right < len(s):
        missing -= needs[s[right]] > 0 # 부족한 원소를 찾았을 때 -1. 혹은 -0이라 변화 없음
        needs[s[right]] -= 1 # 과하게 찾거나, 애초에 t에 없는 원소면 음수(초깃값0)
        if missing == 0: # 필요한만큼만 찾았을 때
            # left를 최대한 right 쪽으로 당겨야 함
            while left < right and needs[s[left]] < 0: # 과하게 찾은 원소는 pass하며 window 크기 줄일 것
                needs[s[left]] += 1
                left += 1
            # 과하지 않게, left가 필요한 substring의 원소 시작점에 가있음
            # size 작아지면 result 갱신
            if not result or len(result) > right-left+1:
                result = s[left:right+1]
           # 다음 순회에서는 left+1부터 볼 것
            missing += 1
            needs[s[left]] += 1
            left += 1

        right += 1
    return result