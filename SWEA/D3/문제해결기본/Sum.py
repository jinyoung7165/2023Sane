# 100*100 배열 주어질 때,각 행/열/대각선의 합 중 최대 구하라
# list(zip(*maps)) # 행열 바꿈... 그렇긴 한데 메모리 아끼자
for _ in range(1, 11): # 10개 tc
    input()
    c = [0]*100 # 열의 합
    answer = 0
    d = 0 # 대각선의 합
    for i in range(100): # 행 최대 구하기
        tmp = list(map(int, input().split()))
        d += tmp[i] # 대각선
        for j in range(100): # 열의 합
            c[j] += tmp[j]
        r = sum(tmp) # 행의 합
        if answer < r: answer = r # 갱신

    answer = max(max(max(c), d), answer)

    print("#"+str(_), answer)