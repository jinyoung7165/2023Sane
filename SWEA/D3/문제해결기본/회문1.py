# ispalindrome. 기러기, 스위스, 토마토
# 8*8 글자판에 원하는 길이를 가진 회문 개수 구하라(가로/세로 퍼즐)
for tc in range(1, 11): # 10 tc
    size = int(input()) # 크기 4인 회문
    cnt = 0
    maps = []
    for _ in range(8):
        row = input()
        for i in range(0, 8-size+1):
            part = str(row[i:i+size])
            if part == str(part[::-1]): cnt += 1
        maps.append(list(row))

    reverse = list(zip(*maps))
    for row in range(8):
        for i in range(0, 8-size+1):
            part = ''.join(reverse[row][i:i+size])
            if part == str(part[::-1]): cnt += 1

    print("#" + str(tc), cnt)

def palindrome(size, row):
    cnt = 0
    for i in range(0, 8-size+1):
            part = ''.join(row[i:i+size])
            if part == str(part[::-1]): cnt += 1
    return cnt
    
def solution():
    for tc in range(1, 3): # 10 tc
        size = int(input()) # 크기 4인 회문
        cnt = 0
        maps = [['']*8 for _ in range(8)]
        for _ in range(8):
            row = input()
            cnt += palindrome(size, row)
            
            for i in range(8): # 행열 바꿔 저장
                maps[i][_] = row[i]

        for row in range(8):
            cnt += palindrome(size, maps[row])

        print("#" + str(tc), cnt)

print(solution())