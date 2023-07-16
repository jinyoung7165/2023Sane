def solution(s):
    nums = sorted(map(int, s.split()))
    answer = str(nums[0]) + ' ' + str(nums[-1])
    return answer