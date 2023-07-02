# 파일 합치기
# 각 ch를 다른 파일에 저장
# 모두 쓰거, 각 파일 합쳐 1 파일로 만듦
# 두 파일 합쳐 하나의 tmp파일 만들고, 이것과 원래의 파일 합펴
# ch가 "연속이 되도록" 합쳐 나감
# 두 파일 합칠 때 필요한 비용이 두 파일 크기 합
# 최종 1파일 완성 시 필요한 비용 총 합
# c1,c2,c3,c4
# 40,30,30,50
# 30 30 40 50
# x1=c2+c3 =60(최소 두 개 합)
# x2=c1+x2 =100(거기다 최소 누적)
# x3=c4+x2 =150(거기다 최소 누적)
# 60+100+150 = 310
# 만약, (c1+c2)+(c3+c4)=70+80+150=300(최소+최대. 최소+최대)
# dp[i][j]: i~j 합 최댓값
# dp[i][i]: gap0 -> 비용 0 주의!!(압축 안 함)
# dp[i][i+1]: gap1 원소끼리 합
# dp[i][i+k]: gapk 뭉탱이끼리 합+해당 범위 n합(sum(i~j) = sum(0~j)-sum(0~i-1))
# dp[i][j] = min(dp[i][mid] + dp[mid+1][j] + (subSum[j]-subSum[i-1]) for mid in range(i, j))
'''
gap=1
(1,2), (2,3), (3,4)
1번~2번파일 비용=(1~1의 비용(0) + 2~2의 비용(0)) + (1~2까지 누적합(70)) = 70
2번~3번파일 비용=(2~2의 비용(0) + 3~3의 비용(0)) + (2~3까지 누적합(60)) = 60
3번~4번파일 비용=(3~3의 비용(0) + 4~4의 비용(0)) + (3~4까지 누적합(80)) = 80
gap=2
(1 + 2,3), (1,2 + 3), (2, + 3,4), (2,3 + 4)
1번~3번파일 비용= min(
    1~1의 비용(0) + 2~3의 비용(60).
    1~2의 비용(70) + 3~3의 비용(0)) 
+ (1~3까지의 누적합(100)) = 160

2번~4번파일 비용= min(
    2~2의 비용(0) + 3~4의 비용(80).
    2~3의 비용(60) + 4~4의 비용(0)) 
+ (2~4까지의 누적합(110)) = 170
'''
from sys import stdin
input = stdin.readline
M = float('inf')
tc = int(input())
for _ in range(tc):
    k = int(input()) # ch개수
    sizes = list(map(int, input().split())) # 각 ch 크기
    dp = [[0]*k for _ in range(k)]
    
    seq_sum = {-1: 0} # 부분연속합(0~idx까지 sizes 합)
    for idx in range(k):
        seq_sum[idx] = seq_sum[idx-1] + sizes[idx]
        
    for gap in range(1, k): # gap 1~k-1
        for i in range(k-gap): # gap1일 때 0~k-2을 출발점으로. gap=k-1일 때 0출발점
            j = i+gap
            result = M
            for mid in range(i, j):
                # (gap1)j=i+1일 때, mid=i일 경우 1번. dp[i][i]=dp[i+1][i+1]=0, sum(i~i+1)=n[i]+n[i+1]
                result = min(result, dp[i][mid]+dp[mid+1][j])
            dp[i][j] = result + (seq_sum[j]-seq_sum[i-1])
    print(dp[0][k-1])