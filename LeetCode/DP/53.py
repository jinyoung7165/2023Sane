# Maximum Subarray
# 최대 부분합. 음수 가능 -> two pointer 말고 dp
# 자기만 포함할지, 누적값에 넣을지 결정
# 1. DP Tabulation 상향식
def maxSubArray(nums) -> int:
    for i in range(1, len(nums)):
        nums[i] = max(nums[i], nums[i-1] + nums[i])
    return max(nums)

# 2. Divide and Conquer
# 전체 원소가 기준이 될 수 있음 -> mid
# 순회하며 특정 원소 기준으로, 자기만 포함할지, 누적시작값으로 넣을지 결정
def maxSum(nums): # 처음부터 누적했을 때, 최댓값
    s = nums[1] # 처음원소 무조건 포함
    for num in range(1, len(nums)):
        s = max(num+s, s)
    return s

def maxSubArray(nums) -> int:
    if len(nums) == 1: return nums[1] # 단일 원소가 최댓값이 됨
    mid = len(nums) // 2
    # [...mid-1] [mid...] 구간내 부분누적합 max 구함
    lmax, rmax = maxSubArray(nums[:mid]), maxSubArray(nums[mid:])
    
    # [..mid-1 mid mid+1..] left일부+right일부 구간 내 max구하고 싶음
    lsum, rsum = float('-inf'), float('-inf')
    s = 0
    # mid-1 포함해서 쭉 왼쪽으로 가며 누적합 구함
    # 음수만나도 stop x, 더 큰 수 만나서 상쇄 가능 
    for i in range(mid-1, -1, -1):
        s += nums[i]
        lsum = max(lsum, s)
    s = 0
    for i in range(mid, len(nums)):
        s += nums[i]
        rsum = max(rsum, s)
    
    crossmax = lsum + rsum
    
    return max(lmax, rmax, crossmax)