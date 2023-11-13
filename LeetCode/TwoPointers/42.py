# Trapping Rain Water
# 빗물 트래핑
# n개의 높이 -> 각 bar의 너비는 1씩 차지
# 비온 후 물을 얼마나 머금을 수 있는지 계산
# 자신 높이보다 크거나 같은 높이 만날 때까지 채울 수 있음
# 그런 높이 못 만나면 넓이에 사용 못함 -> 만날 때까지 이동
# 두 기둥 leftmax, rightmax 중 최소만큼 넓이에 누적시키며 한칸씩 이동
# 최소 기둥을 가진 포인터쪽에서 또다른 기둥(leftmax, rightmax 사이 섹션을 나눌)을 찾으며 이동
# leftmax-> max <-rightmax. (더 낮은 쪽 max-현재 높이)만큼 쌓임
def trap(height) -> int:
    rain = 0
    left, right = 0, len(height)-1
    leftmax, rightmax = height[left], height[right]
    while left < right:
        if leftmax <= rightmax:
            rain += leftmax - height[left]
            left += 1
            leftmax = max(leftmax, height[left])
        else:
            rain += rightmax - height[right]
            right -= 1
            rightmax = max(rightmax, height[right])
    return rain