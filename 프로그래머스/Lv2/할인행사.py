# 일정 금액 지불 시 10일 회원 자격 부여
# 회원->매일 한 가지 제품 할인 행사 -> 할인제품은 하루 하나 구매 가능
# 원하는 모든 제품 할인 날짜 10일 연속 일치 시 회원가입하려 함
# 바나나3, 사과2, 쌀2, 돼지2, 냄비1
# 마트의 15일간 할인 제품:
# 치킨,사과,사과,바나나,쌀,사과,돼지,바나나,돼지,쌀,냄비,바나나,사과,바나나
# 셋째날, 넷째날, 다섯째날 가입 시 모든 제품 할인 받을 수 있음 -> 3리턴
# 가능한 날 없으면 0리턴
# 원하는 상품 종류, 종류별 개수, 할인 일정 주어짐
# 딱 10일치 볼 것. 10개의 물건 사야 함 10일간 물건 count 시 wants dict와 같아야 함
from collections import Counter
def solution(want, number, discount):
    answer = 0
    wants = dict()
    for w, n in zip(want, number):
        wants[w] = n
        
    for i in range(len(discount)-9): # 10개씩 묶어 볼 것
        if Counter(discount[i:i+10]) == wants:
            answer += 1
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],
    ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))

print(solution(["apple"], [10],["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))


'''
시간초과
from collections import defaultdict, deque
def solution(want, number, discount):
    answer = 0
    wants, discounts = dict(), defaultdict(list)
    for w, n in zip(want, number):
        wants[w] = n
    for i, d in enumerate(discount):
        discounts[d].append(i)
        
    days = None # (start, end) 배열
    # 수량 많이 필요한 것부터 확인
    for key, cnt in sorted(wants.items(), key=lambda x:-x[1]):
        if key not in discounts or len(discounts[key]) < cnt: break
        _discounts = discounts[key]
        tmp = []
        for idx in range(len(_discounts)-cnt+1):
            _start, _end = _discounts[idx], _discounts[idx+cnt-1]
            if _end - _start < 10: # 가능한 범위
                tmp.append((_start, _end))
        if not tmp: break
        elif not days: days = deque(tmp) # 첫 종류의 상품 확인했을 때
        else:
            for _ in range(len(days)): # 이전 start, end 집합
                l_s, l_e = days.popleft()
                for t_s, t_e in tmp:
                    _start, _end = min(l_s, t_s), max(l_e, t_e)
                    if _end - _start < 10:
                        days.append((_start, _end))
            if not days: break
    answer = len(days) if days else 0
    return answer
    '''