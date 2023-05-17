# RC카 이동거리 계싼
# 매초마다 command 주어짐.0:유지.1:가속.2:감속
# 가속/감속도 추가로 주어짐
# n개의 command모두 수행했을 때, N초 동안 이동한 거리?
# 1 2 -> 2 -> 2M
# 2 1 -> 1 -> 3M
# 현재 속도보다 감속 속도가 더 크면 속도 0이 됨
tc = int(input())

for _ in range(1, tc+1):
    n = int(input()) # n줄 입력 받을 것
    speed, answer = 0, 0 # 초기 속도. 이동 거리 0

    for i in range(n): # n초
        # map으로 명령어, 속도 풀어서 받는 것보다 list로 받아서 접근하는게 메모리 효율 낫다
        c = list(map(int, input().split())) # 명령, 속도
        if c[0] == 2: # 감속
            speed -= c[1]
            if speed < 0: speed = 0
        elif c[0] == 1:
            speed += c[1]
        # 속도 유지하며 거리 추가
        answer += speed

    print('#'+str(_), answer)