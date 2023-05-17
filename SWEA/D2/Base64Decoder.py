# 24비트 버퍼에 위쪽 MSB부터 한 BYTE씩 3BYTE(24bit)의 문자 넣음
# 버퍼 위(최상위비트) 6비트씩 잘라 읽고, 표의 문자로 encode
# encode된 string 주어졌을 때, 해당 string decode해 원문 출력하세요
# 문자열 길이 항상 4의 배수.
# encode된 한 문자 => 24비트(6비트*4)
# C->ord(C)->99->이진수 변환. 나머지 알파벳들 이어붙임 -> 24비트로 변환
# 24비트를 6비트씩 쪼개 처음부터 읽으며 64bit표에 맞춰 변환
#
tc = int(input())


tb = dict()
for i in range(ord("A"), ord("Z")+1):
    tb[chr(i)] = i-ord("A")
for i in range(ord("a"), ord("z") + 1):
    tb[chr(i)] = 26 + i - ord("a")
for i in range(10):
    tb[str(i)] = 52 + i
tb['+'] = 62
tb['/'] = 63

for _ in range(1, tc+1):
    encoded = input()
    bits = "" # 변환 전 비트
    answer = ""
    for el in encoded:
        bits += bin(tb[el])[2:].zfill(6)
    size = len(bits) // 8
    j = size
    for i in range(1, size+1): # 몫 1부터 시작 -> 8bit씩 잘라
        bit8 = bits[i * 8 - 8:i * 8]
        answer += chr(int(bit8, 2))

    print('#'+str(_), answer)