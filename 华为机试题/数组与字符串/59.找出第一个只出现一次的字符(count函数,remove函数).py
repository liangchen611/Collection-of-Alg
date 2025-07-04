import sys

st = sys.stdin.readline().strip()
st = list(st)

for i in range(0,len(st)):
    if st.count(st[i])==1:
        print(st[i])
        break
    if i == len(st)-1:
        print(-1)


#1.remove函数   调用方式：list.remove(s)   
#remove函数删除在列表中第一个值为s的函数，只可对列表用  
#remove函数会直接在原列表的内存位置上修改，所以该函数的返回值为none
#因为返回为none，所以remove后的结果不可赋值给其他的变量

#————————————

#2.count函数    调用方式：iter.count(s)  
#可以用于字符串，列表，或是元组，用于统计某个元素或者子串在该容器中的出现次数
#其中的s也可以是列表的切片，s[start:]或者s[:end]