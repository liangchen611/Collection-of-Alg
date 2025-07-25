import sys
pw = sys.stdin.readline().strip()

def longest_symmetry(s:str)->str:
    max_length = 1
    start = 0  # 记录最长回文子串起始位置
    n = len(s)
    if n < 2:
        return s

    # dp[i][j]——i为起点，j为终点时是否构成回文子串，大小为n*n
    dp = [[False]*n for _ in range(0,n)]

    # 单字符必为回文字：初始状态
    for i in range(0,n):
        dp[i][i] = True
    
    # DP
    # dp[i][j] = (s[i]==s[j]) and (j-i <= 2 or dp[i+1][j-1]==True)
    for length in range(2,n+1):
        # 长度优先，逐步扩张子串的长度
        for i in range(0,n-length+1):
            # 每次扩展子串的长度，i都从头开始,i为子串左边界，j为右边界
            j = i+length-1
            if s[i] == s[j]:
                if length <= 2 or dp[i+1][j-1] == True:
                    # 更新子状态用于下一次的更新
                    dp[i][j] = True
                    if length > max_length:
                        # 更新长度
                        max_length = length
                        start = i

    return max_length

L = longest_symmetry(pw)
print(L)

#思路：对原始的字符串，求它的最长的对称子串（也称为回文子串）
#函数中需要记录2个数据，1.子串可能的最大长度max_length  2.子串最长时的起始位置start
#创建一个DP二维布尔数组，DP[i][j]表示，以i为起点，j为终点时，此子串是否能够构成一个对称子串
#分析子串仍为对称子串的条件：如果一个以i为起点，j为终点的字符串是一个对称子串，
#1.【满足s[i]=s[j]】
#2.【如果此时s[i:j]的长度在3以下，也就是j-i<3，那么s[i:j]构成一个对称子串】
#3.【如果2不满足，那么必须满足S[i+1:j-1]也是一个对称子串，也就是DP[i+1][j-1]=True

#对此可以构建状态方程：【dp[i][j] = (s[i]==s[j]) and (j-i <= 2 or dp[i+1][j-1]==True)】
#以长度为标准，逐步扩展子串的长度，从2开始到n结束
#测试【从每个i为开头位置，length为子串长度，j为终点位置】这样的一个子串是不是对称子串
#如果判断是存在——通过了布尔检测，且当前循环的长度length要比max_length要长，那么更新长度并记录下当前i的位置

#-----线性规划的思路与分析-----
# 详见线性规划的思路与分析