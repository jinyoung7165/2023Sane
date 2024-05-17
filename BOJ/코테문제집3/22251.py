# 빌런 호석
'''
현재 X, 길이K 수, 0으로 시작 가능
0~9 LED로 이뤄짐.
최대 1~p개 픽셀 반전 시킬 때, 1~N 범위의 수 줄 만들 수 있는 경우의 수?
각 숫자에서 다른 숫자로 바꾸기 위해 몇 개 필요한지 9!개 -> 구하고 시작
'''
from sys import stdin
input = stdin.readline
n, k, p, x = map(int, input().split())

cnt = [[0]*10 for _ in range(10)] # a->b로 바꾸기 위해 바꿔야 하는 led 수
shape = [0b1011111, 0b0000011, 0b1110110, 0b1110011, 0b0101011,
    0b1111001, 0b1111101, 0b1000011, 0b1111111, 0b1111011] # 각 숫자를 나타내는 가로 3, 세로 4

def convert_cnt():
    for i in range(9):
        for j in range(i+1, 10):
            cnt[i][j] = (bin((shape[i] ^ shape[j]))[2:]).count('1')
            cnt[j][i] = cnt[i][j]
           
convert_cnt()
x = str(x).zfill(k)
number = list(x)
answer = 0
def dfs(idx, cur, used):
    global answer
    if idx == k:
        if int(cur) and cur != x:
            answer += 1
        return
    # 원래 int(number[idx]) -> i로 바꿀 것
    origin = int(number[idx])
    for i in range(10):
        if cnt[origin][i] + used <= p and int(cur+str(i)+'0'*(k-idx-1))<=n:
            dfs(idx+1, cur+str(i), cnt[origin][i] + used)
    
dfs(0, '', 0)
print(answer)