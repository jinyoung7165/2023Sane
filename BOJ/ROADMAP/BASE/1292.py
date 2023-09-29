# 쉽게 푸는 문제
'''
1*1번, 2*2번 ... 1 2 2 3 3 3 ... 수열 만들고
일정 구간 동안의 합
수열 a번째 숫자부터 b번째 숫자까지의 합(최대 1000)
'''
a, b = map(int, input().split())
dp = [0] * (b+1)
idx = 1
flag = False
for num in range(1, b+1): # num
    for i in range(idx, idx + num):
        dp[i] = num + dp[i-1]
        if i == b:
            flag = True
            break
    else: idx = i + 1
    if flag: break
print(dp[b] - dp[a-1])

def s(b):
    num = 1
    idx = 1
    answer = 0
    while idx <= b:
        answer += num
        if idx == num*(num+1)//2:
            num += 1
        idx += 1
    return answer

print(s(b) - s(a-1))