from collections import deque,Counter
import sys

t = int(input())

def judge(na, nb, m, k):
    q = deque()
    count = 0
    cnt_b = Counter(nb)
    cnt_c = Counter()
    S = 0   # 当前窗口的最大匹配数

    for i in range(len(na)):
        # 入窗口
        val = na[i]
        q.append(val)
        old = cnt_c[val]
        cnt_c[val] += 1
        # 更新 S
        if val in cnt_b:
            S += min(cnt_c[val], cnt_b[val]) - min(old, cnt_b[val])

        # 窗口超长，移除最左元素
        if len(q) > m:
            left = q.popleft()
            old = cnt_c[left]
            new = old - 1

            if left in cnt_b:
                S += min(new, cnt_b[left]) - min(old, cnt_b[left])

            if cnt_c[left] == 0:
                del cnt_c[left]
            else:
                cnt_c[left]=new                

        # 判断窗口是否满足条件（窗口长度正好等于 m 时才判断）
        if len(q) == m and S >= k:
            count += 1

    return count

for i in range(0,t):
    nmk = sys.stdin.readline().strip().split(" ")
    n, m, k=int(nmk[0]),int(nmk[1]),int(nmk[2])

    a = sys.stdin.readline().strip().split(" ")
    a = [int(asub) for asub in a]

    b = sys.stdin.readline().strip().split(" ")
    b = [int(bsub) for bsub in b]

    print(judge(a,b,m,k))

'''
思路小结：
在滑动窗口中进行值的匹配，关键是维护一个计数的字典，使用"Counter"函数（collection类）。
'''

# counter对一个列表中的各个不相同的元素进行统计，然后返回一个key=元素，value=计数的字典。

'''
对该问题，首先可以轻松算出b的counter字典cnt_b——关键是维护滑动窗口的counter字典cnt_c。

遍历元素时，先有一个子列表q，用来存放当前遍历的元素，并记录遍历的长度。

遍历一个元素后，先将它加入到q中，然后再用old = cnt_c[val]的方法计数（要+1）。

如果val存在于字典cnt_b的键当中，并且当前cnt_c[val]的值比cnt_b[val]的值要小，那么贡献度S+1(这么比是因为匹配的数量不能超过b中的数量，在此之前，每匹配一个贡献度就+1)

用窗口q的长度作为进一步的判断条件，如果超长，那就必须移除q最左端的元素。

移除后，必须考察当前移除的元素是否加入了匹配，并且在cnt_c中减去相应的值，如果这个元素有贡献度，那么S也要减去。

当窗口长度为m并且匹配总贡献S>=k时，计数+1，说明当前的子序列c是一个目标序列。
'''