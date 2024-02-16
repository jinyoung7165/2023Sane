# 숫자 맞추기
'''
회전 가능한 나사 n개 아래로 연결됨(나사 이름 1~n)
각 나사: [0...9] 적혀 있음
하나를 왼쪽으로 돌리면, 아래의 모든 나사 같이 회전
하나를 오른쪽으로 돌리면, 다른 나사는 회전x
위에서 아래로 특정 col 숫자 읽어나갈 때, 가장 적은 움직임으로 원하는 숫자 만들고, 각 위치의 이동 횟수 구하라
현재 상태 주어짐 326 -> 원하는 수 448
각 나사별 필요한 최소 회전 칸 수 출력
왼쪽으로 돌릴 수도 있고(위에서부터 쭉 누적), 오른쪽으로 돌릴 수도 있음. Greedy아님-> bruteforce시 recursionError

뒤에서 누적 결과 볼 때, 누적 위치 중요하지 않음. 누적 횟수만 알면 -> target 수를 만들기 위한 최소 횟수 구할 수 있음
0~i-1까지 왼쪽 누적합: x
현재 위치: (원래 수+x) % 10 = 0~9 (10개 경우의 수)
dp[i][x]: i번째 숫자까지 왼쪽 누적 횟수가 x일 때, target을 만드는 데 필요한 최소 횟수
가장 마지막부터 Top-down 메모이제이션 방식으로 최솟값 찾아감
'''
from sys import stdin
input = stdin.readline
n = int(input())
cur = list(map(int, input().strip()))
target = list(map(int, input().strip()))

dp = [[0]*10 for _ in range(n+1)] # i번째 나사까지 왼쪽으로 j번 돌렸을 때(10 이상일 땐, 나머지로 표현됨), target값 만들기 위한 최소 횟수
path = [[0]*10 for _ in range(n+1)] # 각 경우 left/right 몇 칸씩 선택했는지 기록
for i in range(n-1, -1, -1): # (n-1~i)맨 아래 나사부터
    for j in range(10): # 0~i까지 왼쪽 누적합 j
        # 현재 위치의 수: cur[i]+j
        rleft= (target[i] - cur[i] - j) % 10
        rright = 10-rleft
        # 0~i번째까지 왼쪽 j누적 시, n-1까지 총 회전 수: dp[i][j] 
        # = i위치에서 회전 방향 선택 + [i+1~n-1위치의 왼쪽 누적이 ?일 때, 총 회전 수 재활용]
        # left 선택 -> rleft번 + [i+1~n-1][왼쪽 누적 (j + rleft)]
        # right 선택 -> rright번 + [i+1~n-1][왼쪽 누적 (j)]
        left, right = rleft + dp[i+1][(j+rleft)%10], rright + dp[i+1][j]
        if left < right: dp[i][j], path[i][j] = left, rleft
        else: dp[i][j], path[i][j] = right, -rright

print(dp[0][0]) # 최종 상태: 0번째 왼쪽 0번 누적 결과(초기), n-1번째까지 총 회전 수 [0][0]

j = 0 # 0~i번째까지 왼쪽 누적합 j
for i in range(n):
    cost = path[i][j] # 왼쪽으로 돌린 경우, path값 >= 0
    print(i+1, cost)
    if cost > 0: # 왼쪽 누적합 커지면
        j = (cost + j) % 10