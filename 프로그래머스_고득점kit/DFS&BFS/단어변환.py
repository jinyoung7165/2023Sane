# 두 단어 begin, target과 단어 집합 words
# begin->target 단어로 변환하는 가장 짧은 과정
# 1번에 1개 알파벳만 바꿀 수 있음
# words에 있는 단어로만 변환할 수 있음
# hit->cog, words=["hot","dot","dog","lot","log","cog"]
# hit->hot->dot->dog->cog 총 4단계 거쳐야 함
# 모든 단어의 길이는 같음. begin, target 같지 않음
# words에 중복되는 단어는 없음
# 변환 불가 시 0 리턴
# hit->cog, words=["hot","dot","dog","lot","log"]
# 변환불가(words에 애초에 cog없음)=>0
from collections import deque
def solution(begin, target, words):
    answer = 0
    size = len(words)
    visited = [False] * size
    if target not in words: return 0
    que = deque([(begin, 0)])
    while que:
        cur, cnt = que.popleft()
        if cur == target: return cnt
        for i in range(size):
            if visited[i]: continue
            diff = set(enumerate(cur)) - set(enumerate(words[i]))
            if len(diff) == 1:
                visited[i] = True
                que.append((words[i], cnt+1))
            
    return answer