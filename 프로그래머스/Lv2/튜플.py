# n-tuple. n개의 요소를 가진 튜플 n튜플(a1, a2, ...an)
# 중복 원소 없음
# 순서 다르면 다른 튜플
# 튜플 원소 개수 유한
# 중복 원소가 없는 튜플 주어질 때, {{{a1},a2},...an}}으로 표현 가능
# (2,1,3,4) -> {2},{2,1},{2,1,3},{2,1,3,4} 
# {내에선 순서 무관}: {2,1,3}=={1,2,3}
# {2},{2,1},{2,1,3},{2,1,3,4} 주어지면 n-tuple로 바꿔라 [2,1,3,4]
def solution(s):
    answer = []
    s = s[1:-1]
    size = len(s)
    i = 0
    arr = []
    num_set = set()
    while i < size-2:
        for j in range(i+2, size):
            if s[j] == '}':
                arr.append(s[i+1:j].split(','))
                i = j + 2
                break
    arr.sort(key=len)
    for nums in arr:
        for num in nums:
            if num not in num_set:
                num_set.add(num)
                answer.append(int(num))
                break
    return answer

# print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")) # [2,1,3,1]
# print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")) # [2,1,3,1]
print(solution("{{20,111},{111}}"))
# print(solution("{{123}}")) # [1,2,3]
# print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")) # [3,2,4,1]

# 더 간단한 문자열 처리 방법
def solution2(s):
    answer = []
    s = s.lstrip('{').rstrip('}').split('},{')
    arr = []
    for el in s:
        arr.append(el.split(','))
    arr.sort(key=len)
    
    num_set = set()
    for nums in arr:
        for num in nums:
            if num not in num_set:
                num_set.add(num)
                answer.append(int(num))
                break
    return answer


print(solution2("{{20,111},{111}}"))

# 가장 빠른 문자열처리 방법 + 나온 원소의 빈도 큰 것부터 삽입
import re
from collections import Counter
def solution(s):

    s = Counter(re.findall('\d+', s)) # 숫자만 찾아서 counter 적용 \d+: 연속된 정수
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)])) # 빈도 내림차순 정렬