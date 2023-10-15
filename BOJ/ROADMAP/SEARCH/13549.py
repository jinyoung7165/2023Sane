'''
숨바꼭질3
점n->점k 이동하는 가장 빠른 시간 찾기 (좌표 0~100,000)
0초 뒤에 2*x 위치로 순간 이동 가능
바로 break하면, que에 들어가는 순서가 시간 순이 아니라 3개씩 넣고 돌리는 거기 때문에, 최단 아닐 수 있음
1초 뒤에 x-1, x+1로 걷기 가능
'''
from collections import deque

n, k = map(int, input().split())
M = float('inf')
time = M
que = deque([(n, 0)])

visited = [-1] * 100001
# 2배로 이동하는 거 0초 소요되기 때문에 끝까지 다 가볼 수 있음
# 노드가 너무 많을 땐 in 연산 불리 -> dict대신 배열 쓰자

while que:
    num, cnt = que.popleft()
    if num < 0 or num > 100000: continue
    if visited[num] != -1 and visited[num] <= cnt: continue
    visited[num] = cnt
    if num == k:
        time = min(time, cnt)
        continue
    que.append((num*2, cnt))
    que.append((num+1, cnt+1))
    que.append((num-1, cnt+1))
    
print(time)

''' 더 효율적인 코드
while que:
    node = que.popleft()
    if node == k: #도착
        print(dp[node])
        break
    if k < n:
        print(n-k) #1초에 1칸씩 뒤로 가야함
        break
    if 100001 > node*2 and dp[node*2] > dp[node]:
        dp[node*2] = dp[node]
        que.append(node*2)
    if 0 <= node-1 and dp[node-1] > dp[node] + 1: #갱신 가능
        dp[node-1] = dp[node] + 1
        que.append(node-1)
    if 100001 > node+1 and dp[node+1] > dp[node] + 1:
        dp[node+1] = dp[node] + 1
        que.append(node+1)
'''