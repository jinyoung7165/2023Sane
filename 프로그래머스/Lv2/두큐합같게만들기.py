'''
길이 같은 두 큐. 한 큐 골라 원소 추출 -> 다른 큐에 집어 넣음
두 큐에 담긴 원소 합 같도록. 작업의 최소 횟수?
[3,2,7,2] [4,6,5,1]
[2,7,2,4] [6,5,1,3] 2번
'''
# def solution(que1, que2):
#     queSum = sum(que1) + sum(que2)
#     if queSum % 2:
#         return -1
#     target = queSum // 2

#     n = len(que1) # circular que의 절반 길이
#     start = 0 # 0~n-1, n~2n-1
#     end = n - 1
#     ans = 0

#     cur = sum(que1)
#     que3 = que1 + que2 # circular que
#     while cur != target: # 원하는 합이 될 때까지
#         if cur < target: # target보다 작으면, 뭔가를 더 더해야 함
#             # -> 앞쪽 큐의 길이 늘림
#             end += 1
#             if end == n * 2: # 최대 2n-1이기 때문에, 있을 수 없음
#                 end = 0
#             cur += que3[end] if start != 0 else -1 # 앞쪽 큐의 길이 늘림
#         else: # target보다 커서, 앞쪽 큐의 길이 줄여야 함
#             cur -= que3[start]
#             start += 1
            
#         ans += 1
#     return ans


from collections import deque
def solution(queue1, queue2):
    answer = 0
    size = len(queue1) # 두 큐 길이 같음
    q1, q2 = deque(queue1), deque(queue2)
    tot1 = sum(queue1)
    tot2 = sum(queue2)
    total = tot1+tot2
    if total % 2 != 0: return -1
    while True:
        if tot1 == tot2:
            break
        elif tot1 > tot2:
            tmp = q1.popleft()
            q2.append(tmp)
            tot1 -= tmp
            tot2 += tmp
            answer += 1
        else:
            tmp = q2.popleft()
            q1.append(tmp)
            tot1 += tmp
            tot2 -= tmp
            answer += 1
        if answer == size * 3:
            answer = -1
            break
    return answer
print(solution([1, 2, 9, 4],[1,1,2,2])) # 8
print(solution([1, 10, 1, 2], [1, 2, 1, 2])) # 7