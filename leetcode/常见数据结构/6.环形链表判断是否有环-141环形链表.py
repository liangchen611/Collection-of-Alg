# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:   # 相遇，说明有环
                return True
        return False
    
'''
判断一个链表内是否存在环：
等效为一个龟兔赛跑问题：
一个快fast指针，每次跳2格
一个慢slow指针，每次跳1格

如果存在环，那么fast在环内一定能够追上slow，也就是二者一定会出现相等的情况
'''