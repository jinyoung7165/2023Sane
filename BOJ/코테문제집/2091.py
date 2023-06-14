# 동전 여러 개 중 몇 개 처분
# 1원 a개, 5원 b개, 10원 c개, 25원 d개 가짐
# x원 사려 할 때, 동전 개수를 "최대로" 하려 함
# 각 단위 동전 개수 모두 출력하라(불가능해서 모두 0이어도)
# 최대한 작은 단위 많이 쓰되, 목표 금액 만들 수 있어야 함.
# 12 5 3 1 2 -> 1*2 + 5*2
# 16 0 0 0 1 -> 불가
# 시간 여유로운데, 메모리 빡빡함
# dp->탐색 공간 크기 줄여 시/공간 효율성 높음
# dp[i][j] = i원일때 최대의 동전수를 사용했다고 가정하면, 이때 j 동전의 개수
# dp[i][4]: 전체 동전의 개수
# 1원 사용해서 k원 만들려고 하면, k-1원 보면 됨
# k-1원 만든 동전 개수 > 현재 k원 만든 동전 수보다 많으면 갱신&1원 개수 줄임
# dp[k] = dp[k-coins[j]] + 1
def dp_solve(): # 따봉 지피티야 고마워
    x, *cnts = map(int, input().split())
    coins = [1, 5, 10, 25]
    dp = [[-1]*5 for _ in range(x+1)] # k원 만들기 위해 필요한 각 동전 수
    for i in range(5):
        dp[0][i] = 0 # 0원 못 만든다
        
    for i in range(1, x + 1): # 1~x원 만들자
        for j in range(4): # 작은 단위 동전부터 사용\
            if i < coins[j]: # 단위 코인보다 작으면 볼 필요x
                continue
            # 해당 coin 하나 쓴다고 치면, 
            # 현재 금액보다 나머지 금액(i-coins[j])을 만들기 위한 동전 수가 더 많이 기록돼 있을 때
            if dp[i-coins[j]][4] > dp[i][4]:
                # i-coins[j]원 만든 후, 해당 coin 남아 있는지 확인(처음 주어진 coin[j] 개수와 비교)
                if cnts[j] > dp[i-coins[j]][j]:
                    # 해당 coin 하나 쓸 수 있음 -> i-coins[j] 원 만들었던 동전 개수에 coins[j]원 1개 추가
                    for k in range(4):
                        dp[i][k] = dp[i-coins[j]][k]
                    dp[i][j] += 1
                    dp[i][4] = dp[i-coins[j]][4] + 1 # 전체 동전 수 갱신
    
    if dp[x][4] > 0:        
        for i in range(4):
            print(dp[x][i], end=" ")        
    else:
        print("0 0 0 0")

def short(): # 간단하게 작성
    X, *MAX_COIN = map(int, input().split())
    DP = [[0] * 4 for _ in range(X + 1)]
    coin = [1, 5, 10, 25]

    for c in range(4):
        if coin[c] <= X and MAX_COIN[c]:
            DP[coin[c]][c] += 1 # 단위 coin 금액을 만들기 위한 coin각 1종류만 사용

    for i in range(1, X): # 1~x원 만들기
        if not sum(DP[i]): # 해당 금액을 만들기 위한 이전의 단위 조합 기록 없으면, 못 만드는 금액
            continue
        # 단위 coin 역순으로 사용하며 갱신(단위 작아질수록 총 coin개수 늘어남)
        for c in range(3, -1, -1):
            # i원과 단위coin조합 시 목표 금액보다 작으면 기록
            # i원을 만들 때 들어간 해당coin 수와 처음에 주어진 개수 비교 -> 남아있어야 함
            # i원 만들 때 들어간 전체 coin수보다 현재 갱신돼 있는 coin수보다 클 때 해당 coin으로 조합 가능(25원과 조합했을 때 개수<10원<5원<1원)
            if i + coin[c] <= X and DP[i][c] < MAX_COIN[c] and sum(DP[i + coin[c]]) < sum(DP[i]) + 1:
                DP[i + coin[c]] = list(DP[i]) # i원에 들어간 조합 일단 대입
                DP[i + coin[c]][c] += 1 # coin[c] 하나 쓸 거니까 증가

    print(*DP[-1])

# dfs -> 시간 초과
# coins = [1, 5, 10, 25]
# x, a, b, c, d = map(int, input().split())
# result = coin_combination(x, coins, [a, b, c, d])
# print(*result if result else "0000")

# coins = [1, 5, 10, 25]
# result = []
# def dfs(idx, cnt, left, path):
#     global result
#     if left == 0:
#         return True
#     elif idx==4:
#         return False
#     elif result:
#         return True
#     unit, _cnt = coins[idx], li[idx]
#     if not result:
#         for i in range(_cnt, -1, -1): # 작은 단위의 동전 최대한 많이 쓰기
#             if unit*i <= left:
#                 path.append(i)
#                 if dfs(idx+1, cnt+i, left-unit*i, path):
#                     if not result:
#                         result = path
#                     return True
#                 path.pop()
#     return False

# x, a, b, c, d = map(int, input().split())
# li = [a, b, c, d]
             
# if dfs(0, 0, x, []):
#     for i in range(4-len(result)):
#         result.append(0)

# print(*result if result else "0000")