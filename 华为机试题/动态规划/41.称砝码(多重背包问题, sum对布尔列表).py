import sys

n = int(input())
weights = sys.stdin.readline().strip().split(" ")
weights = [int(w) for w in weights]
nums = sys.stdin.readline().strip().split(" ")
nums = [int(n) for n in nums]

max_weight=0
for i in range(0,len(weights)):
    max_weight += weights[i]*nums[i]

# dp表示某个重量能否称量   
dp = [False]*(max_weight+1)
dp[0] = True

# 遍历砝码
for i in range(0,len(weights)):
    w = weights[i]
    k = nums[i]

    used = [0]*(max_weight+1)
    for weight in range(0,max_weight+1):
        if dp[weight] and used[weight]==0:
            for c in range(1,k+1):
                current_weight = weight + c * w
                if not dp[current_weight]:
                    dp[current_weight] = True
                    used[current_weight] = 1
                else:
                    break
print(sum(dp[0:]))

# 记忆化搜索（递归式的动态规划） & 标准动态规划

#思路：可以将问题转换为一个多重背包问题，有多件物品，每件物品有若干件，从中任意选取，组成若干组合
#可以用dp[i]解决，但不涉及状态转换方程——dp[i]的含义，重量i能否被当前组合所称量出来
#所有砝码可以称量的重量不可能超过所有砝码的质量和W，所以定义一个dp[False]*(W+1)，+1是为了维护0，0质量一定可以被称出
#接着，遍历所有砝码种类，同时在每一轮定义一个used[1/0]的数组，表示当前的称重量在当前砝码种类是否已经被称过

#对单个砝码种类，从0开始遍历所有的质量，方法是：
#对于某个质量，如果它可被称出dp[weight]=True，并且本轮对砝码的遍历use[weight]=0，即还没有被称出过
#（dp为false说明该质量在之前的砝码也称不出,use为1则说明对该种类的砝码，该质量已经称过一次，不可再称）
#那么，逐一往该质量weight上“加砝码”，直到数量到上限为止，加上若干个当前重量的砝码，重量为new_weight
#加上砝码后，如果dp[new_weight]还是false，那么设为True，同时标记该new_weight已经称出过一次，use[new_weight]=1，后续的外层质量遍历不可再称
#如此反复直到所有砝码被称完，最终返回dp数组，其总和表示可以称出的质量种类

#实际上近似暴力穷举方法，但根据weight和砝码的使用情况进行了大量的剪枝，减少了很多重复计算，对比纯暴力搜索要快得多

#——————————
#1.多重背包问题  
#参考几种背包问题.md

#——————————
#2.sum函数对布尔列表
#对象如果是仅有false和true所组成的列表，依然可以使用，因为true也被视为1，false也被视为0
#所以sum(list[bool])会返回一个值，该值表示此列表中为true的数量，可以用来统计“满足情况的条件总数”
