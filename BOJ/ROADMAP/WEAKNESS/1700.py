'''
멀티탭 스케줄링
물건 종류 k개 이하.
그 중 1개씩 중복조합해서 k번(1~100) 사용순서 주어짐
멀티탭 구멍 개수 n개 주어짐(1~100)
플러그를 빼는 최소 횟수
물건 모두 다른 종류로 k번 사용 -> k개의 플러그 필요
물건 1 종류로 k번 사용 -> 1개의 플러그 유지
물건 2 종류로 k번 사용 ->
  if 플러그가 1개면, 연속 같은 거 사용이 아닐 때마다 플러그 필요
  if 플러그가 2개면, 2개의 플러그 유지
물건 3 종류로 k번 사용 ->
 if 플러그가 1개면, 연속 같은 거 사용이 아닐 때마다 플러그 필요
 if 플러그가 2개면, 가장 먼 미래에 올 플러그 빼야 함
 if 플러그가 3개면, 3개의 플러그 유지
가장 먼 미래에 올 거를 빼자
현재로부터 가장 먼 미래를 찾아야 하므로... n*n 돼버림
-> 물건별 위치 나오는 모든 구해놓고, 해당 물건 쓸 때마다 pop...?
'''
n, k = map(int, input().split())
sequence = list(map(int, input().split()))
if n >= k: print(0)
else:
    pos = [[] for _ in range(101)] # 각 물건이 올 위치 리스트
    answer = 0
    plug = set()
    for i in range(k-1, -1, -1): pos[sequence[i]].append(i) # pop()하려고 각 원소가 나오는 위치 마지막부터 넣음

    for i, seq in enumerate(sequence):
        pos[seq].pop() # 얘가 나온 현재 위치 제거
        if seq not in plug: # 꽂혀있는 애가 아니다
            if len(plug) < n: plug.add(seq) # 여분 남았으면 그냥 꽂아
            else:
                M, rm = 0, 0 #  가장 마지막에 나올 플러그의 위치, 해당 플러그
                for p in plug: # 꽂힌 플러그 중, 제거할 애 찾음
                    if not pos[p]: # 다음에 안 나올 때
                        rm = p
                        break
                    elif pos[p][-1] > M: # 가장 나중에 오는 친구
                        M = pos[p][-1]
                        rm = p
                plug.remove(rm)
                plug.add(seq)
                answer += 1
    print(answer)