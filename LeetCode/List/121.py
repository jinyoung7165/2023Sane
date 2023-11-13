# Best Time to Buy and Sell Stock
# 주식 사고 팔기
# min일 때 사고, max일 때 팔기
def maxProfit(prices) -> int:
    answer = 0
    m, M = float('inf'), 0
    for pri in prices:
        if pri < m:
            m = pri
            M = 0
        elif pri > M:
            M = pri
            answer = max(answer, M - m)
    return answer