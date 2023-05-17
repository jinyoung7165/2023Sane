# n명 게임
# 앞으로 던져 원하는 지점에 최대한 가까이 던져야 함
# -100,000~100,000 수직선. 사람들은 100,000위치에서 최대한 0에 가깝게 던져야 함
# n개 떨어진 위치 주어질 때, 가장 가까운 거리 차. 몇 명인지
tc = int(input())
for _ in range(1, tc + 1):
    n = int(input())  # 몇 명 참여
    record = list(map(abs, map(int, input().split())))
    record.sort()
    distance = record[0]
    cnt = 1
    for i in range(1, n):
        if record[i] == distance: cnt += 1
        else: break

    print("#" + str(_), distance, cnt)