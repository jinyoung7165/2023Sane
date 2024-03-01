# 중앙값 구하기
'''
홀수번째 수 읽을 때마다 현재까지 스캔한 수 list의 중앙값(정렬 시 가운데)
전체 수열의 크기는 항상 홀수 (n)
음숫값 포함
입력받는 수열의 크기가 10이상이면, 한 줄에 10개씩 입력받음
-> 중앙값 개수 한 줄 출력 (n//2 + 1)
-> 중앙값 리스트 한 줄에 최대 10개씩 출력

올때마다 자동 정렬 리스트에 붙는다고 생각.
# 큰 애1 작은 애1 -> mid유지
# 큰+큰/같은 / 같은같은 -> mid+1 
# 작은+작/같은 -> mid-1
자기보다 큰 원소 - 자기보다 작은 원소 수 update
작은 애들?
'''
import heapq
from sys import stdin

input = stdin.readline
tc = int(input())

for _ in range(tc):
    n = int(input())
    nums = []
    for _ in range(0, n, 10):
        nums.extend(list(map(int, input().split())))
        
    result = [nums[0]]
    mid = nums[0]
    small, large = [], []
    for i in range(1, n): # 첫번째 mid 이후로 큐에 삽입
        if nums[i] < mid:
            heapq.heappush(small, -nums[i]) # 작은 애 중 큰 게 mid 후보
        else:
            heapq.heappush(large, nums[i]) # 큰 애 중 작은 게 mid 후보
        if i % 2 == 0: # 홀수번째 -> 중앙 구하기
            if len(small) > len(large): # mid-1 포인터 옮겨야 함
                heapq.heappush(large, mid) # 다음 mid보다 현재 mid 같거나 큼
                mid = -heapq.heappop(small) # 이전 mid보다 작은 mid로 옮김
            elif len(small) < len(large):
                heapq.heappush(small, -mid)
                mid = heapq.heappop(large)
            # small, large size 같으면 mid 유지
            result.append(mid)
    
    print(n//2+1)
    for i in range(0, n//2+2, 10):
        print(*result[i:i+10])