import sys

info = sys.stdin.readline().strip().split(" ")
info = [int(inf) for inf in info]
chats = []

for i in range(0,info[-1]):
    desk = sys.stdin.readline().strip().split(" ")
    desk = [int(d) for d in desk]

    stu1 = [desk[0],desk[1]]
    stu2 = [desk[2],desk[3]]

    chats.append([stu1,stu2])

x = {}
y = {}

for j in range(0,len(chats)):
    stu1,stu2 = chats[j][0],chats[j][1]
    x1,x2 = stu1[0],stu2[0]
    y1,y2 = stu1[1],stu2[1]

    #不同列交头接耳
    if x1 == x2:
        if min(y1,y2) not in y:
            y[min(y1,y2)]=1
            continue
        if min(y1,y2) in y:
            y[min(y1,y2)]+=1
    
    #不同行交头接耳
    if y1 == y2:
        if min(x1,x2) not in x:
            x[min(x1,x2)]=1
            continue
        if min(x1,x2) in x:
            x[min(x1,x2)]+=1
            
x = {k:v for k,v in sorted(x.items(),key=lambda item:item[1],reverse=True)}
y = {k:v for k,v in sorted(y.items(),key=lambda item:item[1],reverse=True)}

x = list(x.keys())
y = list(y.keys())

x = sorted(x[:info[2]])
y = sorted(y[:info[3]])

for i in range(0,info[2]):
    print(x[i],end=" ")
print()
for i in range(0,info[3]):
    print(y[i],end=" ")
    
'''
1.存放所有交头接耳对

2.根据不同的交头接耳对，可以根据它们的x和y坐标是否相同来判断，是横向还是竖向的

3.建立2个字典，分别记录横向和竖向的交头接耳的位置的对数，例如某个键值对x（3:3)，表示在第3开头的x向位置，有3对交头接耳的同学

4.对2个字典，根据他们的值进行排列，选出前k个和前l个对数最多的行和列

5.选出这些列后，再根据这些列的坐标大小进行排序，然后输出
'''

#1.基于字典键值对当中的值进行排序,结果返回另一个字典
# dict = {k:v, for k,v in sorted(x.items(),key=lambda item:item[1],reverse=True)}
# 首先，因为要组成一个键值对，所以形式上一定要是像k:v这样的对，然后，选择这样的对的来源
# 此处来源就是一个经过排序sorted之后的列表
# sorted的对象是x当中的键值对，排序的依据key，这里取lambda，lambda相当于函数中的自变量，item相当于x.items()中的其中任意一个值
# 具体排序依据就是item[1]，也就是字典的值
# reverse表示逆序排列

#——————————————————————————
#2.字典转列表
# 将键值对转列表： L = list(dict.items())
# 将值转列表： L =list(dict.value())

# 想要分离键值——ZIP
# 或者用MAP——映射函数

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 转换为键值对元组列表——MAP
result_list = list(map(lambda item: (item[0], item[1]), my_dict.items()))
print(result_list)  # 输出: [('a', 1), ('b', 2), ('c', 3), ('d', 4)]