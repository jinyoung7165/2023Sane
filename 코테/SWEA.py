# 1대 차만 차고에 소유 가능
# n일 동안 각 1명 찾아옴
# n일 중 어떤 날은 손님이 x원 차 팔러옴
# 그 차 받거나, 포기
# 이미 주차장에 차있음 받을 수 없음
# 다른 날은 y월 차 사러 옴
# y원으로 산 차 갖고 있음 팔 수 있다 -> 이익 y원
# 최대이익?
# n=4, [5원 차 팔러, 6원 차 팔러, 5원 차 사러,6원 차 사러]
# 두 대 차 모두 사고 팔 방법x. 첫 날 포기. 둘째 날 사고, 넷째 날 파는 것이 가장 큰 이익(6
# n=1~500
# 각 차 가격 1~20
# 한 번에 한 대의 차만 소유 가능
# n=6, customer=[10, 9, -9, 3, -3, -10] 의 경우 -> 10말고, 9랑 3 선택해야 함
# 차 가격에 대한 제약 조건, 판매 기회 순서 중요 -> bs가 문제의 의도
# bs로 주어진 조건에서 최적의 해를 찾는데 시간 효율적
# 타뷸레이션: 작은 하위 문제로 나누어 테이블 형태로 저장하여 더 큰 문제를 해결하는 DP 기법입니다. 
# 이 코드에서는 판매 가능 기간을 찾아 dp 테이블을 만드는 것이 타뷸레이션 기법을 사용하는 예입니다.
tc = int(input())
for T in range(1, tc+1):
    n = int(input())
    
    maps = []
    for _ in range(n):
        a, b = map(int, input().split())
        # 1 val: 손님이 팜
        # -1 val: 손님이 사
        maps.append(a*b)

    stack = [] # (val, leftIdx, rightIdx)
    dp = [] # 해당 idx를 무조건 산다고 했을 때 누적값, 고려한 rightIdx
    for left in range(n-1):
        a = maps[left]
        if a > 0: # 살 수 있음
            right = left + 1
            while right < n: # 팔 수 있는지
                if maps[right] == -a: # 짝 찾음
                    stack.append((a, left, right))
                    break
                right += 1
                
    for cost, left, right in stack:
        last_cost = -1
        # 내 left 이전의 right. 그 중 max val 가지는 애 찾아서 더해라
        for i in range(len(dp)-1, -1, -1):
            if dp[i][1] < left:
                last_cost = max(dp[i][0], last_cost)
        if last_cost != -1:
            dp.append((cost+last_cost, right))
        else:
            dp.append((cost, right))
    sell = max(dp) if dp else 0
    print("#"+str(T), sell)

# Buy와 Sell을 이용해 차를 사는 경우, 파는 경우 따로 관리
# 각 상황에서 이진탐색으로 서로 짝 지을 수 있는 경우 찾은 뒤 이익 계산
# find_matching_index-> 조건에 맞는 짝 찾기
# 차를 사고 팔 때 이익을 최대화하는 상황 효율적으로 찾아줌
# # BS이용해 차를 사는지에 관계 없이 최고 가치를 찾는 방법

# def find_sell_opportunity(sell_opportunities, cost):
#     low, high = 0, len(sell_opportunities)
#     while low < high:
#         mid = (low + high) // 2
#         if -sell_opportunities[mid] < cost:
#             low = mid + 1
#         else:
#             high = mid
#     return None if low >= len(sell_opportunities) else low

# tc = int(input())
# for T in range(1, tc+1):
#     n = int(input())
#     maps = []
#     for _ in range(n):
#         a, b = map(int, input().split())
#         # 1 val: 손님이 팜
#         # -1 val: 손님이 사
#         maps.append(a*b)
    
#     sell_opportunities = sorted([entry for entry in maps if entry < 0], reverse=True)
#     purchased, profit = set(), 0
    
#     for cost in maps:
#         if cost > 0 and -cost not in purchased:
#             idx = find_sell_opportunity(sell_opportunities, cost)
#             if idx is not None:
#                 profit += cost
#                 purchased.add(-sell_opportunities[idx])
#                 del sell_opportunities[idx]

#     print("#" + str(T), profit)

# # 메모이제이션 : DP에서 동일한 작업을 반복하여 수행하지 않도록 이전에 계산한 값을 캐싱하는 기법
from functools import lru_cache

tc = int(input())
for T in range(1, tc + 1):
    n = int(input())
    maps = []
    for _ in range(n):
        a, b = map(int, input().split())
        # 1 val: 손님이 팜
        # -1 val: 손님이 사
        maps.append(a*b)

    @lru_cache(maxsize=None)
    def max_profit(day, last_bought): # 0번 날부터. -maps[(last_boughtIdx)] 나오면 팔 수 있음
        if day >= n:
            return 0

        buy_profit, no_buy_profit = 0, max_profit(day+1, last_bought) # 해당 날짜의 차를 사면 얻을 이익, 그냥 이전 거를 가지고 있으면 얻을 이익
        cur_cost = maps[day] # 현재 차 가격
    
        if cur_cost > 0 and (last_bought == -1 or cur_cost > -maps[last_bought]): # 사는 경우, 그리고 맨 처음으로 사는 경우거나 현재 가격이 이전에 산 가격보다 크면 살 수 있음 
            for i in range(day + 1, n):
                if maps[i] == -cur_cost: # 현재 가격만큼 팔 수 있는 날 오면
                    buy_profit = max(buy_profit, cur_cost + max_profit(i + 1, -1)) 
                    break

        return max(no_buy_profit, buy_profit)

    print("#" + str(T), max_profit(0, -1))