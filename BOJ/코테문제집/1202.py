# 보석 도둑
# 보석n개. 무게m, 가격v 가짐
# 가방 k개(각 가방 최대 수용 c, 한 개 보석만 넣을 수 있음)
# 최대 보석의 가격 구하라
# n, k, m, v, c 범위 모두 엄청남
# 일단은 정렬
# (500,10),(300,13),(200,2),(100,1)
# 가방 14,10,10,10일 때 답 1100이어야 함
# "작은 가방부터 최대한 큰 val을" 담아야 함
import heapq
from sys import stdin
input = stdin.readline
que = []
n, k = map(int, input().split()) # 보석 수, 가방 수
for _ in range(n): # 최소 무게, 최소 가격
    heapq.heappush(que, list(map(int, input().split())))
caps = [int(input()) for _ in range(k)] # 각 가방 수용 능력
caps.sort() # 최소 무게 정렬

cnt = 0 # 총 value
tmp = [] # 해당 가방까지 봤을 때, 최대 value heap
for bag in caps: # 각 가방에 최대 가격 담자
    while que and bag>=que[0][0]: # 해당 가방에 담을 수 있을 때
        heapq.heappush(tmp, -heapq.heappop(que)[1]) # 최대 value heap
    if tmp: # 현재 무게까지 담을 수 있는 원소들이 존재할 때
        cnt -= heapq.heappop(tmp) # 그 중 최대 val    
    elif not que: break # 누적 원소도 없는데 보석 다 씀
print(cnt)