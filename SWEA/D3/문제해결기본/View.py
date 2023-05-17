# 빌딩 좌우 밀집 지역
# 왼/오 창문 열었을 때, 양쪽 모두 거리 2 이상의 공간 확보 필요
# 조망권 확보된 세대 수 반환
# 0<=가로<1000. 0<높이<=255 (해당 땅에 빌딩 없을 시 높이 0)
# 맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 항상 건물 없어 높이 0

for _ in range(1, 11):
    answer = 0
    n = int(input()) # 건물 개수
    builds = list(map(int, input().split())) # 0~n-1
    for i in range(2, n-2): # 빌딩 순회하자. 양끝 4개는 0(건물 없음)
        cur = builds[i]
        l1 = cur - builds[i-2]
        l2 = cur - builds[i-1]
        r1 = cur - builds[i+1]
        r2 = cur - builds[i+2]
        if l1>0 and l2>0 and r1>0 and r2>0:
            answer += min(l1, l2, r1, r2)
        
    print("#"+str(_), answer)
    
    '''
8
0 0 3 5 2 4 9 0 6 4 0 6 0 0
    '''