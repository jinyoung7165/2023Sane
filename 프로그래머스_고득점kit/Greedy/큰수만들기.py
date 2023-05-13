# 어떤 숫자에서 k개 수 제거 시 만들 수 있는 가장 큰 수
# 1924 ->2개 제거. [19,12,14,92,94,24] -> 94
# 1231234 ->3개 제거. 3234
# 4177252841 -> 4개 제거. 775841
# 부분 수열 만들기 느낌인데, 인덱스별 원소의 크기
# 부분 수열-> 무조건 dfs또는 투포인터라는 생각 버리기!!!! -> stack/que일 수도 있음
def solution(number, k): # 시간 초과
    answer = ''
    idSeq = sorted(list(enumerate((number))), key=lambda x:(-int(x[1]), x[0])) # [idx, val] 저장, val내림, idx오름차순
  
    pos = 0 # 생성할 숫자에서 위치
    path = [] # 제일 큰 자릿수부터 삽입
    visited = set()
    while pos < len(number)-k:
        for i in range(len(idSeq)):
            if i in visited: continue
            id = idSeq[i][0]
            # 남은 수가 만들고자 하는 수의 길이 이상
            # size-id-1 >= size-k-pos-1
            # 해당 수를 해당 자릿수에 배치 가능
            if id > k+pos: # 배치 불가-> 나중 위치에는 가능할 수 있음
                continue
            if path and path[-1] > id: # 이미 선택한 수보다 앞의 수일 때, 더이상 고려할 필요 없이 제거
                visited.add(i)
                continue
            # 배치 
            pos += 1
            path.append(id)
            visited.add(i)
            break
        
    for id in path:
        print(id)
        answer += str(number[id])     
    return answer

from itertools import combinations
def solution(number, k):
    size = len(number)-k
    return ''.join(sorted(list(combinations(number, size)), reverse=True)[0])

# 한 방향으로 이동. 앞에 선택한 원소보다 크고, 
# 뒤에 뽑을 수 있는 원소 남아있어야 함
def solution(number, k):
    stack = []
    for n in number: 
        # 이전 선택이 현재보다 작고, 제거 가능한 기회 남아있으면 제거
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)
    if k > 0: 
        # 제거되지 못한 뒷부분(처음부터 내림차순이라 작은 애들이 맨 뒤로 감)
        stack = stack[:-k]
    return ''.join(stack)
        

# print(solution("1924", 2)) # 94
print(solution("1231234", 3)) # 3234