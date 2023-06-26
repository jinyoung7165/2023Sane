# 미네랄
# 두 사람이 막대기를 서로에게 던지는 방법->누구 소유인지 결정
# 동굴에 미네랄 저장. 던진 막대기가 미네랄 파괴 가능
# R*C동굴. 빈칸/미네랄 칸. 상하좌우 인접한 미네랄 칸은 같은 클러스터
# A는 동굴 왼쪽에. B는 오른쪽에 서 있음
# 턴 번갈아가며 막대 던짐
# 던지기 전, "던질 높이" 정해야 함
# 막대는 수평이루며 날아감->미네랄 만나면 그 칸 미네랄 파괴
# 막대는 그 자리에서 이동 멈춤
# 파괴 이후, 클러스터 분리 가능
# 새로 생성된 클러스터가 떠 있는 경우->바닥에 떨어짐
# 다른 클러스터.땅 만나기 전까지 계속 떨어짐
# 다른 클러스터 위에 떨어질 수 있고, 합쳐지게 됨
# 모든 막대를 던지고 나서 미네랄 모양을 구하라
# .빈칸, x미네랄
# 사방에 연결된 원소 없으면 밑으로 떨어짐
# 파괴된 원소->얘와 연결된 애들을 
'''
......
......
xx....
.xx <-
..xx..
...xx.
....x.

바닥을 만날 때까지 떨어지는게 아니라 원형 유지하며 한칸씩 떨어짐(같은 칸수로)
맞은 친구와 인접한 애들 중 하나라도 땅에 도착하면, 연결된 애들도 1칸씩만 더 떨어지고 끝냄

xx....
._
..xx..    ..xx..
...xx.    xx.xx.
.x..x.    .x..x.
'''

'''
xxxxxx
x        xxxxxx
x<-  x   x    x
xx x x   xx x x
x  x x   x  x x
'''

from sys import stdin, setrecursionlimit
from collections import deque
setrecursionlimit(10**7)
input = stdin.readline
que = deque([])
dirs = [(0,1),(1,0),(0,-1),(-1,0)] # 오, 아래, 왼, 위

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
n = int(input()) # 막대 던진 횟수
heights = list(map(int, input().split())) # 막대 던진 높이(1~r)왼오 번갈아서 던짐

def check(x, y, row, path): # 해당 원소와 이어진 뭉탱이가 공중에 뜨는지
    if x == r-1: # 바닥과 연결
        return True
    for dx, dy in dirs:
        nx, ny = x+dx, y+dy
        if 0<=nx<r and 0<=ny<c and (nx, ny) not in path and graph[nx][ny] == 'x':
            path.add((nx, ny))
            if check(nx, ny, row, path):
                return True
    return False

def destroy(x, y):
    graph[x][y] = '.' # 파괴
    # 인접 원소가 뜨게 되는지 확인
    path_all = set()
    clusters = []
    for dx, dy in dirs:
        path = set()
        nx, ny = x+dx, y+dy
        if 0<=nx<r and 0<=ny<c and (nx, ny) not in path_all and graph[nx][ny] == 'x':
            path.add((nx, ny))
            if not check(nx, ny, x, path): # 공중에 떠버림
                path_all |= path
                clusters.append(sorted(path, key=lambda x:-x[0])) # row 큰 거부터 삽입
    
    for idx, cluster in enumerate(sorted(clusters, reverse=True)): # 각 클러스터 중 row 큰 거부터 아래로
        for path in cluster:
            que.append((path[0], path[1], 0, idx)) # 아래로 움직여야 함

def move():
    bottom = [float("inf")] * 4 # 한 파괴 당 최대 4뭉탱이가 나올 수 있다고 가정
    while que:
        x, y, cnt, idx = que.popleft()
        if cnt > bottom[idx]: # 이미 최대 지나침 -> 내려오지 말고 x표시
            graph[x-1][y] = 'x'
        elif cnt == bottom[idx] or  (x == r - 1 or graph[x + 1][y] == "x"):
            # 현재 뭉탱이의 최대 movecnt 도달하거나, 바닥/미네랄에 닿았을 때
            graph[x][y] = "x"  # 이동 끝
            # 닿았을 때 최소 movecnt 갱신
            bottom[idx] = cnt
        else:  # 아래 한 칸 더 이동
            graph[x][y] = "."
            que.append((x + 1, y, cnt + 1, idx))
            
left = True
for height in heights:
    # 왼->오 혹은 오->왼
    i_range = range(c) if left else range(c-1, -1, -1)
    for i in i_range:
        if graph[r-height][i] == 'x':
            destroy(r-height, i)
            break
    left = not left
    # 인접 미네랄 있으면 하강
    if que:
        move()
            
for i in range(r):
    for j in range(c):
        print(graph[i][j], end='')
    print()