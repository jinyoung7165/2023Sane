# 일정 피로도 이용해 던전 탐험
# 각 던전마다 필요한 준비물 최소 피로도, 종료시 소모 피로도
# 던전을 최대한 여러 개 탐험하려고 함 -> 최대 던전 수
# 최소 필요 >= 소모 피로도
# 80, [[80,20],[50,40],[30,10]] -> 3(1->3->2 순 탐색)
# 최장 경로 -> heapq 생각 버리자!!! DFS
'''DFS'''
answer = 0 # global answer!!!!!
def solution(k: int, dungeons: list):
    global answer
    dfs(k, [], dungeons) # 남은 기력, 경로, 던전
    return answer

def dfs(k: int, visited: list, dungeons: list):
    global answer
    idx = 0
    for require, consume in dungeons:
        if idx not in visited and require <= k:
            dfs(k-consume, visited + [idx], dungeons)
        idx += 1
    answer = max(answer, len(visited))
    
print(solution(80, [[80,20],[50,40],[30,10]]))

'''
남의 dfs 코드. CNT 넘겨줌&방문 취소 직접 대입
'''
answer = 0
N = 0
visited = []

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1 # 방문 표시
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0 # 방문 취소

def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer

'''BFS 코드'''
from collections import deque

def bfs(start, k, dungeons): # 시작노드, 남은 기력, 던전 정보
    counted = []
    
    que = deque([])
    que.append([start, k, 0, [False for _ in range(len(dungeons))]])
    # 노드, 남은 기력, 거친 던전 수, 방문 기록
    while que:
        cur, left, count, visited = que.popleft()
        visited[cur] = True
        left -= dungeons[cur][1]
        count += 1
        counted.append(count)
        
        for i in range(len(dungeons)):
            if not visited[i] and left >= dungeons[i][0]:
                que.append([i, left, count, visited[:]])
    return max(counted) # 그 중 max 리턴

def solution(k, dungeons):
    answer = -1
    for i in range(len(dungeons)):
        if dungeons[i][0] <= k: # 출발지 입력
            answer = max(answer, bfs(i, k, dungeons))
    return answer

'''
Greedy + Brute Force
'''
from itertools import permutations
def solution(k, dungeons):
    length = len(dungeons)
    idx_arr = [i for i in range(length)]
    for i in range(length, 0, -1): # 최대 던전 개수부터 내림차순으로 탐색
        for cases in permutations(idx_arr, i):
            left = k # 기력
            check = True
            for case in cases:
                if left < dungeons[case][0]: # 필요한 기력보다 없으면 못 가
                    check = False
                    break
                else:
                    left -= dungeons[case][1] # 갈 수 있어서 기력 소모
            if check: return i # 최대 탐색 개수