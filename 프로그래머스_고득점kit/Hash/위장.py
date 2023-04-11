# [[의상이름, 의상종류]] 주어지면
# 조합의 수(최소 1 의상 선택, 같은 종류의 옷 중에서 1/0개씩)
# (2+1)(1+1) - 1 : 종류별 1 or nothing 곱한 다음 - nothing
def solution(clothes:list):
    answer = 1
    dic = dict()
    for _, kind in clothes:
        if kind in dic:
            dic[kind] += 1
        else:
            dic[kind] = 2
            
    for el in dic:
        answer *= dic[el]
    
    return answer-1

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])