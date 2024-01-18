'''
len(name) * A로 이뤄진 문자열 -> 조작을 통해 name으로
0: (알파벳+1) % 26
1: (알파벳-1) % 26
2: 커서 왼쪽으로 이동(0 -> len(name)-1)
3: 커서 오른쪽으로 이동(len(name)-1 -> 0)
(left) aaaa (size-right)
주의1. a로 시작하거나 a로 끝나는 문자열의 경우(aaaab), 2를 곱하지 않음 -> 중앙의 a 뭉탱이 공식만으로는 구할 수 없음
주의2. 크기 다양한 A뭉탱이 여러 개 -> 어느 뭉탱이를 분기점으로 삼을지 몰라서 다 해봐야 함
전진하면서 i지점에서 a 뭉탱이 만난 "순간",
[0~i + (a뭉탱이 pass) + 뭉탱이 끝~전체 문자열 끝] 최단 경로 구하는 방법
(1) 0->i + i->0(후진) + 0->a뭉탱이 끝(후진)
(2) 0->a 뭉탱이 끝(후진) + a뭉탱이 끝->0 + 0->i
'''
# 1. Greedy 훨씬 빠름
def solution(name):
    size = len(name)
    lr, ud = size - 1, 0
    for i in range(size):
        ud += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        # 해당 알파벳 바로 옆의 연속된 A 뭉탱이 찾기
        right = i+1
        while right < size and name[right] == 'A':
            right += 1 # A 뭉탱이 끝
        # 1. 초기값: 이름길이-1 (쭉 직진해서 다 봄)
        # 2. 0->i + i->0(후진) + 0->a뭉탱이 끝(후진)
        # 3. 0->a 뭉탱이 끝(후진) + a뭉탱이 끝->0 + 0->i
        lr = min(lr, 2*i + size-right, 2*(size-right) + i)
    return lr + ud

# 2. Bruteforce size 20 제한 있기 때문에 사용
# name -> AAAA 만들면 끝
# JAB(AA..A)DBBC 일 때, JAB+후진+CBBD 방문이 최소. A일지라도, 재방문 가능
# 언제까지 재방문할 것인가? 이미 lr 나왔을 때, 계보다 이동수가 크면 안됨
def solution(name):
    size = len(name)
    init = 'A' * size
    updown, lr = 0, float('inf')
    for i in range(size):
        updown += min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        
    def dfs(idx, count, string):
        nonlocal lr
        if count >= lr: return
        tmp = string[idx]
        string[idx] = 'A'
        if ''.join(string) == init:
            lr = count
            string[idx] = tmp
            return
        for i in [(idx+1)%size, (idx-1)%size]:
            dfs(i, count+1, string)
        string[idx] = tmp
    dfs(0, 0, list(name))
    return updown + lr