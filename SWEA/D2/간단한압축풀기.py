# 너비가 "10"인 여러 줄의 문자열
# 마지막 줄 제외하고, 빈공간 없이 알파벳으로 채워져 있고, 마지막 줄은 왼쪽부터 채워져있음
# 이 문서를 압축한 문서는 알파벳, 연속 개수로 이뤄진 쌍 나열
# A 5 == AAAAA
# 압축 문서를 받아 원본을 만들어라
# A 10 -> AAAAAAAAAA
# B 7  -> BBBBBBBCCC
# C 5  -> CC
tc = int(input())

for i in range(1, tc+1):
    print('#{}'.format(i))
    n = int(input()) # n줄 입력 받을 것
    tmp = ""
    for _ in range(n):
        char, cnt = input().split()
        cnt = int(cnt)
        tmp += char*cnt

    tmp_list = list(tmp)
    for j in range(0, len(tmp), 10):
        print(''.join(tmp_list[j:j+10]))
        

def another():
    print('#{}'.format(i))
    n = int(input()) # n줄 입력 받을 것
    tmp = ""
    for _ in range(n):
        char, cnt = input().split()
        cnt = int(cnt)
        tmp += char*cnt
        
    for i in range(len(tmp)):
        if (i+1) % 10 == 0: # 10으로 나눠떨어지는 문장의 끝
            print(tmp[i])
        else: # 문장의 끝 아님
            print(tmp[i], end="")
    print()