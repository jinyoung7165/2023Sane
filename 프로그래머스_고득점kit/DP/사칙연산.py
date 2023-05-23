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
# DP: 완전탐색에서 발생하는 중복 요소 제거->소요 시간 확실히 줄이는 방법
# 숫자의 위치는 바뀌면 안되고, 연산의 순서만 바뀔 수 있음
# 자기자신만 연산했을 때 최댓값은 자신 -> 최대를 저장하는 DP
# 자기자신 오른쪽(연산자 바로 옆)과 연산했을 때 최댓값은 그 결과
# 뺄셈의 최댓값: 가장 큰 값에서 가장 작은 값 뺐을 때 최대 -> 최소를 저장하는 DP
# MAX_DP[i][j] = i번째 부터 j번째까지 구간의 연산의 최댓값
# MIN_DP[i][j] = i번째 부터 j번째까지 구간의 연산의 최솟값
# 단, DP는 이차원 배열, 각 차원의 길이는 숫자의 개수만큼임.
# DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k] + MAX_DP[k+1][j])
def solution(arr:list):
    answer = None
    size = len(arr)
    op_size = size // 2
    nums, op = [], [] # if op 0, 1, 2 -> num은 (0,1),(1,2),(2,3)
    idx = []
    total_op = set() # 0~op_size 까지 조합 나열
    for i in range(size):
        if i % 2 == 0: nums.append(int(arr[i]))
        else:
            if arr[i] == '+': op.append(1)
            else:
                op.append(-1)
                idx.append(len(op)-1) # op에서 -나오는 위치 기억
    
    # op[minus]=-1 -> op[minus+1]~op[op_size-1]에 -1 적용
    for minus in idx: # - 나오는 위치
        left = op[:minus+1] # 현재 -1포함. 뒤에 - 적용 어디까지 할지 결정
        for swap in range(op_size-minus): # 나머지 op 개수: op개수-minus나온 위치-1. swap:0~나머지op개수만큼
            target = op[minus+1:minus+swap+1] # 연산자 부호 전환 적용할 대상
            right = op[minus+swap+1:] # 그대로 append
            tmp = []
            for tar in target:
                tmp.append(-tar)
            tmp.extend(right)
            total_op.add(tuple(left+tmp))
    
    for ops in total_op:
        n = nums[0]
        for i in range(op_size):
            n += ops[i]*nums[i+1]
        if not answer:
            answer = n
        elif answer < n: # 최댓값 갱신
            answer = n
        
    if not answer: answer = sum(nums) # 모두 +
    
    return answer

print(solution(["1","-","1","-","1","-","1","+","1","-","1"]))
print(solution( ["5", "-", "10", "+", "1", "+", "2", "-", "4"]))

# def solution(arr:list):
#     INF = float('inf')
#     n = # 숫자 개수
#     MIN_DP = [[INF for _ in range(n)] for _ in range(n)]
#     MAX_DP = [[-INF for _ in range(n)] for _ in range(n)]
    
#     for step in range(len(DP)): # i와 j의 간격
#         for i in range(len(DP)-step): # i~j까지의 연산 수행
#             j = 1+step
#             if step == 0:
#                 DP[i][j] = # 해당 숫자
#             else:
#                 for k in range(i, j):
#                     if k번째 연산자 == '+':
#                         MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k] + MAX_DP[k+1][j]) # + 일 경우 최댓값은 최댓값 + 최댓값임.
#                         MIN_DP[i][j] = min(MIN_DP[i][j], MIN_DP[i][k] + MIN_DP[k+1][j]) # + 일 경우 최솟값은 최솟값 + 최솟값임.
#                     else: #k번째에 해당되는 연산이 - 일 경우.
#                         MAX_DP[i][j] = max(MAX_DP[i][j], MAX_DP[i][k] - MIN_DP[k+1][j]) # - 일 경우 최댓값은 최댓값 - 최솟값임.
#                         MIN_DP[i][j] = min(MIN_DP[i][j], MIN_DP[i][k] - MAX_DP[k+1][j])# - 일 경우 최솟값은 최솟값 - 최댓값임.
#     return MAX_DP[0][n-1]