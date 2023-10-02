'''
연산자 끼워넣기
n개 수 수열. n-1개 연산자 주어짐
앞에서부터 우선 계산. 나눗셈은 정수만 몫으로
음/양 -> 양수 간 나눗셈 몫 -> 음수 변환
만들 수 있는 식 최대 결과, 최소 결과
+-*/
-2//3 -> -(2//3)
배열로 만들어서 복구하는 것보다, plus, minus,... 변수로 만들어서 숫자 param으로 넘기는 게 낫다
'''
n = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split())) # +-*/

M, m = -float('inf'), float('inf')

def dfs(depth, cur, op, opleft):
    global M, m
    if op == 0:
        cur += nums[depth]
    elif op == 1:
        cur -= nums[depth]
    elif op == 2:
        cur *= nums[depth]
    else:
        if cur < 0:
            cur = -(-cur // nums[depth])
        else:
            cur //= nums[depth]
            
    if depth == n-1:
        if cur > M: M = cur
        if cur < m: m = cur
        return
    
    for i in range(4):
        if opleft[i] > 0:
            opleft[i] -= 1
            dfs(depth+1, cur, i, opleft)
            opleft[i] += 1
    
for i in range(4):
    if ops[i] > 0:
        ops[i] -= 1
        dfs(1, nums[0], i, ops)
        ops[i] += 1
        
print(M)
print(m)