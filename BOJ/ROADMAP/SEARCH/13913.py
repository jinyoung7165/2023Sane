'''
숨바꼭질4
1초 뒤에 x-1, x+1로 걷기 가능
1초 뒤에 2*x 위치로 순간 이동 가능
가장 빠른 시간, 경로 찾기
'''
from collections import deque

n, k = map(int, input().split())
que = deque([(n)])
M = float('inf')
time = M
visited = [M] * 100001 # 특정 노드까지 도달하기 위한 시간
# 큐마다 이동 경로를 주지 않고, 
# 어차피 방문한 노드는 다시 방문하지 않으므로!!!!
# move 배열을 만들어 node i 를 방문하기 직전 노드를 저장!!!!
move = [M] * 100001
visited[n] = 0
while que:
    cur = que.popleft()
    if cur == k:
        time = visited[cur]
        break
    for node in (cur*2, cur+1, cur-1):
        if 0<=node<=100000 and visited[node]== M:
            visited[node] = visited[cur]+1 # 1초 소요
            move[node] = cur # node 이전 경로는 cur
            que.append((cur*2))
            que.append((cur+1))
            que.append((cur-1))
path = []
node = k         
for _ in range(time+1):
    path.append(node)
    node = move[node]
path.reverse()

print(time)
print(*path)