# 8개의 수 입력 받고,
# 첫번째 숫자 1감소 후 맨 뒤로 보냄
# 다음 첫번째 수 2 감소 후 맨뒤... 5감소 후 맨뒤까지 1 cycle
# 숫자 0보다 작아지는 경우 0으로 만들고 뒤로 보냄. 프로그램 종료
# 종료 숫자 값이 암호가 됨
# 9550 9556 9550 9553 9558 9551 9551 9551 -> 62294130
from collections import deque

cycle = [1,4,2,5,3]
def encode(nums):
    m = min(nums)
    if m > 15: # 5cycle 초과해서 돌아야 함
        share = m // 15 # 몫
        for i in range(8):
            nums[i] -= 15*(share-1)

    que = deque(nums, maxlen=8)
    diff = 1
    while True:
        if diff == 6:
            diff = 1
        el = que.popleft() - diff
        if el <= 0:
            que.append(0)
            break
        que.append(el)
        diff += 1
    return que

for t in range(1, 11):
    input()
    nums = list(map(int, input().split())) # 8개의 숫자
    result = encode(nums)
    print("#" + str(t), *result)