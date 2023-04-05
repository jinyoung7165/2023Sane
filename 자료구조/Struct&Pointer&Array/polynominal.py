# 다항식을 배열에 저장
# x^5 + 6x + 3
# 모든 항을 배열에 저장 -> 100063 => 각종 연산 간단
# 0이 아닌 계수를 지수와 저장 -> [1,5],[6,1],[3,0] => 공간 효율
# 입력된 2 다항식의 합을 화면에 표시하라
# 다항식의 차수는 최대 5를 넘지 않는다

'''
모든 항을 배열에 저장하는 방식 -> 두 다항식 배열 크기 맞춰 같이 pos이동 -> 0으로 이미 차있기 때문에 연산 가능
조건문 주목! or로 항이 남아있기만 하면 while문 안에서 해결
'''
class poly1():
    def __init__(self, coef):
        self.coef = coef # 계수 리스트
        self.degree = len(coef) # 차수
    
    def print_poly(self):
        for i in range(self.degree):
            if i == self.degree - 1: # 가장 마지막=상수항
                if self.coef[i] != 0: # 계수가 있으면
                    if self.coef[i] > 0:
                        print(" + ", end='')
                    else:
                        print(" - ", end='')
                    print("%0.2f" % (abs(self.coef[i])))
                else:
                    print() #상수항이 0인 경우
            else:
                if self.coef[i] != 0: # 계수가 있으면
                    if i == 0: # 첫 번째 항에 abs할 필요없이 바로 부호 붙일 것
                        print("%0.2fx^%d" % (self.coef[i], self.degree-i-1), end='')
                    else:
                        if self.coef[i] > 0:
                            print(" + ", end='')
                        else:
                            print(" - ", end='')
                        print("%0.2fx^%d" % (abs(self.coef[i]), self.degree-i-1), end='')
    def cal_y(self, x): # x를 대입한 식의 y값
        pos = self.degree # 현재 계산 중인 항의 차수
        sum = 0
        for i in range(self.degree): # 모든 항 훑어라
            temp = 1
            for _ in range(pos - 1): # x의 거듭제곱
                temp *= x
            if pos == 1: # 상수항이면 계수 1
                temp = self.coef[i]
            else:
                temp *= self.coef[i]
            sum += temp # 현재 항까지 더한 결과
            pos -= 1 # 다음항
                
        print('결과 값은 %0.1f' %sum)
        
def add_poly(a, b):
    z = [] # 두 다항식 덧셈 결과값
    apos = bpos = 0 # 두 다항식의 현재 위치             
    adeg = a.degree # a 다항식의 차수
    bdeg = b.degree # b 다항식의 차수
    
    # 두 다항식 모두 순회 끝날 때까지
    while (apos < adeg) or (bpos < bdeg):
        print(adeg, bdeg, z)
        if adeg > bdeg: # 애초에 최고차수가 더 크면 합산 불가
            z.append(a.coef[apos]) # 항 더함
            apos += 1
            adeg -= 1 # a다항식 다음 항 훑자
        elif adeg < bdeg: # 차수가 더 크면 합산 불가
            z.append(b.coef[bpos]) # 항 더함
            bpos += 1
            bdeg -= 1 # 다음 항 훑자
        else: # 차수 같으면 연산 가능. 계수 0이라도 더함
            z.append(a.coef[apos] + b.coef[bpos])
            apos += 1 # 같은 차수끼리 계속 더함
            bpos += 1
            # adeg -= 1
            # bdeg -= 1 0으로 채워져있기 때문에 이후는 deg가 맞춰짐
        print(adeg, bdeg, z)
    return poly1(z)


a = list(map(float, input("수식 1을 입력하세요 : ").split(' ')))
while len(a) > 6:
    a = list(map(float, input("최대 차수를 초과하였습니다. 다시 입력해주세요! : ").split(' ')))
b = list(map(float, input("수식 2를 입력하세요 : ").split(' ')))
while len(b) > 6:
    b = list(map(float, input("최대 차수를 초과하였습니다. 다시 입력해주세요! : ").split(' ')))

a = poly1(a)
b = poly1(b)
c = add_poly(a, b)
print('수식 1은 ', end='')
a.print_poly()
print('수식 2는 ', end='')
b.print_poly()
print('수식 1 + 2는 ', end='')
c.print_poly()

x = 2 # x값이 2라고 할 때, a식의 결과값(y)를 구하라
a.cal_y(x)