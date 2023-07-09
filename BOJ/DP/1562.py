# 계단 수
# 45656 인접한 모든 자리의 차이가 1
# 길이가 n이면서(n은 100 이하 자연수)
# 0~9 숫자가 모두 등장하는 계단 수가 총 몇 개 있는지 구하라
# 0으로 시작하는 수는 계단 수가 아님
# 정답을 10^6로 나눈 나머지 출력
# 길이 0~9까지는 계단 수 존재 불가
# 길이 10일 때, 0~9숫자 모두 등장하는 계단 수 1개
# 9876543210
'''
0~9 등장 여부를 추적해야 함 -> 비트마스크(10개의 비트로)
0000000000(아무것도 안 나옴) ~ 1111111111(2진수로 1023)(왼쪽부터 9~ 오른쪽 0모두 등장)
dp[길이][마지막수][비트값]: 해당하는 계단수의 개수
초기값 설정 -> 1~9 : 길이가 1인 계단 수
1 << i : 이동 후, 오른쪽 빈자리를 0으로 채움
1 << 2 : (0001)1을 왼쪽으로 2회 shift : 0100(4). (2^1)**2반환
1 << 3 : (0001)1을 왼쪽으로 3회 shift : 1000(8). (2^1)**3반환
'''
# 비트값은 숫자 i 포함 시 2^i 더해줌
# 그 i 포함되어있는지 비트 연산으로 확인
# 2^0~2^9까지 모두 들어있어야하므로, 1023
# 테이블 최대 크기 dp[100][10][1024]
# 0,9 같은 경계값이 아닌 일반적인 값에 대해
# dp[길이+1][마지막수+-1][비트값|(1<<(마지막수+-1))]+=dp[길이][마지막수][비트값]
n = int(input())# 1보다 크고, 100보다 작거나 같음
mod = 10**9

dp = [{} for _ in range(n+1)] # 마지막 자릿수, 비트마스크를 dict로 관리

# 길이가 1인 계단 수 초기화
for i in range(1, 10): # 1~9 : 길이가 1인 계단 수. 마지막수: 자신
    dp[1][(i, 1<<i)] = 1 # 1<<9: 1을 9번 왼쪽으로 shift : 1000000000 (9 등장여부 체크 가능)
# 길이 1인 계단 수 개수 dp[1]: {(1,10=2):1, (2:100=4):1, (3:1000=8):1, (4:10000=16):1, (5:100000=256):1, ... (9:1000000000=512)}

# dp[length] 기반으로  dp[length+1] 갱신하자
# dp[length]의 마지막 자릿수 +-1 해서 dp[length+1]에 숫자 추가 가능
for length in range(1, n):
    for key in dp[length]:
        last, bit = key

        for i in [-1, 1]:
            if 0 <= last + i < 10: # 이전 length 계단 수의 마지막 자리에 +1또는 -1 해서 0~9 사이가 나와야 숫자 하나 추가 가능
                next_bit = bit | (1 << (last + i)) # dp[length+1]의 마지막 자릿수 last + i -> 기존에 갖고 있던 0~9 포함여부 bitmask에 누적합
                next_key = (last + i, next_bit) # dp[length+1]의 마지막 자릿수, 0~9 비트마스크
                
                if next_key not in dp[length + 1]: # dp[length+1]에 dict 추가
                    dp[length + 1][next_key] = 0 # 계단수 개수 합을 위해 dict의 value를 0으로 init
                
                dp[length + 1][next_key] += dp[length][key] # 마지막 자릿수와 비트마스크 동일하게 존재할 때, 여기다 개수 누적합
                dp[length + 1][next_key] %= mod

answer = 0
for key in dp[n]:
    last, bit = key
    if bit == 1023: # 1111111111(1023)으로 9~0 모두 존재하는 계단 수일 때 answer에 더함
        answer += dp[n][key]
        answer %= mod
print(answer)
''' 0~1023 비트 마스크를 위한 공간 만들 때 비효율적
n = int(input()) # 1보다 크고, 100보다 작거나 같음
mod = 10**9
dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(n+1)]
for i in range(1, 10): # 1~9 : 길이가 1인 계단 수. 마지막수: 자신
    dp[1][i][1<<i] = 1 # 1<<9: 1을 9번 왼쪽으로 shift : 1000000000 (9 등장여부 체크 가능)

# dp[n][][] 위해 길이가 n-1인 계단 수 사용해 갱신
# 각 마지막 자릿수 last에 대해, +1 또는 -1 해주며 기존 bit와 or연산 -> 비트마스크 갱신
for length in range(2, n+1): # 길이가 2~n까지의 계단 수
    for last in range(10): # 마지막 자릿수가 0~9일 때
        for bit in range(1024): # 0~1023 비트마스크(기존 등장)
            if last < 9: # 마지막 자릿수가 9보다 작으면, 다음 숫자 last+1을 계단 수의 마지막 자릿수로(오름차순) 해 비트마스크 업데이트
                next_bit = bit | (1<<(last+1)) # 기존 + 새로 생성한 숫자 합 연산 하겠다(새로운 비트마스크 생성)
                # or연산 -> 두 이진수를 비교해 하나라도 1이면 1로 반환(bit)
                # 기존에 등장한 숫자 bit에 새로운 숫자 추가해 업데이트한 비트마스크
                # 이미 등장한 숫자 표시 계속 유지되면서 새로 등장한 숫자도 추가됨
                dp[length][last+1][next_bit] += dp[length-1][last][bit]
                dp[length][last+1][next_bit] %= mod
            if last > 0: # 다음 숫자 last-1을 계단 수의 마지막 자릿수로(내림차순) 해 비트마스크 업데이트
                next_bit = bit | (1<<(last-1))
                dp[length][last-1][next_bit] += dp[length-1][last][bit]
                dp[length][last-1][next_bit] %= mod
answer = 0
for last in range(10): # 마지막 자릿수가 0~9일 때
    answer += dp[n][last][1023] # 0~9가 모두 등장하는 계단수의 개수
    answer %= mod
print(answer)

'''