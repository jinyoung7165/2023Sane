# n명이 입국심사를 위해 줄 섬
# 각 입국심사대마다 검사 시간 다름
# 맨 처음 모든 심사대 비어 있음.
# 가장 앞에 서 있는 사람-> 비어있는 곳 가거나 더 빨리 끝나는 곳 기다릴 수 있음
# 모든 사람이 심사 받는데 걸리는 시간 최소?
# n, times 범위 엄청 큼 -> 최소 구하기 위해 bs
# n=6, times=[7,10] => 28
# (2명 각 심사대로, 첫 번째 심사대 그 후 7분, 14분, 21분에 빔)
# 2번째 심사대 10분, 20분에 비지만, 마지막 사람은 1분 기다렸다가 21분에 첫번째 심사대로 감
# n=2, times=[1, 3] => 2 (1,2),(3,6)
# n=2, times=[7, 8] => 8 (7,14),(8,16)
# n=3, times=[7, 10] => 14 (7,14,21),(10,20,30)
# n=5, times=[2, 7, 10] => 8 (2,4,6,8,10),(7,14),(10,20)
# n=5, times=[2, 2] => 6 (2,4,6,8,10),(2,4,6,8)
# 각 심사대의 다음 끝날 시간-> 정렬된 times의 몇 번째에 끼워넣을지
# 이분탐색의 범위: 총 시간
# 이분탐색의 기준(mid): 모든 심사관들에게 주어진 시간 -> 그 동안 n명보다 많이 심사한 경우 mid 줄이자
def solution(n:int, times:list):
    times.sort()
    def bs(left, right):
        answer = right
        while left <= right:
            mid = (left+right)//2
            wait = n
            for time in times:
                wait -= mid // time # 남은 인원
                if wait <= 0: break # 손님 끝
            if wait <= 0: # 성공
                right = mid - 1
                answer = mid
            else: # 실패 -> 늘리기
                left = mid + 1
        return answer
    return bs(times[0], n*times[0])