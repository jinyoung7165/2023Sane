# 숫자 체계 0-9 -> 문자열
#"ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
# "TWO NIN TWO TWO FIV FOR" 정렬 -> "TWO TWO TWO FOR FIV NIN"
# 메모리 아끼려면 로직 def로 빼라
# python 3.6부터는 dic의 순서 기억 -> 걍 dic에다 누적해도 됨
tc = int(input())
di = {
"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4,
    "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9
}

def count_sort(size, nums):
    result = [None] * size
    counter = [0] * 10  # 0-9
    for num in nums:
        counter[di[num]] += 1
    for i in range(9):  # 누적합
        counter[i + 1] += counter[i]
    for i in range(size):
        counter[di[nums[i]]] -= 1
        result[counter[di[nums[i]]]] = nums[i]
    return  result

for t in range(1, tc+1):
    _, size = input().split()
    nums = input().split()
    result = count_sort(int(size), nums)

    print("#" + str(t))
    print(*result)