# 동전 분배
'''
동전을 똑같이 둘로 나눠 가져
n종류 동전을 몇 개씩 -> 돈을 반으로 나눌 수 있는지 없는지
500원짜리 1, 50원짜리 1 주어지면 불가능 0 출력
'''
# ?원 만들 수 있는지
# 역순으로 금액 구성해야 중복x
# 해당 동전을 써서 나온 결과에, 같은 동전 중복하면 안됨
# 50원짜리 3개 존재 [50,100,150] 각각을 겹치지 않게, 이전에 나온 값들에 더해야 함
# 150부터 더하고, 150이 방문한 곳을 100은 방문하면 안됨
# 150 1, 50 3개 있어서 150*1, 50*3이 300 만들어놨으면, 100은 300 방문하면 안됨
# 하지만, 각 coin의 개수별 * 만들고자 하는 금액 전체
# 순회 시, 시간 초과 -> 만들고자 하는 금액 별 각 coin 봐야 함
'''
money k, k-1,... k-p원 순회한다고 가정
1) money= k일 때, dp[k] 없고,
2) dp[k-coin] 있으면 dp[k], dp[k+coin], dp[k+coin*2]원 생성 가능

1) money= k일 때, dp[k] 있으면 pass
if dp[k]원이 coin 말고, coin2으로 인해 채워졌다고 하면, dp[k+coin], dp[k+coin*2]원 true로 만드는 기회 놓치는 거 아닌가?
아님. k원 오기 전에 money=k+coin원일 때,
coin2에 의해 dp[k]원 존재하므로, dp[k+coin], dp[k+coin*2]를 이때 이미 채우고 오늘 길이라서 pass해도 됨
'''
from sys import stdin
input = stdin.readline

for _ in range(3):
    n = int(input()) # 종류
    s = 0
    coins = []
    for _ in range(n):
        val, cnt = map(int, input().split())
        coins.append((val, cnt))
        s += val*cnt
    # i번째 동전 j개 썼을 때 나올 수 있는 결과들
    # s//2 나오면 stop
    if s%2: print(0) # 나눠 떨어지지 않음
    else:
        target = s//2
        dp = [False]*(target+1)
        dp[0] = True
        # ?원 만들 수 있는지
        # 역순으로 금액 구성해야 중복x
        for i in range(n):
            coin, cnt = coins[i]
            for money in range(target, coin-1, -1):
                # coin 1개 이상 사용해서
                # target 금액까지 만들 수 있는지 역순
                # 이미 존재하는 money-coin에 + coin*(1~cnt)원 더해서
                # money~money+coin*(cnt-1)원 만들 수 있음
                if dp[money]:
                    continue
                if dp[money-coin]: # money원 만들기 위해 money-coin, coin원 쓸 것
                    for j in range(cnt):
                        if money + coin*j <= target:
                            dp[money + coin*j] = True # coin 1개 이상이면 더 만들 수 있음
            if dp[target]:
                print(1)
                break
        else: print(0)