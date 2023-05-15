# n개의 양수/0 순서 바꾸지 말고. 더하고 빼서 target값(자연수) 만들 방법 개수
# [1.1.1.1.1] -> 숫자 3
# -1+1+1+1+1 등 총 5가지 방법
# [4,1,2,1] -> 4. 총 2가지 방법
# -1을 어디 위치에 배치할지 탐색. if(sum) > target인 경우에 -배치
# [-el 또는 el]선택

def dfs(numbers, target, idx): # 배열, 만들어야 하는 수, answer, 다음 볼 idx
    size = len(numbers)
    
    if idx == size: # 끝 idx까지 다 봄
        if target == 0: # global answer 쓰지말고, global set만들어서 st(+-++++) add하고 개수를 구하거나 dfs내에서는 지역변수를 return해야함
            return 1
        return 0
    
    if sum(numbers[idx:]) < target: return 0 # idx 이후 누적 합이 target보다 작으면 만들 수 없는 수 판정(target 양수이기 때문에)

    # 해당 idx 원소에 + - 연산 -> 다음 원소 확인
    answer = dfs(numbers, target-numbers[idx], idx+1) + dfs(numbers, target+numbers[idx], idx+1)
    return answer

def solution(numbers, target):
    return dfs(numbers, target, 0) # 배열, 만들 수, 다음 볼 idx

solution([1,1,1,1,1], 3)
# solution([4,1,2,1], 4)

# 주어진 입력값 범위 작음
# 리스트 split하고 싶은데, idx처리를 모르겠다? -> 현재 원소를 [0]이라 하고, 남은 리스트를 [1:]로 쪼개면 됨
def solution2(numbers, target):
    if not numbers and target == 0: # 모두 봤는데 target 0이면 해답
        return 1
    elif not numbers: # numbers다 썼는데 target 남았으면 구할 수 없는 target이다
        return 0
    else:
        answer = solution2(numbers[1:], target - numbers[0]) + solution2(numbers[1:], target + numbers[0])
        return answer