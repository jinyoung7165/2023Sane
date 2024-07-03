# 스티커 붙이기
'''
모눈종이에 주어진 모양의 스티커(한 스티커의 각 칸들 연결됨) 붙일 것

1.스티커 주어진 순서대로, 회전시키지 않고, 떼어냄
2.다른 스티커와 겹치거나, 전체 크기범위 벗어나지 않으며 스티커 붙일 위치 찾음
가장 작은 r -> 여러 개면, 가장 작은 c 위치 선택
3. 붙임. 만약 붙일 위치 없었다면, 시계방향 90도 회전후 2번 반복
4. 270도까지 회전해봤는데 위치 없다면, 스티커 버림

다 붙이고, 모눈에 몇 개의 칸 채워졌는지
'''
from sys import stdin
input = stdin.readline

n, m, k = map(int, input().split())
stickers = []
for _ in range(k):
    r, c = map(int, input().split())
    stickers.append([list(map(int, input().split())) for _ in range(r)])

def rotate(sticker):
    return list(zip(*sticker[::-1]))

board = [[0]*m for _ in range(n)]

def put(sticker):
    r, c = len(sticker), len(sticker[0])
    for sx in range(n-r+1):
        for sy in range(m-c+1):
            if compare(sx, sy, r, c, sticker):
                # 해당 시작점부터 붙여도 될 때,
                for x in range(r):
                    for y in range(c): # 모양 맞춰 붙이기 (1인 부분만 1이됨)
                        board[x+sx][y+sy] += sticker[x][y]
                return True
    return False
                        
def compare(sx, sy, r, c, sticker):
    for x in range(r):
        for y in range(c): # sticker 존재하는 부분의 board가 이미 1이면 못 붙임
            if sticker[x][y] == board[x+sx][y+sy] == 1: return False
    return True
       
    
for s in range(k):
    sticker = stickers[s]
    for _ in range(4):
        if put(sticker):
            break # 붙였을 때, 다음 스티커 탐색
        sticker = rotate(sticker)

answer = sum(map(sum, board))

print(answer)