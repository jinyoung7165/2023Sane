# Next Permutation
# [1,2,3] 순열 모두 구하면
# [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# [1,1,5], [1,5,1], [5,1,1]
# Do not return anything, modify nums in-place
# 사전식 ASC 순서 봤을 때, 다음으로 큰 순열
# [1,1,5]의 다음 순서는 [1,5,1]
# 각 숫자는 0~100. 길이는 최대 100
# 앞으로 가며 나보다 작은 거 찾고, 나:i, 내앞:i-1
    # 현재 i-1~i 오름차순, i~-1 내림차순 상황에서
    # -1->i까지 순회하며 자기 앞과 swap하며
    # i-1~i까지 내림차순으로 만들고, i~-1까지 오름차순으로 만들어야 함
    # [2,1,4,3](i-1=1, i=2) -> [2,3,1,4]
# 나보다 작은 애 못 찾으면, 내림차순으로 정렬된 상황이므로 reverse
def nextPermutation(nums) -> None:
    size = len(nums)-1
    for i in range(size, 0, -1): # 맨 끝의 원소부터 보면서 자기 앞이 더 작은 경우 찾으면
        if nums[i-1] < nums[i]: break
    else:
        nums.reverse() # 내림차순 정렬 상황
        return
    
    j = size
    # i-1번째를 뒤에 나온 수 중에서, 자기보다 큰 수(순서상 nums[j-1] 다음 수) swap해야 함
    while i-1 < j and nums[i-1] >= nums[j]:
        j -= 1
    nums[i-1], nums[j] = nums[j], nums[i-1]
    
    # i~-1까지 내림차순 상황 -> 오름차순으로 정렬해야 함
    left, right = i, size
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
        
nextPermutation([1,2,4,3])
nextPermutation([1,4,3,2])
nextPermutation([2,3,1]) # [3,1,2]