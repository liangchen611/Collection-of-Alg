import sys

def test_prime(n):
    if n<=2:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                return False
    return True

prime_number = [2,3]

for i in range(4,1000):
    if test_prime(i):
        prime_number.append(i)

dict_sum = {}
for i in range(0,len(prime_number)-1):
    for j in range(0,len(prime_number)):
        A = prime_number[i]
        B = prime_number[j]

        if A + B not in dict_sum:
            dict_sum[A + B] = [abs(A - B), A, B]
        else:
            if abs(A - B) < dict_sum[A + B][0]:
                dict_sum[A + B] = [abs(A - B), A, B]
print(dict_sum)

n = int(input())
print(dict_sum[n][1])
print(dict_sum[n][2])

#1.对字典中特定键的赋值方法
# 如果想采用统一化的初始化方法，那么可以用setdefault
# dict.setdefault(key,value)
# 此函数对于此前不存在的key，则dict[key]=value

#如果value是一个列表或是其他可迭代元素，那么就可以用dict[value][i]对它内部元素进行访问
#类似append，extend等相应的操作也是可以的

#不用setdefault方法的话，也可以用dict[key]=value的方法直接进行赋值，是最安全的一种方法
#【要进行下标访问需要确保字典的值是可迭代对象，否则会出现越界！】