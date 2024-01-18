# 한번에 "최대 2명". 무게 제한
# [70, 50, 80, 50] limit 100일 때 (50+50) 같이 탈 수 있고, 나머지 2명은 따로
# 최대한 적은 수의 보트 사용해 모두를 구출하라
# 최대한 꽉 채워 사용
# 최대 2명 제한이 아니면, 5 20 35 60 80 -> (5,35,60), (20,80)
# 최대 2명 제한 -> min + max. 안되면 max만 태워보냄
from collections import deque
def solution(people, limit):
    size = len(people)
    people.sort()
    que = deque(people)
    answer = size # 쌍의 수
    while que:
        M = que.pop()
        if que and M + que[0] <= limit: # 쌍 만들 수 있을 때
            que.popleft()
            answer -= 1
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