import sys
from collections import deque,Counter

n = int(input())
nums = sys.stdin.readline().strip().split(" ")
nums = [int(nsub) for nsub in nums]

if n==1:
    print(1)

def judge(num):
    q = deque()
    seen = set()
    max_len = 0
    res = []
    
    # left函数，记录当前运算区间最左端的位置
    left = 0

    for i in range(0,len(num)):
        value = num[i]

        # 有重复的情况，就从运算区间中逐个剔除元素，直到集合中不再重复为止
        # 每次剔除，左端的位置都要前进1格
        while value in seen:
            left_value = q.popleft()
            seen.remove(left_value)
            left+=1
        
        q.append(value)
        seen.add(value)

        length = len(q)
        if length>max_len:
            res = [(left,i)]
            max_len = length
        elif length==max_len:
            res.append((left,i))

    return res

if n!=1:
    result = judge(nums)
    print(len(result))
    for i,t in enumerate(result):
        print(t[0]+1,end=" ")
        print(t[1]+1)


# set-集合，存放两两不相同的元素，用add和remove来给集合增加新的元素，或者是移除已有的元素

'''
用滑动窗口解决，逐个地向右遍历数组当中的元素，可以分成几种情况：
1.当前元素和当前子区间不重复
    再分三种情况：
    1.当前子区间长度<最长长度——这种情况直接将元素加入子区间并进入下一个循环
    2.当前子区间长度=最长长度——将元素加入子区间，弹出当前的left值和当前的right值，加入到result数组当中，表示当前的区间是最长区间的其中之一
    3.当前子区间长度>最长长度——将元素加入子区间，清空原本的result，然后将(left,right)加入到result数组当中

2.当前元素和当前子区间重复
    此时，必须从前面逐个将子区间的元素逐个弹出，直到当前元素在子区间不存在为止。
    每次弹出后，表示左端位置的left都前进1格
'''