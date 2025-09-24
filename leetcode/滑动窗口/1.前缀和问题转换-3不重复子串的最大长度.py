from collections import deque,defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        last = {}  # 记录字符上一次出现的下标
        l = 0
        ans = 0

        # 维护一个字典，字典每个键的值记录某个字母出现的最靠右的位置，不断更新

        for r, ch in enumerate(s):
            if ch in last and last[ch] >= l:
                l = last[ch] + 1
            last[ch] = r

            # 关键在于这一句，只需知道每次出现重复或是不重复后，截断的位置，然后根据大小进行比较即可
            # 具体的字符不关心，只比较长度，不需要对字符串本身做什么操作

            ans = max(ans, r - l + 1)

        return ans