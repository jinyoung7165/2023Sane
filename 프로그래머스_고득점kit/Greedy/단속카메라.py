# 카메라 한 번은 만나도록 설치
# 진입/진출 경로 routes -> 모든 차량이 카메라 한 번은 만나도록
# 최소 몇 대의 카메라 설치해야 하는가
# [[-20,-15],[-14,-5],[-18,-13],[-5,-3]]
# -5지점에 설치 시, 2,4번째랑 만남
# -15지점에 설치 시, 1,3번째랑 만남 -> 총 2개 설치
# "한 방향으로 쭉 달리며!!!!" 이전 지점의 카메라만 보면 됨 O(n)
# 최대한 많은 카메라 공유하려면, 시작 아닌 끝지점에 둬야 함
# 제일 작은 끝에 무조건 1개 설치 후, 카메라 위치랑 다음 원소의 start 비교.
# 뒤의 start <= 설치된 카메라 -> 더 설치할 필요 없음
def solution(routes):
    routes.sort(key = lambda x: (x[1]))
    count = 0
    stack = [] # 지나쳐온 원소 인덱스
    
    pos = -30001 # 가장 마지막으로 설치된 카메라의 위치. 좌표 -30000부터 시작
    for start, end in routes:
        if count == 0: # 가장 작은 end부터 설치
            count = 1
            pos = end
            continue
        else:
            if pos < start: # 카메라 못 만남 -> 설치
                count += 1
                pos = end
            
    return count