# 명함의 가로 세로 길이가 주어짐 -> 눕혀서 수납 가능
# 모두 수납할 수 있는 최소 크기의 직사각형 만들어라
# [[60, 50], [30, 70], [60, 30], [80, 40]]-> 4000(80*50)
def solution(sizes):
    max1, max2 = -1, -1
    for x, y in sizes:
        if y > x: x = y # x쪽에 항상 큰 수 오게
        if x > max1:
            max1 = x
        if y > max2:
            max2 = y
    return max1 * max2

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)