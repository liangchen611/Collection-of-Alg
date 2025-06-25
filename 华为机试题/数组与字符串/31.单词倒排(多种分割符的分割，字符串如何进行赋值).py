import sys

sen = sys.stdin.readline().strip()
for i in range(0,len(sen)):
    if not ("a"<=sen[i]<="z" or "A"<=sen[i]<="Z"):
        sen = sen.replace(sen[i], " ")
        #修改字符串的值
sen = sen.split(" ")

sen = sen[::-1]
for i in range(0, len(sen)):
    print(sen[i],end=" ")
    

#——【多种分割符存在时的分割方法】——
# 如果一个字符串中存在有多个用于标识分割的符号，那么需要将这些符号全部都纳入分割依据中并进行分割。
# 但是，python所自带的str.split()函数本身并不支持输入多个分割符，只能接收一个。
# 对此的方法是，【将原字符串中所有用于标识分割的符号都转换为同一个符号，然后再用split进行分割】（通常，转换为一个空格）
    
#——【字符串的性质以及修改方法】——
# 在 Python 中，【字符串（str）是不可变对象（immutable）】，这意味着字符串一旦创建，它的内容就不能被直接修改。
s = "hello"     # 这种情况下，s为一个字符串，虽然可以通过下标访问，但是不可更改
print(s[1])     # 'e'
s[0] = 'H'      # 报错：TypeError

lst = ['h', 'e', 'l', 'l', 'o']  # 这种情况下，lst为一个列表，列表元素每一个都是一个字符串，可以被更改
print(lst[1])    # 'e'
lst[0] = 'H'     # 修改成功
print(lst)       # ['H', 'e', 'l', 'l', 'o']

# 如果你想“修改”字符串，可以通过构造新字符串实现：
# 或者是通过s.replace方法也可以进行修改，因为【replace本质没有改变原有的字符串，而是返回一个新的字符串】
s = "a-b_c=d"
s = s.replace("-", " ").replace("_", " ").replace("=", " ")
print(s)  # "a b c d"