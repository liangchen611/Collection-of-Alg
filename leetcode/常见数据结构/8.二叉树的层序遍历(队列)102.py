# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        node_deque = deque()
        node_deque.append(root)
        nums = []
        pointer = None
        
        while node_deque:
            level = []
            for _ in range(0,len(node_deque)):
                pointer = node_deque.popleft()
                level.append(pointer.val)
                if pointer.left:
                    node_deque.append(pointer.left)
                if pointer.right:
                    node_deque.append(pointer.right)
            nums.append(level)

        print(nums)
        return nums
        
# 采用BFS-广度优先搜索的策略

'''
在一开始，先加入根节点到顶点队列（node_deque)当中，后续遍历中逐渐地将点逐个地出列与入列

当顶点队列不为空时，说明当前的树还没有遍历完；

因为要保存层数信息，当前层数的信息=当前队列当中的节点数量；

每次遍历执行的操作：
1.将当前的deque头元素出列，并读出它的值

2.将它的左和右子节点顺序地加入到队列当中

3.因为在一开始就规定了循环的次数是每轮遍历之前，队列中节点数量，所以每次遍历=将当前层的父节点全部按顺序地出列读取
'''