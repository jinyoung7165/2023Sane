# 0초에 3초짜리, 1초에 9초짜리, 2초에 6초짜리 작업 요청 들어옴
# 한번에 1요청만 처리 가능 [[0, 3], [1, 9], [2, 6]]
# ->요청순으로 처리 시
# 각 작업의 요청~종료 시간 평균은 10초. (3+11+16)/3
# A->C->B 처리 시
# 평균 9초. (a3+c7+b17)/3
# 제일 적은 평균 시간 구하라. 소수점 이하의 수는 버림
# 작업을 수행중이 아니면 순차적으로
import heapq
def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1 
    heap = []
    
    while i < len(jobs):
        # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        
        if len(heap) > 0: # 처리할 작업이 있는 경우
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1] # 작업 요청시간부터 종료시간까지의 시간 계산
            i +=1
        else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1
                
    return answer // len(jobs)


import heapq
from collections import deque

def solution(jobs):
    que = []
    length = len(jobs)
    job_que = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    # 소요, 요구, 위치 바꿔 나열(heapq 넣기 위함) -> 요구, 소요 순 정렬해 deque 삽입
    heapq.heappush(que, job_que.popleft()) # 소요, 요구 순 정렬
    
    now = 0 # 현재 시간
    total = 0 # 총 대기 시간
    
    while que: # 실행 큐
        dur, req = heapq.heappop(que)
        now = max(dur+now, dur+req) # 현재 시간 이전에 요청(겹침) or 이후 요청(겹치지 않는 작업일 때)
        total += now - req
        while job_que and job_que[0][1] <= now: # 이전에 요청된 거면 실행
            heapq.heappush(que, job_que.popleft())
        if not que and job_que: # 실행 큐 비었는데 대기열에 존재 시(현재 시간 이후 요청 -> now = req+dur)
            heapq.heappush(que, job_que.popleft())
    return total // length