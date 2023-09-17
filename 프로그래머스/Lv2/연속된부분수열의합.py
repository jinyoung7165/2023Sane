'''
오름차순 수열 -> 기존 수열에서 시작idx-끝idx 사이 연속된 수열
합이 k가 되도록 -> 여러 개인 경우, 길이 짧은 것 -> 여러 개인 경우, 인덱스 작은 것
수열의 idx는 0부터 시작.
[1,2,3,4,5], 7 -> [3,4]-> idx[2,3] return
[1,1,1,2,3,4,5], 5 -> [5] -> [6,6] return
[2,2,2,2,2], 6 -> [2,2,2] -> [0,2] return
[2,2,2,3,3], 6 -> [3,3] -> [3,4] return
[1,2,2,3,3], 5 -> [2,3] -> [3,4] return
1 ≤ sequence의 원소 ≤ 1,000
5 ≤ sequence의 길이 ≤ 1,000,000
1 12 123(6) 1234(10 -> k보다 큼 -> popleft 2번 -> k생성됨 -> 일단 기록)
1112(5) k찾음->일단 기록
'''
from collections import deque
def solution(sequence, k):
    answer = []
    cur_sum = 0
    que = deque([]) # 숫자
    for idx, seq in enumerate(sequence):
        if seq < k:
            while cur_sum + seq > k:
                cur_sum -= que.popleft()[1]
            que.append((idx, seq))
            cur_sum += seq
            if cur_sum == k:
                if not answer or len(que) < answer[1] - answer[0] + 1: # 더 짧을 때만
                    answer = [que[0][0], idx]
        else:
            if seq == k: answer = [idx, idx]
            break
    return answer


def solution(sequence, k):
    answers = []
    sum = 0
    l = 0
    r = -1
    
    while True:
        if sum < k:
            r += 1
            if r >= len(sequence):
                break
            sum += sequence[r]
        else:
            sum -= sequence[l]
            if l >= len(sequence):
                break
            l += 1
        if sum == k:
            answers.append([l, r])
    
    answers.sort(key=lambda x: (x[1]-x[0], x[0]))
    return answers[0]