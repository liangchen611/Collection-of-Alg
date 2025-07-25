import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

min_len = min(len(a),len(b))
max_len = max(len(a),len(b))


enter = 0
result_num = []
for i in range(-1,-max_len-1,-1):
    if i >= -min_len:
        result = int(a[i])+int(b[i])+enter
        loss = 0
        if result>=10:
            enter = 1
            loss = result-10
        if result<10:
            enter = 0
            loss = result
        result_num.append(loss)
        if i == -max_len and enter==1:
            result_num.append(1)
    if i < -min_len:
        result = 0
        loss = 0
        if len(a)>=len(b):
            result = int(a[i])+enter
        if len(b)>=len(a):
            result = int(b[i])+enter
        if result>=10:
            enter = 1
            loss = result-10
        if result<10:
            enter = 0
            loss = result
        result_num.append(loss)
        if i == -max_len and enter==1:
            result_num.append(1)
result_num = result_num[::-1]

for j in range(0,len(result_num)):
    print(result_num[j],end="")


#思路：对两个数，从后向前遍历它们的位并进行加和与进位操作
#需要注意处理的是数组的长度关系，短的遍历完后再继续遍历长的剩余部分；
#如果两个数组长度相同直接处理完毕
#另外需注意遍历到最左端时，是否存在进位，如果没有进位直接按位输出值，存在进位的话，就需要多加1位
#因为是逆向遍历，但最后输出时需要正向，所以在遍历的过程中都加入到数组中，遍历结束后进行反向重置