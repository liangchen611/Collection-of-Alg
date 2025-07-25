import sys

m1 = sys.stdin.readline().strip()
m2 = sys.stdin.readline().strip()

for i in range(0,len(m1)):
    if "a"<=m1[i]<"z":
        asc = ord(m1[i])
        asc = asc - 32 + 1
        print(chr(asc),end="")
    if m1[i] == "z":
        print("A",end="")

    if "A"<=m1[i]<"Z":
        asc = ord(m1[i])
        asc = asc + 32 + 1
        print(chr(asc),end="")
    if m1[i] == "Z":
        print("a",end="")   

    if "0"<=m1[i]<="9":
        num = int(m1[i])
        num = (num + 1) % 10
        print(str(num),end="")

print("")
for i in range(0,len(m2)):
    if "A"<m2[i]<="Z":
        asc = ord(m2[i])
        asc = asc + 32 - 1
        print(chr(asc),end="")
    if m2[i] == "A":
        print("z",end="")

    if "a"<m2[i]<="z":
        asc = ord(m2[i])
        asc = asc - 32 - 1
        print(chr(asc),end="")
    if m2[i] == "a":
        print("Z",end="")   

    if "0"<=m2[i]<="9":
        num = int(m2[i])+10
        num = (num - 1) % 10
        print(str(num),end="")