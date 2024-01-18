# 카메라 한 번은 만나도록 설치
# 진입/진출 경로 routes -> 모든 차량이 카메라 한 번은 만나도록
# 최소 몇 대의 카메라 설치해야 하는가
# [[-20,-15],[-14,-5],[-18,-13],[-5,-3]]
# -5지점에 설치 시, 2,4번째랑 만남
# -15지점에 설치 시, 1,3번째랑 만남 -> 총 2개 설치
# "한 방향으로 쭉 달리며!!!!" 이전 지점의 카메라만 보면 됨 O(n)
# 모든 차량이 한번씩 만나야 함(진입/진출 스쳐도 만난 것 간주)
# 최소 몇 대의 카메라 필요?
# 늦게 시작해서 늦게 끝나는 애부터 먼저 보면서, 걔의 처음 부분에 둬야 겹칠 일 많음
def solution(routes):
    size = len(routes)
    routes.sort(reverse=True)
    answer = 0
    last = 30001 # 최근에 설치한 위치
    for start, end in routes:
        if end < last:
            answer += 1
            last = start
    return answer