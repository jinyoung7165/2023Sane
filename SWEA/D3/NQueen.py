# 퀸은 같은 행/열/대각선 위 말 공격 가능
# n*n 보드에 n개 퀸을 서로 공격 못하게 놓는 경우의 수?
# 일단 모두 다른 행, 열에 둬야 함
# [i+1][j-1], [i+1][j+1], [i-1][j-1], [i-1][j+1] 비워야 함
# 최장 경로, 모든 경우의 수 -> DFS로 풀자
def dfs(row, path):
    global answer
    if row == n:
        answer += 1
        return
    for col in range(n): # 열 정하기    
        flag = True
        for i in range(len(path)): # 지난 행의 퀸들
            if path[i] == col or abs(path[i]-col) == row-i:
                flag = False
                break # 같은 행/열, 또는 대각선 존재 시, 이 col은 버린다
        if flag: dfs(row+1, path+[col])

tc = int(input())

for T in range(1, tc+1):
    n = int(input())
    answer = 0
    dfs(0, []) # 첫 번째 행부터 queen을 두자
    print("#"+str(T), answer)