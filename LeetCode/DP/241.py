# Different Ways to Add Parentheses
'''
괄호 여러 경우로 집어넣어서 output 출력. +-* 만 존재
2-1-1 -> [0,2]
2*3-4*5  -> [-34,-14,-10,-10,10]
식 최대길이 20
숫자 개수 n이라면, op 개수 n-1, 괄호=OP 순서 바꾸는 경우의 수 (n-1)!
1. 이미 계산한 결과 재사용 시 -> DP(더 효율적)
2. 결과 재사용하지 않고 범위 쪼개기만 할 것 -> Divide and Conquer(재귀 느림)
'''
# 1. DP. Tabulation 상향식. 작은 것부터 해결해서 재사용하며 합침
# i~j 작은 gap부터 dp[i][j][k] * op범위 -> 3중 list를 op범위만큼 돌리기 때문에, 5중 for문이 나옴
'''
2-1-1-1이면, 숫자[0~3], op[0~2] 존재.
결과[0~3][0]: 결과[0~0], 결과[1~3]를 op[0]으로 계산한 결과"들"
결과[0~3][1]: 결과[0~1], 결과[2~3]를 op[1]로 계산한 결과"들"
결과[0~3][2]: 결과[0~2], 결과[3~3]를 op[2]로 계산한 결과"들"
: 결과[i][j:i+1~op][k:i~j-1]= 결과[i][k] , 결과[k+1][j]를 op[k]로 계산 

결과[0~0]: 숫자 시작==끝이면, 숫자[0]
결과[0~1][0]: 숫자[0], 숫자[1]을 op[0]으로 계산
'''
def diffWaysToCompute(expression: str):
    def operate(a, b, o):
        if o == '+': return a+b
        elif o == '*': return a*b
        return a-b

    op, nums = [], []
    idx = 0 # 숫자 시작 idx
    for i, ch in enumerate(expression):
        if ch in '+-*':
            op.append(ch)
            nums.append(int(''.join(expression[idx:i])))
            idx = i+1
    nums.append(int(''.join(expression[idx:]))) # 마지막 숫자
    size = len(nums)
    if size == 1: return [nums[0]]

    dp = [[[] for _ in range(size)] for _ in range(size)]
    for i in range(size): # 숫자 초기화. dp[i][j]. j-i 차이 0
        dp[i][i].append(nums[i])
    for i in range(size-1): # 두 num씩 계산. dp[i][j]. j-i 차이 1
        dp[i][i+1].append(operate(nums[i], nums[i+1], op[i]))

    # 결과[i:j][op범위:i~j-1]= 결과[i:op범위], 결과[op범위+1:j]를 op로 계산 
    for k in range(2, size): # j-i 차이
        for i in range(0, size-k): # j=i+k인데, size 미만이어야 함
            for o in range(i, i+k): # op범위: i~j-1
                for l in dp[i][o]: # num1 후보들
                    for r in dp[o+1][i+k]: # num2 후보들
                        dp[i][i+k].append(operate(l, r, op[o]))
    
    return dp[0][size-1]


# 2. Divide and Conquer. 쪼개서 해결만 할 것. 재사용x
# 분할 정복을 이용한 모든 조합 구하기
# "만나는 연산자 순서"에 따라 값이 달라지므로,
# 연산자 리스트 순회하며 연산자 위치 기준 식 분할(숫자 하나 남을 때까지)
# [left 결과] 기준 연산자 [right 결과]
# -> 반환된 left수, right수 계산에 현재 연산자를 '마지막으로'(재귀함수) 사용할 것
'''
2-1-1-1이면, 숫자[0~3], op[0~2] 존재.
op 사용 순서에 따라 값이 달라짐
0->1->2
0->2->1
1->0->2 ....
연산자 기준 식을 left, right로 나눠버림
'''
def diffWaysToCompute(expression: str):
    # o기준 left, right식 안에서 앞서 선택한 연산 순서에 따라,
    # 왼/오른쪽에 다양한 결과들이 모임
    # 현재 시점까지 얻은 left, right를 이용해 o 사용할 때 결과들 반환
    def operate(left, right, o):
        TMP = []
        for l in left: # o 기준 왼쪽에 오는 결과값들
            for r in right: # o 기준 오른쪽에 오는 결과값들
                if o == '+': TMP.append(l+r)
                elif o == '-': TMP.append(l-r)
                else: TMP.append(l*r)
        return TMP
    
    if expression.isdigit(): return [int(expression)] # 숫자 하나면 바로 return
    
    results = []
    # 연산이 수행되는 순서에 따라 값이 달라지므로
    # left, right 결과를 가져와 i 위치의 op를 마지막에 사용
    for i in range(len(expression)):
        if expression[i] in '+-*':
            # 현재 연산자 기준으로 분할
            left = diffWaysToCompute(expression[:i])
            right= diffWaysToCompute(expression[i + 1:])
            
            # 양쪽 결과를 병합해서 나온 값들을 넣어줌
            # 여러 값이 리스트로 나오는 것은 순서마다 나올 수 있는 값이 다르기 때문!
            results.extend(operate(left, right, expression[i]))
    return results