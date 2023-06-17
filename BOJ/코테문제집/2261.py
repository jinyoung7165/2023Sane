# 가장 가까운 두 점
# 2차원 평면에 n개 점 주어졌을 때, 이 중 가장 가까운 두 점
# 점은 2~100000개
# 각 좌표 절댓값이 10000을 넘지 않는 정수
# 여러 점이 같은 좌표 가질 수 있음
# 가장 가까운 두 점 거리의 제곱 출력
# 점 2개를 고르는 방법 : n(n-1)/2 ->O(n^2)
# y축과 나란히 직선을 그어 평면을 둘로 나눔
# 모든 점을 x좌표 기준으로 정렬-> n/2, n/2+1점의 x좌표 평균 기준
# 두 점 모두 왼쪽에 속할 경우, 모두 오른쪽에 속할 경우, 서로 다른 쪽에 속할 경우
# 각 경우에 대해 최솟값, 세가지 중 가장 작은게 최종 정답
# x좌표 기준 정렬
# 점들의 중앙값->양분할, 2개까지로 분할되면 점 사이 최소 거리를 찾고,
# 해당 거리보다 x좌표끼리 가까운 것만 후보 점으로 등록
# y좌표 기준으로 정렬하고, y좌표 차이가 최소 거리보다 작은 것들만 대상으로 거리 계산
# 최소 거리를 정해두고, 해당 거리보다 긴 것은 모두 배제하는 가지치기
# x축에 대해 거리->후보 고름->그 중 y축에 대해 거리->최솟값
# 기준선 기준으로 거리가 d이내인 영역에 있는 점들을 후보로 등록
 
from sys import stdin
input = stdin.readline
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
points.sort() # x축 기준 정렬
def dist(p1, p2): # 두 점 사이 계산
    return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

def divide_conquer(start, end):
    if start == end: # 점 하나 남음
        return float('inf')
    if end - start == 1: # 점 2개 남음 -> 거리 구하자
        return dist(points[start], points[end])
    
    # 분할 정복
    mid = (start+end)//2
    # 해당 범위에서 mid-점 사이 최소 거리 구함
    mdist = min(divide_conquer(start, mid), divide_conquer(mid, end))
    # mid기준 mdist보다 작은 x거리를 가진 점들만 남김
    target = []
    for i in range(start, end+1):
        if (points[mid][0]-points[i][0])**2 < mdist:
            target.append(points[i])
    
    # x최소 거리에 대해 살아남은 점들
    # y축 기준 정렬
    target.sort(key=lambda x:x[1])
    # y축 기준으로 후보 점들 사이 거리 비교
    # mdist보다 짧은 거리 내의 y좌표를 가진 점들끼리만 비교해 mdist 갱신
    t_len = len(target)
    for i in range(t_len-1):
        for j in range(i+1, t_len): # i다음부터. 두 점 사이 거리
            if (target[i][1]-target[j][1])**2 < mdist:
                mdist = min(mdist, dist(target[i], target[j]))
            else:
                break
            # 현재 후보 점이 다음 점과 최소 거리보다 멀다면 break
            # 이 처리로 시간 효율 챙김
    return mdist

print(divide_conquer(0, n-1))