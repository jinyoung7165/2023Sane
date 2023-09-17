'''
01로 이뤄진 2^n*2^n 크기 2차원 정수 배열 arr
쿼드 트리로 압축
1 특정 영역 s
2 s내부 모든 수가 같으면, s를 해당 수로 압축
3 그렇지 않다면, s를 4균일 정사각형 영역으로 쪼갬. 각 영역에 대해 압축 시도
배열에 최종적으로 남는 0의 개수, 1의 개수 배열에 담아 return
row//2, col//2
'''
    
def solution(arr):
    answer = [0, 0]
    def conquer(arr, r_start, c_start, size):
        last = None
        for r in range(r_start, r_start+size):
            for c in range(c_start, c_start+size):
                val = arr[r][c]
                if last == None:
                    last = val
                elif val != last: return -1
        print(last, r_start, "~", r_start+size-1, c_start,"~", c_start+size-1)
        return last # 0 or 1

    def divide(arr, r_start, c_start, size):
        if size == 1:
            answer[arr[r_start][c_start]] += 1
            return
        val = conquer(arr, r_start, c_start, size)
        if val == -1:
            t_size = size // 2
            for r in [r_start, r_start+t_size]:
                for c in [c_start, c_start+t_size]:
                    val = conquer(arr, r, c, t_size)
                    if val == -1: # 압축 불가
                        divide(arr, r, c, t_size)
                    else:
                        answer[val] += 1
        else: answer[val] += 1
        divide(arr, 0, 0, len(arr))
    return answer


def solution(arr):
    answer = [0, 0]

    def check(size, x, y):
        if size == 1:
            answer[arr[y][x]] += 1
            return
        else:
            first = arr[y][x]
            for dy in range(size):
                for dx in range(size):
                    if first != arr[y + dy][x + dx]: # 첫번째 원소랑 다른 원소가 area에 나오면 바로 divide
                        check(size // 2, x, y)
                        check(size // 2, x + size // 2, y)
                        check(size // 2, x, y + size // 2)
                        check(size // 2, x + size // 2, y + size // 2)
                        return
            answer[first] += 1 # divide될수록 더 많이 중가
    check(len(arr),0,0)


    return answer

print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))