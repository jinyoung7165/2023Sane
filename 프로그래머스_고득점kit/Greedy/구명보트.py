# "최대 2명씩". 무게 제한
# [70,50,80,50], limit 100 -> 2+4(100) 가능
# 최대한 적은 move로 모두 구출 -> 3
# [70,80,50], 100 -> 3(각각 따로)
# 가장 큰 + 가장 작은 사람
# [30,30,40,60], 90 -> (30+60),(30+40)
def solution(people, limit):
    answer = 0
    people.sort()
    s = 0
    size = len(people)
    visited = set()

    for l in range(size): # 0~len-1
        s = people[l]
        visited.add(l)
        for r in range(size-1, l, -1): # len-1~l+1
            if r not in visited:
                tmp = s + people[r]
                if tmp <= limit: # 싣기
                    s += people[r]
                    visited.add(r)
                    break
        if s == people[l]: # l 자신
            answer += 1
    return answer

# 최대 2명 명심하자..
from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people, reverse = True))
    
    while len(people) > 1:
        if people[0] + people[-1] <= limit: # 최댓값과 최솟값 묶어서 보트태움
            answer += 1
            people.pop()    #최소 빼내고
            people.popleft()    #최대 빼내고
        else:
            answer += 1 # 최댓값. 1명만 태우기
            people.popleft()
            
    if people:  #people에 1명 남아있는 경우 처리
        answer += 1
                
    return answer

# 투 포인터
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        # 현재 짝 태울 수 있을 때-> answer증가(짝의 수), a+1, b-1
        # 현재 짝 못 태우면 -> b-1해서 작은 짝의 합 구하려 함. b 오른쪽에 남은 최댓값들은? 혼자씩 타야 함
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1 # 현재
    return len(people) - answer # 전체 사람 수 - 짝짓기 수