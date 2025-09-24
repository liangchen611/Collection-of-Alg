from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = []

        current_sum = 0

        for i in  range(0,len(nums)):
            current_sum+=nums[i]
            pre.append(current_sum)

        k_count = 0

        pre_cnt = defaultdict(int)
        pre_cnt[0]=1

        for i in range(0,len(nums)):
            if pre_cnt[pre[i]-k]>0:
                k_count+=pre_cnt[pre[i]-k]
            pre_cnt[pre[i]]+=1
        
        return k_count

        # sub_sum = [1,3,6],前缀和，查找区间[l,r]之间的和时，求sub[r]-sub[l-1]，其中l必然≥1，因为当l=0时，查询值就是前缀和
          
        #    0 1 2   
        #  0 1 3 6 
        #  1   2 5
        #  3     3

        # sub[r]-sub[l-1]=k，可以转换成：sub[l-1]=sub[r]-k，右边这个出现过几次

# 前缀和pre：从列表的头部，到该处位置，所有的元素相加的和
# pre[i] = pre[i-1] + num[i]
# 从第l项开始，到第r项结束的数组之和，可以表示为pre[r] - pre[l-1]

# 如果要使得某个子数组的和为k，可以用以下的等式表示：pre[r] - pre[l-1] = k
# 看上去似乎可以用填表法来求得所有为k的索引，但这样的时间复杂度为O(n^2)

# 实际上，稍作分析可有以下的结论：
'''
关于大小，l<=r，也就是r比l大，遍历时r在l后，上面的等式通过移项可以转换为：pre[l-1] = pre[r] - k 

【当遍历一个pre[r]时，如果在此之前的pre当中，存在有某个pre[l-1]满足pre[r]-k，那么就存在相应的一个满足条件的子数组。】
我们不关心这些满足条件的子数组的位置在哪里，因此只需要统计其数量即可。

因此，前缀和为pre[i]的情况下，满足条件的子数组的数量就会增加【前缀和为pre[i]-k的值的数量】。

所以可以用一个【计数字典】来解决：
初始化 dict[0] = 1，表示从以下标0为结尾的前缀和至少有1个。

在之后的遍历过程中，先判断字典中pre[i]-k的键所对应的值是否为0，如果dict[pre[i]-k]不为0，就说明字典当中存在某个前缀和为该值。

因此count就加上相应的值。

在比较完之后，因为前面的前缀和值要提供给后面的前缀和值的判断，所以将pre[i]加入到计数字典当中。

'''