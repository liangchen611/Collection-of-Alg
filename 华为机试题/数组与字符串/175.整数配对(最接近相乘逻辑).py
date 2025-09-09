import sys

nk = sys.stdin.readline().strip().split(" ")
n,k = int(nk[0]),int(nk[1])

nums = sys.stdin.readline().strip().split(" ")
nums = [int(ns) for ns in nums]

#对数组进行从大到小的排序，两个乘数越接近，二者相乘的结果也越大
nums.sort(reverse=True)

result = 0

for i in range(0,n-1):
    if nums[i]==-1:
        continue
    diff = nums[i]-nums[i+1]
    # 最接近的也越界，那么后面必然也越界,所以可以直接排除
    # 用nums[i]=-1，来判断，该数是不能用，还是已经用过，变为-1之后直接跳过
    if diff>k:
        nums[i]=-1
        continue
    
    # 在可接受的差值之内，直接求积加上，然后标记这些位置已经用过
    if diff<=k:
        result+=nums[i]*nums[i+1]
        nums[i]=-1
        nums[i+1]=-1
# 5 4 4 1 1 1    

print(result)