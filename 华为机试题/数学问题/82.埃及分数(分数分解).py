from math import floor
import sys

num = input().strip().split("/")
a,b = int(num[0]),int(num[1])
num = a/b

less = num
m_list = []
n = 0

while less>1e-16:
    if b%a == 0:
        n = b/a
    if b%a != 0:
        n = floor(b/a)+1
    m_list.append(int(n))
    less = less - 1/n
    a = a*n - b 
    b = b*n

for i in range(len(m_list)):
    if i<len(m_list)-1:
        print("1/"+str(m_list[i])+"+",end="")
    if i==len(m_list)-1:
        print("1/"+str(m_list[i]))
       
# 问题描述：给定一个分子小于分母的分数，将它表示为若干个1/n形式的数的和，称为埃及分数
# 例如：1/2 = 1/3 + 1/6


"""
问题求解：用贪心的方法，对给定的数a/b，假设存在一个1/n和它最为接近或相等，1/n ≤ a/b < 1/(n-1)
可知：n≥b/a，n必须为整数，且必须比b/a大，如果b/a为整数，那么n=b/a，否则的话n = int(b/a)+1，将n加入到分母列表当中

由此可以求得埃及分数中的其中一个组成部分，所以可以如此往下做，将a/b减去1/n，然后继续对a/b - 1/n，求它的最接近的n
a'/b' = a/b - 1/n，可以得到a'和b’的表示形式，a'=na-b  b'=nb

如此循环，直到a'/b'接近0为止（因为a'/b'为浮点数，所以应该是a'/b'<1e-16，或是其他精度，当a'/b'足够小的时候，就可以跳出循环
"""
