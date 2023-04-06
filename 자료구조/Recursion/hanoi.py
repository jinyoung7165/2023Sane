# n개의 원판을 1번째 기둥에서 3번째 기둥까지 옮기는 방법
# 기둥 3개, 원판 크기 작을수록 위에 쌓여져있음
# 한 번에 1 원판 이동 가능 & 큰 원판이 작은 원판 위에 오면 안됨
# n개의 원판을 최소 횟수로 이동할 것 (n은 15 이하)
# n=2 -> result: [[1,2],[1,3],[2,3]] #1->2,1->3,2->3 이동 있었다
# 기둥1의 남은 n-1개의 원판을 중간 기둥으로 이동(계속...마치 반복문)
# 기둥1의 n번째 원판 1개를 3번째 기둥으로 이동
# 기둥2의 남은 n-1개의 원판을 3번째 기둥으로 이동(계속...마치 반복문)
# 위의 과정을 n번 반복
def solution(n):
    answer = []
    def move(start, end, mid, idx): # start->end로 이동했음. mid는 나중에 옮길 곳
        if idx == 1: # 1개는 그냥 이동
            answer.append([start, end])
            return
        move(start, mid, end, idx-1) # 남은 원판 개수만큼 이동
        answer.append([start, end])
        move(mid, end, start, idx-1)
    move(1, 3, 2, n) # start, end, mid, idx
    return answer