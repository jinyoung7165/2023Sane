# L의자. X=0시계방향으로 돌며 L-1위치까지 놓임
# 초밥은 각 의자 앞에 여러 개 가능. 1초에 한 칸씩 시계회전
# 초밥벨트 위 처음엔 0개. 의자 위 사람도 0. 오는 손님의 이름 모두 다름
'''
시간이 무한히 흘렀을 때 만들어진 모든 초밥은 손님에 의해 다 사라지며, 손님 역시 정확히 n개의 초밥을 먹고 코드트리 오마카세를 떠나게 됨
100 T X NAME ) 초밥을 T초에 X앞에 있는 벨트 위에 NAME 초밥 놓음. 같은 위치에 여러 개의 같은 NAME 초밥 가능
200 T X NAME N) NAME 손님이 시각 T에 위치X에 앉아 NAME 적힌 초밥 N개 먹고 떠남. 동시에 여러 개 먹기 가능. 다 못 먹으면 계속 기다림
300 T ) T초에 1->2 과정 후, 현재 남아있는 손님 수 공백 초밥 수 출력
L 엄청 큼-> [[] for _ in range(l)] 이거보단, name기준으로 각 위치 리스트 저장

손님 앉혀두고, 1초 지날 때마다 손님 앞의 초밥 이동함
"손님이 초밥을 먹는 시각"을 효율적으로 구해야 함

L, t의 범위 엄청 큼. 명령의 범위는 작음(주어지는 t의 개수 작음)
t초에 손님이 p위치에 있어야 먹을 수 있으면,
T초에 ((T-t)+p)%L 위치 시 먹을 수 있음

t초에 p위치에 앉은 손님이 먹을 수 있는 초밥: t-1초에 p-1위치의 초밥... t초~미래에는 p위치의 초밥 놓여지면 바로
초밥 = name: {t: p, t: p} 저장
손님 = name: [t, p, 남은 할당량] 저장

틀린 이유:
손님이 exit하는 time은, 초밥이 들어온 st 순서대로 먹는 게 아니라,
회전한 다음 최종적으로 먹히게 되는 ft 순서대로 할당량을 채워야 함
'''
from collections import defaultdict
l, q = map(int, input().split())
ccount, scount = 0, 0 # customer, sushi count
customer = defaultdict(list)
# name: [t, p, 남은 할당량] 저장
sushi = defaultdict(dict)
# name: {t: p, t: p} 저장

# t초에 x위치에 앉은 손님이 먹을 수 있는 초밥: t-1초에 x-1위치의 초밥... t초~미래에는 x위치의 초밥 놓여지면 바로
commands = []
# 모든 명령 바로바로 실행하지 말고,
# 초밥이 손님 온 뒤로 언제 먹혀지는지부터 알아낸 다음에, 명령 실행하며 명령 시점 비교하는 게 낫다
for _ in range(q):
    command, t, *detail = input().split()
    if command == '100': # 초밥 = name: {t: p, t: p} 저장
        x, name = detail
        t, x = int(t), int(x)
        sushi[name][t] = x
    elif command == '200': # 손님 = name: [t, p, 남은 할당량] 저장
        x, name, n = detail
        t, x, n = int(t), int(x), int(n)
        customer[name].append(t)
        customer[name].append(x)
    else:
        t = int(t)
    commands.append((command, t))

# 손님 = name: [t, p, 남은 할당량] 저장
for name, val in customer.items():
    ct, cp = val
    exit_time = 0 # 손님이 exit하는 time은, 초밥이 들어온 st 순서대로가 아닌, 최종적으로 먹히게 되는 ft를 고려해야 함
    for st in sushi[name]:
        if st <= ct: # 초밥 놓은 다음 사람 옴
            np = (sushi[name][st] + (ct-st))%l # ct일 때, 초밥의 위치
            # np -> cp 가려면 기다려야 하는 시간
            wait = (cp - np) % l
            # 회전하며 최종적으로 먹히는 시간
            ft = wait + ct
        else: # 사람 온 다음에 초밥 놓음
            np = sushi[name][st]
            # sushi[name][st] -> cp 가려면 기다려야 하는 시간
            wait = (cp - sushi[name][st]) % l
            # 회전하며 최종적으로 먹히는 시간
            ft = wait + st
        commands.append(("111", ft)) # ft에 del sushi[name][st] 초밥 제거
        exit_time = max(exit_time, ft)
        
    commands.append(("222", exit_time)) # 가장 마지막 ft에 손님 제거

commands.sort(key=lambda x: (x[1], x[0])) # 먹고 초밥/손님 제거하는 명령 추가했기 때문에, 시간 순, 명령번호 순 정렬
for c, t in commands:
    if c == '100':
        scount += 1
    elif c == '111': # 초밥 제거
        scount -= 1
    elif c == '200':
        ccount += 1
    elif c == '222': # 손님 제거
        ccount -= 1
    else:
        print(ccount, scount)