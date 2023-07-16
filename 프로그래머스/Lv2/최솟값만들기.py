# 길이 같 배열 a, b
# 각 배열 자연수로 이뤄짐
# a, b에서 1숫자씩 뽑아 곱함
# 배열 길이만큼 반복 -> 곱 결과 누적해 더함
# 최종 누적값이 최소가 되도록

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    while A:
        answer += B.pop() * A.pop()
    return answer