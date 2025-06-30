import sys

hw = sys.stdin.readline().strip().split(" ")
h,w = int(hw[0]),int(hw[1])

r = [[0]*w for _ in range(h)]
for i in range(0,h):
    line = sys.stdin.readline().strip().split(" ")
    for j in range(0,w):
        r[i][j] = int(line[j])

visited = [[False] * w for _ in range(h)]
Path = []

# 搜索迷宫中的可行路径，深度优先搜索DFS，四向搜索，dxdy
def dfs(r,x,y,h,w,path):
    # xy值越界
    if x<0 or x>=h or y<0 or y>=w:
        return False

    # 墙
    if r[x][y] == 1:
        return False

    # 本轮递归已经来到过
    if visited[x][y]:
        return False

    # 若不符合上面跳出条件，先将该点加入路径并标记
    path.append((x,y))
    visited[x][y]=True

     # 到达终点，加入到visted数组中并返回true退出
    if x==h-1 and y==w-1:
        visited[x][y]=True
        return True

    # 从当前xy进行四个方向的递归
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
        if dfs(r,x+dx,y+dy,h,w,path):
            return True

    # 若是进入此处，说明上面的循环中出现了最上面的几种跳出方式，因此要弹出当前的节点，因为数据结构是栈，先入后出，后入先出，
    # 所以前面先append，visited先设true，后面弹出再用pop并设为false
    path.pop()
    visited[x][y]=False
    return False


if dfs(r,0, 0, h, w, Path):
    for i in range(len(Path)):
        print("("+str(Path[i][0])+","+str(Path[i][1])+")")

#迷宫问题，一般可以通过深度优先搜索DFS来解决——记忆化搜索+递归【出栈入栈】

#思路：先用一个二维数组r来存放迷宫的情况，1为墙0为通路,墙不可通过
#另外设置一个标记二维数组vistited，形状与r相同，表示在DFS中某个点是否已经被搜索过
#【DFS的要点：如何进行扩张，记忆化（出栈和入栈），判断结束的边界】
#先设定几个返回false，导致该路线返回可以跳出（越界，墙，或者已经vistied)
#如果不符合以上的条件，那么先将该节点加入到路径列表当中，并将该点的visit设为true（避免后续递归时对该点进行重复计算）

#如果当前的xy已经是终点的坐标，那么将终点加入visited，并返回true
#还未到终点的话，进行四向的DFS递归，当内层递归返回true时，外层也返回true表示该路可行，否则就说明此路径不通
#此路径不通，则从path弹出该点，并将visited标记为false【DFS是栈结构】

#——————————

#1.二维数组的合法快捷定义
# 对二维数组，假设它的高为h，宽为w，那么合法的定义方式是[[elem]*w for _ in range(h)]
# 即先将有w个元素的一行当做一个整体，然后用列表推导式，创建h个

# 类似[[elem] for _ in range(w)]*h ——————这种方法是不合法二代，所以一定要在内部先乘以宽度，外部再扩展

#——————————

#2.DFS深度优先搜索
#参考DFS.md。