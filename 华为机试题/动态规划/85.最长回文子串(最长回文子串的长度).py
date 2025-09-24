class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_l = 0
        # DP[i][j]表示，当字符串以i为开头，j为结尾时，是否构成一个回文子串
        DP = [[False]*len(s) for _ in range(0,len(s))]

        # 当字符串只有一个字符时，它显然是回文子串
        for i in range(0,len(s)):
            DP[i][i]=True

        # 外层的L，回文子串的长度，循环中不断扩展回文串长度
        for l in range(2,len(s)+1):
            # 如果字符串本身的长度为1，那么没必要扩展直接输出
            if len(s)==1:
                return s
            else:
                # 从i开头搜索，根据当前搜索长度设置范围
                for i in range(0,len(s)-l+1):
                    # j是当前长度回文串的结尾
                    j = i+l-1

                    # 必须相等才构成回文串
                    if s[i]==s[j]:
                        # 仅有2个字符，或者内层也是回文串时，才成立
                        if l==2 or DP[i+1][j-1]==True:
                            DP[i][j]=True
                            if l>max_l:
                                max_l=l