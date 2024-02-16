# 공백문자가 연속해 나올 수 있음
def solution(s):
    s = list(s.lower())
    last = True # last가 공백인데, 지금 알파벳 나오면? 대문자로 바꿔라
    for i in range(len(s)):
        if s[i] == ' ': last = True
        elif last:
            last = False
            if s[i].isalpha(): s[i] = s[i].upper()
    return ''.join(s)