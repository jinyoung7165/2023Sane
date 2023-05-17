# 상자가 쌓여 있음
# 높은 곳->낮은 곳에 옮기며 최고점-최저점 간격을 줄이자
# 평탄화 수행 후, 최고점-최저점 차이가 최대 1이내.
# 옮기는 횟수에 제한 있을 때, 최고점-최저점 차이 반환
# 최고점->최저점 옮기는 작업을 제한 횟수만큼
# 가로 길이 항상 100. 최고점-최저점 차이가 최대 1이내->그만둬라
from collections import defaultdict
for _ in range(1, 11): # tc 수
    limit = int(input()) # dump 횟수
    height_pos = defaultdict(list) # height->pos 찾기
    boxes = list(map(int, input().split()))
    for i in range(100): # 가로 길이 100
        height_pos[boxes[i]].append(i)
    
    m, M = min(boxes), max(boxes)
    for i in range(limit): # dump 진행
        if M-m <= 1: break # 더이상 진행할 필요x
        m_pos, M_pos = height_pos[m].pop(), height_pos[M].pop()
        boxes[m_pos] += 1
        boxes[M_pos] -= 1
        height_pos[m+1].append(m_pos)
        height_pos[M-1].append(M_pos)
        m, M = min(boxes), max(boxes)
        
    print("#{} {}".format(_, M-m))

# 간단한 list문제 -> 높이에 해당하는 위치의 개수를 세는 배열
def another():
    for t in range(1, 11):
        n = int(input())
        src = list(map(int, input().split()))
        buff = [0]*101
        MIN = min(src)
        MAX = max(src)
        for i in src:
            buff[i] += 1
        for i in range(n):
            if MAX - MIN <= 1:
                break
            buff[MAX] -= 1
            buff[MAX-1] += 1
            buff[MIN] -= 1
            buff[MIN+1] += 1
            if buff[MAX] == 0:
                MAX -= 1
            if buff[MIN] == 0:
                MIN += 1
        print(f"#{t} {MAX-MIN}")