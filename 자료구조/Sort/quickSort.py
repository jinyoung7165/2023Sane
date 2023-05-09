# 중간 피벗 방식
# pivot기준 작은 원소->lesser_arr에
# pivot기준 큰 원소->greater_arr에
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

# 최적화. in-place 정렬
def quick_sort(arr):
    def sort(low, high):
        if high <= low:
            return

        mid = partition(low, high)
        sort(low, mid-1)
        sort(mid, high) # pivot을 rightList에 포함시킴

    # pivot에 따라 왼쪽에 작은 값, 오른쪽에 큰 값 배치, 다음 pivot=low리턴
    def partition(low, high):
        pivot = arr[(low + high) // 2] # 중간 pivot
        while low <= high: # 두 포인터 교차할 때까지 반복-><-
            while arr[low] < pivot: # pivot보다 큰 값 찾거나, pivot 위치에 올 때까지
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high: # 아직 교차해 지나치지 않았으면 swap해서 약한 정렬
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low # 교차해 지나쳤다면 다음 pivot이 될 low 리턴
    return sort(0, len(arr)-1)