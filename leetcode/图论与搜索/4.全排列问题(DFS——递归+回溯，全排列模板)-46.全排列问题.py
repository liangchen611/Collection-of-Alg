class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def dfs(start):
            if start==n:
                res.append(nums[:])
                return

            for i in range(start,n):
                nums[start],nums[i] = nums[i],nums[start]
                dfs(start+1)
                nums[start],nums[i] = nums[i],nums[start]
        
        dfs(0)
        return res
        
'''
全排列问题的一般解法：深度优先搜索DFS——递归+回溯

解法思想：
对于产生的排列的每一个位置，逐个地尝试用每个元素来代替它，
【“枚举每个位置上可能放的数” + “递归剩下的排列” + “回溯恢复现场”】

“我把第 start 个位置换成第 i 个元素的值（试试看）——nums[start], nums[i] = nums[i], nums[start]
递归看看剩下的怎么排——确定当前的搜索后，往下看
再把它换回来（回溯）。”
'''