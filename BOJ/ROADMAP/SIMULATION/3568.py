'''
isharp
배열[], 참조&, 포인터*는 순서에 상관없이 혼합해 사용
i#은 여러 변수를 한 줄에 정의
공통 변수형 제일 먼저 쓰고, 다음에 각 변수 이름과 추가적 변수형
int& a*[]&, b, c*
int*& a == int a&*
변수 오른편에 있는 형은 왼편에 붙일 수 있음
한줄에 하나씩 선언
int& a*[]&, b, c*;
=>
int&&[]* a;
int& b;
int&* c;
'''
sentence = input().rstrip()
common = sentence.split()[0]
vars = sentence[len(common)+1:-1].split(', ')
type = {'[':']', ']':'[', '*':'*', '&':'&'}
result = []
for i in range(len(vars)):
    cur = vars[i]
    size = len(cur)
    tmp = []
    for j in range(1, size):
        if cur[j] in type:
            tmp.append(type[cur[j]])
    var = len(tmp)
    result.append(common+''.join(tmp[::-1])+' '+vars[i][:size-var]+';')

for res in result:
    print(res)