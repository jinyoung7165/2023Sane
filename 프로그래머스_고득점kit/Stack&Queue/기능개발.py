from collections import deque
from math import ceil
def solution(progresses:list, speeds:list): # 쓰레기 코드... que & 반복문 1개로 날짜와 count 누적하게 하자
    answer = []
    if not progresses: return [0]
    que = deque([])
    for i, progress in enumerate(progresses):
        left = 100 - progress
        speed = speeds[i]
        day = ceil(left / speed)
        que.append(day)

    last = que.popleft()
    count = 1
    while que:
        el = que.popleft()
        if last >= el:
            count += 1
        else:
            answer.append(count)
            last = el
            count = 1
    answer.append(count)
    return answer

def solution(progresses:list, speeds:list): # 단순한 변수, day 계속 누적 시 반복 많음
    answer = []
    day, count = 0, 0 # 누적 날짜, 기능 수
    while progresses:
        p, s = progresses[0], speeds[0] # 달성 불가능하면 day 증가 기다림
        if (p + day*s) >= 100: # 누적 날짜로 달성 가능하면 기능 추가
            count += 1
            progresses.pop(0)
            speeds.pop(0)
        else: # 현재 day로는 달성 불가능
            if count > 0: # 이전에 기능이 쌓여있었으면 flush
                answer.append(count)
                count = 0
            day += 1
    answer.append(count)
    return answer

def solution(progresses, speeds): # 공간 복잡도 줄이자
    Q = []
    for p, s in zip(progresses, speeds): # 두 배열 같이 묶어 순회
        if not Q or Q[-1][0]<-((p-100)//s): # 음수 나누기 시 자연스럽게 ceil 가능
            Q.append([-((p-100)//s), 1]) # 날짜, 기능 수 추가
        else: # Q의 top이 현재 시간보다 클 때, 해당 날짜의 기능 수 누적
            Q[-1][1] += 1
    return [q[1] for q in Q]