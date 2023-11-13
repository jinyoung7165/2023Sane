# 3Sum
# nums[i] + nums[j] + nums[k] == 0이 되는 조합 1개 return
# idx return 아니니까 sort 가능
# 원래라면 3중 반복문, i번째 원소 반드시 포함한다고 치고, 슬라이딩 윈도우 이동하며
# left, right 지정해서 O(n^2)로 바꿈
# "같은 조합은 한 번만 result에 추가해야 함"
# -4 -4 2 2 2 2 ... 일 때,
# 4(target) = 2+2 조합이 계속 반복되기 때문에
# i-1 == i+1일 때 다른 target수 만들기 위해 건너뛰어야 함
# 또한, twoSum에서 0이 되는 조합 찾은 후에, target수를 만들기 위한 조합에(4=2+2)
# 이미 left수(2)가 쓰였는데, left+1수(2)도 같은 수라면 똑같은 조합(4=2+2)이 나오기 때문에 건너뛰어야 함
def threeSum(nums):
    answer = []
    def twoSum(i):
        left, right, target = i+1, len(nums)-1, -nums[i]
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                answer.append([-target, nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]: # 이미 본 조합만 나올 것
                    left += 1
                while left < right and nums[right] == nums[right-1]: # 이미 본 조합만 나올 것
                    right -= 1
                left += 1
                right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1

    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]: continue # 이미 본 조합만 나올 것
        twoSum(i)
    return answer