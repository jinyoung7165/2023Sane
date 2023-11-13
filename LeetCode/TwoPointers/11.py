# Container with most water
# 투포인터
# n개의 높이 주어짐()
# two lines 물을 머금을 수 있는 기둥 두 개 지정(각 기둥의 너비 고려x)
# 최대 물 양?
# 최대 높이 기둥, 적당한 높이인데 너비가 크면 넓이 최대일 수도 있음
# leftmax, rightmax 중 작은 애만 높이에 쓰임 -> 둘 중 작은 기둥이 최대가 되게 이동
# cap = max(cap, min(leftmax, rightmax) * (right - left))
def maxArea(height) -> int:
    cap = 0
    left, right = 0, len(height)-1
    leftmax, rightmax = height[left], height[right]
    while left < right:
        # 큰 기둥은 가만히 있고(넓이에 아직 변화 못 줌), 작은 기둥을 더 키우기 위해 이동
        if leftmax < rightmax:
            cap = max(cap, leftmax * (right-left))
            left += 1
            leftmax = max(leftmax, height[left])
        else:
            cap = max(cap, rightmax * (right-left))
            right -= 1
            rightmax = max(rightmax, height[right])
    return cap