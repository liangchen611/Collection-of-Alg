import sys
from collections import deque

nk = sys.stdin.readline().strip().split(" ")
n,k = int(nk[0]),int(nk[1])

nums = sys.stdin.readline().strip().split(" ")
nums = [int(ns) for ns in nums]

def max_sliding_window(nums, k):
    q = deque()  # 存放下标
    res = []

    for i, num in enumerate(nums):
        # 确保队列单调递减
        while q and nums[q[-1]] <= num:
            q.pop()
        q.append(i)

        # 移除滑出窗口的元素
        if q[0] <= i - k:
            q.popleft()

        # 窗口形成后记录结果
        if i >= k - 1:
            res.append(nums[q[0]])

    return res

res = max_sliding_window(nums,k)
for i in range(0,len(res)):
    print(res[i],end=" ")

'''
标准的滑动窗口问题——解决思路：单调队列
单调队列的基本思路：单调队列deque

另外开一个队列，队列存放下标，这个队列用来表示“最有可能，最有潜力成为窗口最大值的下标”，并且严格递减

例如[9, 7, 2, 5, 4]，设单调队列dq=[]
一开始，dq为空，9对应的下标0进入dq，dq=[0],窗口大小=1

下一个7，比9小，但是因为9可能会过期，所以7仍然入队，dq=[0,1]，窗口大小=2

下一个2，处理同7，2入列后，窗口被填满，此时输出队首的最大值——nums[0]=9

下一个5，首先它比末尾的2要大，意味着这个2在之后不可能是最大值，因为有一个5在前面挡着，所以2对应的下标出列，5入列
dq = [0,1,3]
然后注意到，窗口大小为3，而此时下标0< 3（当前5所对应的下标）-k(窗口大小)+1，所以也必须移除
最终dq = [1,3]，输出队首的nums[1]=7

下一个4，因为比5小，所以有潜力入列，dq=[1,3,4]
1<4-3+1，所以队首元素已经过期，它需要移除
最终队列变为dq = [3,4]
'''