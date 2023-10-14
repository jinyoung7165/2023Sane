'''
숨바꼭질2
점n->점k 이동하는 가장 빠른 시간, 경우의 수 찾기 (좌표 0~100,000)
1초 뒤에 x-1, x+1로 걷기 가능
1초 뒤에 2*x 위치로 순간 이동 가능
'''
from collections import deque

n, k = map(int, input().split())
M = float('inf')
time, answer = M, 0
que = deque([(n, 0)]) # 숫자, 시간
visited = dict()
while que:
    num, cnt = que.popleft()
    if num < 0 or num > 100000: continue
    if num in visited and visited[num] < cnt: continue
    visited[num] = cnt
    if time != M: # 답이 나옴
        if num == k: answer += 1
        continue
    if num == k:
        time = cnt
        answer += 1
        continue
    que.append((num*2, cnt+1))
    que.append((num+1, cnt+1))
    que.append((num-1, cnt+1))

print(time)
print(answer)