# 시간에 따른 가격 배열 -> 가격이 떨어지지 않은 기간 몇 초인지
# [1,2,3,2,3] -> [4,3,1,1,0]
# 자신의 값과 이후 비교
# stack의 top과 비교 -> top이 작거나 같으면 stack의 모든 원소에 대해 time++
# top이 크면 stack.pop. stack에서 빠질 때도 +1초 버텼다고 생각
# stack에 idx만 저장하자
def solution(prices: list):
    answer = [0] * len(prices)
    stack = []
    for i, p in enumerate(prices):
        for idx in stack: # stack의 모든 원소에 대해 time 증가
            answer[idx] += 1
        while stack and prices[stack[-1]] > p:
            stack.pop()
        stack.append(i)
            
    return answer
'''
한번에 idx로 answer 계산하는 법? (현재idx-top idx) stack에 idx와 price같이 저장 -> 훨씬 빠름
'''
def solution(prices: list):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        while stack and stack[-1][1] > prices[i]: # top의 price가 더 크면, 하락
            top, _ = stack.pop() # top의 idx가져옴
            answer[top] = i - top
        stack.append([i, prices[i]]) # 현재 idx, price 넣음
    for i, s in stack: # 끝까지 남은 상승세의 answer 계산
        answer[i] = len(prices) - 1 - i
    return answer

print(solution([1, 2, 3, 2, 3])) # [4, 3, 1, 1, 0]
print(solution([3, 1, 2, 2, 3, 1])) # [1, 4, 3, 2, 1, 0]
print(solution([1, 2, 3, 1, 2, 3, 3, 1, 2])) # [8, 2, 1, 5, 3, 2, 1, 1, 0]