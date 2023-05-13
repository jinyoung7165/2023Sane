# 원하는 길이의 A로만 이뤄져 있음
# 위 -> 다음 알파벳 (Z->A)
# 아래 -> 이전 알파벳 (A->Z)
# 왼 -> 커서 왼쪽으로 이동. (<-___)
# 오른 -> 커서 오른쪽으로 이동
# 위*9 ->J (0위치의 A->J)
# 왼*1 -> (0위치 이전: 맨마지막 문자)
# 아래*1 -> (마지막 문자 A->Z)
# 만들고자 하는 문자 주어질 때, 몇 번의 연산?
# ord(문자) -> ASCII
# chr(숫자) -> 문자
# jb-n-n -> a 방문해도 되고, 안해도 되지만 최소 걸음이어야 함
# 0 [1,n-1]
from collections import defaultdict
leri = float('inf')
def solution(name):
    graph = defaultdict(list)
    size = len(name)
    init = 'A' * size
    updown = 0
    for i in range(size):
        updown += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        graph[i].append((i+1)%size)
        graph[i].append((i-1)%size)
    
    def dfs(v, path, count):
        global leri
        if count >= leri: return # 최솟값 못내는 경로
    
        path = list(path)
        path[v] = 'A'
        
        if ''.join(path) == init: 
            leri = min(leri, count) # NAME ->'AAAA'이면 더 이상 방문X
            return
        
        for u in graph[v]:
            dfs(u, ''.join(path), count+1)
    dfs(0, name, 0)
    answer = updown+leri
    return answer
#print(solution("JEROEN")) # 56
#print(solution("JAZ")) # 11
#print(solution("JAN")) # 23

# 다른 사람의 시간 효율적 코드
def solution(name):
    answer = 0
    n = len(name)

    def alphabet_to_num(char):
        num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
        return num_char[ord(char) - ord('A')]

    for ch in name:
        answer += alphabet_to_num(ch)

    move = n - 1
    for idx in range(n):
        next_idx = idx + 1
        while (next_idx < n) and (name[next_idx] == 'A'):
            next_idx += 1
        distance = min(idx, n - next_idx)
        move = min(move, idx + n - next_idx + distance)

    answer += move
    return answer