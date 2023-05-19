# 자성체 성질->색. 푸른 s극. 붉은 n극
# (아래)s극 ->푸른붉은<- n극(위) 충돌 시 교착 상태
# 윗쪽에 n극(붉은) 1
# 아랫쪽에 s극(푸른) 2
# y축으로만 탐색하며 붉은->푸른 순서 찾아라
for tc in range(1, 11): # 10 tc
    input() # 100
    maps = [list(input().split()) for _ in range(100)]
    cnt = 0 # 교착상태 수
    for i in range(100):
        j = 0
        while j < 99: # j+1과 비교하기 때문
            if maps[j][i] == '1':
                while j < 98 and maps[j+1][i] != '2':
                    j += 1
                if maps[j+1][i] == '2':
                    cnt += 1
            j += 1
    print("#" + str(tc), cnt)