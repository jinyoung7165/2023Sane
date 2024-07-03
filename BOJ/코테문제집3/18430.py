# 무기 공학
'''
재료 n*m 직사각형. 각 칸의 힘 다름
이를 잘라서, 여러 개의 ㄱ모양(2*2중 한칸 뺌) 만들려함
ㄱ모양의 중심(두 칸과 인접)칸은 힘 2배
전체 직사각형를 여러 ㄱ으로 분해했을 때, 강도의 합 최대
특정 칸은 사용하지 않아도됨
'''
from sys import stdin
input = stdin.readline
dirs = [(0,1),(1,0),(0,-1),(-1,0)] # 우상좌하
# 날개는 0-1, 0-3, 2-1, 2-3 시도
n, m = map(int, input().split()) # 최대 5*5
board = [list(map(int, input().split())) for _ in range(n)]
answer = 0

def check(nx, ny):
    if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
        return True
    return False

def visit(x, y, dlist):
    wings = []
    for d in dlist:
        dx, dy = dirs[d]
        nx, ny = x+dx, y+dy
        if not check(nx, ny): break
        wings.append((nx, ny))
    else: # 날개 둘다 방문 가능
        return wings
    return [] # ㄱ 실패      
    
def dfs(x, y, visited, count):
    global answer
    if y >= m:
        dfs(x+1, 0, visited, count)
        return
    elif x >= n:
        if answer < count:
            answer = count
        return
    if not visited[x][y]: # 날개 살피기
        visited[x][y] = True # 중심부
        cnt = board[x][y]*2
        for dlist in [(0,1),(0,3),(2,1),(2,3)]:
            wings = visit(x, y, dlist)
            if wings:
                for nx, ny in wings:
                    visited[nx][ny] = True
                    cnt += board[nx][ny]
                dfs(x, y+1, visited, count+cnt)
                for nx, ny in wings:
                    visited[nx][ny] = False
                    cnt -= board[nx][ny]
        visited[x][y] = False
    dfs(x, y+1, visited, count)
    
if n==1 or m==1: print(0) # ㄱ만들 수 없는 경우
else:
    visited = [[0]*m for _  in range(n)]
    dfs(0, 0, visited, 0)
    print(answer)