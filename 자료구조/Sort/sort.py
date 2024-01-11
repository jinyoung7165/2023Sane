def bubbleSort(x):
    for i in range(len(x)-1): # 각 pass. 오른쪽부터 max채워짐
        swapped = False
        for j in range(len(x)-i): # 이전 pass에서 오른쪽 max가 확정됨. 범위 감소
            if x[j]>x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
                swapped = True
        if not swapped: # 해당 pass에서 swap 발생x
            break # 이미 정렬된 상태

def selectionSort(x): # 최솟값을 맨 왼쪽에 배치
    for i in range(len(x)-1):
        min_idx = i
        for j in range(i+1, len(x)): # 최솟값의 idx 갱신
            if x[j]<x[min_idx]:
                min_idx = j
        x[i], x[min_idx] = x[min_idx], x[i]
      
def insertionSort(x):
    for i in range(1, len(x)): # pivot이 왼쪽 sortedList보다 크면 정렬 끝
        j, pivot = i-1, x[i]
        while pivot < x[j]: # 원래 x[j]를 j+1위치로 밀어내고, pivot보다 작은 원소 나올 때까지 j-1
            x[j+1] = x[j]
            j = j-1
        x[j+1] = pivot
    return x

def shellSort(x): # gap: n/2->1될때까지 insertionSort
    n = len(x)
    gap = n//2
    while gap>0: # 1이 될 때까지
        for i in range(gap, n): # pivot
            pivot = x[i]
            j = i-gap # i와 gap만큼 떨어진 왼쪽 원소
            while j>=0 and x[j]>pivot: # pivot보다 왼쪽 원소가 크면 swap
                x[j+gap] = x[j] # 원래 x[j]를 j+gap위치로 밀어내고, pivot보다 작은 원소 나올 때까지 j-gap
                j -= gap
            x[j+gap] = pivot
        gap //= 2
    return x

def heapSort(x):
    def heapify(arr, parent, size): # subtree-> max heap으로
        largest = parent
        left = 2*parent+1
        right = 2*parent+2
        
        if left<size and arr[left]>arr[largest]:
            largest = left
        if right<size and arr[right]>arr[largest]:
            largest = right
            
        if largest != parent: # 부모보다 자식이 크면 swap
            arr[largest], arr[parent] = arr[parent], arr[largest]
            heapify(arr, largest, size) # 자식 idx level로 넘어감
            
    n = len(x)
    # 최대 heap 생성 -> 루트가 서브트리 노드보다 큼 보장
    for i in range(n//2-1, -1, -1): # 맨마지막 원소의 루트부터 전달(n은 전체 노드 수)
        heapify(x, i, n)
    
    # root와 마지막 노드 swap후, 마지막 노드(제일 큰 수)빼고 heap화
    for i in range(n-1, 0, -1):
        x[i], x[0] = x[0], x[i]
        heapify(x, 0, i)

def mergeSort(x):
    if len(x)<2:
        return x
    mid = len(x)//2 # 기준 idx
    left_list = mergeSort(x[:mid]) # 정렬된 부분 list
    right_list = mergeSort(x[mid:])
    
    result = []
    l = r = 0 # 정렬된 두 부분 list 비교를 위한 포인터
    while l<len(left_list) and r<len(right_list):
        if left_list[l] < right_list[r]:
            result.append(left_list[l])
            l += 1
        else:
            result.append(right_list[r])
            r += 1
    # 둘 중 하나의 리스트는 아직 원소 남아 있음
    result += left_list[l:]
    result += right_list[r:]
    return result

def mergeSortOptimized(x): # result 따로 만들지 말고 inplace업데이트
    def sort(l, r): # 비교해야 하는 idx만 전달
        if r-l < 2:
            return
        mid = (l+r)//2
        sort(l, mid)
        sort(mid, r)
        merge(l, mid, r) # 두 인접 리스트 합치자
        
    def merge(low, mid, high): # 두 인접 리스트: low~mid, mid~high로 나뉨
        temp = []
        l, r = low, mid # l:low~mid, r:mid~high
        while l<mid and r<high:
            if x[l] < x[r]:
                temp.append(x[l])
                l += 1
            else:
                temp.append(x[r])
                r += 1
                
        while l<mid: # 털기
            temp.append(x[l]) 
            l += 1
        while r<high:
            temp.append(x[r])
            r += 1
        print(low, mid, high, x, temp)
        # x가 [3,4,5,2,3,4]일 때, low1~3high면, temp=[4,5]로 잘림
        # x[low] = temp[low-low]
        # x[high] = temp[high-low]
        for i in range(low, high):
            x[i] = temp[i-low]
        
    sort(0, len(x))
    return x # in-place update
print(mergeSortOptimized([3,4,5,2,3,4]))

from collections import deque
def radixSort(x):
    bucket = [deque() for _ in range(10)] # 0-9까지 큐
    max_num = max(x)
    que = deque(x)
    pos = 1 # 1의 자리 수부터 보기 위함

    while max_num >= pos: # 가장 큰 수의 자릿수 뛰어 넘으면 stop
        while que:
            num = que.popleft() # que에 들어간 순서대로 pop FIFO
            bucket[(num//pos) % 10].append(num) # 현재 자릿수 숫자에 해당하는 큐에 넣음
        
        for b in bucket: # 0-9 큐
            while b:
                que.append(b.popleft()) # 해당 자릿수에서 작았던 숫자부터 QUE에 들어감
        print(pos, "자릿 수 정렬: ", list(que))        
        pos *= 10 # 자릿수 증가
    return list(que)
print(radixSort([123,2154,222,4,283]))

def countSort(x):
    count = dict()
    for num in x: # 해당 원소가 list에 몇 개 있는지
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    result = [0]*len(x)
    for num in x:
        count[num] -= 1
        result[count[num]] = num
    return result
