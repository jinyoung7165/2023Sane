# 문자열 게임 2
'''
1. w, k 주어짐
2. 어떤 알파벳 정확히 k개 포함하는 가장 짧은 연속 문자열 길이
3. 어떤 알파벳 정확히 k개 포함, 첫번째와 마지막 글자가 해당 알파벳인 가장 긴 연속 문자열의 길이
2, 3번 연속 문자열의 길이를 공백을 두고 출력
없으면 -1 출력
'''
from sys import stdin
from collections import Counter

input = stdin.readline

tc = int(input())
for _ in range(tc):
    answer = []
    w = input().strip()
    k = int(input())
    if k == 1: answer = [1, 1]
    else:
        cnt, mxcnt = Counter(), Counter()
        last_id = dict() # 해당 위치의 알파벳 나온 직전의 인덱스 기록
        last_seq = [-1]*len(w)
        left = 0
        for right in range(len(w)):
            c = w[right]
            
            if c in last_id: last_seq[right] = last_id[c]
            last_id[c] = right
                
            cnt[c] += 1 # 축소용 카운터
            mxcnt[c] += 1 # 확장용 카운터
            
            if cnt[c] == k:
                while left < right and w[left] != c: # 범위 축소
                    cnt[w[left]] -= 1
                    left += 1
                size = right - left + 1
                if not answer:
                    answer = [size, size]
                else:
                    if answer[0] > size: answer[0] = size
                cnt[w[left]] -= 1
                left += 1
            
            if mxcnt[c] == k:
                tmp = 1
                mxleft = right
                while tmp != k:
                    mxleft = last_seq[mxleft]
                    tmp += 1
                answer[1] = max(answer[1], right-mxleft+1)
                mxcnt[c] -= 1
                
    if answer: print(*answer)
    else: print(-1)
    
    
import sys
from collections import defaultdict
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    answers = []
    W = input().rstrip()
    K = int(input())
    alpha = defaultdict(list)

    # 각 알파벳 딕셔너리에 인덱스 저장
    for i, w in enumerate(W):
        alpha[w].append(i)

    # K개 이상인 알파벳에 대해 k만큼 슬라이싱 짧은 문자열, 긴 문자열 찾기
    for k, v in alpha.items():
        if len(v) < K: continue
        for i in range(len(v)-K+1):
            answers.append(v[i+K-1]-v[i]+1)

    if answers:
        print(min(answers), max(answers))
    else:
        print(-1)