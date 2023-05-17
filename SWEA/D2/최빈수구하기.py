# 1000명의 성적
# 최빈수 이용해 평균 짐작(가장 여러번 나타나는 값)
# 최빈수 출력
from collections import Counter

tc = int(input())
for _ in range(1, tc + 1):
    input()
    li = input().split() # 1000명의 점수
    li.sort(reverse=True)
    m = Counter(li).most_common(1)[0][0]
    answer = m
    print("#" + str(_), answer)
    
def without_lib():
    tc = int(input())
    for _ in range(1, tc + 1):
        input()
        li = input().split() # 1000명의 점수
        li.sort(reverse=True)
        answer, cnt = 0, 0 # 최빈값, 빈도
        left, right = 0, 1
        while left<right and right<len(li):
            while right<len(li) and li[left] == li[right]: # freq>1
                right += 1
            freq = right-left
            if freq > cnt:
                cnt = freq
                answer = li[left]
            left = right
            right += 1
        print("#" + str(_), answer)

def without_lib2():
    for i in range(1, int(input()) + 1):
        _ = input()  # 테스트케이스 번호
        grades = list(map(int, input().split()))  #점수
        freq = [0] * 101  #0~100점까지의 빈도를 구하기 위함
        mode = 0  #최빈값
        for grade in grades:
            freq[grade] += 1 #현재점수의 빈도상승
            if freq[grade] >= freq[mode]: mode = grade #현재점수 빈도가 최빈값 이상이면 최빈수 변경
        print(f"#{i} {mode}")