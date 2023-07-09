# 가운데를 말해요
# a가 말한 수 중 중간값을 말해야 함
# 외친 개수가 홀수라면, 정렬했을 때 중앙에 오는 값(중간값)
# 외친 개수가 짝수라면, 중간 두 수 중 작은 수 말해야 함(leftHeap에 있어야 함)
# 1,5,2,10,-99,7,5 외쳤다
# 1,1,2,2,2,2,5 를 답해야 함
# 1보다 작거나 같은 애들 몇 갠지
'''
leftHeap의 root가 중간값이 되도록 함(maxHeap으로 구성)
rightHeap의 root~모든 노드가 left의 root보다 크도록 구성(minHeap)
어떻게?
일단, leftHeap과 rightHeap 길이 최대한 맞추는 방식으로 삽입
leftHeap과 rightHeap의 길이 같다면, 중간값의 기준이 되는 left에 넣기
길이 다르면, left길이와 맞추기 위해 right에 삽입 
이후, leftHeap의 root가 rightHeap의 root보다 크면, leftHeap과 rightHeap의 root 바꾸기
1->1 
1 5 -> 1
12 5 -> 2
12 510 -> 2
-99,1,2, 5,10 ->2
-99,1,2, 5,7,10 -> 2
-99,1,2,5, 5,7,10 -> 5 (leftHeap, rightHeap 길이 같다면 left에 삽입)
'''
# 매번 출력해야함 -> 정렬 반복 시 시간 초과 -> HEAP 쓰자
import heapq
from sys import stdin
left, right = [], []
input = stdin.readline
n = int(input())
for i in range(n):
    num = int(input())
    if len(left) == len(right): # 양쪽 힙의 길이 맞춰가며 삽입
        heapq.heappush(left, (-num))
    else:
        heapq.heappush(right, (num))
    if right and -left[0]>right[0]: # 두 힙 루트의 대소 맞추는 작업
        l_root = heapq.heappop(left)
        r_root = heapq.heappop(right)
        heapq.heappush(left, (-r_root))
        heapq.heappush(right, (-l_root))
        
    print(-left[0])