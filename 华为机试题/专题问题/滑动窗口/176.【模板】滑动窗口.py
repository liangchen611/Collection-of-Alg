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