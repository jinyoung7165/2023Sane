# +는 결합법칙 성립. - 성립x(묶는 순서에 따라 결과 다름)
# 1-5-3은 (1-5)-3=-7 , 1-(5-3)=-1
# 1-3+5-8은 연산 순서에 따라 5가지 결과 나옴 [-15,-5,-5,1,1]
# 그 중 최댓값 1 return
# 1-(3+(5-8)) = 1
# 5-3+1+2-4 -> 5-(3+((1+2)-4)) = 3
# 5-3-1-2-4=
# 앞에 -나오면 -> 뒤의 operand 몇 개까지 - 적용할지.
# 1-(3+5-8)
# 1-3-5-8= -15
# 1-3+5-8= -5
# 1-3-5+8= 1
# 맨 뒤에서부터 연산하며 최대, 최소 갱신. 부호 - 만나면, 최대<->최소
# 최대 = (최대) - (최소)
def solution(arr:list):
    m, M = 0, 0
    s = 0 # 누적sum : +로만 이뤄진 구간
    size = len(arr)
    # 뒤에서부터 봄 => 숫자 - (min=-max) 최종 연산
    # 빼려는 min값을 계속해서 min으로 유지한다음, 마지막에 빼면 됨
    for idx in range(size-1, -1, -1):
        if arr[idx] == '+': # + 뒤에 나온 숫자들 s에 계속 누적
            continue
        elif arr[idx] == '-':
            # M/m = ? - v + s + (M/m: -가 전에도 나왔을 때 기록. 다시 -가 앞에 나오면 M/m 전환)
            # m,M 갱신 위해 누적한 -뒤 (s(+덕에 모인 수) + M/m(이미 - 나왔을 때 구한 수))를 더할지 뺄지 생각해야 함
            # ? - (누적sum+M/m) : - 뒤 전체에 - 적용해 m/M 반전
            # ? - (누적sum) + M/m : - 뒤 +로만 이뤄진 부분에만 - 적용
            # ? - 뺄값 + (누적sum-뺄값+M/m) : - 뒷 수에만 - 적용함
            tmp_m, tmp_M = m, M # 대입해서 변화 생기기 때문에 값만 일단 저장
            minus_v = int(arr[idx+1]) # -바로 뒷 수 하나

            m = min(-s-tmp_M, -s+tmp_m, -2*minus_v+s+tmp_m)
            M = max(-s-tmp_m, -s+tmp_M, -2*minus_v+s+tmp_M)
            s = 0 # 연산자 뒤 누적 sum 초기화. + 나오면 s다시 누적 시작
        else: # + 뒤의 숫자 -> 일단 더해놓고, - 나오면 s 전체에 적용할지 고민하자
            s += int(arr[idx])
    M += s # 맨 앞 숫자 부분까지 더함
    return M
print(solution(["1","-","1","-","1","-","1","+","1","-","1"]))
print(solution( ["5", "-", "10", "+", "1", "+", "2", "-", "4"]))
def solution(arr):
    arrs = ''.join(arr).split('-') # (?)-(?)-(?) -> [(?),(?),(?)]
    val0 = sum(list(map(int, arrs[0].split('+')))) # 첫 번째 뭉탱이의 sum 구함
    if len(arrs) == 1:
        return val0
    # val0 - (?) - (?) ...
    min_val = 0
    max_val = 0
    # 마지막부터 두번째 뭉탱이까지(첫번째는 이미 val0 계산함)
    for arr in arrs[:0:-1]:
        # 각 뭉탱이는 +로만 이뤄져있음
        x = list(map(int, arr.split('+')))
        _min_val = -(sum(x)) # 해당 뭉탱이의 최솟값. +누적합 전체에 - 처리
        _max_val = sum(x[1:]) - x[0] # 해당 뭉탱이의 최댓값. 맨앞 val만 -처리. 그 뒤는 어차피 +로만 이뤄진 양수
        min_val, max_val = min(_min_val + min_val, _min_val - max_val), max(_max_val + max_val, _min_val - min_val)
        # 전체 연산의 뭉탱이에서 앞으로 이동하며 누적 최소, 최댓값 갱신
    return val0 + max_val
# DP: 완전탐색에서 발생하는 중복 요소 제거->소요 시간 확실히 줄이는 방법
# 숫자의 위치는 바뀌면 안되고, 연산의 순서만 바뀔 수 있음
# 자기자신만 연산했을 때 최댓값은 자신 -> 최대를 저장하는 DP
# 자기자신 오른쪽(연산자 바로 옆)과 연산했을 때 최댓값은 그 결과
# 뺄셈의 최댓값: 가장 큰 값에서 가장 작은 값 뺐을 때 최대 -> 최소를 저장하는 DP
# MAX_DP[i][j] = i~j번째까지 구간의 연산의 최댓값
# MIN_DP[i][j] = i~j번째까지 구간의 연산의 최솟값
# 덧셈일 때 MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k] + MAX_DP[k+1][j])
# 뺄셈일 때 MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k] - MIN_DP[k+1][j])

def solution(arr):
    INF = float('inf')
    n = len(arr) // 2 + 1 # 숫자 개수
    # 숫자는 가만히 있고. 둘러싼 범위를 조정하며 최대 최소
    min_dp = [INF for _ in range(n)]
    max_dp = [-INF for _ in range(n)]
    for i in range(n): # 각 숫자.
        # i~i 범위 봤을 때 연산 불가.(피연산자 2개부터 연산 가능)
        # i~i 범위에서 최대/최소는 자기 값 가짐
        min_dp[i][i] = arr[i*2+1]
        max_dp[i][i] = arr[i*2+1]
    for gap in range(1, n): # 일렬의 숫자 배열 ->간격 1~n로 조정
        for left in range(n-gap): # 맨 뒷의 숫자부터 보자
            right = left + gap # gap=1->left=n-2, right=n-1
            for k in range(left, right): # 해당 범위 내 원소 idx
                if arr[k*2+1] == '+':# 해당 범위의 연산자
                    max_dp[left][right] = max(max_dp[left][right], max_dp[left][k]+max_dp[k+1][right])
                    min_dp[left][right] = min(min_dp[left][right], min_dp[left][k]+min_dp[k+1][right])
                elif arr[k*2+1] == '-':# 해당 범위의 연산자
                    max_dp[left][right] = max(max_dp[left][right], max_dp[left][k]-min_dp[k+1][right])
                    min_dp[left][right] = min(min_dp[left][right], min_dp[left][k]-max_dp[k+1][right])
    return max_dp[0][-1] # 첫 번째 숫자~마지막 숫자까지 봤을 때 최대