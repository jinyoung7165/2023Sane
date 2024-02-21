'''
부분합
만 이하 자연수 길이 N 수열
연속된 수 부분합 중, S이상 되는 것 중, 가장 짧은 것의 길이
합 만드는 게 불가능한 경우, 0 출력
투포인터
다음 윈도우와 현재 윈도우 일부 겹칠 수 있음 -> left+1 한번 더 하지 않음
'''
n, s = map(int, input().split())
numbers = list(map(int, input().split()))

answer = float('inf')
l, r = 0, 0
tmp = 0 # 누적합
while r < n:
    tmp += numbers[r] # 오른쪽 확장하며 누적합 구하기
    if tmp >= s: # 조건 만족하면
        while l < r and tmp - numbers[l] >= s:
            tmp -= numbers[l]
            l += 1 # 범위 좁히기
        answer = min(answer, r - l + 1)
    r += 1
    
print(0 if answer == float('inf') else answer)