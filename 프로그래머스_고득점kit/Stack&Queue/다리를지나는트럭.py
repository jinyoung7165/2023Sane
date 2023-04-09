# 트럭 여러 대가 순서대로 지나감, 최소 몇 초?
# 다리 길이는 b_length
# 다리는 weight 이하의 무게를 견딜 수 있음
# 무게 [7,4,5,6] 트럭이 순서대로 다리를 건너려면 최소 8초(b_length=2, weight=10)
# 무게 10인 트럭이 길이 100인 다리를 지나려면 101초 걸림
# FIFO -> Queue
from collections import deque

def solution(bridge_length: int, weight: int, truck_weights: list):
    answer = 0
    que = deque(0 for _ in range(bridge_length)) # 다리 길이만큼 0 채움 -> weight 합 편하게 구함
    while que:
        que.popleft()
        if truck_weights:
            if truck_weights[0] + sum(que) <= weight:
                que.append(truck_weights.pop(0))
            else:
                que.append(0)
        answer += 1
    return answer

'''
deque 쓰니까 시간 초과 에러, 그냥 pop(0)으로 뽑자
or 원래 배열 reverse해서 pop()
'''
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for _ in range(bridge_length)]
    
    while bridge:
        answer += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:            
                t = truck_weights.pop(0)
                bridge.append(t)
            else:
                bridge.append(0)

    return answer

'''
deque 쓰지만 빠른 경우
'''
def solution(bridge_length, weight, truck_weights):
    bridge = deque(0 for _ in range(bridge_length))
    total_weight = 0
    answer = 0
    truck_weights.reverse() # pop()하기 위함

    while truck_weights:
        total_weight -= bridge.popleft()
        if total_weight + truck_weights[-1] > weight:
            bridge.append(0)
        else:
            truck = truck_weights.pop()
            bridge.append(truck)
            total_weight += truck
        answer += 1

    answer += bridge_length # 맨마지막 트럭 올리고 나서 bridge 길이만큼 이동해야 함

    return answer