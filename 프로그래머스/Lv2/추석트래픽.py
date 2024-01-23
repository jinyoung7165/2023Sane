# 초당 최대 처리량
# "1초"간 처리하는 요청 최대개수(완료 여부x)
'''
응답완료시간s, 처리시간t
t:시작, 끝포함 -> 시작 시간은, [s-t+0.001] ~ [s]
늦게 끝나고 짧은 애부터 보면서. 
현재 애의 start - 1 + 0.001~ 다음 애의 end + 1 - 0.001 겹침 (기록 시 0.001 버림)
겹치지 않으면, 다음 다음으로 넘어감
'''
def solution(lines):
    answer = 0
    log = [] # log의 (시작시간, 끝시간) 저장

    for line in lines:
        date, s, t = line.split() # 날짜, 응답완료시간, 처리시간
        s = s.split(':')
        t = t.replace('s', '')

        end = (int(s[0])*3600 + int(s[1])*60 + float(s[2])) * 1000 # 끝시간을 msec 단위로 저장
        start = end - float(t)*1000 + 1 # 시작 시간을 msec 단위로 저장
        log.append([start, end])

    for x in log:
    	# 최대 초당 처리량 구하기. start 범위에 속하는지. end 범위에 속하는지 둘 중 max가 답
        answer = max(answer, throughput(log, x[0], x[0] + 1000), throughput(log, x[1], x[1] + 1000))

    return answer

# 초당 처리량을 구하는 함수
def throughput(log, start, end):
    cnt = 0
    for x in log:
        if x[0] < end and x[1] >= start:
            cnt += 1
    return cnt