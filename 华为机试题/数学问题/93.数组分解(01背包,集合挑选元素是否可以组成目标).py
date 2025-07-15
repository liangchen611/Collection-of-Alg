import sys

n = int(input())
A = input().strip().split(" ")
A = [int(a) for a in A]

a = []
b=[]
for i in range(len(A)):
    if A[i]%5==0:a.append(A[i])
for j in range(len(A)):
    if A[j]%3 == 0 and A[j] not in a:b.append(A[j])

less = [l for l in A if l not in a and l not in b]
less.sort()

diff = 0
if a and b:
    diff = sum(a)-sum(b)
else:
    if a and not b: diff = sum(a)
    if not a and b: diff = 0-sum(b)

temp_a = []
temp_b = []

def can_balance(A, B, C):
    D = diff
    total_C = sum(C)
    
    if (total_C - D) % 2 != 0:
        return False
    target = (total_C - D) // 2
    
    # 背包问题：是否存在子集使得和为 target
    dp = set()
    dp.add(0)
    
    for num in C:
        new_dp = dp.copy()
        for s in dp:
            new_dp.add(s + num)
        dp = new_dp
    
    return target in dp

if can_balance(a,b,less):
    print("true")
else:
    print("false")
    
# 思路：首先简化题目，将原本序列当中5和3的倍数全部分到a和b，之后剩下less，然后对a和b两个列表中的数值和进行作差，得到D
"""
再引入两个列表A和B，用来存放将要放入两个数组中的数

假设要选取若干个数分别放到a和b，结果满足以下的式子：
(sum(a)+ca) - (sum(b)+cb) = 0
进一步推导以及移项：
sum(a)-sum(b)+ca-cb=0
D+ca-cb=0
cb = D+ca

并且，cb+ca=sum(C)
cb = sum(C)-ca

代入，得：
D+ca-sum(C)+ca=0
2ca = sum(C)-D
所以要满足的条件有：1.sum(C)-D是偶数  2.存在一组和为ca的值，使得sum(C)-D/2
"""

# 要找出这样的组合，实际上就是个0-1背包问题，每个物品只能拿一次，不断组合得到集合
"""
    dp = set()
    dp.add(0)
    
    for num in C:
        new_dp = dp.copy()
        for s in dp:
            new_dp.add(s + num)
        dp = new_dp
"""