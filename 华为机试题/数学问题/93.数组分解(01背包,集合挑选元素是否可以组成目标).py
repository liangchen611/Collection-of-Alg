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
