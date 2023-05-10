# 생산 n개-> h번 이상 h개 인용
# [3, 0, 6, 1, 5] 총 len(5)개 중 3개가 최소 3회 이상 인용됨 > 3
# [6,5,3,1,0] -> 3
#i 0 1 2 3
# [6,5,4,1,0] -> 3
#i 0 1 2 3
# [5,5,5,5,0] -> 4 (4보다 큰 원소가 4개)
#i 0 1 2 3 4
# [1,0]
#i 0 1
# 특정 기준점 x으로 나눴을 때, 그것 이상인 원소는 x개, 나머진 x 이하
# x <= len(citations)
# 인덱스, 인용횟수 비교해 인덱스보다 인용횟수 작아지면, 직전 인덱스가 답
def solution(citations):
    citations.sort(reverse=True)
    h_index = 0
    for c in citations:
        if c > h_index:
            h_index += 1
    return h_index