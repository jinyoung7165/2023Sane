# 가르침
'''
k개 글자로만 이뤄진 단어 읽을 수 있음. 
n개 중 읽을 수 있는 최대 단어 개수
모든 단어는 anta로 시작, tica로 끝남
9개 단어 존재하는데, 8개 글자만 알면 읽을 수 있는 단어 수 3개
메모리 제한 빡셈
antabtica (b)
antaxtica (x)
antadtica (d)
antaetica (e)
antaftica (f)
antagtica (g)
antahtica (h)
antajtica (j)
antaktica (k)
antic (5개 기본 필요)
8개 글자 알면, 저 중 3 단어만 읽을 수 있음
각 단어마다 알파벳 set 갖고, 각 알파벳별 배웠는지 여부(visited) 배열 필요
26알파벳 중 5 기본 배우고, 나머지 중 k-5 알파벳 선택하면 몇 단어인지
'''
from itertools import combinations
from sys import stdin
input = stdin.readline

def word2bit(word):
    bit = 0
    for char in word: # or 연산이기 때문에 input시 set으로 안 걸러줘도 됨
        bit |= 1 << ord(char) - ord('a')
    return bit

n, k = map(int, input().split())
words = [word2bit(input().rstrip()) for _ in range(n)]
answer = 0
learn = word2bit('antic')

if k < 5: print(0) # 최소 antic 알아야 함
elif k == 26: print(n) # 모든 알파벳 알면 모든 단어 읽음
else:
    alphabit = [1<<i for i in range(26) if not (learn & 1<<i)] # antic 제외한 alphabet 선택지
    for comb in combinations(alphabit, k-5):
        curlearn = sum(comb) | learn # learn이랑 어차피 안 겹쳐서 + 가능. 아니면 | 해줘야 함
        tmp = 0
        for wordbit in words:
            if wordbit & curlearn == wordbit:
                # curlearn이 wordbit보다 더 많은 alphabet 배울 가능성 있음
                # worbit와 & 연산 시, 더 적게 1을 포함하는 wordbit 나올 것
                tmp += 1
        answer = max(answer, tmp)
    print(answer)
'''
dfs로 풀면 시간초과 문제
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

if K < 5:
    print(0)
    exit()
elif K == 26:
    print(N)
    exit()

words = []
essential = {'a', 'c', 'i', 'n', 't'}
for _ in range(N):
    word = input().rstrip()[4:-4]
    mask = 0
    for ch in set(word) - essential:
        mask |= (1 << (ord(ch) - ord('a')))
    words.append(mask)

alpha = [ch for ch in "bdefghjklmopqrsuvwxyz"]
result = 0

def backtrack(idx, k, mask):
    global result
    if k == K - 5:
        count = 0
        for word in words:
            if word & mask == word:
                count += 1
        result = max(result, count)
        return

    if idx == 21:
        return

    # 현재 알파벳을 선택하는 경우
    backtrack(idx + 1, k + 1, mask | (1 << (ord(alpha[idx]) - ord('a'))))
    # 현재 알파벳을 선택하지 않는 경우
    backtrack(idx + 1, k, mask)

backtrack(0, 0, 0)
print(result)
