import sys

MASK = sys.stdin.readline().strip().split(".")
IP1 = sys.stdin.readline().strip().split(".")
IP2 = sys.stdin.readline().strip().split(".")
stat = -1

# 是否含有越界
for i in range(0,4):
    if int(MASK[i])>255 or int(MASK[i])<0 or int(IP1[i])>255 or int(IP1[i])<0 or int(IP2[i])>255 or int(IP2[i])<0:
        stat = 1

# 掩码是否符合格式
mask_b = ""
mask = ""
if stat != 1:
    for i in range(0,len(MASK)):
        section = format(int(MASK[i]),"08b")
        mask = mask + MASK[i]
        mask_b = mask_b+section
    if "01" in mask_b:
        stat = 1
    if mask == "255255255255" or mask == "0000":
        stat = 1

# 两个IP是否处于同一个子网
if stat != 1:
    for i in range(0,4):
        section_MASK = int(MASK[i])
        section_1 = int(IP1[i])
        section_2 = int(IP2[i])

        AND_1 = section_MASK & section_1
        AND_2 = section_MASK & section_2

        if AND_1 != AND_2:
            stat = 2
            break

    if stat != 2:
        stat = 0

print(stat)
    
#思路：先逐个检查IP，掩码的各个位置是否有越界0~255的情况；
#然后检查掩码是否符合格式，将掩码转换成【32位二进制码】，因为掩码左边全为1，右边全为0，所以不会存在"01"的子串，用来判断是否符合格式
#然后，对两个IP的各个位与掩码的各个位进行按位与，如果按位与的结果不同，则直接break返回不同

#-----
#1.按位与运算
#可以用&的方式对数值进行按位与（但是&接收的对象不可以为字符串，必须为整形数）