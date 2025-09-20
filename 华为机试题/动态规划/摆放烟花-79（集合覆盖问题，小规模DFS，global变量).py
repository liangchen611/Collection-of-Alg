from math import inf
import sys

nmq = sys.stdin.readline().strip().split(" ")
n,m,q = int(nmq[0]),int(nmq[1]),int(nmq[2])

G = []
for i in range(0,n):
    g = sys.stdin.readline().strip()
    g = [int(sg) for sg in g]
    G.append(g)

P = []
sub_p = []

for i in range(1,n*q+1):
    p = sys.stdin.readline().strip()
    p = [int(sp) for sp in p]
    sub_p.append(p)
    if i%n == 0:
        P.append(sub_p)
        sub_p = []

best_count = inf
best_choice = [0]*q
current_choice = [0]*q

uncovered_g = []
for i in range(0,n):
    for j in range(0,m):
        if G[i][j]==0:
            uncovered_g.append((i,j))

def dfs(idx,count,uncovered):

    global best_count,best_choice

    # 超过已有最优长度时，剪枝
    if count>=best_count:
        return

    # uncovered长度为0时，说明已经被覆盖完
    if len(uncovered)==0:
        best_count = count
        for ct in range(0,q):
            best_choice[ct] = current_choice[ct]
        return 

    # 索引到达终点，没有可以遍历的表了
    if idx==q:
        return

    #dfs(idx+1,count,uncovered)

    # 当前表可以覆盖的点
    covered = []
    for (i,j) in uncovered:
        if P[idx][i][j]==1:
            covered.append((i,j))
    
    # 构建一个点覆盖后的状态表
    new_covered = []
       
    # 如果当前可覆盖的点数不是0，那么这个表是可用的
    if len(covered)>0:
        for (x,y) in uncovered:
            has = 0
            # 如果unconvered中的点(x,y),遍历convered中的点，存在(i,j)使得x=i,y=j，说明当前表可以覆盖这个点(x,y)
            # 我们要构建一个还未被覆盖的点的列表，因此用一个标识has表示此点是否能够入列
            for (i,j) in covered:
                if i==x and j==y:
                    has = 1
                    break
            # has=0，说明(x,y)不可被当前的表覆盖，因此加入到新的待覆盖列表中
            if has==0:
                new_covered.append((x,y))
    
    current_choice[idx] = 1
    
    # 计数+1
    dfs(idx+1,count+1,new_covered)
    current_choice[idx] = 0

dfs(0,0,uncovered_g)

print(best_count)
print(best_choice)

'''
	DFS 过程：
•	每次选择一个「未覆盖的 0」。
•	尝试所有能覆盖它的 P。
•	递归下去，直到所有 0 被覆盖。
•	用全局变量记录当前找到的最优解（最少表格数）。
'''

'''
gloabl变量：
一般在函数内部使用，表示该函数将会使用外部的变量，并且在该函数中全局使用。

global变量在递归函数中是全局共享的，如果不是全局共享的话，每次递归函数都需要维护自己独自的一份，DFS就没法更新值
'''