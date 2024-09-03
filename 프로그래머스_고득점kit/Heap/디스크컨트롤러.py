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
    wait = [] # 우선순위대로 정렬된 후, 실행될 큐
    size = len(jobs)
    jobs.sort(reverse=True) # 먼저 온 요청 순서대로 sort(pop하려고 거꾸로 둠)
    now = 0 # 앞 작업 끝나는 시간
    total = 0
    req, need = jobs.pop()
    heapq.heappush(wait, (need, req)) # 아무것도 없을 때 그냥 실행할 것
    while wait:
        need, req = heapq.heappop(wait) # 우선순위 제일 높은 거 실행
        if now <= req: # 기다렸다가 실행
            total += need
            now = req + need
        else: # 밀린 작업. 바로 실행
            total += now-req + need
            now += need
        while jobs and now >= jobs[-1][0]: # 밀린 애들 -> 우선순위 정렬
            req, need = jobs.pop()
            heapq.heappush(wait, (need, req))
        # 밀린 애들 없는데, wait도 없으면, 남은 jobs 중에서 가져와서 바로 실행해야 함
        if not wait and jobs:
            req, need = jobs.pop()
            heapq.heappush(wait, (need, req))
    return total // size

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