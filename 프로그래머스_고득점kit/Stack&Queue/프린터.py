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
                
'''
대기 큐에서 프로세스 꺼냄
대기 큐 중 우선순위 더 높은 거 있으면, 꺼낸 거 다시 큐에 넣음
[A,B,C,D] # 실행큐: 그냥 순서대로 온 큐
[2,1,3,2] # 대기큐: 우선순위 큐
실행큐에서 꺼냈는데 대기큐의 3이 더 큼 -> 실행큐에 넣음 [(3c,2d),(2a,1b)]
[c,d,a,b] 순 실행
location idx(0~)의 프로세스가 몇 번째(1~)에 실행되는지 return해라
실행 큐, 대기 큐 -> 순회하며
대기 큐의 우선 순위(최대)랑 같을 때, 실행큐에서 제거. 
그렇지 않을 때 뒤에 다시 붙여가며 실행큐 계속 순회
'''
def solution(priorities:list, location:int):
    seq = sorted(priorities)
    idx = 1
    while seq:
        for i in range(len(priorities)):
            if priorities[i] == seq[-1]:
                if i == location: return idx
                seq.pop()
                idx += 1