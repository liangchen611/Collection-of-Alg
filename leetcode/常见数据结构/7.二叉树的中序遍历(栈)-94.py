# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        node_stack = []
        num_stack = []
        pointer = root

        while pointer or node_stack:
            # 向左遍历，把左子树节点压入栈中
            while pointer:
                node_stack.append(pointer)
                pointer = pointer.left
            
            # 左遍历完，弹出当前栈顶，当前栈顶是最后一个访问的节点，加它的值加入到值数组当中
            pointer = node_stack.pop()
            num_stack.append(pointer.val)

            # 然后向右进行遍历
            pointer = pointer.right

        return num_stack
       
"""
栈法的结构是：

外层 while 控制“整体还没结束”

内层 while 不断入栈走到最左

出栈 → 访问 → 转右
"""

'''
    1
     \
      2
     /
    3
    
运行过程：

curr=1 → 入栈 → curr=None

栈弹出1 → 输出 1 → curr=2

curr=2 → 入栈 → curr=3 → 入栈 → curr=None

栈弹出3 → 输出 3 → curr=None

栈弹出2 → 输出 2 → curr=None

栈空结束
结果：[1,3,2]
'''