import sys

# 一只大鸡5块，一只母鸡3块，3只小鸡1块，用100元买100只鸡，问有几种方案？
# 5a + 3b + (100-a-b)/3 = 100
# 15a + 9b + 100 - a - b = 300
# 14a + 8b = 200 ———— b = 25-1.75a
# b需为整数，a=0, 2, 4, 8, 12 
a=[0,2,4,8,12]

for i,A in enumerate(a):
    B = 25 - 1.75*A
    C = 100 - A - B
    B = int(B)
    C = int(C)
    if A>=0 and B>=0 and C>=0 and A+B+C==100:
        print(str(A)+" "+str(B)+" "+str(C))
        

# 注意：涉及到浮点数计算时，哪怕最后的计算结果是个整数，它依然会带小数点，所以要控制浮点类型数据的输出形式

# 浮点输出方法
# 1.round函数
num = 3.1415926535
rounded = round(num, 2)  # 保留 2 位小数
print(rounded)  # 输出 3.14

rounded_int = round(num)  # 四舍五入取整
print(rounded_int)  # 输出 3

# 2.强制转换
num = 3.9
print(int(num))  # 输出 3（直接截断小数部分）

#使用 math.floor()（向下取整）
import math
num = 3.9
print(math.floor(num))  # 输出 3

# 使用 math.ceil()（向上取整）
import math
num = 3.1
print(math.ceil(num))  # 输出 4