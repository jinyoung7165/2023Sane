'''
열차 시간보다 앞선 인간 남았는데 막차 끝남 
    -> 마지막으로 보낸 차가 full이면, 마지막으로 온 애-1분
    -> 마지막으로 보낸 차가 full이 아니면, 막차 시간
앞선 인간 다 보냈는데 막차 안 끝남 -> 막차 시간
'''
def convert(string): # 09:00 -> 540
    h, m = map(int, string.split(':'))
    return h*60 + m
def convert_re(time):
    h, m = divmod(time, 60)
    return str(h).zfill(2) + ':' + str(m).zfill(2)
def solution(n, t, m, timetable):
    times = []
    for time in timetable:
        times.append(convert(time))
    times.sort() # 자기보다 크거나 같은 게 오기를 기다림
    train = 540
    candidate = 0
    for i in range(n):
        for j in range(m): # 최대 m명 나갈 수 있음
            if times and times[0] <= train: # 얘가 탈 수 있으면
                candidate = times.pop(0) - 1
            else: # 얘도 못 탄 상태로 끝날 수 있음
                candidate = train
        train += t # 다음 열차 시간

    return convert_re(candidate)