import sys

a = sys.stdin.readline()
appear = {}
ch_appear = {}

def sort_key(k):
    return (k.lower(), 0 if k.isupper() else 1)

for i in range(0,len(a)):
    appear.setdefault(a[i],[]).append(i)

ch_appear = {key:value for key,value in appear.items()
                    if ("A"<=key<="Z") or ("a"<=key<="z")}
app_sort = sorted(ch_appear,key=sort_key)
chr_sort = {k: ch_appear[k] for k in app_sort}
chr_list = list(chr_sort.items())

new_str = []
i = 0
while i < len(chr_list):
    ft = chr_list[i][0]
    if i == len(chr_list)-1:
        new_str.extend([ft] * (len(chr_list[i][1])))
        break
    try:
        rear = chr_list[i + 1][0]
        if ord(rear) == ord(ft)+32:
            ft_indx = chr_list[i][1]
            r_indx = chr_list[i+1][1]
            f_count=0
            r_count=0
            while f_count < len(ft_indx) and r_count < len(r_indx):
                if ft_indx[f_count] < r_indx[r_count]:
                    new_str.append(ft)
                    f_count+=1
                else:
                    new_str.append(rear)
                    r_count+=1
            new_str.extend([ft]*(len(ft_indx)-f_count))
            new_str.extend([rear]*(len(r_indx)-r_count))
            i += 2
            continue
        else:
            new_str.extend([ft] * (len(chr_list[i][1])))
            i += 1
    except:
        break

it = iter(new_str)
for ch in a:
    if ("A"<=ch<="Z") or ("a"<=ch<="z"):
        print(next(it),end="")
    else:
        print(ch,end="")


#----while循环体和for循环体的区别-----
# for在循环体中，自动对循环计数i进行更新，如果在循环体内对i进行更改，它只会影响当前循环体中当前的i，但是对i的更改不会影响到下一次的循环中
# 因为循环会自动地对i进行更新覆盖，所以for并不能自由地对i进行管理，但稳定性强
# for会至少执行一次循环
# ------
# while不一定会执行循环，依据判断逻辑来决定是否继续循环
# 可以在循环体外定义i，然后就能在while循环体中对i进行维护，这种维护方法可以让循环时可以进行一定的跳步

# for是数值性更强的循环体，while则更偏向于逻辑判断

#-----二路归并----- 
# 对两个数组列表按照递增顺序进行合并
# 简单的方法就是定义2个数组的索引值，并使用while循环对其进行更新（不适合用for循环自动增值），逐一比较两个列表中的位置，较小者的值出列，同时索引进位
# 如果当某个数组的索引已经加到最后，就补充剩下的值

#-----取字母的方法-----
#1.取ASCII码，ord(A),65~90-大写，97~122-小写
#2.直接用数值不等式：“A”<s<"Z", “a"<s<"z"的方法也可以进行比较
#3.isalpha()函数可以直接进行判断


#-----迭代器iter-----
# it = iter(letters_sorted)      iter迭代器，按排序后的顺序输出字母
# next(it) 读取下一个位置，起始位置为0，第一次
# 把迭代器当成“只能向前读取的懒队列 / 流”最贴切：它提供 FIFO 弹出行为，却没有存储、随机访问和复用能力。
# 可以通过next()方法逐个访问迭代器当中的元素，但顺序固定，也不能往回读取，想要重新读取只能新建另一个迭代器
# 当迭代器读取到末尾时，该迭代器会被销毁，所以它是一个只能播放一次且单向播放的磁带

#-----可变对象的插入insert-----
# 对于python中的可变迭代对象，可以用insert(position, value)来对值进行插入
# 一般可以插入的都是列表，字符串不可用insert，因为字符串不可变
# 对字符串，应该如此插入： str = str[:pos] + "要插入的字符" + [pos:]
