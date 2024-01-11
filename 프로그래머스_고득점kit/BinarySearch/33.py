# Search in Rotated Sorted Array
# 피벗 기준 회전 정렬된 배열에서 target 검색
# nums=[4,5,6,7,0,1,2] target=1 =>5(pivot4.원래 배열[0,1,..]에서 위치 1+ 4칸)
# O(logN) 제한 -> for i in range(n) 금지 -> BS
# 일반적 투포인터(mid x) 사용 시, O(n)
def search(nums, target):
    if not nums:
        return -1
    
    left, right = 0, len(nums)-1
    while left < right:
        mid = (left + right)//2
        
        #배열의 최솟값(0)의 인덱스(4)를 찾아 피벗 설정
        if nums[mid] > nums[right]: #중간이 오른쪽보다 클 때 -> mid의 오른쪽에 최솟값 존재
            left = mid+1
        else: #중간이 오른쪽보다 작을 때(정렬된 부분이다) -> mid의 왼쪽에 최솟값 존재
            right = mid
    pivot = left #최솟값의 인덱스
    
    #pivot기준 bs
    left, right = 0, len(nums)-1 
    while left <= right:
        mid = (left + right)//2
        midpivot = (mid + pivot) % len(nums) #pivot만큼 mid를 틀어줌
        
        if nums[midpivot] < target:
            left = mid + 1
        elif nums[midpivot] > target:
            right = mid - 1
        else:
            return midpivot
    return -1
