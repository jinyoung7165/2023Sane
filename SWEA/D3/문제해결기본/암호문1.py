# 0-999999 사이 수 나열한 암호문
# | x y s:  x-1 idx 다음, s(여러 개)를 y개 삽입
# 명령어 주어졌을 때, 암호문 수정하고, 처음 10개의 숫자 출력하라
# 원본 암호문 길이 N (10~20)
# 원본 암호문
# 명령어 개수 (5~10)
# 명령어
for t in range(1, 11):
    input() # 원본 암호문 길이
    origin = list(input().split()) # 원본 암호문
    input()
    inst = list(input().split('I ')) # 명령어
    for ins in inst:
        cur = ins.split()
        if cur: # x는 9까지만
            x, y, *s = cur
            x, y = int(x), int(y)
            if x <= 9: # 명령어 처리해야함
                for i in range(y):
                    if x + i > 9: break
                    origin.insert(x+i, s[i])
    print("#" + str(t), *origin[:10])