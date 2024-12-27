import sys

number = input()
sign = [0]*10
for i in range(len(number)-1, -1, -1):
    value = int(number[i])
    if sign[value]==1:
        continue
    sign[value]=1
    print(value,end="")
