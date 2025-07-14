import sys

ip = input().split(".")
if len(ip) != 4:    # 排除长度不为4部分的
    print("NO")
else:
    for i in ip:
        if (
            not i.isdigit()    # 排除不是数字的
            or (len(i) > 1 and i[0] == "0")    # 排除首位为0的
            or int(i) < 0    # 排除在[0,255]范围外的
            or int(i) > 255
        ):
            print("NO")
            break
    else:
        print("YES")

# 1.判断字符串中的某个字符是否为数字或者字母

# 判断为数字：【char.isdigit()】，属于"0"-"9"（isdigit只能匹配0~9，如果是多位的数字，那么还需要其他的规则进行辅助）

# 判断为字母：【char.isalpha()】，可以判断大写和小写字母