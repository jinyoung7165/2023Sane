'''
멀티탭 스케줄링
사용 순서 기반으로 플러그 빼는 횟수 최소화
3구 멀티탭. 사용 패턴 주어짐
A->B->C->D->A->B
D 사용 전, C 플러그 빼면 최소 제거 비용 : 1
2구 멀티탭. 
2 3 2 3 1 2 7
2323 그대로 쓰다가. 3빼고, 1빼면 됨 : 2
나중에 사용하지 않을 애, 가장 나중에 재사용할 애 뽑아야 함
'''
n, k = map(int, input().split()) # 멀티탭 구멍 수, 총 사용 패턴 길이(100이하)
record = list(map(int, input().split())) # 각 제품 이름은 1~k이하 자연수로 주어짐

tabs = [] # 현재 사용중
using = 0 # 사용 중인 구멍
answer = 0 # 뺀 횟수
for idx, rec in enumerate(record):
    if rec in tabs:
        continue # 이미 사용 중
    if using < n:
        tabs.append(rec)
        using += 1
    else:
        answer += 1 # 하나 골라서 빼야 함
        after = record[idx+1:]
        selected, selectedIdx = None, -1
        for tab in tabs: # 사용 중인 것 중
            # 나중에 필요하지 않은 원소 제거
            if tab not in after:
                selected = tab
                break
            # 가장 나중에 필요한 원소 제거
            idx = after.index(tab)
            if idx > selectedIdx:
                selectedIdx = idx
                selected = tab
        tabs.remove(selected)
        tabs.append(rec)
                
print(answer)