# n명 참여 토너먼트
# 1 rnd: 1번↔2번, 3번↔4번, ... , N-1번↔N번
# 2 rnd; 승자 다시 대결, n/2개의 배정
# 처음 라운드에서 A번을 가진 참가자->B번 참가자와 몇 번째 라운드에서 만나는지
# A,B 만날 때까지 항상 이김
# 양수로 만드록, 2로 나눈 몫 동일
def solution(n,a,b):
    rnd = 0
    if a > b: a, b = b, a
    
    while a!=b:
        if a % 2 != 0: a += 1
        if b % 2 != 0: b += 1
        a //= 2
        b //= 2
        rnd += 1
    return rnd


print(solution(4, 1, 2))
print(solution(4, 1, 4))
print(solution(6, 1, 6))
print(solution(12, 1, 8))