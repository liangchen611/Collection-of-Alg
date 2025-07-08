import sys

def dfs(nums):
    if not nums:
        return False

    # 如果当前待算的nums数组只有1个数，说明已经算出了当前分支的最终结果，与24进行作差判断
    if len(nums)==1:
        return abs(nums[0]-24)<1e-6
    
    else:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    a = nums[i]
                    b = nums[j]
                    # 按索引删除，而不是按值删除
                    rest_num = [nums[k] for k in range(len(nums)) if k!=i and k!=j]

                    for k in range(0,4):
                        # 0-+，1-*,2--,3-/
                        new_val = 0
                        if k<2 and i>j:
                            #加法乘法有对称性，所以当i超过j时，说明顺序相反，可以被剪枝
                            continue
                        if k==0:new_val = a+b
                        if k==1:new_val = a*b
                        if k==2:new_val = a-b
                        if k==3:
                            # 分母不为0，分母为0的情况下需要剪枝
                            if abs(b)<1e-6:
                                continue
                            new_val = a/b
                            
                        # 将算出的新数加入到剩余的nums当中，然后进行递归
                        rest_num.append(new_val)
                        if dfs(rest_num):
                            return True
                        # 结束当前轮次后，需要弹出——DFS的固定操作
                        rest_num.pop()
    
    return False
                        
N = sys.stdin.readline().strip().split()
N = [int(n) for n in N]
if dfs(N):print("true")
else:print("false")

# 为什么24点可以使用DFS暴力枚举法：因为有多个因素对搜索空间进行了大幅的限制：
# 1.限制只有4个数   2.运算符号只有加减乘除  3.除数为0的情况被剪枝  4.【加法和乘法具有对称性，要剪枝一半】

#——————————

#2.浮点计算中的判0
# 因为浮点计算中存在有大量的浮点数，所以不宜直接进行与0的判等计算
# 判0的方法就是将待判定的数与目标进行作差，如果其差小于1e-6，那么可以认为结果为0
# 1e-6是常用的一个浮点最小值 