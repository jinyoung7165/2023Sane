# 0또는 양의 정수 -> 이어 붙여 가장 큰 수
# [6,10,2] -> [6102, 6210, 1062, 1026, 2610, 2106] =>"6210"
# numbers의 길이가 100,000이기 때문에 하나씩 조합하면서 비교할 수 없다.
# 가장 큰 수를 만들기 위해서는 각 첫자리가 더 큰 수가 앞에 오도록 만들어야한다.
# 원소가 1000로 자릿수가 크기 때문에 radix sort는 사용할 수 없고 문자열 비교 방식으로 해결할 수 있다.
# 최대 1000자 -> 자릿수 만들기 위해 str화 -> 자신 3개씩 이어 붙여 비교 999 > 909090  str*3
def solution(numbers:list):
    if sum(numbers) == 0 : # 모두 0이면
        return "0"
    answer = sorted([str(n) for n in numbers], key=lambda x: x * 3, reverse=True)
    return "".join(answer)
    
# ['9','5','34','30','3'] -> "9534303"이 기댓값 "9534330"과 다릅니다.
# [3012, 31,23, 2, 12] -> [31, 3012, 23, 2, 12]