import sys

n = int(input())
seq = sys.stdin.readline().strip().split(" ")
seq = [int(s) for s in seq]

def generate_sequence(pull,pop,output,result):
    if not pull and not pop:
        result.append(output)
        return 
    
    # 只有两种操作，让一个新的最前元素入栈，或者让一个栈顶元素出栈
    # 最前的元素入栈，从待入栈元素中弹出第一个，并将元素压入待弹出列表中，并加入到结果序列中
    if pull:
        next_input = pull[0]
        # 但是这个入栈的元素还未出，所以output不更新
        generate_sequence(pull[1:],pop+[next_input],output,result)

    # 待弹出中最后的元素出栈
    if pop:
        next_ouput = pop[-1]
        generate_sequence(pull,pop[:-1],output+[next_ouput],result)
    
results = []
generate_sequence(seq,[],[],results)
results.sort()

for i in range(len(results)):
    for j in range(len(results[i])):
        print(results[i][j],end=" ")
    print()


# 1.栈的操作序列
# 对一个栈，如果不限制栈元素的出栈时间（即入栈后的元素可以立即出栈），问可以有几种操作序列
# 给定元素序列，它可以执行的操作只有两种：将序列当前最前的元素入栈，或者将栈顶的元素出栈
# 由此进行递归操作

#————————

# 2，递归中的引用传递
"""
在 Python 中：列表（list）、字典（dict）、集合（set）等是可变对象,它们的变量名其实是一个“引用”或“指针”，指向实际的数据
当你把一个列表传给函数，传入的是这个引用（地址），而不是复制一份新的内容
"""

"""
所以，pop，append等操作是直接对可变对象的内存进行修改，如果在此后进行了传参，那么会导致后续所有分支都出错

因此，特别对于递归函数，传入的应该是可变对象的副本，而不是直接对对象进行操作然后再传入

例如，我想传入一个弹出了最后一个元素的列表，不能先进行pop，而是应该用list[:-1]的形式，复制一份副本传入函数当中

list+[]的操作方式也不会影响原本的可变对象
"""

#——————————

# 3.sort函数与sorted函数
"""
sort: list.sort()
sorted: sorted(list)

sort会修改原本的对象，所以需要进行副本复制来传参
sorted则是生成一个新的列表

sort只会进行一层的字典排序，如果列表内部依然为列表，那么内部的嵌套列表并不会因为sort改变顺序
它是逐位置对其中的元素值进行排序，例如[1,2,3]，[1,3,2]，[2,1,3]，先比较第一位，第一位相同再比较第二位，如此类推
"""