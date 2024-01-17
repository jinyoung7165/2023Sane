# Gas Station
# 원형 큐. 각 원소의 양 gas[i]
# 다음 원소까지 이동 비용 cost[i]
# 시계방향으로 돌아 처음으로 돌아올 수 있으면 출발지 idx return
'''
전체 기름 양보다 전체 비용이 크면 순회 불가능
i->i+1: status = (누적gas-cost[i])+gas[i+1]
1->2->3->4 누적하다가 갑자기 minus
: 2/3에서 출발해도 누적된 gas는 더 작기 때문에 minus 나올 것 -> 어차피 정답이 안되는 구간
노드 4부터 다시 출발지 탐색하면 됨(새로운 구간 -> two pointer 이용)
'''
# 1. 어차피 가능한 출발지점은 하나 전제-> 안되는 지점을 모두 빼면 정답이 됨 O(n) greedy
def canCompleteCircuit(gas, cost) -> int:
    if sum(gas) < sum(cost): return -1 # 애초에 순회 불가
    last, answer = 0, 0
    for i in range(len(gas)-1): # 모든 출발지 중, 안되는 노드 빼면 정답
        if last + gas[i] < cost[i]:
            answer = i+1 # 다음 노드를 출발지로 삼아라
            last = 0
        else:
            last += gas[i]-cost[i] # 누적해서 cost 빼고, gas 충전
    return answer

# 2. 쭉 순회하다가 어차피 안되는 구간 나오면, 그 다음 구간 탐색: O(n) two pointers
def canCompleteCircuit(gas, cost) -> int:
    if sum(gas) < sum(cost): return -1 # 애초에 순회 불가
    last, left = 0, 0
    for right in range(len(gas)):
        last += gas[right] - cost[right] # 현재노드->다음노드 이동 준비
        if last < 0: # 다음 노드부터 탐색해야 함
            left = right + 1
            last = 0
    
    return left