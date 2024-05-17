# 하늘에서 별똥별이 빗발친다
'''
떨어지는 별 수 최소화
l*l 트램펄린 - 최대한 많은 별을 튕겨냄
몇 개의 별이 떨어지는지
떨어지는 별의 위치는 다르며, 트램펄린의 모서리에 맞아도 튕겨나감

별의 맵 칠했다 가정 -> 트램펄린의 좌표 (0,0)부터 시작해서 범위 내의 별 수 count
=> 시간 초과 남

전체 맵의 크기 말고,
별 기준으로 생각
해당 별의 좌표 기준 l크기 내로, 다른 별 count

해당 x,y 을 l*l 종이 위
(0,0),(l,l),(0,l),(l,0) 중 어디에 맞출지에 따라 cnt 달라짐

하지만, (x,y)를 꼭짓점 말고도, 모서리에 두는 경우에도 최적의 cnt 나올 수 있음
최적의 정사각형이 시작되는 꼭짓점 찾기 위해, 두 점 기준으로 minx, miny 구해서
해당 꼭짓점 기준으로 count
'''
from sys import stdin
input = stdin.readline

n,m,l,k = map(int, input().split())
# 별 구역의 가로, 세로, 트램펄린 길이, 별의 수
answer = 0
pos = [list(map(int, input().split())) for _ in range(k)]

for ax, ay in pos:
    for bx, by in pos:
        cnt = 0
        mx, my = min(ax, bx), min(ay, by)
        # 두 점을 포함하는 정사각형의 최적 꼭짓점 찾음
        for x, y in pos:
            if mx<=x<=mx+l and my<=y<=my+l:
                cnt += 1
        if cnt > answer: answer = cnt
        
print(k-answer)