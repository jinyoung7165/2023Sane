# LCS
# 최장 공통 부분 수열
# 두 수열 주어짐. 모두의 부분 수열이 되는 수열 중 가장 긴 것
# ACAYKP , CAPCAK => ACAK
# 최대 1000글자
# dp[i]: i번째 글자까지 봤을 때 최대 길이
# dp[i] = i번째 글짜 포함 시 st2의 idx or 이전 최대 길이
from sys import stdin
input = stdin.readline

st1 = input().strip()
st2 = input().strip()

size1 = len(st1)
size2 = len(st2)
# 테이블 (i, j)까지 봤을 때 최장 공통 수열 길이
dp = [[0] * (size2+1) for _ in range(size1+1)]

# 같은 알파벳 찾으면 -> 오른쪽, 아래로 확장
for i in range(size1):
    for j in range(size2):
        if st2[j] == st1[i]:
            dp[i+1][j+1] = dp[i][j] + 1 # 해당 위치 다음 행열에 영향
        else: # 누적값 -> 오른쪽, 아래로 적용. xfound시 이전에 누적한 아래, 또는 오른쪽의 영향 받음
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
print(dp[size1][size2])