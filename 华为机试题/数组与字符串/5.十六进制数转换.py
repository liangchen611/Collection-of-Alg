import sys

number_16 = input()

number_16 = number_16[2:len(number_16)]
summary = 0

for i in range(len(number_16) - 1, -1, -1):
    value = number_16[i]
    base = 16 ** (len(number_16) - 1 - i)
    if value == 'A':
        summary += 10 * base
        continue
    if value == 'B':
        summary += 11 * base
        continue
    if value == 'C':
        summary += 12 * base
        continue
    if value == 'D':
        summary += 13 * base
        continue
    if value == 'E':
        summary += 14 * base
        continue
    if value == 'F':
        summary += 15 * base
        continue
    else:
        summary += int(value) * base

print(summary)

# 十六进制数的表示：0xXXXXXX（数位）
# 注意数位是从右到左，需要反向计算
# 注意数位对应的基数
