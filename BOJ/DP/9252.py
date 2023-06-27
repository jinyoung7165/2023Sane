# LCS 2
# 최장 공통 부분 수열
# ACAYKP & CAPCAK -> ACAK
# LCS의 길이와 LCS 출력하라
# 현재 꺼를 lcs에 붙이거나, 붙이지 않거나
# 이전에 기록한 오른쪽/아래(공통 발생시 기록한 대각선)에서 탐색
'''
['', '', '',    '',    '', '', '', ''] (a의 A보고 아랫줄에 기록)
['', '',  'A',  'A',   'A',  'A',   'A'] (a의 AC봄. 아랫줄에 기록)
['', 'C', 'C',  'C',   'AC', 'AC',  'AC'] (a의 ACA봄. 아랫줄에 기록)
['', 'C', 'CA', 'CA',  'CA', 'ACA', 'ACA'] (a의 ACAY봄. 아랫줄에 기록)
['', 'C', 'CA', 'CA',  'CA', 'ACA', 'ACA'] (a의 ACAYK봄. 아랫줄에 기록)
['', 'C', 'CA', 'CA',  'CA', 'ACA', 'ACAK'] (a의 ACAYKP봄. 아랫줄에 기록)
['', 'C', 'CA', 'CAP', 'CAP','CAP', 'ACAK']
'''
a = input().rstrip()
b = input().rstrip()

size1, size2 = len(a), len(b)
dp = [['']*(size2+1) for _ in range(size1+1)]

for i in range(size1):
    for j in range(size2):
        if a[i] == b[j]: # LCS 대각선으로 채워나감
            dp[i+1][j+1] = dp[i][j] + a[i]
        else: # 공통 원소가 아니면, 주변(아래/오른쪽)에서 탐색
            if len(dp[i+1][j]) >= len(dp[i][j+1]):
                dp[i+1][j+1] = dp[i+1][j]
            else:
                dp[i+1][j+1] = dp[i][j+1]
result = dp[size1][size2]
print(len(result))
if result: print(result)