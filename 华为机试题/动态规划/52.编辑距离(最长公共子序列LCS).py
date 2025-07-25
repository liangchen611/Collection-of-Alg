import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

# 编辑距离
def edit_distance(A: str, B: str) -> int:
    n, m = len(A), len(B)
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    #DP定义：dp[i][j] 为将 A[0:i] 转成 B[0:j] 所需的最少操作数。 
    #dp[0][j]=j，将A从空串补充为B的前j个元素，需要进行j次操作 
    #dp[i][0]=i，将A从的前i个元素删除为空串，需要i次操作

    for i in range(n+1):
        dp[i][0] = i
    for j in range(m+1):
        dp[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:
                # 如果在某个位置A的值和B的值相同，那么该值是不需要进行操作，所以所需操作数和前一个位置相同
                dp[i][j] = dp[i-1][j-1]
                
                # 如果不同，那么需要进行一定的修正操作
            else:
                dp[i][j] = min(
                    dp[i-1][j-1],  # 替换
                    dp[i][j-1],    # 插入
                    dp[i-1][j]     # 删除
                ) + 1
    return dp[n][m]

DP = edit_distance(s,t)
print(DP)

# DP类问题，尝试通过画DP图的方式来解决，用DP图自己手动推理
