# 참여자, 완주자 배열 주어졌을 때 완주하지 못한 선수 1명을 return
# 동명이인 존재 가능
from collections import defaultdict, Counter
def solution(participant, completion):
    com_dic = defaultdict(int)
    for com in completion:
        com_dic[com] += 1

    for par in participant:
        if com_dic[par]:
            com_dic[par] -= 1
        else:
            return par

def solution(participant, completion): # Counter 빼기 -> 0인 애들 사라짐
    return list((Counter(participant) - Counter(completion)))[0]
           
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part # {hash값: 이름}
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
     