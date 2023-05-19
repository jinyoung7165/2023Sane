# 100*100 table에서 가로,세로 봤을 때 가장 긴 회문 길이 구하기
# input() 한번에 하는 게 시간 효율에 좋다
# -> maps=[list(input()) for _ in range(100)]
def palindrome(row, start): # start: 이미 찾은 회문의 최대 길이
    cnt = start
    for size in range(start+1, 101): # 찾으려는 회문의 길이 # 2-100
        for i in range(0, 100-size+1):
            part = ''.join(row[i:i+size])
            if ''.join(part) == part[::-1]:
                cnt = size
                break # 더 큰 사이즈 찾자
    return cnt

for tc in range(1, 11): # 10 tc
    input()
    cnt = 1 # 기본 길이 1
    maps = [['']*100 for _ in range(100)]
    for _ in range(100):
        row = input()
        cnt = palindrome(row, cnt)
        for i in range(100): # 행열 바꿔 저장
            maps[i][_] = row[i]

    for _ in range(100):
        row = ''.join(maps[_])
        cnt = palindrome(row, cnt)

    print("#" + str(tc), cnt)
    
def solution():
    for tc in range(1, 11): # 10 tc
        cnt = 1 # 기본 길이 1
        maps = [list(input()) for _ in range(100)]
        
        for size in range(100, 1, -1): # 100~2 size 회문 찾기
            if palindrome2(maps, size): # 해당 크기 회문 찾으면 break
                cnt = size
                break
        print("#" + str(tc), cnt)
    
def palindrome2(arr, size):
    for i in range(100):
        for j in range(0, 100-size+1): # row 확인
            if arr[i][j] == arr[i][j+size-1]: # 양끝 값이 같을 때
                for k in range(1, size//2):
                    if arr[i][j+k] != arr[i][j+size-k-1]:
                        break
                else: return True
        for j in range(0, 100-size+1): # col 확인
            if arr[j][i] == arr[j+size-1][i]:
                for k in range(1, size//2):
                    if arr[j+k][i] != arr[j+size-k-1][i]:
                        break
                else: return True
        return False