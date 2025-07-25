import sys

formula = sys.stdin.readline().strip()

def cal(op,a,b):
    if op=="+":return a+b
    if op=="-":return a-b
    if op=="/":return a/b
    if op=="*":return a*b

def presence(op):
    return 1 if op in "*/" else 0

left = ["(","[","{"]
right = [")","]","}"]
matching = {")":"(", "]":"[", "}":"{"}

nums = []
ops = []

i=0
while i<len(formula):
    ch = formula[i]

    # 支持正数和负数
    if ch == '-' and (i == 0 or formula[i-1] in "+-*/([{"):
        # 一元负号：读取负数
        i += 1
        temp_sum = 0
        while i < len(formula) and '0' <= formula[i] <= '9':
            temp_sum = temp_sum * 10 + int(formula[i])
            i += 1
        nums.append(-temp_sum)
        continue

    if "0"<=ch<="9":
        # 如果是数字，判断它是否连续，如果是连续数字，那么需要按位逐渐加得到完整的数值
        temp_sum = 0
        while i < len(formula) and "0"<=formula[i]<="9":
            temp_sum = temp_sum*10 + int(formula[i])
            i = i+1
        nums.append(temp_sum)
        continue
    
    if ch in "+-*/":
        while ops and ops[-1] not in left and (presence(ops[-1]) >= presence(ch)):
            op = ops.pop()
            num1 = nums.pop()
            num2 = nums.pop()
            nums.append(cal(op,num2,num1))
        ops.append(ch)
        i+=1
        continue

    if ch in left:
        ops.append(ch)
        i+=1
        continue

    if ch in right:
        while ops and ops[-1] != matching[ch]:
            op = ops.pop()
            num1 = nums.pop()
            num2 = nums.pop()
            nums.append(cal(op,num2,num1))

        if ops and ops[-1] == matching[ch]:  
            ops.pop()

        i+=1
        continue

while ops:
    op = ops.pop()
    num1 = nums.pop()
    num2 = nums.pop()
    nums.append(cal(op,num2,num1))

print(int(nums[0]))

#思路：关键在于，理解四则运算的基本规则：不同级的先算高级的，同级间的运算从左往右，括号优先级最高

#——————————

# 分类依次考虑各种字符所对应的情况：
#1.【数字，可能是负数或者整数，可能是一位也可能是多位】
# 先判负数：以负号打头，后面所跟着的一定是数字，若为其他字符，那么就不是负号而是减号
# 然后判正数：因为可能有多个整数一起构成一个数字，所以遇到数字时需要进行循环遍历直到下一个字符不是数字为止
# 如果是多位整数还需要按位加和： i*100 + (i+1)*10 + (i+2)

#2.【加减乘除号】
# 要分情况讨论，具体来说就是看它的字符下一位是什么，如果下一位不是括号，说明不涉及先后问题，可以直接算
# 乘除的优先级要高于加减，所以如果读出乘除而上一个运算符又正好是加减，那么该乘除需要立刻算出

#3.【括号】
# 括号一定是成对出现的，为了避免括号堆叠，当出现【右括号】时，说明已经构成了一个闭环子片段，需要把当前括号内的算出
# 子片段的终点，就是当前【右括号】所匹配的【左括号】，所以可以进行反向的遍历，直到遇到与之对应的左括号为止

#——————————

#【数据结构】
# 因为在遍历过程中，存在有运算的优先级问题，所以可以用栈解决，不过需要分别用【数值栈】和【操作符栈】
# 同时，先定义函数来表示不同运算符下的返回结果(+-*/)
# 每当需要执行计算操作时，就从nums和ops中弹出顶层元素进行操作，计算完的结果再返回到nums当中
# 不需要执行计算操作时，就将遍历到的算符和数字都压入栈中待命

# 【不过要注意出栈顺序的问题，先进后出】，
# 例如Num1=nums.pop()，Num2=nums.pop()，Num2是在Num1前面的值，所以计算减法除法等运算时，顺序是Num2-Num1，Num2/Num1

3+2*{1+2*[-4/(8-6)+7]}
# 每次输出2行，一行为数字栈，另一行为	
3	[3]		
4	[]		

5	[3]		
6	['+']	

7	[3, 2]		
8	['+']		

9	[3, 2]		
10	['+', '*']	

11	[3, 2]		
12	['+', '*', '{']		

13	[3, 2, 1]		
14	['+', '*', '{']		

15	[3, 2, 1]		
16	['+', '*', '{', '+']	

17	[3, 2, 1, 2]		
18	['+', '*', '{', '+']		

19	[3, 2, 1, 2]		
20	['+', '*', '{', '+', '*']	

21	[3, 2, 1, 2]		
22	['+', '*', '{', '+', '*', '[']	

23	[3, 2, 1, 2, -4]		
24	['+', '*', '{', '+', '*', '[']		

25	[3, 2, 1, 2, -4]		
26	['+', '*', '{', '+', '*', '[', '/']	

27	[3, 2, 1, 2, -4]		
28	['+', '*', '{', '+', '*', '[', '/', '(']	

29	[3, 2, 1, 2, -4, 8]		
30	['+', '*', '{', '+', '*', '[', '/', '(']		

31	[3, 2, 1, 2, -4, 8]		
32	['+', '*', '{', '+', '*', '[', '/', '(', '-']		

33	[3, 2, 1, 2, -4, 8, 6]		
34	['+', '*', '{', '+', '*', '[', '/', '(', '-']		

35	[3, 2, 1, 2, -4, 2]		
36	['+', '*', '{', '+', '*', '[', '/']		

37	[3, 2, 1, 2, -2.0]		
38	['+', '*', '{', '+', '*', '[', '+']	

39	[3, 2, 1, 2, -2.0, 7]		
40	['+', '*', '{', '+', '*', '[', '+']		

41	[3, 2, 1, 2, 5.0]		
42	['+', '*', '{', '+', '*']		
