# 8개의 숫자->암호
# 홀수 자리 합*3 + 짝수 자리 합 = 10의 배수 돼야함
# 88012346 -> (8+0+2+4)*3 + (8+1+3+6) = 60 == 10의 배수
# 10의 배수가 아니라면 잘못된 암호코드
# 스캐너는 암호코드 1개 포함된 직사각형 배열(1/0) 읽음
# 숫자 하나는 7비트로 암호화됨. 가로 길이:56(7*8)
# 2차원 배열 입력받아 올바른 암호코드인지 판별
# 옳은 코드인 경우, 숫자 합 출력. 잘못된 경우 0
# 0 1 0 1
# 0 - 9 나타내기
dic = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}
tc = int(input())
for T in range(1, tc+1):
    n, m = map(int, input().split())
    maps = [input() for _ in range(n)]
    answer = 0
    null = '0'*m
    code = ""
    origin = []
    for row in range(n):
        if maps[row] == null: continue
        flag = 0 #1->0->1 찾자
        for col in range(1, m):
            if flag == 16 and maps[row][col]=='0':
                break
            if maps[row][col] > maps[row][col-1]: # 1<-0
                flag += 1
            if flag > 0: # 1발견 이후
                code += maps[row][col]
        code = code.zfill(56)
        break
    for i in range(0, 56, 7):
        origin.append(dic[code[i:i+7]])
    s = sum(origin)
    tmp = 0
    for i in range(1, 8, 2):
        tmp += origin[i]
    
    if ((s-tmp) * 3 + tmp) % 10 == 0:
        answer = s
    print("#"+str(T), answer)