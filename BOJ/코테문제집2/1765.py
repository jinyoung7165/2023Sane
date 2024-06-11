# 닭싸움 팀 정하기
'''
1. 친구의 인접 친구들도 친구
2. 원수의 인접 원수들은 친구
친구면, 같은 팀에 속해야 하며
같은 팀에 속한 사람들끼리 모두 친구여야 함
최대한 많은 팀 만들어라
친구끼리 무조건 합쳐져야 함 -> union find
완성 후, parents 찾으러 감-> not visited면 +1씩
'''
from sys import stdin
input = stdin.readline
n = int(input())
m = int(input())
enemies = [[] for _ in range(n+1)]
parents = [i for i in range(n+1)]
def find_parents(a):
    if parents[a] != a:
        parents[a] = find_parents(parents[a])
    return parents[a]

def union(a, b):
    pa, pb = find_parents(a), find_parents(b)
    if pa == pb: return False
    if pa < pb: parents[pb] = pa
    else: parents[pa] = pb
    return True

for _ in range(m):
    rel, a, b = input().split()
    a, b = int(a), int(b)
    if rel == 'F': # union
        union(a, b)
    else: # a<->b
        enemies[a].append(b)
        enemies[b].append(a)

for i in range(1, n+1):
    if len(enemies[i]) > 1:  # 적의 적끼리 친구
        for j in range(1, len(enemies[i])):
            union(enemies[i][j-1], enemies[i][j])
answer = 0
for i in range(1, n+1):
    if parents[i] == i: answer += 1 # 루트 수만 셈
        
print(answer)