# n*n 배열 쥬어짐 -> 1차원 배열 만들고자 함
# i=1,...n에 대해 대각선 (1,1) -> (i,i) 모든 빈칸을 숫자 i로 채움
# 모든 행 잘라내 이어붙인 1차원 배열 arr 생성
# arr[left], arr[left+1], ..., arr[right] 만 남기고 나머지 지움
'''
123 
223 
333 
'''
def solution(n, left, right):
    answer = []
    for idx in range(left, right+1):
        r = idx // n + 1
        c = idx % n + 1
        if r >= c:
            answer.append(r)
        else:
            answer.append(c)
    return answer
'''
클 때 작을 때 append 틀 동일 -> max로 해결 가능
'''
def solution(n, left, right):
    answer = []
    for idx in range(left, right+1):
        answer.append(max(idx // n, idx % n) + 1)
    return answer
print(solution(3,2,5))
print(solution(4,7,14))
