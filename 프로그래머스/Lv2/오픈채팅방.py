'''
중복 닉넴 허용. 입출 메시지
"[닉네임]님이 들어왔습니다."/"[닉네임]님이 나갔습니다."
닉네임 변경법: 2가지
1. 채팅방 나가고, 새 닉네임으로 다시 들어감
2. 채팅방에서 닉네임 변경
변경 후, 기존 메시지의 닉넴도 모두 변경될 것
Muzi, Prodo 존재
"Muzi님이 들어왔습니다."
"Prodo님이 들어왔습니다."
"Muzi님이 나갔습니다."

Muzi 나감 -> Prodo로 변경 후 다시 들어옴
"Prodo님이 들어왔습니다." ---- 원래의 무지
"Prodo님이 들어왔습니다." ---- 원래의 프로도
"Prodo님이 나갔습니다." ---- 이전에 무지 나갔을 때
"Prodo님이 들어왔습니다." ---- 추가된 프로도

Prodo -> Ryan 닉변 시,
"Prodo님이 들어왔습니다."
"Ryan님이 들어왔습니다." ---- 원래의 프로도
"Prodo님이 나갔습니다."
"Prodo님이 들어왔습니다."
uid, 닉넴: 대소문자 구분. 닉넴. 아이디 모두 1~10 길이
''' 
result = []
def msg(inout, nicks):
    global result
    for hs, flag in inout:
        if flag: # 들어왔을 때
            result.append(nicks[hs] + '님이 들어왔습니다.')
        else:
            result.append(nicks[hs] + '님이 나갔습니다.')

def solution(record):
    inout = []
    nicks = dict()
    for rec in record:
        commands = rec.split()
        hs = hash(commands[1])
        if commands[0] == 'Leave':
            inout.append((hs, 0))
        else:
            nicks[hs] = commands[2]
            if commands[0] == 'Enter':
                inout.append((hs, 1))
    msg(inout, nicks)
    return result


def solution(record):
    result = []
    nicks = dict()
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for rec in record:
        commands = rec.split()
        hs = hash(commands[1]) # uid
        if commands[0] != 'Leave':
            nicks[hs] = commands[2]
    for rec in record:
        commands = rec.split()
        hs = hash(commands[1]) # uid
        if commands[0] in printer:
            result.append(nicks[hs] + printer[commands[0]])
    return result