tc = int(input())
for _ in range(1, tc + 1):
    n, a, b = map(int, input().split()) # n, a, b
    m = float('inf')
    for i in range(1, n+1):
        j = 1
        while i*j <= n:
            m = min(m, a*abs(i-j)+b*(n-i*j))  # 최솟값
            j += 1

    print("#" + str(_), m)