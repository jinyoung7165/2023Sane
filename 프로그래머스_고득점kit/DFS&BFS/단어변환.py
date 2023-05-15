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
import heapq
from collections import defaultdict
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    que = []
    size = len(words)
    visited  = defaultdict(size+1)# 각 words를 방문하기까지의 최소 거리
    # 변환 수, 현재 단어, 사용한 word
    heapq.heappush(que, (0, begin))
    while que:
        cost, cur = heapq.heappop(que)
        if cur == target:
            answer = cur
            break
        if visited[cur] < cost: # 더 최단거리로 방문한 경험 있으면
            continue
        visited[cur] = cost # 방문처리
        for word in words:
            diff = set(enumerate(cur))-set(enumerate(word))
            if len(diff) == 1 and visited[word] == size+1: # 알파벳 1개 차이
                heapq.heappush(que, (cost+1, word))
    return answer