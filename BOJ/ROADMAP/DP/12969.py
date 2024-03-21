# ABC
'''
ABC 중 하나 두면서 남은 K쌍 수 감소
C: 자기 왼쪽의 A, B 셈
B: 자기 왼쪽의 A 셈
오른쪽으로 순회하면서 왼쪽의 결과 재활용 가능
이미 나온 루틴 (a 몇 개, b 몇 개, c 몇 개인데 s도 같으면 다음 경로도 같을 거임)
dp[n**2][n][n][n] 이 dp[n][n][n][n**2] 보다 나음
'''
from sys import stdin

input = stdin.readline

n, k = map(int, input().split())
result = []
visited = set()
def dfs(i, s, a, b, c):
    if (s, a, b, c) in visited: return False
    if s > k: return False
    visited.add((s, a, b, c))
    if i == n:
        if s == k: return True
        return False
    
    # A 놨음
    if dfs(i+1, s, a+1, b, c):
        result.append('A')
        return True
    
    # B 놨음
    if dfs(i+1, s+a, a, b+1, c):
        result.append('B')
        return True
    
    # C 놨음
    if dfs(i+1, s+a+b, a, b, c+1):
        result.append('C')
        return True
    
    return False

dfs(0, 0, 0, 0, 0)
print(''.join(result[::-1]) if result else -1)