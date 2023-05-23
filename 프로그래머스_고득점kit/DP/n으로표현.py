# 5와 사칙연산->12 표현 가능
# 12=5+5+(5/5)+(5/5) = 10+1+1
# 12=55/5+5/5 = 11+1
# 12=(55+5)/5 : 60/5
# 5를 사용한 횟수는 각각 6,5,4. 제일 적게 사용:4 return
# n과 number주어질 때, n과 사칙연산만 사용해서 number표현
# n=1~9. number=1~32000
# 괄호, 사칙연산만 가능. 나누기 시 나머지 무시
# 최솟값이 8보다 크면 -1 return
# n=5, number=12 -> 4
# n=2, number=11 -> 3 (11=22/2. 2를 3번 사용)
# n=5, number=31168 -> -1
from collections import defaultdict
def solution(N, number):
    dp = defaultdict(set) # N몇 번:[생성 number]
    dp[1].add(N)
    if N==1: dp[1].add(1)
    else: dp[2].add(1) # 같은 수 나눠서 1
    if number in dp[1]: return 1
    elif number==1:  return 2
    
    answer = set()
    for i in range(2, 9): # n을 2~8번 쓰기
        st = str(N)*i # 조합 없이 제일 빠르게 증가
        dp[i].add(int(st))
        dp[i].add(N*i)
        dp[i].add(N**i)
        if number in dp[i]: return i
        # n을 1~i번 쓴 것과 조합
        for j in range(1, i+1):
            if i+j > 8: break # 최대 n==8번 쓸 수 있음
            for el1 in dp[i]:
                for el2 in dp[j]:
                    dp[i+j].add(el1+el2)
                    dp[i+j].add(el1*el2)
                    if el1 > el2: # 0,1 넣지 않겠다
                        dp[i+j].add(el1//el2)
                        dp[i+j].add(el1-el2)
                    elif el2 > el1:
                        dp[i+j].add(el2//el1)
                        dp[i+j].add(el2-el1)
            if number in dp[i+j]:
                answer.add(i+j)
    if answer:
        return min(answer)
    return -1

# print(solution(5, 12))
# print(solution(2, 11))
print(solution(11, 11111)) # (i+j=2i >= i+1. 다음 i순회에서 min이 나올 수 있기 때문에 바로 return 못함)

def another(N, number):
    dp = defaultdict(set) # N개수: {생성 number}

    for i in range(1, 9): # n의 개수
        dp[i].add(int(str(N)*i)) # 조합 없이 제일 빠르게 증가
        # n최대 개수 i개를 지키며 이전 값과 조합
        for j in range(i): # j 1부터 시작하면 틀리는 이유 모르겠음.
            # 연산자 케이스 
            for op1 in dp[j]: # 0~i-1개 n(이전에 나온 누적값). dp[0] 어차피 없어서 for문 안 돈다
                for op2 in dp[i-j]: # i~1개 n과 조합 => j+i-j -> n개수 i를 지킴-> 다음 i순회보다 n개수 무조건 작기 때문에 number나오면 바로 return
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
            if number in dp[i]: # 총 i개 썼을 때 원하는 number 나왔으면, 다음 순회(i+1) 전에 stop. 속도 훨 높임
                return i

    return -1

print(another(11, 11111))

from collections import defaultdict
def solution3(N, number):
    dp = defaultdict(set) # N몇 번:[생성 number]
    dp[1].add(N)
    if N==1: dp[1].add(1)
    else: dp[2].add(1) # 같은 수 나눠서 1
    if number in dp[1]: return 1
    elif number==1:  return 2
    
    for a in range(2, 9): # 2 ~ 8 중에 답이 있음
        dp[a].add(int(str(N) * a)) # 5, 55, 555, ...
        for b in range(1, a): # [1, a)개 만큼 n사용
            for i in dp[b]: # 1~a-1개 썼을 때 만들 수 있는 num
                for j in dp[a-b]: # a-1~1개 썼을 때, 즉 총 a개의 n 쓰는 조합
                    dp[a].add(i + j)
                    dp[a].add(i * j)
                    if i > j: # 0과 1은 넣지 않겠다
                        dp[a].add(i - j)
                        dp[a].add(i//j)
                    if i < j:
                        dp[a].add(j - i)
                        dp[a].add(j//i)
            if number in dp[a]: return a
    return -1
print(solution3(11, 11111))