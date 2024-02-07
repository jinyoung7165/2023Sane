# 구역 나누기2
'''
구역 개수 = 1 -> M-m
구역 개수 = len(전체 길이) -> 0
len(전체 길이) = 1 -> 0
특정 인덱스를 기준으로 구간 나눠가면서,
만약 그 구간의 값이 answer보다 크거나 같으면 그만둠 분할 정복 시간 초과 -> 이분 탐색해야 함
'''
n, k = map(int, input().split())
numbers = list(map(int, input().split()))
def bs(numbers):
    answer = max(numbers) - min(numbers)
    left, right = 0, answer
    if k == 1: return answer
    elif len(numbers) == k: return 0
    while left <= right:
        mid = (left+right) // 2
        m, M = float('inf'), 0
        cnt = 1 # 나눈 구간의 수
        for i in range(len(numbers)):
            if numbers[i] < m: m = numbers[i]
            if numbers[i] > M: M = numbers[i]
            if M - m > mid:
                cnt += 1
                m = numbers[i] # 여기서부터 새로운 구간 시작
                M = numbers[i]
                if cnt > k: break
        if cnt > k: # 불가능
            left = mid + 1 # 최댓값 늘리기
        else:
            right = mid - 1
            answer = min(answer, mid)
    return answer   
        
print(bs(numbers))