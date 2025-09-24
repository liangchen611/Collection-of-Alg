from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        win = deque()
        seq = []

        if k==1:
            return nums

        if len(nums)<=k:
            seq.append(max(nums))
            return seq

        # 只将每次有可能成为最大值的值加入到列表当中

        for i in range(0,len(nums)):
            s = nums[i]
            if len(win)==0:
                win.append(i)
                continue

            # 列表末尾比当前元素小，它不再可能是窗口最大值，反之若是末尾更大，那么就直接入列
            elif len(win)>0:

                while win and s>=nums[win[-1]]:
                    win.pop()
                
                win.append(i)
                
                if i<k-1:
                    continue
                
                if i>=k-1:
                    if i-win[0]>=k:
                        win.popleft()
                    
                    seq.append(nums[win[0]])
        
        return seq

                    
                