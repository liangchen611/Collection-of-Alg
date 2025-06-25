import sys

ST = sys.stdin.readline().strip().split(" ")
u = ST[0]+ST[-1]
odds=[]
evens=[]
u2 = []

end = 0
if len(u)%2 == 0:
    end = len(u)-1
if len(u)%2 != 0:
    end = len(u)

i=0
while i < end:
    odds.append(ord(u[i]))
    try:
        evens.append(ord(u[i+1]))
        i = i + 2
    except:
        break
odds = sorted(odds)
odds = [chr(asc) for asc in odds ]
evens = sorted(evens)
evens = [chr(asc) for asc in evens]
longer = 1 if len(odds)<len(evens) else 0

for i in range(0,min(len(evens),len(odds))):
    u2.append(odds[i])
    u2.append(evens[i])
    if i == min(len(evens),len(odds))-1:
        if len(odds)==len(evens):
            break
        if longer == 0:
            u2.extend(odds[i+1:])
        if longer == 1:
            u2.extend(evens[i+1:])    

for i in range(0, len(u2)):
    t = u2[i]
    if not ("0"<=t<="9" or "a"<=t<="f" or "A"<=t<="F"):
        print(t,end="")
    else:
        t = format(int(t,16),"04b")[::-1]
        t = int(t,2)
        t = format(t,"X")
        print(t,end="")
        
#思路：先计算字符串的长度的奇偶性，防止越界，若为偶数，则遍历字符串的终点为len-1
#使用while循环，将str[i]和str[i+1]分别存放到奇数位数组odds和偶数位数组evens中，分别将odds和evens中的值都用ord转ascii，再用sort进行排序，再chr转回
#比较odds和evens的长度，用longer标识，然后用for循环，逐步将odds[i]和evens[i]增加到u中
#直到i=min(len(odds),len(evens))-1，根据longer标识，使用extend对u进行补充，odds或evens较长的一方中剩下的值[i+1:]

#对u的0~F，先用int(u,16)转16进制（整型），再用format(int(u,16),"04b")转四位二进制数（字符串型），然后用[::-1]翻转，
#再用一次int(u,2)转回二进制（整型），最后再用format(u,"X")转为大写十六进制（字符型）
#|
#————————————
#|
#——【extend（元素）和append（对象）函数】——
# extend() 和 append() 是 Python 列表中常用的两个方法，都用于向列表中添加元素，但它们的行为完全不同。
# append()：把整个对象作为一个元素添加到列表末尾，如果对象是一个列表，那么加入到列表中的也会是一个列表
# extend()：将一个可迭代对象的所有元素逐个添加到列表末尾
# 即，append添加的是整个对象，且append并不要求对象的类型；extend内部必须是一个可迭代对象，它添加的是对象中的每个元素


#——【format函数】——
# format转换的结果是一个字符串
# 将单个数值，字符串等对象进行格式化，只能接受1个处理对象，不能接受容器或一组对象
# 例如，以下的格式是合法的：
# format(3.14159, '.2f')  # 输出: '3.14'——浮点数的格式化
# format("Hi", '>10')  # 输出: '        Hi'——字符串右对齐，宽度10


#——【进制转换法（int和format)】——
# 通过int和format都可以转换格式，不过二者有所区别
# int(n,2),int(n,8),int(n,16)——将十进制的n转换为相应的进制，返回的数值依然为【整型数】
# 如果int【接收了超过进制上限的值，会发生错误】，例如int("G",16)，G越界，会报错



# format(num, "格式码“)——将数值按照格式码，转换为对应进制下的表示，返回的结果是【字符串】（不包括0x)

# 【格式码】：指定转换后的输出格式，格式为：[填充符][对齐方式][宽度][类型码]
# 填充符：左侧数位的填充字符，一般为0
# 对齐方式：一般可以用【>】让输入进行右对齐
# 宽度：表示输出的字符串为多少位
# 类型码：进制，一共有5种选择
# 【b——二进制， o——八进制，d——十进制，x——小写十六进制，X——大写十六进制】
# 例如，format(int(n,2),"04x")，先将n转换为2进制整型数，然后转换为0填充的4位小写十六进制的字符串。