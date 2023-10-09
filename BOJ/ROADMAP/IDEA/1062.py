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
def word2bit(word):
    tmp = 0
    for w in word:
        tmp |= 1 << (ord(w) - ord('a'))
    return tmp

n, k = map(int, input().split())
words = [word2bit(set(input().rstrip()) -{'a','n','t','i','c'}) for _ in range(n)]
candidate = [word2bit(ch) for ch in "bdefghjklmopqrsuvwxyz"]
answer = 0

def dfs(cur, visited, cnt):
    global answer
    if cnt == k - 5:
        tmp = 0
        for word in words:
            if word & visited == word:
                tmp += 1
        answer = max(answer, tmp)
        return
    if cur == 21: return
    
    dfs(cur+1, visited | candidate[cur], cnt+1) # 다음 알파벳 배우거나
    dfs(cur+1, visited, cnt) # 안 배우거나
    
    
if k < 5: print(0)
elif k > 25: print(n)
else:
    dfs(0, 0, 0)
    print(answer)