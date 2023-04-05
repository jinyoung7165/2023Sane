# stack의 top끼리 비교해 다르면 push
def solution(arr):
    answer = []
    last = -1 # java -> Arraylist의 top 구하기 번거로워 이 방식
    for el in arr:
        if last != el:
            answer.append(el)
            last = el
    return answer

def solution(arr): # java -> Stack<Integer> 사용
    answer = []
    for el in arr:
        if len(answer) == 0 or el != answer[-1]:
            answer.append(el)
    return answer