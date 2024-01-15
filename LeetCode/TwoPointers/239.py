# Sliding Window Maximum
from collections import deque
#최적화 - data많을 때 max너무 느림
def maxSlidingWindow(nums, k):
    results = []
    window = deque() #FIFO
    # nums를 통해 현재 숫자들 window에 들어옴
    # window 중간에 있는 애보다 지금 들어오는 애가 크다 -> window 중간 원소 버림
    for i, n in enumerate(nums):
        while window and nums[window[-1]] <= n: # 방금 window에 들어간 애보다 지금 num이 더 큼
            window.pop()
        window.append(i)
        
        if i < k-1: continue # 첫번째 k window 채워질 때까지 result 기록 x
        results.append(nums[window[0]])

        if i-window[0]+1 == k: # window 사이즈 초과 -> 하나씩 제거
            window.popleft()

    return results