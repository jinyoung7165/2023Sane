# 앱
# 앱 활성화: 메인 메모리에 직전 상태 기록돼 있는 것
# 비활성화: 활성화 앱 중 몇 개 선택해 메모리에서 삭제
# 비활성화 후 재실행 시 시간 더 필요
# 활성화 된 앱이 각각 특정 바이트씩 메모리 사용
# 비활성화 후, 재실행 시 추가 비용 C
# 새로운 앱 B를 실행하고자 해, 추가로 M바이트 필요
# 비활성화 시, 비용 C합 최소화 해 M바이트 확보하는 방법
# dp[i][j]: i까지 봤을 때, j원 썼을 때 만들 수 있는 최대 memo
n, m = map(int, input().split())
memos = list(map(int, input().split())) # 차지 중인 메모리 바이트
costs = list(map(int, input().split())) # 비활성화 시 드는 비용
graph = []
M = float('inf')
answer = M
s = sum(costs)
dp = [[0]*(s+1) for _ in range(n+1)]

for i in range(1, n+1):
    memo = memos[i-1]
    cost = costs[i-1]
    # dp[i][cost] = memo
    # cost가 0일 때도 있음
    for j in range(s+1): # 이전에 쓴 비용으로 만든 memo 보고, 현재 j원 썼을 때 만들 수 있는 memo 갱신
        # cost가 커서 이전 누적+현재앱 사용으로 j원 만들 수 없을 때. 이전 누적값만 사용
        if j < cost:
            dp[i][j] = dp[i-1][j]
        # 같은 비용(j) 내에서 이전 누적+현재앱 사용, 현재 앱 사용x memo 비교
        else: #  dp[i][cost] = memo+dp[i-1][0](0) 또는 이전 누적 dp[i-1][cost]
            dp[i][j] = max(memo+dp[i-1][j-cost], dp[i-1][j])
        if dp[i][j] >= m: # m이상의 메모리 확보 시
            answer = min(answer, j)
print(answer)