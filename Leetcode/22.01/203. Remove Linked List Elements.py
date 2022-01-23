# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        
        res = ListNode(0)
        res.next = head
        s = head
        e = res
        
        while s:
            while s and s.val == val:
                s = s.next
            e.next = s
            e = s
            if s:
                s = s.next
        return res.next