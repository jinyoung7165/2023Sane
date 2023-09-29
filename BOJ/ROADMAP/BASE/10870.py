# 피보나치 수 5
# 0과 1로 시작. 
# n번째 피보나치 수를 구하라
# n은 20보다 작은 자연수
n = int(input())
fibo = [0] * (n+1)
if n > 0: fibo[1] = 1
def func(num):
    if num < 2 or fibo[num]: return fibo[num]
    fibo[num] = func(num-1) + func(num-2)
    return fibo[num]

print(func(n))