'''
월드컵
6개국. 
각 조별로 동일 조에 소속된 국가와 한번씩
각 국가당 총 5번 경기 치름
조별 리그 끝난 후, 각 나라의 승,무승부,패 가능한 결과인지 판별
네 가지 결과 주어질 때 각 결과에 대해 가능하면 1, 불가능하면 0 출력
승 무 패 승 무 패...
각 줄씩 가능한 건지 판단
5 0 0 3 0 2 2 0 3 0 0 5 4 0 1 1 0 4
4 1 0 3 0 2 4 1 0 1 1 3 0 0 5 1 1 3
5 0 0 4 0 1 2 2 1 2 0 3 1 0 4 0 0 5
5 0 0 3 1 1 2 1 2 2 0 3 0 0 5 1 0 4
->
1 1 0 0
총 5+4+3+2+1 번(15. 6C2)의 경기
'''
from itertools import combinations
from sys import stdin

input = stdin.readline

result = []
allcomb = ((0,2), (1,1), (2,0)) # 1씩 뺄 승무패의 idx(0,1,2)
rounds = list(combinations(range(6), 2)) # 15번의 경기
def dfs(idx):
    global flag
    if flag == 1: return # 이미 가능한 조합이 나왔으면 그만
    # allcomb의 0,1,2 나올 수 있음
    if idx == 15:
        flag = 1
        for r in res: # 모든 팀의 승무패
            if r.count(0) != 3: # 모두 0이 아니면
                flag = 0
                break # 0인채 끝남
        return # 1인채 끝나면 
    
    a, b = rounds[idx] # 팀1, 팀2 번호
    for ares, bres in allcomb: # 결과 더할 idx
        if res[a][ares] > 0 and res[b][bres] > 0: # 빠른 검증 가능
            res[a][ares] -= 1
            res[b][bres] -= 1
            dfs(idx+1)
            res[a][ares] += 1
            res[b][bres] += 1

for _ in range(4):
    flag = 0 # 일단 아니라고 둔 다음에. 
    tmp = list(map(int, input().split()))
    res = [tmp[i:i+3] for i in range(0, 16, 3)]
    dfs(0)
    result.append(flag)
    
print(*result)