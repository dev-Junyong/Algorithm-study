# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next:
            return True
        k = [head.val]
        
        while head.next:
            head = head.next
            k.append(head.val)
        len_k = len(k)
        
        for i in range(len_k//2):
            if k[i] != k[len_k-i-1]:
                return False
        return True