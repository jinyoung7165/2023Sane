# Evaluate Division
'''
각 변수 사용한 연산 결과 주어짐
연산 조합해 새로운 연산 결과 알려고 함
undetermined -> -1(input에 없는 수식이거나, 답 모르겠으면)
a z 알고, z b 알고, b c 알면 -> a c 가능
'''
from collections import defaultdict, deque

def calcEquation(equations, values, queries):
    result = []
    graph = defaultdict(list)
    for eq, v in zip(equations, values):
        a, b = eq
        graph[a].append((b, v))
        graph[b].append((a, 1/v))

    for a, b in queries:
        if a in graph and b in graph:
            if a == b: result.append(1.0)
            else:
                visited = set()
                visited.add(a)
                que = deque([(a, 1.0)]) # a//a에서 출발
                while que:
                    cur, val = que.popleft()
                    if cur == b: # b 만날 때까지 계속 중간 게산하며 이동
                        result.append(val)
                        break
                    for n, n_val in graph[cur]: # b 만날 때까지 계속 이동
                        if n not in visited: # 출발지로 사용하지 않은 노드만 사용
                            que.append((n, n_val * val))
                            visited.add(n)
                else: result.append(-1.0) # b에 도달 못 함
        else: result.append(-1.0)
    return result