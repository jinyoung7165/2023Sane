# 마을의 모든 집 둥글게 배치
# 서로 인접한 집 -> 방범장치 연결
# 인접한 두 집 털면 경보가 울림
# 각 집 money 배열 주어질 때, 훔칠 수 있는 돈 최대?
# [1,2,3,1] -> 4
# dp[i][j] = max(현재집+dp[i-2][j], dp[i-1][j]) : i번집까지 봤을 때 최댓값
# 원형-> 첫번째 집-마지막 집 무조건 연결돼 있어서 둘 중 하나만 털어야 함

def solution(money:list):
    size = len(money) # 0~size-1
    dp1 = [0]*(size-1) # 첫 번째 집 무조건 터는 경우
    dp2 = [0]*size # 마지막 집 무조건 터는 경우
    dp1[0] = money[0] # 무조건 털어서 나온 이익
    dp1[1] = max(money[0], money[1]) # 둘 중 최대만 털자
    dp2[0] = 0 # 털지 않음
    dp2[1] = money[1] # money[0] 선택 불가
    for i in range(2, size-1): # 마지막 집 포함x
        dp1[i] = max(money[i]+dp1[i-2], dp1[i-1])
    for i in range(2, size): #
        dp2[i] = max(money[i]+dp2[i-2], dp2[i-1])
    answer = max(dp1.pop(), dp2.pop())
    return answer
print(solution([2,1,1,1])) # 3
print(solution([2,1,1,5])) # 7말고, 6
print(solution([1,2,3,1])) # 4
print(solution([100,3,3,100,8,100, 0])) # 300이 나와야 함
