# n = 2^a*3^b*5^c*7^d*11^e
# n주어질 때, abcde 출력하라
# n>=2
tc = int(input())

dic = [11, 7, 5, 3, 2] # 11부터 순회하며 n의 약수인지 확인
for _ in range(1, tc+1):
    n = int(input()) # n줄 입력 받을 것
    result = [0] * 5
    for j in range(5):
        num = dic[j]
        cnt = 0
        while n % num == 0: # 배수일 때 계속 나눔
            n //= num
            cnt += 1
        if cnt: result[4-j] = cnt

    print('#'+str(_), *result)