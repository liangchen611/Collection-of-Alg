import sys

t = int(input().strip())

for i in range(0,t):
    s = input().strip()
    # 10000009-可能换的情况最多为8位，9位不可能再换
    new_s = []
    temp_s = s
    for j in range(0,len(s)):

        local_max = int(temp_s[0])
        index = 0
        sub_length = 8 if len(temp_s)>=8 else len(temp_s)

        if sub_length>=2:
            for k in range(0,sub_length):
                sub_s = int(temp_s[k])-k

                if sub_s>local_max:
                    local_max=sub_s
                    index = k

            if index==0:
                temp_s=temp_s[1:]

            elif index==sub_length-1:
                temp_s=temp_s[:-1]

            else:
                temp_s = temp_s[:index]+temp_s[index+1:]

        if sub_length==1:
            local_max = int(temp_s[0])

        new_s.append(local_max)

    for i in range(0,len(new_s)):
        print(new_s[i],end="")
    
    print()
   
#思路：
#抓取局部数组：每次抓8个，然后选取按位移动后最大的，拉出来放入存储数组中，实际上，每位数移动到最左的值就是s[i]-i，所以比较该值就足够
#取出后，剩下的数变为新数组temp_s，重复此过程

#最后按序输出存储数组的数，最后得到的就是变化后的数