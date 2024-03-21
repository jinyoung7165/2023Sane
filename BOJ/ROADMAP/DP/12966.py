# ACKA
'''
dp[0] = [0]까지 필요한 곡수에 맞게 할당했을 때, 경우의 수 
combinations 쓰면 안됨. 각 곡에 1곡 이상씩은 할당돼야 하기 때문에 확인하는 작업 필요
s는 최대 50. a, b, c는 1~s 범위 -> dfs로 직접 조합해라
dp[i][j][k][l]: i번째 곡을 어떤 사람들의 조합으로 골라서 그들의 선택 각각 (j, k, l)남은 상황
i곡을 누가 골랐는지 기록해야 함 + 그들의 선택 각각 몇 개 남았는지 봐야 하기때문에 4차원 배열
'''
from sys import stdin

input = stdin.readline

s, a, b, c = map(int, input().split())
dp = [[[[-1]*(c+1) for _ in range(b+1)] for _ in range(a+1)] for _ in range(s)]

# i번째 곡을 어떤 사람들의 조합으로 골라서 그들의 선택 각각 (j, k, l)남은 상황
def dfs(i, j, k, l): # i+1번째 곡도 어떤 사람들의 조합으로 구할 것 -> 해당 경우의 수가 이전 실행에 더해짐
    if i == s: # 다 골랐음
        if j == 0 and k == 0 and l == 0: return 1 # 모두 소진 시 성공
        return 0
    if j < 0 or k < 0 or l < 0: return 0 # 잘못 골랐음
    
    # i번째 곡까지 또 다른 조합으로 왔는데, 결과적으로 같은 j, k, l이 남았을 수 있음 -> 이후 결과 동일
    if dp[i][j][k][l] != -1: return dp[i][j][k][l]
    dp[i][j][k][l] = 0
    # i번째 곡 부를 사람의 조합 구함
    for js in range(2): # 첫 번째 사람이 고르거나 말거나
        for ks in range(2): # 두 번째 사람이 고르거나 말거나
            for ls in range(2):
                if js == 0 and ks == 0 and ls == 0: continue # 모두 안 고르는 경우는 없음
                dp[i][j][k][l] += dfs(i+1, j-js, k-ks, l-ls)
    dp[i][j][k][l] %= 1000000007
    return dp[i][j][k][l]
    
if a+b+c >= s: print(dfs(0, a, b, c))
else: print(0)