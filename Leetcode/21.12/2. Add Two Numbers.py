# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        res_end = res
        carry = 0 # save upper
        
        while l1 or l2 or carry:
            if l1:
                tmp1 = l1.val
            else:
                tmp1 = 0
            
            if l2:
                tmp2 = l2.val
            else:
                tmp2 = 0
            
            carry, out = divmod(tmp1+tmp2+carry, 10)
            
            res_end.next = ListNode(out)
            res_end = res_end.next
            
            if l1:
                l1 = l1.next
            else:
                pass
            if l2:
                l2 = l2.next
            else:
                pass
            
        return res.next