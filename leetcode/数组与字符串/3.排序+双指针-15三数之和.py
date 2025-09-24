class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 顺序排序数组
        n = sorted(nums)
        res = []
        all_z = 1
        print(n)

        for i in range(0,len(n)-2):

            # 防止数组全为0的情况
            if n[i]!=0:
                all_z=0
            if i == len(n)-2 and all_z==1:
                return [[0,0,0]]

            # 防止重复
            if i>0 and n[i]==n[i-1]:
                continue
            
            # 设定左右指针的位置
            l = i+1
            r = len(n)-1
            
            while l<r:
                s = n[i]+n[l]+n[r]
                print("S="+str(s))
                if s==0:
                    res.append([n[i],n[l],n[r]])
                    print(l)
                    print(r)
                    # 防止出现重复的情况，如果有重复，就移动指针，l往右移，r往左移
                    while l<r and n[l]==n[l+1]:
                        l+=1
                    while r>l and n[r]==n[r-1]:
                        r-=1
                    l+=1
                    r-=1
            
                # 因为原数组已经经过了从小到大的排序，所以加和小于0，则要左指针要右移尝试变大；加和大于0，右指针左移尝试变小
                elif s<0:
                    l+=1

                elif s>0:
                    r-=1

        return res
