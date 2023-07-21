# 지도에서 도시 이름 검색 -> 관련 게시물 읽기
# 캐시 적용 시 캐시 크기에 따른 실행 시간 측정
# 각 도시 이름은 공백,숫자,특수문자 없는 영문자로 구성. 대소 구분x
# 총 실행시간 출력 LRU(hit1, miss5)
from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = dict()
    que = deque([]) # 시간 deque
    curSize = 0 # cache 실제 저장된 개수
    for _city in cities:
        city = _city.lower()
        if city in cache and cache[city] > 0:
            answer += 1
            cache[city] = answer
            que.append([city, answer])
        else: # 새로 추가
            answer += 5
            curSize += 1
            cache[city] = answer
            que.append([city, answer])
            while curSize > cacheSize:
                key, time = que.popleft()
                if cache[key] == time: # 후에 업뎃 안 됨
                    cache[key] = -1
                    curSize -= 1
                    break
    return answer

# maxlen -> 초과시 가장 first 객체 제거되고 append됨
def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    time = 0
    for i in cities:
        s = i.lower()
        if s in cache:
            cache.remove(s)
            cache.append(s)
            time += 1
        else:
            cache.append(s)
            time += 5
    return time