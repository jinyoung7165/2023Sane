# 1:30
# 두 숫자 선택해 정해진 횟수만큼 위치 교환 -> 최대 숫자 만들기
# 32888 -> 2회 교환-> 82838 -> 88832
# 88832 -> 2회 교환 -> 88832
# 88832 -> 3회 교환 -> 88832 (8끼리 교환)
# 94 -> 1회 교환(필수)-> 49
# 2737 1 -> 7732
# 123 1 -> 321
# 최대자릿수 6. 최대교환횟수 10.

def dfs(cnt):
    global answer
    if cnt == 0:
        answer = max(answer, int(''.join(num)))
        return

    for i in range(length): # 처음부터 끝까지 탐색하며 2개 바꿈
        for j in range(i + 1, length):
            num[i], num[j] = num[j], num[i]
            snum = ''.join(num)
            if not (snum, cnt) in visited: # 중복 아니면
                visited[(snum, cnt)] = 1
                dfs(cnt-1)
            num[i], num[j] = num[j], num[i]

tc = int(input())
for T in range(1, tc + 1):
    num, target = input().split()  # 숫자, 교환 횟수
    visited = dict()
    answer = 0
    length = len(num)
    num = list(num)
    dfs(int(target))
    print("#" + str(T), answer)