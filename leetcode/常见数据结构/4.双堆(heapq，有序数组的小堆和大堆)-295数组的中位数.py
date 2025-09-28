import heapq

class MedianFinder:

    def __init__(self):
        self.large = [] # 存放较大的数（最小堆）
        self.small = [] # 存放较小的数（最大堆）
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)

        heapq.heappush(self.large,-heapq.heappop(self.small))

        # 保证 small 的数量 >= large
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2

# 对一个有序排列的数组，可以将它分成“大的一半”和“小的一半”

# 其中，大的一半是一个【最小堆】，其堆顶存放当前堆中最小值（因为最小堆输出时是从小到大输出）

# 小的一半是一个【最大堆】，堆顶是其中最大值

# 求中位数，只需考虑这两个堆的堆顶元素即可——不过要考虑数组长度的奇偶性

# 因此，我们刻意让两个数组维持特定的大小关系——small数组的长度总是≥large长度

# 这样，当数组长度为奇数时，small长度＞large长度——输出small堆顶元素；当数组长度为偶数时，取堆顶的两个元素做平均值

# 时间复杂度——建堆O(logn)，查找O(1)

'''
情况一：刚开始没有数
来了第一个数，先放进 small。因为我们规定 small ≥ large。


情况二：新数来了
步骤 1：无脑先放到 small（加负号），即假设它属于“小的一半”。

步骤 2：再把 small 的堆顶元素移动到 large。这样能确保 small 的数都 ≤ large 的数。

步骤 3：如果 small 数量比 large 少，就把 large 堆顶再移回 small。这样保证了“数量平衡” (len(small) >= len(large))。
'''