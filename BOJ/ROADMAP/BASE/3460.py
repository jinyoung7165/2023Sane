# 양의 정수 n 주어졌을 때, 이진수로 나타냈을 때 1의 위치 모두 찾아
# 최하위 비트 위치는 0

t = int(input())
for _ in range(t):
    answer = []
    n = int(input())
    b = bin(n)[2:][::-1]
    for i, _ in enumerate(b):
        if _ == '1':
            answer.append(i)
    print(*answer)


def convert(num):
    tmp = ''
    while num:
        tmp = str(num % 2) + tmp # 이전 결과 앞에 붙임!!
        num //= 2
    return tmp
print(convert(13))