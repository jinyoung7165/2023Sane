'''
숨바꼭질2
점n->점k 이동하는 가장 빠른 시간, 경우의 수 찾기 (좌표 0~100,000)
1초 뒤에 x-1, x+1로 걷기 가능
1초 뒤에 2*x 위치로 순간 이동 가능
'''
from collections import deque
n, k = map(int, input().split())
M = max(n, k) * 2
visited = [M] * (M+1)
visited[n] = 0
que = deque([n]) # pos, time
cnt = 0
while que:
    pos = que.popleft()
    if visited[pos] > visited[k]: break
    if pos == k:
        cnt += 1
        continue
    for node in (pos*2, pos-1, pos+1):
        if node < 0 or node > M: continue
        if visited[node] >= visited[pos]+1:
            visited[node] = visited[pos]+1
            que.append(node)
print(visited[k])
print(cnt)