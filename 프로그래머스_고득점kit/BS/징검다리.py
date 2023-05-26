# 출발지부터 distance만큼 떨어진 도착지점
# 그 사이 바위들이 놓임 -> 몇 개 제거하려 함
# 도착지가 25만큼 떨어져있고, [2,14,11,21,17] 놓여있을 때
# 바위 2개 제거 시
# 제거한 바위 위치, 출발지~도착지까지 각 바위 간 거리, 거리 최솟값
# [21, 17], [2,9,3,11], 2
# [2,21], [11,3,3,8], 3
# [2,11], [14,3,4,4], 3
# [11, 21], [2, 12, 3, 8], 2
# [2, 14], [11, 6, 4, 4], 4
# 출발~도착까지 distance, 바위위치 배열, 제거할 바위 수 주어지면
# 바위 n개 제거 후 각 지점 간 거리 최솟값 중 가장 큰 값 return
# 입력 범위 엄청 큼
# [0, 10, 20, 25] mid=13. 10제거 시 5, 20제거 시 10
# [0,2,11,14,17,25] mid=13, 시작~mid보다 먼 거를 제거해야 최댓값 나옴
# 가능한 돌 사이 최소 거리:1~distance
# 돌 사이 거리가 mid보다 작은 돌 제거
# 너무 많이 제거했을 때는 mid가 너무 컸구나.
# [0,2,4,6,8,10,12], 제거 바위 수:2인 경우, 최소 간격에 변동x
# 1개든 2개든 최소 간격에 변동x-> n개 이하 제거 시 최소 간격에 변동 없을 수 있음
# 배열의 앞부분부터 순회하며 특정 간격으로 제거해야 최소 간격 구할 수 있음
def bs(left, right, rocks, n):
    answer = 0
    while left <= right:
        cnt = 0
        pivot = 0 # 기준점부터 mid(최소 거리 가정) 후 rock이 나타나야 함
        mid = (left+right) // 2
        for rock in rocks:
            if rock - pivot < mid: # 가정 최소거리보다 더 가까운 rock=> 제거하자
               cnt += 1
            else: # 가정 최소거리 만족 시 pivot 갱신 
               pivot = rock # 다음 순회부터 이 rock 기준 mid 이내 거리 확인
            if cnt > n: # 너무 많이 제거. mid가 너무 크다
                break
        if cnt > n:
            right = mid - 1
        else: # n개 이하로 제거함. 최소 간격에 변동x
            left = mid + 1
            answer = mid
    return answer

def solution(distance:int, rocks:list, n:int):
    rocks.sort()
    rocks.append(distance) # 마지막까지의 거리 측정을 위해
    # 1~distance 거리의 rock n개 제거
    answer = bs(1, distance, rocks, n)
    return answer

print(solution(25, [2,14,11,21,17], 2)) # 4
print(solution(1,[1],1))