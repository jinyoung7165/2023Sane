# 모든 지수를 k 이상으로 만들기 위해 가장 낮은 두 개를 섞는 것 반복
# 섞은 지수 = 가장 낮은 지수+두 번째로 낮은 지수*2
# 최소 횟수
# [1, 2, 3, 9, 10, 12], k=7
# -> [5, 3, 9, 10, 12], [13, 9, 10, 12] => 2번
import heapq
from collections import deque
def solution(scoville: list, K: int):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        el1 = heapq.heappop(scoville)
        if el1 < K:
            if scoville:
                el2 = heapq.heappop(scoville)
                heapq.heappush(scoville, el1 + el2*2)
                answer += 1
            else: return -1
        else: break
    return answer