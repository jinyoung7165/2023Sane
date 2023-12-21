# n명 대회 참가. (1-n 번호)
# 1대1 방식/ a의 실력>b의 실력 -> a항상 이김
# 주어진 경기 결과 가지고 대략의 선수 순위 매기자
# 정확하게 순위를 매길 수 있는 선수의 수 return
# [a,b]: a가 b를 이겼다. 모든 경기 결과엔 모순 없음
# 5명, result=[[4,3], [4,2], [3,2], [1,2], [2,5]]
# 2번:[1,3,4]에 패배. [5]에게 승리 -> 4위
# 5번:[2]에 패배. -> 5위
# => 2,5번의 순위만 정확히 알 수 있음 -> 2return
# 가장 많이 진 애부터 탐색하며(리프 가능성) winners의 크기 증가시킴
# 최대한 "길게 탐색"했을 때, 같은 level에 자기만 있으면 됨
# 1~n 순회하며 해당 원소가 가진 것을 위로 전달, 아래로 전달하면 빠트릴 위험 없음
# 방향성 비순환 ingress -> 무엇을 전파할지 잘 생각하자!!
from collections import defaultdict
    
def solution(n:int, results:list):
    answer = 0
    winners = defaultdict(set) # 자기가 이긴 상대 저장(센:약한)
    losers = defaultdict(set) # 자기가 진 상대 저장(약한:센)
    
    for win, lose in results: # win으로 가기 위해선 lose를 거쳐야 함
        winners[win].add(lose)
        losers[lose].add(win)

    for i in range(1, n+1):
        for loser in winners[i]: # 나보다 약한 집합에 대한 강한 집합 크기 늘리기(나보다 큰 애들이 당연히 나보다 약한 애들보다 큼)
            losers[loser].update(losers[i])
        for winner in losers[i]: # 나보다 강한 집합에 대한 약한 집합 크기 늘리기
            winners[winner].update(winners[i])
    
    for i in range(1, n+1): # 정확한 순위 구할 수 있음
        if len(winners[i]) + len(losers[i]) == n-1:
            answer += 1
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))