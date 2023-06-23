# 교환
# 0으로 시작하지 않는 정수 n. 이때, m을 정수 n의 자릿수라고 할 때
# 해당 연산을 k번 수행
# 1<=i<j<=m인 i와 j를 고름
# 다음, i번 위치의 숫자와 j번 위치의 숫자 바꿈
# 바꾼 수가 0으로 시작하면 안됨
# 나올 수 있는 수의 최댓값 구하라
# N은 1,000,000이하 자연수이고, K는 10이하 자연수
# 연산을 k번 할 수 없으면 -1 출력
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

num, target = input().split()  # 숫자, 교환 횟수
visited = dict()
answer = 0
length = len(num)
num = list(num)
if length == 1 or (length==2 and ''.join(num[1:])=='0'*(length-1)):
    print(-1)
else:
    dfs(int(target))
    print(answer)