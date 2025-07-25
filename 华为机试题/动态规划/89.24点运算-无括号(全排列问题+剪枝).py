import sys

cards = sys.stdin.readline().strip().split(" ")

matching_cn = {"A":1,"J":11,"Q":12,"K":13}
matching_nc = {1:"A",11:"J",12:"Q",13:"K"}
matching_op = {0:"+",1:"*",2:"-",3:"/"}

pts=[]
for i in range(len(cards)):
    if cards[i]=="A":pts.append(1)
    if cards[i]=="J":pts.append(11)
    if cards[i]=="Q":pts.append(12)
    if cards[i]=="K":pts.append(13)
    if cards[i] not in ["A","J","Q","K","joker","JOKER"]:
        pts.append(int(cards[i]))

def generate_permutations(arr):
    res = []
    n = len(arr)

    def backtrack(start):
        # 排列到达终点，加入当前排列
        if start == n:
            res.append(arr[:])  # 收集当前排列
            return

        # 从start=0开始，每一项与后面交换，然后递归一层，递归到终点后，跳出，回溯
        for i in range(start, n):
            arr[start], arr[i] = arr[i], arr[start]
            backtrack(start + 1)
            arr[start], arr[i] = arr[i], arr[start]

    backtrack(0)
    return res

def cal(k,n1,n2):
    if k==0:return n1+n2
    if k==1:return n1*n2
    if k==2:return n1-n2
    if k==3:
        if abs(n2)<1e-6:return None
        else: return n1/n2

def judge24(nums,op):
    for i in range(0,4):
        for j in range(0,4):
            for k in range(0,4):
                a = nums[0]
                b = cal(i,a,nums[1])
                if b==None:continue

                c = cal(j,b,nums[2])
                if c==None:continue

                d = cal(k,c,nums[3])
                if d==None:continue
                elif abs(d-24)<1e-6:
                    op.append(i)
                    op.append(j)
                    op.append(k)
                    return True
    return False

seq = []
ops = []
sign = 0

if "joker" in cards or "JOKER" in cards:
    print("ERROR")
else:
    P = generate_permutations(pts)
    for i,p in enumerate(P):
        if judge24(p,ops):
            seq = p
            sign = 1
            break

if sign==0:
    print("NONE")
elif sign==1:
    for i in range(0,3):
        seq_n = seq[i]
        op = ops[i]
        if seq_n in matching_nc:print(matching_nc[seq_n],end="")
        else: print(seq_n,end="")
        print(matching_op[op],end="")
    if seq[-1] in matching_nc:print(matching_nc[seq[-1]])
    else: print(seq[-1])
        
# 全排列问题：给定一个元素数量有限的迭代对象，返回其所有可能的排列所组成的列表
"""
规定起始位置，然后用递归的方法逐个交换元素的位置，递归到最终深度——一般用长度来判断，将当前序列的一个复制加入，然后回溯，交换位置
def generate_permutations(arr):
    res = []
    n = len(arr)

    def backtrack(start):
        # 排列到达终点，加入当前排列
        if start == n:
            res.append(arr[:])  # 收集当前排列
            return

        # 从start=0开始，每一项与后面交换，然后递归一层，递归到终点后，跳出，回溯
        for i in range(start, n):
            arr[start], arr[i] = arr[i], arr[start]
            backtrack(start + 1)
            arr[start], arr[i] = arr[i], arr[start]

    backtrack(0)
    return res
"""