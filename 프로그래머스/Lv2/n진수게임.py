'''
숫자 하나씩 차례대로
0부터 시작. 0->1...->9
10 이상부터 한 자리씩 끊어 말함
1 0 1 1 1 2
이를 모두 이진수로 바꿔 한 자리씩 끊어 말함
0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1,
n진법으로 진행 시. 게임 참여자 m명 중, 나의 순서 p
나의 대답 총 t번을 구해서 출력하라(총 t자리)
'''
def convert(num:int, base:int):
    TMP = '0123456789ABCDEF'
    q, r = num // base, num % base
    return convert(q, base) + TMP[r] if q else TMP[r]

def solution(n:int, t:int, m:int, p:int):
    answer = ''
    tmp = ''
    for i in range(m*t): # m*t번의 대답
        tmp += convert(i, n) # 일단 그만큼의 수 모두 구해놓기
    for i in range(t): # t번 내 대답
        answer += tmp[p-1]
        p += m # m명 모두 거쳐야 다시 내 순서
    return answer


print(solution(2,4,2,1))