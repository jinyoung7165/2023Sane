# I 숫자 -> 큐에 삽입
# D 1 -> 큐 최댓값 삭제
# D -1 -> 큐 최솟값 삭제
# (삭제 시 같은 값 여러 개면 하나만. 빈 큐면 무시)
# 이중 우선순위큐가 할 연산이 주어질 때
# 처리 후 큐가 비어있으면 [0, 0]
# 비어있지 않으면 [최댓값, 최솟값] return
# heap은 자식 간의 순서 정렬x -> que의 맨마지막이 최대 보장x!!!!
import heapq

def solution(operations: list):
    answer = [0, 0]
    que = []
    
    for operation in operations:
        op, num = operation.split()
        if op == "I":
            heapq.heappush(que, int(num)) # num 최솟값
        else:
            if not que: continue
            if num == "-1":
                heapq.heappop(que)
            else:
                # 큐에서 가장 큰 수를 제외하고 다시 힙큐화
                que = heapq.nlargest(len(que), que)[1:]
                heapq.heapify(que)
                # 둘 다 같음
                # que.sort()
                # que = que[:-1]
                # heapq.heapify(que)
    if que:
        answer[0] = max(que) # heapq는 자식 간의 정렬x -> max는 스스로 구해야 함
        answer[1] = que[0]
    return answer

''' 정석 풀이 -> 최소 heap, 최대 heap'''
def solution(arguments):
    max_heap = []
    min_heap = []
    for arg in arguments:
        if arg == "D 1": # 최대 힙에서 제거
            if max_heap:
                heapq.heappop(max_heap)
                if not max_heap or -max_heap[0] < min_heap[0]: # 최대 힙 empty or 최소 힙이 더 커지면 숫자 없는 상태. 둘 다 비워라
                    min_heap = []
                    max_heap = []
        elif arg == "D -1": # 최소 힙에서 제거
            if min_heap:
                heapq.heappop(min_heap)
                if not min_heap or -max_heap[0] < min_heap[0]: # 최소 힙 empty or 최소 힙이 더 커지면 숫자 없는 상태. 둘 다 비워라
                    max_heap = []
                    min_heap = []
        else:
            num = int(arg[2:])
            heapq.heappush(max_heap, -num) # 최대 힙
            heapq.heappush(min_heap, num) # 최소 힙

    if not min_heap:
        return [0, 0]
    return [-heapq.heappop(max_heap), heapq.heappop(min_heap)] # 최대, 최소
