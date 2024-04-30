# A와 B 2
'''
두 문자열 S,T -> S를 T로 바꾸는 게임. 두 연산만 가능
1) 문자열 뒤에 A 추가
2) 문자열 뒤에 B 추가하고, 문자열 뒤집음
S를 T로 만들 수 있는지 없는지 알아내라 1/0
'''
from sys import stdin
from collections import defaultdict
input = stdin.readline
s = input().strip()
t = input().strip()
trev = t[::-1]
size = len(t)
visited = defaultdict(set)
answer = 0

def dfs(cur, depth):
    global answer
    if answer: return
    if depth == size:
        if cur == t:
            answer = 1
        return
    sA, sB = cur+'A', (cur+'B')[::-1]
    if sA not in visited[depth+1] and (sA in t or sA in trev):
        visited[depth+1].add(sA)
        dfs(sA, depth+1)
    if sB not in visited[depth+1] and (sB in t or sB in trev):
        visited[depth+1].add(sB)
        dfs(sB, depth+1)
    
dfs(s, len(s))
print(answer)

'''

str1=list(input())
str2=list(input())
n=len(str1)



def dfs(temp):
    
    if temp==str1:
        return 1
    if len(temp)<n:
        return 0
    
    if temp[-1]=='A' and dfs(temp[:-1]):#a가 추가된 경우
        return 1       
        
    if temp[0]=='B' and dfs(temp[1:][::-1]):
        return 1
    

print(1 if dfs(str2) else 0)
'''