class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        L = len(nums)
        res = []

        def dfs(start,path):
            res.append(path[:])
            for i in range(start,L):
                path.append(nums[i])
                dfs(i+1,path)
                path.pop()
        
        dfs(0,[])
        return res
        

def subsets(nums):
    L = len(nums)
    res = []
    
    def dfs(start,path):
        # 每深入一次，将结果加入到列表当中
        for i in range(start,L):
            path.append(nums[i])
            dfs(start+1,path)
            path.pop()
     
    dfs(0,[])
    
'''
可以用想象这么一个过程，一开始是一个空列表——[]

对于一串数字，每一个数字都先尝试将它放进去，例如，先放1，[1]——最外层的循环，start为1，进入当前的DFS

然后我们尝试放接下来的数字，例如2，我们放进去，得到[1,2]，接着放，放到没有数字可用了为止，例如放到[1,2,3]，start=L，不再执行循环了

那么我们弹出最后一个，变成[1,2]，内层弹出2，变为[1]，然后接着跑循环，变为[1,3]

[]
[1]
[1 2]
[1 2 3]——弹出
[1 2]——弹出
[1 3]——弹出
[1]——弹出
[]
[2]
[2 3]——弹出
[2]——弹出
[]
[3]

[0]
|——[1]
|——|——[1 2]
|——|——|——[1 2 3]
|——|——[1 3]
|——[2]
|——|——[2 3]
|——[3]
'''