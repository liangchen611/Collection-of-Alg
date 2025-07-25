import sys

s = input().strip()
new_s = list(s)
index = []
num_s = ""
for i in range(0,len(s)):
    # 当前数字串为空且读到字母
    if not num_s and s[i].isdigit()==False:
        continue
    if num_s and s[i].isdigit()==False:
        index.append(i)
        num_s=""
    if s[i].isdigit()==True:
        if not num_s:
            index.append(i)
        num_s+=s[i]

for i in range(0,len(index)):
    new_s[index[i]] = "*"+new_s[index[i]]

for i in range(0,len(new_s)):
    print(new_s[i],end="")
if s[-1].isdigit():
    print("*")
    
# insert函数，不适合在循环当中使用，特别是for循环
# 因为for循环的步长和当前步伐的下标是固定的，所以insert会直接地影响了列表的长度，因此插入的方法最好有所改变
# 例如，将插入字符变为直接修改对应元素的字符串（做加法）