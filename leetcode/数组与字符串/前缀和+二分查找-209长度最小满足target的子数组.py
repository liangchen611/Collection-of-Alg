import bisect
from math import inf

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 找到一个子数组，满足：pre[r]-pre[l-1]>=target
        # 转换条件，pre[l-1]<=pre[r]-target，找到最近的满足此式子的l，然后将r和l进行作差

        # 计算前缀和
        pre = [nums[0]]
        for i in range(1,len(nums)):
            pre.append(pre[i-1]+nums[i])

        best_l = inf
        current_l = 0
        has = 0

        for i in range(0,len(pre)):
            # 不能进行裁剪，还要继续往下找
            if pre[i]-target<0:
                continue

            # 当前前缀和=target，那么当前最优长度一定为i+1，还不能缩进
            if pre[i]-target == 0:
                has = 1
                current_l = i+1
            
            # 前缀和与target之差大于0的时候，则可能存在可以裁剪掉的值
            if pre[i]-target>0:
                has = 1

                # 没有满足的可以缩进的项，如果为开头，那么当前长度为1，否则，当前长度就是到i为止的长度
                if pre[i]-target<pre[0]:
                    if i==0:
                        current_l=1
                    if i>0:
                        current_l=i+1
                
                # 找最近的，第一个满足大于pre[i]-target的位置
                pos = bisect.bisect_right(pre,pre[i]-target)-1
                
                # 找到最近的有效位置pos，然后将i与之作差，可以得到长度
                if pos>=0 and pos<=len(pre):
                    current_l = i-pos

                # pos<0，说明找不到这样的一个位置，那么就不能缩减
                if pos<0:
                    current_l = i+1
                                    
            if current_l<best_l:
                best_l = current_l

        if has==0:
            return 0
        else:
            return best_l
       
'''
二分查找bisect
'''