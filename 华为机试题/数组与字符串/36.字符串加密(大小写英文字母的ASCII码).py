import sys

s = sys.stdin.readline().strip()
cha = {}
for i in range(0,len(s)):
    cha.setdefault(s[i],i)
cha = list(cha)

for i in range(0,26):
    lower = chr(ord("a")+i)
    if lower not in cha:
        cha.append(lower)

t = sys.stdin.readline().strip()
for i in range(0,len(t)):
    index = ord(t[i])-97
    print(cha[index],end="")
