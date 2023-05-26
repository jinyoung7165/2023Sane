# NQueen
# n이 주어졌을 때, n*n판에 퀸을 놓는 방법의 수
# 다른 행, 열, 대각선에 n개의 퀸 놓아야 함
n = int(input())
answer = 0

pos = [0] * n # n개의 Queen의 자리. 더 효율 좋음
# pos[i] = j : 해당 퀸을 (i,j)에 놓겠다
visited = [False] * n # col에 대한 방문 처리

def check(row): # 이전 행에 둔 queen들과 비교
    for i in range(row): # (0~row-1) 이전 행에 둔 위치 확인
        if pos[row] == pos[i] or \
            abs(pos[row] - pos[i]) == row - i: # 같은 열에 뒀거나, 대각선일 때 false
                return False
    return True

def dfs(row):
    global answer
    if row == n: # n행까지 왔으면 이미 n개의 퀸 다 둔 것
        answer += 1
        return
    for col in range(n):
        # 해당 행의 col열에 퀸을 놓겠다.
        if visited[col]: continue # 이전 행에서 해당 열 방문함
        pos[row] = col
        # 이전 행에 둔 queen들과 비교
        if check(row): # 이 열에 둘 수 있음
            visited[col] = True # 해당 열 방문 처리
            dfs(row+1)
            visited[col] = False # 끝까지 갔거나, nqueen불가해서 return->해당 열 방문 취소

dfs(0) # 첫 번째 행부터 두자
print(answer)

def dfs(row, visit):
    global answer
    if row == n: # 마지막 행까지 다 놓은 것
        answer += 1
        return
    for i in range(n): # 해당 행의 각 열
        flag = True
        for l_row, l_col in enumerate(visit):
            if l_col==i or row - l_row == abs(i - l_col):
                flag = False
                break
        if flag: # 해당 열에 놓을 수 있음
            dfs(row+1, visit+[i])

dfs(0, [])  # 첫번째 행부터 queen두자