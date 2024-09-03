a = [[[1], [2]],[[1], [2]]]
b = [[j[:] for j in r] for r in a]
a[0][0][0] = 100

print(b)

c = [[0,1]]
c[0][0] = 2 # [[2, 1]]
c[0] = 1, 2 # [(1, 2)]
c[0] = [1, 2] # [[1, 2]]
print(c)

print(format( (( 0b1010 >> 1 )) , 'b'))
print(format( ( 0b1010 << 1 ) , 'b'))
'''
2진수로 입력받기
n = int(input(), 2)
'''

print(int('1010', 2) >> 1)
print(bin(int('1010', 2) >> 1)[2:].zfill(8))
print(bin(int('1010', 2) << 1)[2:].zfill(8))

print(-1%4)

if 1: print("1")
if -1: print('-1')
if 2: print('2')
if 0: print('0')
if not 2: print('not 2')


print("ABA" in "BBBBABACC")