# 2018 KAKAO BLIND [3차] 자동완성
# prefix 문제. 원소 엄청 많음 -> Trie 자료구조 사용
# 문자열 학습해서 다음 입력에 활용. go 있으면, g만 입력해도 go 추천 -> o 입력할 필요x
# 학습 단어들의 prefix 같은 경우, 같지 않을 때까지 계속 입력해야 함
# go, gone, guild 있을 때
# gu까지만 입력하면 guild 완성
# go -> go, gon -> gone, gu -> guild. 총 7문자 입력해서 3단어 찾을 수 있음
'''
Trie에 미리 삽입(등록) go 삽입: root!->g(1)->o(1)->none(1), gone 추가:  root!->g(2)->o(2)->[none, n(1)->e(1)]
검색: word1 찾을 건데,
1) prefix 밑에 달린 leaf 1개면, 해당 단어만 달려 있는 것 -> prefix len만 탐색하면 됨
2) leaf 여러 개 달리면, prefix 크기 늘려서 그 밑 단어(leaf) 1개 될 때까지 탐색
'''
class Node:
    def __init__(self, char):
        self.char = char
        self.cnt = 1 # 해당 노드에서 출발했을 때, leaf로 가는 갈래(단어) 개수
        self.children = {}
        
def solution(words):
    answer = 0
    
    # 트라이 생성, 삽입
    root = Node("!")
    for word in words: # [go, gone, guild]
        parent = root # "!" 맨 위에서 볼 것
        
        for c in word: # go: g, o
            if c in parent.children.keys():
                # 부모 알파벳에 이미 달려 있으면, 부모 따라서 도착할 leaf(단어) 하나 더 추가될 것 
                # (g->o(1)->nothing 존재. g->o(2)->ne 추가할 것)
                parent.children[c].cnt += 1
            else: # 부모 알파벳에 달려 있지 않으면, 해당 알파벳 노드 달기 g(leaf로 가는 갈래:1)->o(1)->none
                parent.children[c] = Node(c)
            parent = parent.children[c] # ! -> g로 내려감 -> o 달 것
    
    # 검색
    for word in words:
        parent = root # "!" 맨 위에서 볼 것
        cnt = 0 # 만난 알파벳 개수
        
        for c in word: # go: g->o
            parent = parent.children[c]
            cnt += 1
            if parent.cnt == 1: break # 해당 알파벳으로부터 도착하는 단어 개수가 1개이면 stop(none도착 or 갈래1개)
        
        answer += cnt
    
    return answer