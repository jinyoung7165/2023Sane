'''
16bit. 주어진 입력
"opcode rD rA rB" 또는 "opcode rD rA #C"의 형태
rA, rB/C에 대해 op후 rD에 저장
bit마다 자리의 의미
0~4
'''
from sys import stdin
input = stdin.readline
OP = {'ADD': '0000',
      'SUB': '0001',
      'MOV': '0010',
      'AND': '0011',
      'OR': '0100',
      'NOT': '0101',
      'MULT': '0110',
      'LSFTL': '0111',
      'LSFTR': '1000',
      'ASFTR': '1001',
      'RL': '1010',
      'RR': '1011'
    }
# 0~4까지 OP
# 5 = 0
# 6~8 RD
# 9~11 RA
# OP[4] == 0 => 12~14 RB + 0
# OP[4] == 1 => 12~15 #C 
n = int(input())
for _ in range(n):
    comm = input().split()
    if comm[0] in OP:
        answer = OP[comm[0]] + '00' + bin(int(comm[1]))[2:].zfill(3) +  bin(int(comm[2]))[2:].zfill(3) + bin(int(comm[3]))[2:].zfill(3) + '0'
    else: # 뒤에 c가 붙음
        answer = OP[comm[0][:-1]] + '10'+ bin(int(comm[1]))[2:].zfill(3) + bin(int(comm[2]))[2:].zfill(3) + bin(int(comm[3]))[2:].zfill(4)
        
    print(answer)