# 오일러 회로
# 한 점 출발. "모든 간선 지나되, 한번 지난 간선 재방문x"
# 출발점으로 돌아와야 함. 양방향 그래프
# 경로를 출력하라
# 정점 개수 n(1~1000)
# n노드에 대한 인접 행렬(노드 간 간선 수 0~10) 주어짐
# 두 정점 사이 여러 간선 존재 가능
# 그래프는 모두 연결돼 있고, 루프는 없음(자기 자신)
# 시작점 위치 상관 없이 한 경로만 출력. 불가능한 경우 -1 출력
# 한붓그리기 가능, 모든 정점 간선 개수가 짝수여야 가능
# 무방향/양방향 그래프에서 오일러 판단
# 시작점, 도착점 제외 나머지 정점의 차수가 짝수(오일러 경로)
# 모든 정점의 차수가 짝수(오일러 회로)
# 유향 그래프에서 오일러 판단
# 시작점, 도착점 제외 나머지 정점의 indegree, outdegree 일치(오일러 경로)
# 모든 정점의 indegree, outdegree 일치(오일러 회로)
# 아무 정점에서 자신으로 돌아오는 경로(ABCDA)탐색 후,
# 방문하지 않은 간선이 존재하는 정점 C에서 다시 C로 돌아오는 경로 탐색(CEFC)
# 이른 원래 경로에 끼워넣으면 ABCEFCDA 완성
# dfs 시간 초과 -> bfs로 풀어야 함
# from sys import stdin, setrecursionlimit, exit
# from collections import defaultdict
# setrecursionlimit(10**6)
# input = stdin.readline
# n = int(input()) # 노드 수
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
#     if sum(graph[i])%2:
#         print(-1)
#         exit()
# edges = 0
# for i in range(n-1):
#     for j in range(i+1, n):
#         edges += graph[i][j]
    
# def dfs(cur:int, path:list):
#     path.append(cur+1)
    
#     if cur == 0 and len(path) == edges+1:
#         return True

#     for can, edge in enumerate(graph[cur]):
#         if edge > 0:
#             graph[cur][can] -= 1
#             graph[can][cur] -= 1
#             if not dfs(can, path):
#                 graph[cur][can] += 1
#                 graph[can][cur] += 1
#                 path.pop()
#             else: return True
#     return False
# path = []
# if dfs(0, path):
#     print(*path)
# else:
#     print(-1)
# 여행경로 문제와 유사. 근데 시간초과 때문에 재귀함수x
# start 아무데서나. 간선 존재 시 계속 이동하다가
# 그 노드에서 확장 불가 시 리프 노드로 간주하고 path에 삽입
# 이전 노드로 돌아가(dfs 마냥). 확장하다가 리프 만나면 삽입
# 모든 간선 다 썼을 때 오일러 회로임
# 출력 시 거꾸로
from sys import stdin
input = stdin.readline
from collections import defaultdict

def find_path(graph, start):
    path = []
    stack = [start]

    while stack:
        cur = stack[-1]
        if graph[cur]: # 간선 존재
            node = next(iter(graph[cur])) # 다음 노드
            graph[cur][node] -= 1
            graph[node][cur] -= 1

            if graph[cur][node] == 0: # 두 노드 사이 간선 없음
                del graph[cur][node]
                del graph[node][cur]
            stack.append(node) # 다음 노드로 이동
        else: # 현재 노드 cur에는 간선 없음. 확장 불가(리프 노드 간주)
            path.append(stack.pop())
    return path[::-1]

def main():
    n = int(input())
    degrees = [0] * n # 각 노드가 가진 간선 수
    graph = [defaultdict(int) for _ in range(n)] # i->j 간선 수

    for i in range(n):
        for j, cnt in enumerate(list(map(int, input().strip().split()))):
            if cnt:
                graph[i][j] = cnt
                degrees[i] += cnt

    # 양방향 오일러 회로를 위해선, 모든 정점의 간선 수가 짝수여야 함
    if any(degree % 2 != 0 for degree in degrees):
        print(-1)
        return

    path = find_path(graph, 0) # 노드 0부터 출발
    if len(path) != sum(degrees) // 2 + 1: # 노드 수: 간선 수+1이어야 다 순회한 것
        print(-1)
    else: # 모두 순회함
        print(*[v+1 for v in path])

if __name__ == "__main__":
    main()