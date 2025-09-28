# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        print(prev)
        return prev

'''
prev = None
curr = 1
链表: 1 → 2 → 3 → 4 → 5  
'''

'''
1 → None
prev = 1
curr = 2
剩余链表：2 → 3 → 4 → 5
'''

'''
一开始，prev 是空的，curr 指向链表的第一个节点（1）。
我们要做的，就是一路走下去，把每个节点的“指向”扭过来，让它指向前面，而不是后面。

第一步：
先把 curr 的下一个节点（也就是 nxt）存起来，不然等会指针改掉就找不到后面了。
然后把 curr.next 指向 prev（也就是让 1 不再指向 2，而是指向空）。
接着把 prev 往前走一步，让它指向 curr，再把 curr 往前走一步，让它变成刚才保存的 nxt。
——现在链表前半部分是 1 → None，后半部分还是 2 → 3 → 4 → 5。
'''

 public ListNode reverseList(ListNode head) {
        ListNode ans = null;
        for (ListNode x = head; x != null; x = x.next) {
            ans = new ListNode(x.val,ans);
        }
        return ans;
    }