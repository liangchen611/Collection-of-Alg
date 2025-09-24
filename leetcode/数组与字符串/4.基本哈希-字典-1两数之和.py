class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n_dict = {}
        for i in range(0,len(nums)):
            n_dict.setdefault(nums[i],[]).append(i)
        print(n_dict)

        rst = []
        for i in range(0,len(nums)):
            s = target-nums[i]
            
            value = n_dict.get(s,None)
            
            if value is not None:
                # 差等于自己的情况，此时值列表长度需要在2以上才有可能，为1的情况不成立
                if s == nums[i] and len(n_dict[s])>1:
                    if i!=n_dict[s][0]:
                        rst.append(n_dict[s][0])
                        rst.append(i)
                        break
                    if i==n_dict[s][0]:
                        continue

                elif s==nums[i] and len(n_dict[s])==1:
                    continue
                    
                rst.append(i)
                rst.append(value[0])
                break

        return rst