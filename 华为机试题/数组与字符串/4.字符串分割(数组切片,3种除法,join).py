import sys

string = input()

length = len(string)
value = length//8

for i in range(0,value):
    print(string[8*i:8*(i+1)])
if length%8!=0:
    redundant = length%8
    new_string = ["0"]*8
    new_string[0:redundant] = string[8*value:8*value+redundant]
    new_string = "".join(new_string)
    print(new_string)

    # string[a:b:c]，ab切片，c步长

    # a//b整数商，a/b一般除法得浮点数，a%b求模

    # join，接收可迭代对象并转换为新字符串   “连接符”.join(目标串，可以是列表，字典，元组等)
