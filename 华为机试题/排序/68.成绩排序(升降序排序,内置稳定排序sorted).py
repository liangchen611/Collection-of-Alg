import sys

n = int(input())
op = int(input())
stu_mark = []
for i in range(0,n):
    mess = sys.stdin.readline().strip().split(" ")
    sub_list= [mess[0],int(mess[1])]
    stu_mark.append(sub_list)

new_mark = []
if op==1:
    new_mark = sorted(stu_mark,key=lambda x:x[1])
elif op==0:
    new_mark = sorted(stu_mark,key=lambda x:-x[1])
    
#print(new_mark)
for i,a in enumerate(new_mark):
    print(a[0],end=" ")
    print(a[1])
    

# 1.python的内置排序函数sorted
# python内置的排序函数，sorted，采用的是timesort排序算法
# 该算法基于插入排序和归并排序的组合，时间复杂度为O(nlogn)，它属于稳定排序，排序前后元素相同的位置相对不变

# 对数值类型的数据，sorted是默认采取升序排序

# 2.升序和降序排序
# 如果要进行降序排序，可以在原数据基础上，对所有的数值取反，这样就是改变了数值的排序顺序
# 对数值取反进行排序后，将排序后的数组中的值再进行取反，就可得到降序排序的数组

#——————————
# 3.常见排序的小结  
# 参考markdown