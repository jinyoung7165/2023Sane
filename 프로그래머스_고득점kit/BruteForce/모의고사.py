# 1번 사람: 1,2,3,4,5 순서대로 돌아가먀
# 2번 사람: 21, 23, 24, 25, 다시 21
# 3번 사람: 33, 11, 22, 44, 55, 다시 33
# 01 23 45 67 89
# 0 2 4 6 8
# 0 1 2 3 4
# 정답 배열이 주어졌을 때 가장 많이 맞힌 사람은 누구인지
second = [2,1, 2,3, 2,4, 2,5]
third = [3,3, 1,1, 2,2, 4,4, 5,5]
def solution(answers):
    score = [0,0,0]
    answer = []
    for idx, an in enumerate(answers):
        if an == (idx % 5) +1:
            score[0] += 1
        
        if second[idx % len(second)] == an:
            score[1] += 1
        if third[idx % len(third)] == an:
            score[2] += 1
   
    for idx, s in enumerate(score):
        if s == max(score):
            answer.append(idx+1)
    return answer


print(solution([1, 3, 2, 4, 2]))