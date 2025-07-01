import sys

mess = sys.stdin.readline().strip().split(" ")
n = int(mess[0])
h = int(mess[1])
k = int(mess[-1])
G = [int(mess[m]) for m in range(2,len(mess)-1)]

link_dic = {h:0}
link = [h]

i=0
while i<=len(G)-2:
    insert = G[i]
    former = G[i+1]
    if former not in link:
        i += 2
        continue
    if former in link:
        if insert in link:
            i += 2
            continue
        if insert not in link:
            index = link_dic[former]
            link.insert(index+1,insert)
            for l in link_dic:
                if link_dic[l]>=index+1:
                    link_dic[l]+=1
            link_dic[insert]=index+1
            i += 2
            continue

link.remove(k)

for j in range(0,len(link)):
    print(link[j],end=" ")

#思路：先提取出各种信息，然后构建出一个待加列表，一个存放字符串中所有字符及它们的位置的字典，以及一个link表用来存放目标数组
#因为每种不同的字符只能出现一次，所以要加入判断，判断当前待加入的字符和前缀是否存在
#若前缀不存在于链表中，结束本轮的循环；若前缀存在，但当前字符已经存在于链表中，也结束当前轮的循环
#若前缀存在，当前字符不存在，那么获取前缀在字典中的下标index，将该字符插入到link表当中，位置为index+1
#因为插入到链表了，所以需要对字典进行一定更新，【位置在index之后的字符的位置值都需要+1】，然后再将新入列的字符和下标index+1也加入到字典中

#——————————
#1.insert函数  
#insert函数的格式为：list.insert(index,num)，其中，index就是要插入的下标，例如要将num插入到下标1的位置，那么就是insert(1,num)
#表示在 index 位置之前插入

#——————————
#2.remove函数 
#remove(p)函数可以删掉列表中第一个匹配到的值为p的元素，但只能删去第一个
#如果要删去列表中所有符合对应值的元素，可以用列表推导式——用布尔条件进行筛选
lst = [x for x in lst if x != P]

#——————————
#3.字典中元素的格式   
#如果用print函数来打印字典中的元素，那么字典中的一个键值对大致呈如下格式：k:v，中间用冒号进行分隔
#所以用字典推导式，或是遍历字典中的元素时，采用如下的访问形式
#for k:v in dict.items()
#items()可以访问字典中的键值对

#——————————
#4.链表元素的插入  
#因为链表是单向且有明确的前驱和后缀，所以当有其他元素插入链表时，其插入位置的所有后续元素的信息都需要进行更新，否则会出错
#可以用字典的形式来对链表中元素信息进行更新