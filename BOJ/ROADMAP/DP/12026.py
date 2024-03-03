'''
BOJ 거리
1~n(최대 길이 1000)번까지 번호 매겨진 노드 일렬로 놓임. 위에 B/O/J 쓰임
1번은 반드시 B
1 -> N 만나기 위해 점프해 갈 것(번호 증가하는 방향으로만)
K칸만큼 점프할 때 에너지 소모 K**2
B,O,J,B,O... 순으로 밟으며 점프해야 함
N만나기 위한 최소 에너지양 구하라.
.단순히 먼저 나온 bojboj... 아님
n만나지 못하면 -1 출력
dp[i]: i번째 원소를 선택할 때, 이전 순서의 원소까지의 누적합에 더한 최솟값.
가장 가까운 것만 보면 안됨(나랑은 가깝지만, 그 전 원소랑 더 멀어질 수 있음) BOOOOOO..J. 그냥 이중 for문으로 이전 원소 다 봐야 함
내가 B일 때, 이전에 나온 J 뒤져야 함 -> 매번 J인지 비교하지 않고, J만 모아둔 stack 사용하면 시간 복잡도 엄청 감소함
방문 초기화를 float(inf)가 아닌, n**2 + 1로 둘 수 있음
'''
n = int(input())
board = input()

circle = {'B':'J', 'O':'B', 'J':'O'} # 자기 이전에 나왔어야 하는 거
M = float('inf')
dp = [M] * n
dp[0] = 0
for i in range(1, n):
    need = circle[board[i]]
    for j in range(i): # 자기 이전의 원소 볼 것
        if board[j] == need:
            dp[i] = min(dp[i], dp[j]+(i-j)**2)

print(-1 if dp[n-1] == M else dp[n-1])