'''
이모티콘
3가지 연산 -> s개를 화면에 만들 것. 최소 시간?
1초씩 소요. 
1. 화면의 모든 이모티콘 복사해 저장(덮어쓰기. 이전 거 사라짐. 0개/일부 복사 불가)
2. 저장한 이모티콘 모두를 화면에 붙여넣기(누적)
3. 화면의 이모티콘 중 하나 삭제
초기 화면: 1개 존재
S (2 ≤ S ≤ 1000) 
visited를 한다면, (screen, clipboard)를 저장해서, 재방문하지 않도록
'''
from collections import deque
n = int(input())
answer = 0
que = deque([(1, 0, 0)]) # 화면 개수, 저장 개수, 시간
visited = set()
visited.add((1, 0))
while que:
    screen, clipboard, time = que.popleft()
    if screen == n:
        answer = time
        break
    if screen > 0:
        # 복사해 저장
        if (screen, screen) not in visited:
            visited.add((screen, screen))
            que.append((screen, screen, time+1))
        # 화면 거 하나 삭제
        if (screen-1, clipboard) not in visited:
            visited.add((screen-1, clipboard))
            que.append((screen-1, clipboard, time+1))
    if clipboard > 0:
        if (screen+clipboard, clipboard) not in visited:
            visited.add((screen+clipboard, clipboard))
            que.append((screen + clipboard, clipboard, time+1))
    
print(answer)