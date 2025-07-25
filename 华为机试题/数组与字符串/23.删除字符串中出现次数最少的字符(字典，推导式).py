import sys

s = input()
freq = {}

for i in range(0,len(s)):
    char = s[i]
    freq[char] = freq.get(char,0)+1

min_freq = min(freq.values())

for i in range(0,len(s)):
    char = s[i]
    if freq[char] >min_freq:
        print(char,end="")

#用dic = {}的方式创建一个空字典
#向字典中加入新的键值对的方法——依照键名来加入，dic[key] = dic.get(key,0)+1
#其中，dic[key]表示其中key键所对应的值，dic.get(key,0)则是获取key的值，默认返回0，如果此前不存在key键就会新建一个键值对(key,value)

#用正则表达式来进行筛选，例如：
#result = "".join(char 
#                for char in freq if freq[char]!=min_freq 
#                    for j in range(0,freq[char]))
#其中join部分就用了正则表达式，选出满足特定条件的char，外层循环遍历所有键值对，而内层循环则是让当前char键的次数重复其对应值的次数