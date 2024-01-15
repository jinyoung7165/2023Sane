# Longest Repeating Character Replacement
from collections import Counter
'''
최대 k번 switch해서 중복 문자로만 이뤄진 문자열의 최대 길이 return
앞에서부터 지금까지 가장 빈번한 문자로 switch해야 함
left~right 사이 가장 많은 문자 외의 문자가 k개 초과: left~right 모두 같은 문자로 switch 불가
k개 이하면, switch 가능
left~right window 사이즈 줄어들지 않고, right 늘어남에 따라 유지 또는 증가 -> 최대 크기 기억
'''
def characterReplacement(s: str, k: int) -> int:
    answer = 1
    left, right = 0, 0
    counter = Counter()
    for right, c in enumerate(s):
        counter[c] += 1
        M = counter.most_common(1)[0][1] # 가장 많이 나온 원소의 수
        if right - left + 1 - M > k: # 그 이외의 문자가 k개 이상이면, switch해도 연속 중복 불가
            counter[s[left]] -= 1
            left += 1
    return right - left + 1