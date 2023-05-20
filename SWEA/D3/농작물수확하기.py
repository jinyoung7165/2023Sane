# n*n 농장(n홀수)
# 농장 크기에 딱 맞는 정사각 마름모 형태로 수확
# 1*1-> 1칸
# 3*3-> 1+3+1.4칸(9-1*4)
# 5*5-> 1+3+5+3+1. 13칸.(25-3*4)
tc = int(input())
for T in range(1, tc + 1):
    n = int(input())
    maps = [list(map(int, input())) for _ in range(n)]
    answer = 0
    mid = n//2 # 중심 위치(mid, mid)에서 퍼져 나감
    for i in range(mid+1):
        if i == 0:
            answer += sum(maps[mid])
        else:
            answer += sum(maps[mid-i][i:n-i]) + sum(maps[mid+i][i:n-i])
        
    print("#" + str(T), answer)