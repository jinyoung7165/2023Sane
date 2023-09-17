'''
정수 n. 밑변의 깉이와 높이가 n인 삼각형에서 맨 위부터 반시계 방향으로 달팽이 채우기 진행
첫 행부터 마지막 모두 순서대로 합친 새 배열 return
n=4
1 (1개)-> 1
2 9 (2개)-> 11
3 10 8 (3개) 11+10
4 5 6 7 (4개) 11+11

n=5
1 -> 1
2 12 (2개) 14
3 13 11 (3개) 14+13
4 14 15 10 (4개) 14+14+14+1
5 6 7 8 9 (5개) 14+14+7

n=6
1(0)
2(1) 15
3(2) 16 14
4(3) 17 21 13
5(4) 18 19 20 12
6(5) 7 8 9 10 11
'''
# row+1, row, row-1 반복
# 1 0 -1
def solution(n):
    rows = [[0 for _ in range(1, i+1)] for i in range(1, n+1)]
    num = 1
    x, y = -1, 0 # 좌표. 처음 시작은 +1이므로 -1 넣어줌
    # 방향: 하, 우, 상 반복
    for i in range(n): # 방향
        for _ in range(i, n): # 그 방향 동안 들어갈 개수: 1씩 줄어듦
            if i % 3 == 0: # 아래로
                x += 1
            elif i % 3 == 1: # 오른쪽으로
                y += 1
            else: # 위로
                x -= 1
                y -= 1
            rows[x][y] = num
            num += 1
    return sum(rows, []) # 2차원->1차원 배열

print(solution(4))
print(solution(5))
print(solution(6))

# graph 탐색 방식
def solution(n):
    dx=[0,1,-1];dy=[1,0,-1]
    b=[[0]*i for i in range(1,n+1)]
    x,y=0,0
    num=1
    d=0
    while num<=(n+1)*n//2:
        b[y][x]=num
        ny=y+dy[d];nx=x+dx[d]
        num+=1
        if 0<=ny<n and 0<=nx<=ny and b[ny][nx]==0:
            y, x = ny, nx
        else:d=(d+1)%3;y+=dy[d];x+=dx[d]
    return sum(b,[])
