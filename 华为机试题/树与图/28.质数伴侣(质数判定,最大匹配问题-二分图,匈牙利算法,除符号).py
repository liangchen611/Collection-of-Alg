# 最大匹配问题（二分图，匈牙利算法）
# 思路：判质数+二分图匹配（根据质数的性质，拆成奇数集与偶数集两个集合，然后对两个集合用二分图匹配）

# 判质数方法，试除法，复杂度O(√n),从2~√n进行整除测试
def prime_judge(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            # 判断能否整除：%
            # 判断n是否小于i：//
            return False
    return True

# 二分图的邻接表，两两配对，两个图的长度不重要，但左边要少于右边。
# 收集graph，下标为odd中元素所对应下标，
# 下标对应的值表示odd中某个元素可以与even中元素组成质数的下标的列表集合
# 例如odd=[1,3,9],even=[2,4,6]，则graph=[[0,1,2],[0,1],[0,1]]
def by_graph(odd,even):
    graph = [[] for _ in range(len(odd))]
    # 其中_表示变量占位符，表示该变量不会被使用，在循环中相当于只求循环的次数，可用于创建空队列
    for i in range(0, len(odd)):
        for j in range(0, len(even)):
            if prime_judge(odd[i]+even[j]):
                graph[i].append(j)
    return graph

# 增广路径算法，匈牙利算法寻找二分图的最大匹配
def bpm(L, visited, match_to, graph):
    # 尝试让小孩L坐上某张椅子R
    for R in graph[L]:  # 遍历小孩L能坐的椅子
        if not visited[R]:  # 如果这把椅子今天还没尝试过
            visited[R] = True  # 标记：尝试过了
            if match_to[R] == -1:
                # 椅子没人坐，直接登记为L坐
                match_to[R] = L
                return True
            else:
                # 椅子有人坐（小孩L'），让L'去找别的椅子
                if bpm(match_to[R], visited, match_to, graph):
                    # 若L'成功换了椅子，那么R空了，L坐上R
                    match_to[R] = L
                    return True
    return False  # 所有椅子都尝试失败

def max_prime_pairs(arr):
    odds = [elem for elem in arr if elem % 2 == 1]
    evens = [elem for elem in arr if elem % 2 == 0]
    # 左为小孩，右为椅子
    # 二分图最大匹配，左侧图要更短，交换位置
    if len(odds) > len(evens):
        odds, evens = evens,odds
    graph = by_graph(odds,evens)
    
    match = [-1]*len(evens)
    max_match = 0

    # visited[] 每轮都要清空（重置）；孩子抢座位时自己带的尝试表
    # match_to[] 却是整个过程都保留（全局匹配状态）；全局记录当前位置被哪个孩子坐

    for i in range(0,len(odds)):
        visited = [False]*len(evens)
        if bpm(odds[i],visited,match,graph):
            max_match += 1
    return max_match


#-----notes!-----
#1.几种除法符号的区别-%,//,/
# /——除法，返回两个数相除后所得的商的精确值浮点数
# //——整除，求两个数相除之后的整数部分
# %——求余数，若为0，则可被整除，在算质数的时候需要用%来进行判断

#2.质数的判定-时间复杂度O(√n)
#0和1不是质数，2为质数，所以判定从2开始，输入一个整数n
#从2到√n(n的0.5次方）为止（因为python中的range(a,b)，范围是从a~b-1，所以在范围中用range(2,n**0.5+1)
#逐个用n去除，求其余数，如果出现有余数为0的情况，则n不是一个质数，直接结束循环
#循环结束时，若未出现上面的情况，则判断n是一个质数

#3.二分图的邻接表
#现在有N和M两个集合，按某个条件构建一个二分图的邻接表
#实际上，就是依据N中的元素所对的下标，将M中的下标进行赋值对应。
#不过，N的长度需要不大于M
#新建另一个表称为graph来进行值的存储，一般会有如下的形成格式：
# for i in range(len(N)):
#   for j in range(len(M)):
#       if (N[i]和M[j]满足一定的条件)：
#           graph[i] = j ——增添的邻接表元素

#4.最大匹配问题
#详见二分图-最大匹配问题.md。