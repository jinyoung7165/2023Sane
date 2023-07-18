# k칸 앞 점프 or 이동거리*2 좌표 순간이동
# k칸 앞 점프 시 건전지 k만큼 줄어듦 -> 순간이동 더 효율적
# 이동하려는 거리 n주어졌을 때, 사용해야 하는 건전지 사용량 최솟값 return
# 거리 5만큼 떨어진 장소
# 0->1칸 점프 -> (2로 순간이동 -> 4로 순간이동) -> 1칸 점프(건전지 -2) -> 답
 
# 거리 6만큼 떨어진 장소
# 0->1칸 점프 -> 2로 순간이동 -> 2->3 1칸 점프 -> 6으로 순간이동(건전지 -2)

# dp[i]: i까지 오기 위한 최소 비용. [i//2] or [i-1]
# 2로 나눠떨어지면 -> i//2 시 비용과 같음 dp[2] = 1
# 나눠떨어지지X -> i//2시 비용 + i%2(1)
def solution(n):
    ans = 0
    while n > 0: # 0일 때 비용 0, 1, 2일 때 비용 1
        ans += n%2 # 홀수면 1 건전지 써야 순간이동 가능
        n //= 2 # 몫 홀수인지 짝수인지 또 확인 필요
    return ans
# print(solution(1)) # 1
# print(solution(2)) # 1
# print(solution(5)) # 2
print(solution(6)) # 2
# print(solution(5000)) # 5

'''
    MAX = float('inf')
    dp = [MAX]*(n+1)
    if n > 1: dp[2] = 1
    dp[0], dp[1]= 0, 1
    for i in range(3, n+1):
        if i%2 == 0:
            dp[i] = min(dp[i-1]+1, dp[i//2])
        else:
            dp[i] = dp[i-1]+1
    ans = dp[n]

'''