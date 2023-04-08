# 중요도 높은 문서를 먼저 인쇄
# 대기목록 가장 앞 문서를 꺼냄
# 나머지 목록에서 그것보다 중요도 높은 문서 존재 시 그것을 대기목록 맨 마지막에 넣음
# 그렇지 않음 그것 인쇄
# FIFO -> deque. 근데 순서 정렬 필요해서 PQ?
# heapq는 형제 노드간 반정렬 상태
import heapq
from collections import deque
def solution(priorities:list, location:int): # location:내가 궁금한 문서의 현재 위치
    answer = 0
    que = deque([(idx, p) for idx, p in enumerate(priorities)])
    while True:
        cur = que.popleft()
        if any(cur[1] < el[1] for el in que): #cur[1]보다 큰 수 존재 시
            que.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

def solution_pq(priorities:list, location:int):
    que = []
    answer = 0
    for p in priorities:
        heapq.heappush(que, (-p)) # p 오름차순
    while que:
        for i in range(len(priorities)): # 가장 큰 p -> 다음에 나타나는 인덱스에 대해 살핌-> 자연스러운 재배치
            if priorities[i] == -que[0]: # 현재 가장 큰 p를 priorities에서의 위치 찾기
                answer += 1
                if i == location: # 원하던 위치까지 오면
                    return answer
                heapq.heappop(que)