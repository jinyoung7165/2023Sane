# 전구와 스위치
'''
1~n전구, 1~n스위치
각 전구는 0/1상태
i번 스위치 누르면, i-1, i,i+1 전구 상태 바뀜
1번 누르면, 1, 2번만 바뀜
n번 스위치 누르면, n, n-1번만 바뀜
n개의 전구들 각각 원하는 상태로
만들기 위해 스위치를 최소 몇 번 눌러야 하는가? 불가능한 경우, -1

누르는 순서 상관없음 -> bfs로 하면 메모리 초과남
'''
from sys import stdin

input = stdin.readline

n = int(input())
before = list(map(int, list(input().strip())))
after = list(map(int, list(input().strip())))
temp_before = before[:]
print(before)

def check(answer, before):
    for i in range(1, n): # 중간 것 기준으로 3개씩 바꿀 것
        if before[i-1] != after[i-1]:
            before[i-1] =  1^before[i-1]
            before[i] = 1^before[i]
            if i != n-1: before[i+1] = 1^before[i+1]
            answer += 1
    if before == after:
        print(answer)
        return True
    return False

# 첫번째 자리에서 안 누른 거 실패했으면
if not check(0, before):
    #첫번째 자리에서 누름
    temp_before[0] = 1^temp_before[0]
    temp_before[1] = 1^temp_before[1]
    if not check(1, temp_before):
        print(-1)