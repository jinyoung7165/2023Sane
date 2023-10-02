# 빗물
'''
최대 크기 500*500 map
빌딩 높이 주어짐. 바닥 항상 막혀 있음
고이는 빗물 총량
높이 탐색 x 0 좌표부터 시작.
투포인터 범위 좁혀가며 해당 범위 내 만나는 벽 leftmax, rightmax 높이 구함
'''
n, m = map(int, input().split())
buildings = list(map(int, input().split()))

answer = 0
l, r = 0, m-1
leftmax, rightmax = buildings[l], buildings[r]
# l, r 현재 위치 움직이며 만나는 가장 높은 벽 leftmax, rightmax에 저장
# 현재 위치 기준 <- -> 두 방향에서 가장 높은 두 벽의 높이 찾아야 하기 때문
while l < r:
    # 현재 위치 높이가 더 크면, 큰 기둥 높이 갱신
    # 두 기둥 사이에서, 더 낮은 쪽 - 현재 위치만큼 빗물 저장 가능
    # 중간 높이들만큼 minus, 두 기둥 중 작은 기둥만큼 plus
    # 투 포인터 -> 더 낮은 위치의 포인터부터 이동시켜 시간 복잡도 O(n)으로
    leftmax, rightmax = max(leftmax, buildings[l]), max(rightmax, buildings[r])
    if leftmax < rightmax:
        answer += leftmax - buildings[l]
        l += 1
    else:
        answer += rightmax - buildings[r]
        r -= 1
    
print(answer)