import sys

a = input()
char = ""

for i in range(0,len(a)):
    if int(ord(a[i]))<=111 and int(ord(a[i]))>=97:
        t = int(ord(a[i]))-97
        t = t//3
        t = 2+t
        char = str(t)       
    elif a[i] in ("p","q","r","s"):
        char = "7"
    elif a[i] in ("t","u","v"):
        char = "8"
    elif a[i] in ("w","x","y","z"):
        char = "9"
    elif int(ord(a[i]))<=89 and int(ord(a[i]))>=65:
        t = int(ord(a[i]))+32+1
        char = chr(t)
    elif int(ord(a[i]))==90:
        char = chr(97)
    elif int(ord(a[i]))<=57 and int(ord(a[i]))>=48:
        char = a[i]
    print(char,end="")
    
#ע��python�е�������Ϊand��&��python���ǰ�λ�����
#��ȡascii����ord��ת��ascii����chr