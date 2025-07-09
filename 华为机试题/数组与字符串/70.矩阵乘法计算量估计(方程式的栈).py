import sys

n = int(input())
matrixs = []

for i in range(n):
    row_column = sys.stdin.readline().strip().split(" ")
    row_column = [int(row_column[0]),int(row_column[1])]
    matrixs.append(row_column)

formula = sys.stdin.readline().strip()

stack = []
ops = []
results = []

for i, F in enumerate(formula):
    
    if F == "(":   
        ops.append(F)

    if F!="(" and F!=")":     
        asc = ord(formula[i])
        asc = asc - 65
        stack.append(matrixs[asc])

    if F==")":     
        if stack:
            latter = stack.pop()
            former = stack.pop()
            result = former[0]*former[1]*latter[1]
            new_matrix = [former[0],latter[1]]
            results.append(result)
            stack.append(new_matrix)
            ops.pop()
print(sum(results))

# 分成2个栈，数值栈与计算符栈

# 计算表达式——用栈的方法进行计算，同时注意区分左右括号
# 左括号入栈，数字/字母等代表常数的量入栈
# 右括号，弹出当前数值栈最顶上的2个元素以及计算符，按照计算符对它们进行相应的运算，然后将结果再插回栈中
# 【上面的弹出过程要直到弹出的计算符为一个左括号为止】