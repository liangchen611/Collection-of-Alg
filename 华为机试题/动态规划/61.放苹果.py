import sys

mn = sys.stdin.readline().strip().split(" ")
m = int(mn[0])
n = int(mn[1])

DP = [[0] * (m + 1) for _ in range(n + 1)]  # 行是盘子数，列是苹果数

# 初始化
for j in range(1, m + 1):  # 1个盘子
    DP[1][j] = 1
for i in range(n + 1):     # 0个苹果
    DP[i][0] = 1

# 状态转移
for i in range(2, n + 1):      # 盘子数
    for j in range(1, m + 1):  # 苹果数
        if j < i:
            DP[i][j] = DP[j][j]
        else:
            DP[i][j] = DP[i - 1][j] + DP[i][j - i]

print(DP[n][m])  # 将 m 个苹果放入 n 个盘子的方案数

#DP[i][j]：将j个苹果放到i个盘子中的方案数量
#状态转换关系：1.如果只有1个苹果或者1个盘子，那么总方案数显然为1
#如果盘子的数量比苹果还多，那么此时增加盘子并不会增加方案数量，所以dp[i+1][j]=dp[i][j]

#其他情况下：i个盘子放j个苹果，首先一定会继承i-1个盘子时放j个苹果的方案数，因为只需要在这些方案中加一个空盘即可
#那么就考虑，先把所有盘子都放一个苹果，剩下j-i哥苹果，这种情况下，和都是空盘没有区别，然后就在剩余苹果的数量之上，计算子方案数

#状态转换方程可以写为：dp[i][j] = dp[i-1][j] + dp[i][j-i]