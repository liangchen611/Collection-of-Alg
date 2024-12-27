import sys

number = int(input())

def prime_factors(n):
    factors = []
    # 处理 2 的因子
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    # 处理其他因子（奇数）
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 2
    # 如果 n 是质数并且大于 2
    if n > 2:
        factors.append(n)
    return factors


prime_factor = prime_factors(number)

for i in range(0,len(prime_factor)):
    print(prime_factor[i],end=" ")

# 先依次处理2的因子，直到整除2不为0为止，说明此时2不再是质因子
# 然后再处理其他奇数因子，从3开始测，如果f*f大于当前数则停止，因为它必然不是当前数的质因子
# 处理完各种奇数若仍大于2，说明此过程中没有任何质因子，则该数本身就是质数
# python同行输出的方法end，不加指定的情况下，end的值默认为换行符
