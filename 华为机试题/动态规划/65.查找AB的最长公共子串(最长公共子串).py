from math import inf
import sys

s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

# DP:A为A[i-1]结尾，B为B[j-1]结尾时的最长公共子串长度
DP = [[0]*(len(t)+1) for _ in range(len(s)+1)]
longer = -1
if len(s)>len(t):
    longer = 1
else:
    longer = 0

max_len = 0
candidates = []


# 

for i in range(1,len(s)+1):
    for j in range(1,len(t)+1):
        if s[i-1] == t[j-1]:
            DP[i][j] = DP[i-1][j-1]+1
            if DP[i][j] > max_len:
                max_len = DP[i][j]
                candidates = [(i,j)]
            if DP[i][j] == max_len:
                candidates.append((i,j))

# t更短
end_index = inf
if longer == 1:
    for i in range(0,len(candidates)):
        index = candidates[i][1]
        if index < end_index:
            end_index = index
    print(t[end_index-max_len:end_index])

# s更短
if longer == 0:
    for i in range(0,len(candidates)):
        index = candidates[i][0]
        if index < end_index:
            end_index = index
    print(s[end_index-max_len:end_index])


# 最长公共子串——动态规划
# DP[i][j]——A为A[i-1]结尾，B为B[j-1]结尾时的最长公共子串长度（为什么要i-1和j-1——防止越界，并且更符合人的直觉）

# 状态转移条件：如果A[i-1] == B[j-1]，那么当前DP[i][j]的长度就在DP[i-1][j-1]上+1
# 使用两层循环，外层为A的下标，内层为B的下标

# 确认状态转移后，比较当前DP[i][j]和max_len最大长度的关系，如果DP[i][j]更大，则更新max_len的值，同时记录下节点i（对应A中下标）

# 补充条件：【要求较短的字符串中最早出现的最长公共子串】——解决方法，比较DP长度后加入到候选节点列表中
# 当max_len被更新时，清空并更新candidates列表，如果当前DP长度=max_len，将(i,j)加入到candidates

# 之后，若A较短，搜索candidates的[0]，若B较短则搜索[1]
# 找出其中最小的下标index，然后用列表切片进行打印：String[index-max_len:index]