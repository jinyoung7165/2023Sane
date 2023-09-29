# 자연수 p, q 있을 때, p를 q로 나눴을 때 나머지 0이면 q는 p의 약수
# 6의 약수는 1,2,3,6 총 4개
# 두 자연수 n, k 주어졌을 때 n 약수 중 k번째로 작은 수
n, k = map(int, input().split())
# k번째 약수 존재x시, 0 출력
result = 0
tmp = 1 # 1번째 약수
while tmp <= n:
    if n % tmp == 0:
        k -= 1 # 약수 하나 찾음
        if k == 0:
            result = tmp
            break
    tmp += 1
print(result)