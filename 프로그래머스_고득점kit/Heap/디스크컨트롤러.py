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

import heapq
from collections import deque
# 아무 작업도 하지 않을 때는 먼저 들어온 애 바로 실행됨(스케줄링X)
def solution(jobs):
    que = [] # 실행 큐
    exe = deque(sorted([(y, x) for x, y in jobs], key=lambda x: (x[1],x[0]))) # 나열 후 정렬이 포인트!!! 순서 헷갈리니 주의 (요구,소요)나열 후, (소요,요구)정렬
    # 대기 큐 -> 요청 시간 빠른 애부터 일단 넣어/ FIFO -> 큐 비면 실행 끝
    # 일단 실행하려는 차에, 겹치면 소요 더 적은 애 넣어
    # 요청, 소요, 현재 시간(앞 task 끝) 필요
    now = 0 # 앞의 작업 끝난 시점
    total = 0 # 평균 내기 전 (작업 끝-요구) 전체 시간
    # 현재 아무 것도 하지 않는 초기 상태 -> 1번 요청 작업 바로 실행
    # 이후 대기 큐에서 스케줄링(겹치면 소요 더 작은 애 먼저 실행 -> 최소 큐)
    heapq.heappush(que, exe.popleft()) # 소요, 요구
    length = len(jobs)
    while que:
        dur, req = heapq.heappop(que) # 실행
        # 비어있을 때 새 작업이 오기까지 기다린 시간(req) + 소요(dur)
        # 작업 겹친다면 req 기다리는 게 아니라, 바로 실행되기 때문에 +dur만
        # 이전 작업 끝, 현재 요청 시점 비교
        if now <= req: # req가 나중. 겹치지 않고 바로 실행
            now = req + dur # 이 작업 요청이 들어오기까지 기다림 + dur
            total += dur # 소요 시간만큼만 기다림(dur=now-req)
        else: # 작업 겹침
            now += dur # 이전 작업 끝나면 바로. 수행. 현재 작업 끝
            total += now - req # 현재 작업의 끝- 요구 시점
        # 실행할 일 남았고, 요구 시점이 이전이거나 현재와 "같음" -> 스케줄링 대상("둘 다 선택할 수 있기 때문에!!!!!!")
        while exe and exe[0][1] <= now:
            heapq.heappush(que, exe.popleft())
        if not que and exe:
            # 현재 시점에는 요청된 일이 없지만, 나중에 들어올 작업 있을 경우
            heapq.heappush(que, exe.popleft()) # 아무것도 실행x -> fifo실행
    return total // length