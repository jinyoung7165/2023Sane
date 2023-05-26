# 2xn 타일링
# 2*n크기 직사각형을 1*2, 2*1 타일로 채우는 방법의 수
# % 10007 해서 출력
# 2*1인 경우, 1 (세로1)
# 2*2인 경우, 2 (세로2 or 가로1)
# 2*3인 경우, 3 (세로3 or 2 * 가로1+세로1)
# 2*4인 경우, 5 (세로4 or 가로2 or 3 * 가로1+세로2)
# 2*5인 경우, 8 (세로5 or 3 * 가로2+세로1 or 4* 가로1+세로3)
# 2*6인 경우, 13(세로6 or 가로3 or 6 * 가로2+세로2+ 5*가로1+세로4)
n = int(input())
dp = [0, 1, 2]
if n < 3:
    print(dp[n])
else:
    a, b = dp[1], dp[2]
    cur = 0
    for i in range(3, n+1):
        cur = a + b
        a, b = b, cur
    print(cur%10007)
    
n = int(input())
dp = [0, 1, 2]
if n < 3:
    print(dp[n])
else:
    for i in range(3, n+1):
        dp.append(dp[i-2] + dp[i-1])
    print(dp[n]%10007)