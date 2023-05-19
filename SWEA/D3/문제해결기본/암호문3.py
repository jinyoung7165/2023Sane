# 0-999999 사이 수 나열한 암호문
# I x y s:  x 다음, s(여러 개)를 y개 삽입
# D x, y : x 다음부터 y개의 숫자를 삭제
# A y s : 맨 뒤에 y개 숫자 덧붙임
# 명령어 주어졌을 때, 암호문 수정하고, 처음 10개의 숫자 출력하라
# 원본 암호문 길이 N (10~20)
# 원본 암호문
# 명령어 개수 (5~10)
# 명령어
for t in range(1, 11):
    input() # 원본 암호문 길이
    origin = list(input().split()) # 원본 암호문
    n = int(input()) # 명령어 개수
    inst = list(input().split()) # 명령어
    i = 0
    while i < len(inst):
        if inst[i] in ('I', 'D', 'A'):
            ins = inst[i]
            tmp = []
            i += 1
            while i < len(inst) and inst[i].isdigit():
                tmp.append(inst[i])
                i += 1
            if ins == 'I':
                x, y, *s = tmp
                x = int(x)
                for j in range(int(y)):
                    origin.insert(x+j, s[j])
            elif ins == 'D':
                x, y = map(int, tmp)
                for j in range(y):
                    if len(origin)<=x: break
                    del origin[x]
            else:
                y, *s = tmp
                origin.extend(s)
    print("#" + str(t), *origin[:10])