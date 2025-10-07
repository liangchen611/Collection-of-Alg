from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # 当grid为空时，直接返回0，不存在岛屿
        if not grid: 
            return 0
        
        rows,columns = len(grid),len(grid[0])
        count = 0
        
        def bfs(i,j):
            q = deque()
            q.append((i,j))
            grid[i][j]="#"
            while q:
                x,y = q.popleft()
                for dx,dy in (1,0),(-1,0),(0,1),(0,-1):
                    x+=dx
                    y+=dy
                    if 0<=x<rows and 0<=y<columns and grid[x][y]=='1':
                        grid[x][y]="#"
                        q.append((x,y))
            
        
        for i in range(0,rows):
            for j in range(0,columns):
                if grid[i][j]=='1':
                    count+=1
                    bfs(i,j)
                
        return count
        
'''
采用BFS广度优先搜索的策略：当一片陆地搜索过一次之后，就不再进行回退

假设图中某个地方(i,j)出现陆地，那么它至少会连通一片陆地，因此count+=1
然后，基于这个点，进行BFS搜索，搜索四个方向(0,1),(0,-1),(1,0),(-1,0)

广度优先搜索一般采用队列方式来解决，用定义一个deque，它用来存放当前待搜索的点

从deque中逐个弹出队列里的元素，然后向四个方向扩展，是陆地就标记为#，表示已经搜索，并且不回退状态，然后将这个点加入队列

表示此点在下一次的循环当中会充当一个搜索起点
'''