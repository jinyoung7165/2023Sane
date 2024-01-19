# Majority Element
'''
크기 n인 배열 -> n/2 초과해서 나타나는 원소 찾아라
O(n)시간 아래, O(1) space 제한 -> sort x
python timsort 가능할지도...
배열 크기 10^4이므로, 특정 원소가 10^2 초과해서 나와야 함
답이 항상 존재함 전제
count sort의 경우, O(n) 시간 복잡도 가짐, but, 수의 범위 너무 크기 때문에 활용 불가
리스트 절반으로 잘랐을 때, 그것의 절반이상 나와야 함
절반으로 쪼갰을 때 right에 적어도 하나 이상 포함
12122의 경우
12  / 122
(1) / (1/22(2))
1 / (2)
2를 선택하는 법 -> 두 list merge된 상태에서 세는 것밖에 없음
'''
def majorityElement(nums) -> int: # python 특성 이용 -> 가장 효율적
    return sorted(nums)[len(nums)//2]


def majorityElement(nums) -> int: # 재귀. divide and Conquer
    def divide(nums, size):
        if size == 1:
            return nums[0]
        mid = size // 2
        left = divide(nums[:mid], mid)
        right = divide(nums[mid:], size-mid)
        if left != right and nums.count(left) > mid: return left
        return right
    return divide(nums, len(nums))