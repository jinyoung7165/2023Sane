'''
소수
자연수 M과 N이 주어질 때, M이상, N이하 자연수 중 소수인 것 모두 골라
소수 합과 최솟값
M=60, N=100 -> 60 이상 100 이하 자연수 중 소수는 61, 67, 71, 73.. 97
소수 합 620, 최솟값 61
'''
def isPrime(num):
    if num == 1: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

m = int(input())
n = int(input())

answer = []
for i in range(m, n+1):
    if isPrime(i): answer.append(i)

if not answer: print(-1)
else:
    print(sum(answer))
    print(answer[0])