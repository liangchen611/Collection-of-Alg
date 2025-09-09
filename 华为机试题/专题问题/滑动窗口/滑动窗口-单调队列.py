from collections import deque

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

'''

deque:双端队列

双端操作 O(1)

左边（队首）/右边（队尾）都可以快速 append / appendleft / pop / popleft

列表 list 在开头插入或删除是 O(n)，而 deque 是 O(1)

'''

q = deque()
q.append(3)      # 队尾加入
q.append(1)      
q.popleft()       # 队首弹出
q.append(5)
print(q)          # deque([1,5])