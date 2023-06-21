# 스티커
# 문방구에서 스티커 2n개 구매
# 스티커 떼면, 변을 공유하는 스티커 모두 사용 불가
# 상하좌우
# 각 스티커에 점수 매기고, 점수 합이 최대가 되게 떼려 함
# 뗄 수 있는 스티커의 점수 최댓값
# 점수 합 최대가 되며, 서로 변 공유하지 않는(상하좌우x) 스티커 집합
# 현재 col의 row=0 떼면,
# 다음 col의 row=1 떼고, 그 다음 col의 row=0
# 그다음 col의 row=1 떼기
# from sys import stdin
# input = stdin.readline

# tc = int(input())
# for _ in range(tc):
#     result = 0
#     n = int(input())
#     dp = [] # dp[i][j]: icol의 jrow 뗐을 때 누적 최댓값
#     stickers = [list(map(int, input().split())) for _ in range(2)]
    
#     dp.append([stickers[0][0],  stickers[1][0]])
#     if n > 1:
#         dp.append([stickers[1][0]+stickers[0][1], stickers[0][0]+stickers[1][1]])

#     for i in range(2, n):
#         dp.append([max(stickers[0][i]+dp[i-1][1], stickers[0][i]+dp[i-2][1]), max(stickers[1][i]+dp[i-1][0], stickers[1][i]+dp[i-2][0])])
    
#     print(max(max(dp[n-1]), max((dp[n-2])))) if n>1 else print(max(dp[n-1]))

# 주어진 배열과 col 수 같음
# dp 따로 만들 필요업음
from sys import stdin
input = stdin.readline

tc = int(input())
for _ in range(tc):
    n = int(input())
    # stickers[0][i]: icol의 0row 뗐을 때 누적 최댓값
    stickers = [list(map(int, input().split())) for _ in range(2)]
    
    if n > 1:
        stickers[0][1] += stickers[1][0]
        stickers[1][1] += stickers[0][0]

    for i in range(2, n):
        stickers[0][i] += max(stickers[1][i-1], stickers[1][i-2])
        stickers[1][i] += max(stickers[0][i-1], stickers[0][i-2])
    
    print(max(stickers[0][n-1], stickers[1][n-1]))