# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        flag = head
        while flag:
            if flag.next and flag.val == flag.next.val:
                flag.next = flag.next.next
            else:
                flag = flag.next
        return head