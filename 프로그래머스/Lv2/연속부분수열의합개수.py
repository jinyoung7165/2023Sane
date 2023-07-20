# (자연수) 원형 수열(처음과 끝 연결) 연속하는
# 부분 수열의 합 몇 가지
# [7,9,1,1,4]
'''
길이 1인 연속 부분 수열로부터 [1, 4, 7, 9] 네 가지의 합
길이 2인 연속 부분 수열로부터 [2, 5, 10, 11, 16] 다섯 가지의 합
길이 3인 연속 부분 수열로부터 [6, 11, 12, 17, 20] 다섯 가지의 합
길이 4인 연속 부분 수열로부터 [13, 15, 18, 21] 네 가지의 합
길이 5인 연속 부분 수열로부터 [22] 한 가지의 합
중복되는 값을 제외하 18가지의 수
[1,2,4,5,6,7,9,10,11,12,13,15,16,17,18,20,21,22]
'''
from collections import deque
def solution(elements):
    answer = set()
    size = len(elements)
    que = deque([0]*size)
    for i in range(size): # 1~len길이의 수열 만들기
        for j in range(size):
            cur = que.popleft()
            last = elements[(j+i)%size]
            answer.add(last+cur)
            que.append(last+cur)
            if i==size-1 and j==0: break
    return len(answer)
print(solution([7,9,1,1,4]))

'''


'''
def solution2(elements):
    answer = set()
    size = len(elements)
    for i in range(size):
        ssum = elements[i] # 해당원소가 들어간 모든 수열의 합
        answer.add(ssum) # 길이 1인 수열
        for j in range(i+1, i+size):
            # i원소는 i+1번째 원소에부터 더해져야 함(size-1번)(자신빼고)
            ssum += elements[j%size]
            answer.add(ssum)
    return len(answer)

print(solution2([7,9,1,1,4]))