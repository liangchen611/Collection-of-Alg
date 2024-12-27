import sys
string = input()
char = input()

asc = ord(char)
asc2 = 0

if 65 <= asc <= 90:
    asc2 = asc + 32

if 91 <= asc <= 116:
    asc2 = asc - 32

count=0

for i in range(0,len(string),1):
    if ord(string[i])==asc or ord(string[i])==asc2:
        count+=1

print(count)

# 获取ASCII码，ord
# 大写字母的ASCII：从65~90
# 小写字母的ASCII：在大写字母基础上+32
# 0~9的ASCII：从48~57
