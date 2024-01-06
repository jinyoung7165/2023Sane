# 모든 지수를 k 이상으로 만들기 위해 가장 낮은 두 개를 섞는 것 반복
# 섞은 지수 = 가장 낮은 지수+두 번째로 낮은 지수*2
# 최소 횟수
# [1, 2, 3, 9, 10, 12], k=7
# -> [5, 3, 9, 10, 12], [13, 9, 10, 12] => 2번
import heapq
def solution(scoville: list, k: int):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        if len(scoville) == 1:
            if scoville[0] < k: answer = -1
            break
        if scoville[0] >= k: break
        answer += 1
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville)*2)
    return answer