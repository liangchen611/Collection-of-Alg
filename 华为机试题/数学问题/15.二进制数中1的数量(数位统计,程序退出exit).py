import sys

number = int(input())

sum = 0
nof1 = 0
if sum == number:
    print(0)
    sys.exit()

# 输入为0时，直接返回数值0

while number > 0:
    if number % 2 == 1:  # 检查当前最低位是否为1
        sum += 1
    number = number // 2  # 右移一位

print(sum)

# 每次对n求模，如果结果为1，则当前数位上为1
# 并且每次对n进行整除更新数值，相当于往右进一位
# 相当于把原数拆成n*2^0+n*2^1+n*2^2+....的形式
