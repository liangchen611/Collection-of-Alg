#-----二分查找---------
#1.找到第一个比x大的下标
def lower_bound(arr, target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid+1
        else:
            high = mid
    return low

#2.找到第一个比x小的下标
def lower_bound_decrease(arr,target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) //2
        if arr[mid] > target:
            low = mid+1
        else:
            high = mid
    return low
#-----------------------------------------------------
#-----最长递增子序列LIS(Longest Increasing Sequence)-----
#贪心算法+线性规划：设有一个tails，一开始只有数组第一个元素，往后遍历，如果当前元素比tails最后的值要大，那么将它加入tails中。
#继续遍历，如果当前的元素，比tails中某个元素要小，例如tails=[1,3,5]，找到2，则替换3，tails变成[1,2,5]。
#因为tails存放的是“有最大潜力可以让LIS变得更长的值，2在第二位会比3在第二位更有潜力，所以替换。
#这样得到的tails，其长度就是数组所对应的LIS的值。
#LIS和LDS的最短长度为2，如果长度为1就只有一个元素，就不会构成严格递增与严格递减。


#1.对某个数组，找出其LIS的长度
def LIS_length(arr):
    tails = arr[-1]
    #tails：第i个元素中，最有可能产生更长的递增序列的值（基于贪心算法），但tails数组的最终值并不是最终LIS的值，只表示长度
    for i in range(0,len(arr)):
        num = arr[i]
        if num > tails[-1]:
            tails.append(num)
        else:
            pos = lower_bound(tails, num)
            # 如果导入了bisect，可以用bisect.bisect_left函数进行替代
            tails[pos] = num
    return len(tails)

#2.如果要搜索一个数组中所有位置为末尾时的LIS长度
def LIS_count(arr):
    tails = arr[-1]
    inc = [1]*len(arr)
    # 新增inc数组来统计，该下标位置为末尾时LIS的长度，数组的长度与原数组的长度相等，并且LIS长度至少为2，因此初始化为1
    for i in range(0,len(arr)):
        num = arr[i]
        if num > tails[-1]:
            tails.append(num)
            inc[i] = len(tails)
        else:
            pos = lower_bound(tails, num)
            # 如果导入了bisect，可以用bisect.bisect_left函数进行替代
            tails[pos] = num
            inc[i] = pos+1
            # pos位置表示LIS的长度
    return len(tails)

#3.如果要计算最小递减子序列LDS(longest decreasing sequence)的长度:
#则将数组倒转过来求LDS，然后将结果倒转，即为LIS
#LIS = LIS_count(arr)
#LDS = LIS_count(arr[::-1])

#4.返回最长递增序列的具体值
#需要再引入一个新的前导数组prev以及下标数组index，进行辅助记录
def LDS_sequence(arr):
    tails = []
    indx = []
    prev = [-1]*len(arr)

    for i in range(0,len(arr)):
        num = arr[i]
        pos = lower_bound_decrease(tails,num)
        if pos == len(tails):
            tails.append(num)
            indx.append(i)
        else:
            tails[pos] = num
            indx[pos] = i
        if pos > 0:
            prev[i] = indx[pos-1]
            #当前链接元素的上一个元素的索引下标——需强调是在pos，也就是LIS中寻找的，而不是原数组，根据LIS中的下标值，通过index确认该值对应的原始数组的下标

    # 回溯：从最后一堆的下标一路沿 prev 找回去
    k, seq = indx[-1], []
    while k != -1:
        seq.append(arr[k])
        k = prev[k]

    # 回溯的过程：从后往前看，从indx最后一位开始，可以获取到最长子序列的最后一位元素，Prev就是最长子序列构成的元素所对应的原始数组中的下标，只需读出来再调换
    # prev数组与原始数组的下标是一一对应的关系，数组长度相同，所以可以用prev作为参考值来逐步回溯得到的最子序列，并且不会发生重复
    return seq[::-1]