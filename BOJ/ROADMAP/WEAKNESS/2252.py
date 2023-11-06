'''
줄 세우기
N명 학생 키 순서대로 줄 세우려고 함.
두 학생 키 비교하는 방법 - 일부만 알 수 있음
a b : a가 b 앞에 와야 함
답 여러 개인 경우 아무거나 출력
순서 있는 task 정렬 -> cycle없음. 위상 정렬(ingress)
ingress 0인 것부터 수행 가능: 내가 실행되기 위해 필요한 간선 수
graph: 내가 실행되고 나서 이동 가능한 노드
'''
from sys import stdin
input = stdin.readline
que = [] # deque 쓸 필요 없이 stack
v, e = map(int, input().split()) # 학생 수, 비교 수
ingress = [0] * (v+1)
graph = [[] for _ in range(v+1)]
left = set(range(1, v+1))
result = []
for _ in range(e):
    a, b = map(int, input().split())  # a->b
    ingress[b] += 1 # b 실행하기 위한 준비과정 1 증가
    graph[a].append(b) # a->b

for i in range(1, v+1):
    if ingress[i] == 0:
        que.append(i)
        
while que:
    cur = que.pop()
    left.remove(cur)
    result.append(cur)
    for node in graph[cur]:
        ingress[node] -= 1
        if ingress[node] == 0:
            que.append(node)
for node in left:
    que.append((node))

print(*result)