import sys

message = sys.stdin.readline().strip().split(" ")
n, x, k = int(message[0]), message[-2], int(message[-1])
ss = message[1:-2]

x_dict = {}
for i in range(0,len(x)):
    x_dict.setdefault(x[i],0)
    x_dict[x[i]]+=1


temp_dict = {}
bro = []
for i in range(0,n):
    if ss[i] == x:
        continue
    if len(ss[i]) != len(x):
        continue
    else:
        temp_dict = {}
        for j in range(0,len(ss[i])):
            if ss[i][j] not in x_dict:
                temp_dict = {}
                break
            else:
                temp_dict.setdefault(ss[i][j],0)
                temp_dict[ss[i][j]]+=1
        if temp_dict == x_dict:
            bro.append(ss[i])

sort_bro = sorted(bro)
print(len(sort_bro))
if k <= len(sort_bro):
    print(sort_bro[k-1])
    
#思路：先将输入拆分，得到目标字符串，然后通过字典的方式，统计字符串中的字符及它们的出现次数，形成一个字典
#逐个遍历待比较的字符串，满足条件的字符串，字母出现情况与目标字符串一定相同，所以：出现目标字符串不同的字符；长度不同，两种情况都可直接筛掉
#通过以上筛选可以得到一个兄弟单词组成的列表，对列表使用sorted进行字典排序得到目标列表，最后输出其长度以及k值下标所对应的字符串
#|
#-----------------
#|
#-----输入拆分-----
# strip函数：会去掉行首行尾的所有空白字符（包括 \n、空格、制表符等）；
# 接着 .split()（不带参数）会把连续任意空白都当分隔符。但最好还是指定split的具体空格长度
# 例如：sys.stdin.readline().strip().split(" ")
# 将输入去掉行末的换行符的情况下，以长度1的空格为分割符，得到若干元素组成的序列
# 不加strip的话会导致split分割后保留换行符

#-----字典判空------
# python的布尔上下文中（主要是if xxxx等涉及布尔判断的语句），空的容器会被识别为false
# 例如空列表list=[]，空字典={}，空元组=()，都会被识别成false
# 用if not Iter的方法可判断一个迭代对象是否为空

#-----字典判等-----
# 一般可以用dict1 == dict2来判相等，判相等有如下的标准：
# 1.每个键在两个字典里都必须存在（d1.keys() == d2.keys()）。

# 2.对应键的值也“相等”，比较方式仍是使用各自值的 ==。如果值本身是容器（list、dict 等），就递归地再用 == 去比。

# 3.键的顺序忽略。Python 3.7+ 字典虽然保持插入顺序，但 == 比较时完全不看顺序。

# 4.键的“相等”规则用 __eq__ 与 hash，例如 True 和 1 的哈希相等且 True == 1，所以它们被视作同一个键；如果两边出现了 “True” vs “1”，结果会是一个键覆盖另一个，而不是冲突。

# 5.类型也得一样。 例如，值 1（int） 与 '1'（str）不同；键同理。

# 6.浮点近似误差不自动容忍

# 如果想知道两个字典有什么地方不同，可以用取对称差的方式：set(dict1.items())^set(dict2.items())

# 注意相等≠恒等，dict1 == dict2 与 dict1 is dict2 所表达的概念不同，后者需要要求dict1和dict2指向同一片内存