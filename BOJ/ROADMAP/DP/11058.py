# 크리보드
'''
1. a 화면에 추가
2. 화면 전체 선택
3. 선택을 버퍼에 복사
4. 화면에 버퍼 내용 추가(버퍼가 비어있지 않으면)
버튼 총 N번 눌러서 화면에 출력된 a 최대 개수

dp[i]: i초에 screen의 a 최대 개수
clip 계속 유지될 수도, screen을 복붙해 커질 수도 있음
유효 3 <= clip <= screen -> 1초후에 screen에 더해지거나, 3초후 screen이 2배가 되거나
clip이 0->3이 된 후, 복붙은 적어도 dp[7]부터 영향을 미침
i-2, i-1, i, i+1, i+2, i+3 있을 때
screen[i-2]>clip[i-2]에서 시작.
1) i-2에서 복붙 시작 -> i+3에서 4*screen[i-2]
2) i-1에서 복붙 시작 -> i+3에서 3*screen[i-1]
3) i에서 복붙 시작 -> i+3에서 2*screen[i]
'''
from sys import stdin
input = stdin.readline
n = int(input())
dp = [i for i in range(n+1)] # clip=0일 때 i초 screen의 값

for i in range(4, n-2):
    dp[i+3] = max(dp[i]*2, dp[i-1]*3, dp[i-2]*4)

print(dp[n])