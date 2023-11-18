# Next Greater Element II
# 한 방향 원형으로 순회하면서 해당 원소보다 처음으로 큰 수 기록
# 순회하며 나온 수 중 나보다 큰 수. 없으면 -1
# 나보다 큰 수 기다리며. 현재 수가 더 크면, pop되는 stack 존재
# [1,2,1] -> [2,-1,2]
# [1,2,3,4,3] -> [2,3,4,-1,4]
def nextGreaterElements(nums):
    size = len(nums)
    answer = [-1] * size
    stack = [] # 나보다 큰 원소 기다리는 애들의 idx
    for i in range(size * 2):
        while stack and nums[stack[-1]] < nums[i%size]:
            answer[stack.pop()] = nums[i%size]
        if i < size: stack.append(i)

    return answer