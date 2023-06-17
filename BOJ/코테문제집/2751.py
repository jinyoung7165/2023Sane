# n개 수 주어질 때 오름차순으로 정렬
# 수 범위 큼. 중복되지 않음
# mergeSort
from sys import stdin
input = stdin.readline
n = int(input())
li = []
def mergeSort(x):
    def sort(l, r): # 비교해야 하는 idx 전달
        if r-l < 2:
            return
        mid = (l+r)//2 # 전달 받은 idx 계속 반으로 쪼개나감
        sort(l, mid) # l~mid-1
        sort(mid, r) # mid~r-1
        merge(l, mid, r) # 두 인접 리스트 합치기
    def merge(low, mid, high): # 두 리스트: low~mid, mid~high로 나뉨
        tmp = []
        l, r = low, mid
        while l<mid and r<high:
            if x[l] < x[r]:
                tmp.append(x[l])
                l += 1
            else:
                tmp.append(x[r])
                r += 1
        while l<mid: # 둘 중 하나 털기
            tmp.append(x[l])
            l += 1
        while r<high:
            tmp.append(x[r])
            r += 1
        # 즉, 정렬된 값들이 저장된 임시 리스트 tmp의 값을 원래 리스트 x의 low부터 high-1까지 대입
        for i in range(low, high):
            x[i] = tmp[i-low]
    sort(0, len(x))
    return x # in-place update
        
li = list(int(input()) for _ in range(n))
result = mergeSort(li)
for i in result:
    print(i)