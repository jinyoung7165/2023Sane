# 중앙이 노란색, 테두리가 갈색으로 색칠된 격자
# 10, 2 -> [4,3]
# 1 1 1 1
# 1 0 0 1
# 1 1 1 1
# 두 색 격자의 수 주어질 때, 카펫의 가로, 세로 크기는?
# 가로 >= 세로
# 전체 = yellow + brown = w*h
# yellow = (w-2)*(h-2)
# brown = 전체 - yellow
def solution(brown, yellow):
    answer = []
    s = brown + yellow # 전체 면적
    for width in range(s, 1, -1): # 9*1 -> width가 s일 수 있음
        if s % width: continue # 나눠 떨어지지 않을 때
        height = s//width
        temp_yell = (width-2)*(height-2)
        if temp_yell == yellow and s-temp_yell == brown:
            answer.append(width, height)
            break
    return answer