# 괄호 추가하기 3
'''
길이 n인 수식. 0~9정수, x+- 로 이뤄짐
x를 먼저, +,- 나중에
왼쪽부터 계산
중첩된 괄호 사용 가능
결과의 최댓값 구하라
괄호 개수 제한x. 추가하지 않아도 됨

-붙으면 min <-> max
MAX_DP[i][j] = i~j번째까지 구간의 연산의 최댓값
MIN_DP[i][j] = i~j번째까지 구간의 연산의 최솟값
덧셈일 때 MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k] + MAX_DP[k+1][j])
뺄셈일 때 MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k] - MIN_DP[k+1][j])
뺄셈일 때, MIN_DP[i][j] = min(MIN_DP[i][j], MIN_DP[i][k] - MAX_DP[k+1][j])
하지만, 곱셈일 때는 모든 조합을 다 보고 min, max 해야 함
-랑, - 곱하면 + 되기 때문에 max될 수도 있음
-랑, +곱하면 min될 수 있음
'''
from sys import stdin
input = stdin.readline

n = int(input())
express = input().strip()
INF, size = float('inf'), n//2+1
dp_min, dp_max = [[INF]*size for _ in range(size)], [[-INF]*size for _ in range(size)]

for i in range(size):
    dp_min[i][i] = int(express[i*2])
    dp_max[i][i] = int(express[i*2])

for gap in range(1, size):
    for left in range(size-gap):
        right = left+gap
        for k in range(left, right):
            if express[k*2+1] == '*':
                dp_min[left][right] = min(dp_min[left][right],
                                    dp_min[left][k] * dp_min[k + 1][right],
                                    dp_min[left][k] * dp_max[k + 1][right],
                                    dp_max[left][k] * dp_min[k + 1][right],
                                    dp_max[left][k] * dp_max[k + 1][right])
                dp_max[left][right] = max(dp_max[left][right],
                                    dp_min[left][k] * dp_min[k + 1][right],
                                    dp_min[left][k] * dp_max[k + 1][right],
                                    dp_max[left][k] * dp_min[k + 1][right],
                                    dp_max[left][k] * dp_max[k + 1][right])
            elif express[k*2+1] == '+':
                dp_min[left][right] = min(dp_min[left][right],
                                          dp_min[left][k] + dp_min[k + 1][right])
                dp_max[left][right] = max(dp_max[left][right],
                                          dp_max[left][k] + dp_max[k + 1][right])
            else:
                dp_min[left][right] = min(dp_min[left][right],
                                          dp_min[left][k] - dp_max[k + 1][right])
                dp_max[left][right] = max(dp_max[left][right],
                                          dp_max[left][k] - dp_min[k + 1][right])

print(dp_max[0][-1])