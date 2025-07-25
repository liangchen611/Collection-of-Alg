import sys

pairs = input()
pairs = int(pairs)
datasheet = {}

for i in range(0,int(pairs)):
    index, value = map(int, input().split())
    if index in datasheet:
        datasheet[index] += value
    else:
        datasheet[index] = value

for index in sorted(datasheet.keys()):
    print(index, end=" ")
    print(datasheet[index])

# 要排除重复的值对象时可以使用字典
# D={}直接定义一个空的字典对象
# D[index]=value，直接为字典D添加一个key值index，及其相应的value值
# sorted对可迭代对象(可以是字符串，字典，列表等等)进行排序，并返回一个列表
