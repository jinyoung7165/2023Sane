# 비슷한 단어
'''
n개 영단어 -> 가장 비슷한 두 단어
접두사 길이(공통적으로 나타나는 문자열) 최대
제일 앞에 입력된 최대 접두사를 가진 단어 두 개
같은 두 단어는 제외해야 함

다른 방법: 모든 단어의 모든 부분 prefix에 대한 dict(list)
items 길이로 sort (길이 같은 거 있어도 python이라서 입력순으로 정렬됨)
-> 그 중에서 다시 단어 [:2] 입력순 뽑을 수 있음

다른 방법: 길이 배열 파서, 입력된 인덱스: 갱신된 접두사의 길이 저장
'''
from sys import stdin

input = stdin.readline
n = int(input())
origin  = list((input().strip(), i) for i in range(n))
words = sorted(origin)

prefix = 0
answer = dict()
for i in range(n-1):
    if words[i][0] != words[i+1][0] and words[i][0][0] == words[i+1][0][0]:
        size = 1
        msize = min(len(words[i][0]), len(words[i+1][0]))
        while size < msize and words[i][0][size] == words[i+1][0][size]:
            size += 1
        string = words[i][0][:size]
        if prefix < size:
            prefix = size
            answer.clear()
            answer[string] = {words[i][1], words[i+1][1]}
        elif prefix == size:
            if string in answer:
                answer[string].add(words[i][1])
                answer[string].add(words[i+1][1])
            else:
                answer[string] = {words[i][1], words[i+1][1]}
                
result = sorted(list(map(sorted, answer.values())))[0][:2]

for re in result:
    print(origin[re][0])