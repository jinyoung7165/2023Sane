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