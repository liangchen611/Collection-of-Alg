import sys

IP = sys.stdin.readline().strip().split(".")
IP_O = ""

for i in range(0,len(IP)):
    eight_bi = format(int(IP[i]),"08b")
    IP_O = IP_O+eight_bi
print(int(IP_O,2))

D_IP = sys.stdin.readline().strip()
D_IP = format(int(D_IP),"032b")

for i in range(0,4):
    section = D_IP[i*8:i*8+8]
    section = int(section,2)
    if i < 3:
        print(section,end=".")
    if i == 3:
        print(section)
    
#思路：
#通过结合int(n,i)将i进制的字符串n转换为十进制的字符串n'
#以及format(int(n),"032b")，将字符串n的数值传给format，然后将其转为补0的32位二进制数
#format接收的只能是十进制下的数值