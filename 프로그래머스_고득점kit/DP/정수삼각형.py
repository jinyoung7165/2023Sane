# 삼각형 꼭대기-> 바닥 경로 (아래 대각선 타고 이동)
# 거쳐간 숫자 합이 가장 큰 경우
# 아래 칸으로 이동할 때는 대각선 방향으로 1칸 오른쪽/왼쪽
# [[7],[3,8],[8,1,0],[2,7,4,4],[4,5,2,6,5]]
# [0,(0,1),(0,1,2),(0,1,2,3),(0,1,2,3,4)]
# 각 level 1,2,3,4,5의 원소 가짐
# 0->0/1. 1->1/2. 2->2/3. 3->3/4 인덱스로 이동 가능
# 0<-0, 1<-0/1, 2<-1/2. 3<-2/3 n<-n-1
def solution(triangle:list):
    size = len(triangle)
    dp = [[] for _ in range(size)]
    dp[0].append(triangle[0][0]) # level 1. 무조건 1원소
    for i in range(1, size): # ilevel->i+1원소 (1~n-1)
        # 1 level->2개 원소 가짐
        for j in range(i+1): # 0~i idx 가짐
            cur = triangle[i][j]
            if j == 0:
                dp[i].append(cur + dp[i-1][0])
            elif j == i:
                dp[i].append(cur + dp[i-1][j-1])
            else:
                dp[i].append(cur + max(dp[i-1][j], dp[i-1][j-1]))
    return max(dp[-1])

def solution(triangle): # 내려가며 주어진 배열에 바로 누적
    for t in range(1, len(triangle)): # t level->t개 원소 존재
        for i in range(t+1): # 0~t idx
            if i == 0: # 아래 원소 idx 0이면 위의 0 타고 내려온 것
                triangle[t][0] += triangle[t-1][0]
            elif i == t: # 아래 원소 idx 마지막이면 위의 마지막 idx 타고 내려온 것
                triangle[t][-1] += triangle[t-1][-1]
            else: # 위의 i 또는 i-1 타고 내려온 것
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])


def solution(triangle): # 리프에서 루트로 올라가자
    height = len(triangle)
    while height > 1: # height==1이 될 때까지 위로 올라감. triangle: height-1~1 idx까지 위로 순회
        for i in range(height - 1): # level=height일 때, idx를 0~height-1(원소 height개). 근데 2개씩(i, i+1) 비교할 거라 i=0~height-2
            print(triangle[height-1][i], triangle[height-1][i+1])
            triangle[height-2][i] += max([triangle[height-1][i], triangle[height-1][i+1]])
        height -= 1

    answer = triangle[0][0]
    return answer
