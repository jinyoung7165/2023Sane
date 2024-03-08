# 1학년
'''
마지막 두 숫자 사이에 =
나머지 숫자 사이에 + or -
8+3-2-4+8-7-2-4-0+8=8
올바른 등식. 왼쪽부터 계산할 누적 결과 모두 0~20 이어야 함
8+3+2-4-8-7 (불가능)
수열 주어졌을 때, 올바른 등식의 수를 구하라

target만들기 위해 i번째 연산 볼 때, 다음 피연산자 정해져있으므로 i-1번째에 나와야 하는 수들 정해져 있음
backtracking하는 것보다, i-1번째까지 특정 숫자가 몇 번 나왔는지를 사용
dp[i][j]: i번째까지 계산 결과, j(0~20) 나올 경우의 수.
'''
n = int(input()) # 3~100
nums = list(map(int, input().split())) # 각 수는 0~9
dp = [[0]*21 for _ in range(n)] # i번째까지 누적 계산했을 때, j가 나온 경우의 수
# 아무튼 n-1번째 나와야 하는 수는 정해져 있음
dp[0][nums[0]] = 1
for i in range(1, n-1):
    cur = nums[i] # 얘를 이전 결과에 더하거나 뺄 것
    for j in range(21):
        if dp[i-1][j]:
            if j + cur <= 20:
                dp[i][j + cur] += dp[i-1][j]
            if j - cur >= 0:
                dp[i][j - cur] += dp[i-1][j]
print(dp[n-2][nums[-1]])