# Longest Palindromic Substring
# 가장 긴 팰린드롬 부분문자열 출력
# 투포인터, 슬라이딩 윈도우
# 각 원소끼리 비교해야 함 -> 엄청난 트리, dp로는 여부를 빠르게 아는 게 낫고
# 이 경우에는, left, right 부분합처럼 투포인터
# 1. 투포인터 -> 중앙을 중심으로 확장해 나가는 형태 빠름
# 시작점: 왼쪽에서부터 left, right 포인터(생성될 palindrome의 중앙을 상징)를 전진하며 시작(슬라이딩 윈도우. 주어진 문자열 처음부터 끝까지 순회해야 함)
# 홀수 길이 palindrome과 짝수 길이 palindrome의 비교를 위해서는 다른 idx 전달 필요
# 다른 경우로 취급해서 각각 봐야 함
def longestPalindrome(s):
# 팰린드롬이면 중앙부 확장해나감
    def expand(left, right): # s의 left~right를 중심부로 볼 것
        while 0 <= left < right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1 # 확장
        # while문 타면, 즉, left==right일 때
            # 이후 범위 벗어나면 (원래 left-1, 원래 right+1)될 것. 
            # left~right표현해야 하므로
            # s[left+1:right]하면 원래의 left~right
        # while문 아예 안 탈때, ex: abcd 전달해서
            # 짝수 ab mid일때, expand(0, 1)에서 while문 타지 않고, s[1:1]
            # 홀수 abc mid일때, expand(0, 2)에서 s[1:2] b (한자리 palindrome 완성)
        return s[left+1:right]
    result = ''
    if len(s) < 2 or s == s[::-1]: return s # s가 이미 palindrome인 거 알 수 있음
    for i in range(len(s)-1): # 생성될 palindrome의 중앙부 시작점 idx
        result = max(result, expand(i, i+1), expand(i, i+2), key=len) # 짝수일때(i~i+1), 홀수일때(i~i+2) mid전달 후 생성된 palindrome 갱신
    return result

# 2. dp -> 효율성 안좋음
def longestPalindrome(s: str) -> str:
    answer = s[0]
    size = len(s)
    dp = [[0] * size for _ in range(size)] # dp[i][j] : i == j 여부
    for i in range(size-1):
        dp[i][i] = 1
        if s[i] == s[i+1]:
            dp[i][i+1] = 1 # 2개 붙어있는 거
            if len(answer) == 1:
                answer = s[i:i+2]
    dp[size-1][size-1] = 1

    for gap in range(1, size-1):
        for i in range(size-gap-1): # 시작점
            j = i + gap + 1 # 끝점
            if s[i] == s[j]: # 양끝이 같으면 그 사이 누적 dp를 봐야 함
                if dp[i+1][j-1] == 1: # i+1~j-1이 팰린드롬이었으면
                    dp[i][j] = 1 # i~j로 확장
                    if len(answer) < gap + 2:
                        answer = s[i:j+1]
    return answer