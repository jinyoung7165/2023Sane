# 공백문자가 연속해 나올 수 있음
def solution(s):
    def conv(_s):
        res = ''
        if len(_s) > 1: right = ''.join(list(map(lambda x: x.lower(), _s[1:])))
        else: right = ''
        if _s[0].isdigit():
            res = _s[0] + right
        else:
            res = _s[0].upper() + right
        return res
    
    answer = []
    last = ''
    for _s in s:
        if _s == ' ':
            # 문자였으면
            if last != ' ':
                answer.append(conv(last))
                last = ' '
            answer.append(' ')
        else:
            if last == ' ':
                last = _s
            else:
                last += _s
    if last != ' ': answer.append(conv(last))
    return ''.join(answer)